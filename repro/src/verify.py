from __future__ import annotations

import glob
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from core import feasibility_certificate, mutated_condition, proposition_condition
from latent_audit import audit_latent_theorems
from quantifier_audit import (
    audit_claim4_decomposition,
    audit_claim4_falsification_eligibility,
    audit_claim4_scaling,
    audit_claim4_specification,
    audit_theorem42_indicator,
)
from theorem31 import audit_theorem31


ROOT = Path(__file__).resolve().parents[2]
SEEDS = [1031, 2081, 4093, 8179]
ESTIMATED_CORES = 2
SELECTED_FLAVOR = "cpu-upgrade"
FIXED_COMMAND = "uv sync --frozen && .venv/bin/python repro/src/verify.py"


def actual_cpu_allocation() -> int:
    if hasattr(os, "sched_getaffinity"):
        return len(os.sched_getaffinity(0))
    return os.cpu_count() or 1


def git_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_proposition_trials() -> dict[str, object]:
    dimension = 64
    factors = [0.25, 0.75, 1.25, 2.0]
    agreement = 0
    total = 0
    positive = 0
    negative = 0
    max_target_residual = 0.0
    max_norm_excess = 0.0
    mutation_disagreements = 0

    for seed in SEEDS:
        rng = np.random.default_rng(seed)
        for trial in range(100):
            w_star = rng.normal(size=dimension)
            w_star *= np.sqrt(dimension) / np.linalg.norm(w_star)
            w_hat = rng.normal(size=dimension)
            x = rng.normal(size=dimension) / np.sqrt(dimension)
            w_perp = w_hat - w_star * (
                np.dot(w_star, w_hat) / np.dot(w_star, w_star)
            )
            threshold = abs(np.dot(w_hat, x)) / np.linalg.norm(w_perp)
            epsilon = threshold * factors[trial % len(factors)]

            predicted = proposition_condition(w_star, w_hat, x, epsilon)
            certificate = feasibility_certificate(w_star, w_hat, x, epsilon)
            independently_feasible = bool(certificate["feasible"])
            agreement += int(predicted == independently_feasible)
            positive += int(independently_feasible)
            negative += int(not independently_feasible)
            max_target_residual = max(
                max_target_residual, abs(float(certificate["target_inner_product"]))
            )
            max_norm_excess = max(
                max_norm_excess,
                float(certificate["delta_norm"]) - epsilon,
            )
            mutation_disagreements += int(
                mutated_condition(w_star, w_hat, x, epsilon)
                != independently_feasible
            )
            total += 1

    for _ in range(20):
        w_star = np.zeros(dimension)
        w_star[0] = np.sqrt(dimension)
        w_hat = 4.0 * w_star
        w_hat[1] = 1.0
        x = w_hat / np.dot(w_hat, w_hat)
        epsilon = 0.5
        certificate = feasibility_certificate(w_star, w_hat, x, epsilon)
        mutation_disagreements += int(
            mutated_condition(w_star, w_hat, x, epsilon)
            != bool(certificate["feasible"])
        )

    passed = (
        agreement == total
        and positive > 0
        and negative > 0
        and max_target_residual < 1e-10
        and max_norm_excess < 1e-12
        and mutation_disagreements >= 1
    )
    return {
        "status": "VERIFIED" if passed else "FALSIFIED",
        "scope": "Proposition 1, q=2, strict non-boundary numerical cases",
        "trials": total,
        "agreement": agreement,
        "feasible_cases": positive,
        "infeasible_cases": negative,
        "max_target_invariance_residual": max_target_residual,
        "max_budget_excess": max_norm_excess,
        "negative_control": {
            "mutation": "replace ||w_hat_perp|| with ||w_hat||",
            "detected_disagreements": mutation_disagreements,
            "status": "REJECTED_AS_EXPECTED"
            if mutation_disagreements >= 1
            else "UNEXPECTED_PASS",
        },
        "passed": passed,
    }


def main() -> int:
    started = time.perf_counter()
    gpu_devices = sorted(glob.glob("/dev/nvidia*"))
    proposition = run_proposition_trials()
    theorem31 = audit_theorem31(SEEDS)
    latent = audit_latent_theorems()
    claim4_route1 = audit_claim4_specification()
    claim4_route2 = audit_claim4_scaling(SEEDS)
    claim4_route3 = audit_claim4_decomposition(SEEDS)
    claim4 = audit_claim4_falsification_eligibility()
    claim5 = audit_theorem42_indicator(SEEDS)
    result = {
        "schema_version": 1,
        "paper": "arXiv:2506.12454v1",
        "claim": "Proposition 1",
        "git_sha": git_sha(),
        "fixed_command": FIXED_COMMAND,
        "environment": {
            "manager": "uv",
            "python": sys.version.split()[0],
            "uv_lock_sha256": file_sha256(ROOT / "uv.lock"),
        },
        "compute": {
            "backend": "hugging-face",
            "estimated_cores": ESTIMATED_CORES,
            "selected_flavor": SELECTED_FLAVOR,
            "actual_cpu_allocation": actual_cpu_allocation(),
            "gpu_devices": gpu_devices,
        },
        "seeds": SEEDS,
        "claims": {
            "claim_1": proposition,
            "claim_2": theorem31,
            "claim_3": latent["claim_3"],
            "claim_4": claim4,
            "claim_5": claim5,
        },
        "prior_routes": {
            "claim_4_route_1": claim4_route1,
            "claim_4_route_2": claim4_route2,
            "claim_4_route_3": claim4_route3,
            "claim_5_route_1": latent["claim_5"],
        },
        "unresolved_claims": [4],
    }
    result["runtime_seconds"] = time.perf_counter() - started
    result["all_passed"] = (
        proposition["passed"]
        and theorem31["verifier_passed"]
        and latent["claim_3"]["verifier_passed"]
        and claim4["verifier_passed"]
        and claim5["verifier_passed"]
        and not gpu_devices
    )
    print("BEGIN_MACHINE_READABLE_EVIDENCE")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("END_MACHINE_READABLE_EVIDENCE")
    print(
        "SUMMARY: claim_1={status}; claim_2={claim2}; claim_3={claim3}; claim_4={claim4}; claim_5={claim5}; mutation_control={control}; all_passed={passed}".format(
            status=proposition["status"],
            claim2=theorem31["status"],
            claim3=latent["claim_3"]["status"],
            claim4=claim4["status"],
            claim5=claim5["status"],
            control=proposition["negative_control"]["status"],
            passed=result["all_passed"],
        )
    )
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
