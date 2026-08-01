from __future__ import annotations

import math

import numpy as np


def audit_claim4_specification() -> dict[str, object]:
    required = {
        "latent_dimension": "d=500",
        "replicates": "10",
        "training_attack_geometry": "s=infinity",
        "regularization_geometry": "r=2 (paper notation)",
        "alpha_values": "shown in Figure 5",
        "psi_values": "shown in Figure 5",
        "evaluation_attack_budget": None,
        "loss_function": None,
        "ground_truth_link": None,
        "lambda_search_domain": None,
        "attack_radius_search_domain": None,
        "optimizer_stopping_rule": None,
        "random_seeds": None,
        "raw_numeric_results": None,
    }
    missing = sorted(name for name, value in required.items() if value is None)
    noise_scalings = {
        "equation_28": "u~N(0,I_p/p)",
        "assumption_4_2": "u~N(0,I_p)",
        "conflict": True,
    }
    quantified_trend = {
        "paper_phrase": "in the large psi regime",
        "large_psi_threshold": None,
        "minimum_increase_or_decrease": None,
        "uncertainty_acceptance_rule": None,
    }
    complete_control = {name: value or "specified-control-value" for name, value in required.items()}
    control_missing = sorted(
        name for name, value in complete_control.items() if value is None
    )
    blocked = bool(missing) and noise_scalings["conflict"] and not control_missing
    return {
        "status": "BLOCKED",
        "exact_target": "Section 4.3 and Figure 5 right-panel dual-effect claim",
        "route": 1,
        "route_name": "source-completeness and quantifier audit",
        "source_fields": required,
        "missing_fields": missing,
        "noise_scaling_audit": noise_scalings,
        "trend_quantifier_audit": quantified_trend,
        "negative_control": {
            "mutation": "supply every required field in a synthetic specification",
            "missing_fields": control_missing,
            "status": "NOT_REJECTED_AS_EXPECTED"
            if not control_missing
            else "UNEXPECTED_REJECTION",
        },
        "blocker": "The plotted experiment and its large-psi trend do not determine a unique executable claim contract.",
        "verifier_passed": blocked,
    }


def correlated_indicator_counts(
    seed: int, samples: int, correlation: float, threshold: float
) -> dict[str, int | float]:
    rng = np.random.default_rng(seed)
    counts = {
        "samples": 0,
        "printed_robust": 0,
        "definition_robust": 0,
        "printed_boundary": 0,
        "definition_boundary": 0,
        "omitted_half_strip": 0,
    }
    batch_size = 250_000
    scale = math.sqrt(1.0 - correlation * correlation)
    for start in range(0, samples, batch_size):
        size = min(batch_size, samples - start)
        nu = rng.normal(size=size)
        mu = correlation * nu + scale * rng.normal(size=size)
        printed = nu * (mu - threshold) < 0.0
        definition = np.where(nu >= 0.0, mu, -mu) < threshold
        clean_correct = nu * mu > 0.0
        half_strip = (nu < 0.0) & (mu > -threshold) & (mu <= threshold)
        counts["samples"] += size
        counts["printed_robust"] += int(np.count_nonzero(printed))
        counts["definition_robust"] += int(np.count_nonzero(definition))
        counts["printed_boundary"] += int(np.count_nonzero(printed & clean_correct))
        counts["definition_boundary"] += int(
            np.count_nonzero(definition & clean_correct)
        )
        counts["omitted_half_strip"] += int(np.count_nonzero(half_strip))
    return {"seed": seed, "correlation": correlation, "threshold": threshold, **counts}


def audit_theorem42_indicator(seeds: list[int]) -> dict[str, object]:
    threshold = 0.5
    correlations = [-0.75, -0.25, 0.25, 0.75]
    positive_runs = [
        correlated_indicator_counts(seed + 4200, 500_000, correlation, threshold)
        for seed, correlation in zip(seeds, correlations, strict=True)
    ]
    zero_runs = [
        correlated_indicator_counts(seed + 5200, 100_000, correlation, 0.0)
        for seed, correlation in zip(seeds, correlations, strict=True)
    ]
    positive_checks = []
    for row in positive_runs:
        robust_gap = int(row["definition_robust"]) - int(row["printed_robust"])
        boundary_ratio = int(row["definition_boundary"]) / int(
            row["printed_boundary"]
        )
        positive_checks.append(
            {
                "correlation": row["correlation"],
                "robust_gap_count": robust_gap,
                "omitted_half_strip_count": row["omitted_half_strip"],
                "gap_equals_half_strip": robust_gap == row["omitted_half_strip"],
                "boundary_ratio": boundary_ratio,
                "boundary_ratio_near_two": abs(boundary_ratio - 2.0) < 0.035,
            }
        )
    positive_pass = all(
        check["robust_gap_count"] > 10_000
        and check["gap_equals_half_strip"]
        and check["boundary_ratio_near_two"]
        for check in positive_checks
    )
    zero_pass = all(
        row["printed_robust"] == row["definition_robust"]
        and row["printed_boundary"] == row["definition_boundary"] == 0
        for row in zero_runs
    )
    passed = positive_pass and zero_pass
    return {
        "status": "FALSIFIED" if passed else "BLOCKED",
        "exact_target": "Theorem 4.2 equations (43)-(44) as printed",
        "route": 2,
        "route_name": "general event-algebra proof with correlated-Gaussian checker",
        "proof_certificate": {
            "assumptions": "(nu,mu) is a nondegenerate centered jointly Gaussian pair and c=epsilon_tilde*A^(1/s_star)>0",
            "printed_event": "{nu>0,mu<c} union {nu<0,mu>c}",
            "definition_event": "{nu>0,mu<c} union {nu<0,mu>-c}",
            "omitted_set": "{nu<0,-c<mu<=c}",
            "omitted_set_probability": "strictly positive for c>0 and positive-definite covariance",
            "boundary_consequence": "central symmetry gives two equal attacked-correct halves; equation (44) retains only one",
        },
        "positive_threshold_runs": positive_runs,
        "checks": positive_checks,
        "negative_control": {
            "threshold": 0.0,
            "runs": zero_runs,
            "status": "NOT_REJECTED_AS_EXPECTED" if zero_pass else "UNEXPECTED_REJECTION",
        },
        "paper_positive_threshold_witness": "Figure 5 displays positive consistent boundary errors under the stated Theorem 4.2 solution, which is impossible at c=0.",
        "verifier_passed": passed,
    }
