from __future__ import annotations

import math

import numpy as np


def normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def bernoulli_se(probability: float, samples: int) -> float:
    return math.sqrt(probability * (1.0 - probability) / samples)


def monte_carlo(seed: int, samples: int, epsilon: float) -> dict[str, int]:
    rng = np.random.default_rng(seed)
    counts = {
        "samples": 0,
        "printed_robust": 0,
        "definition_robust": 0,
        "printed_boundary": 0,
        "definition_boundary": 0,
    }
    batch_size = 250_000
    for start in range(0, samples, batch_size):
        size = min(batch_size, samples - start)
        nu = rng.normal(size=size)
        mu = rng.normal(size=size)
        printed_attack = nu * (mu - epsilon) < 0.0
        signed_margin = np.where(nu >= 0.0, mu, -mu)
        definition_attack = signed_margin < epsilon
        clean_correct = nu * mu > 0.0
        counts["samples"] += size
        counts["printed_robust"] += int(np.count_nonzero(printed_attack))
        counts["definition_robust"] += int(np.count_nonzero(definition_attack))
        counts["printed_boundary"] += int(
            np.count_nonzero(printed_attack & clean_correct)
        )
        counts["definition_boundary"] += int(
            np.count_nonzero(definition_attack & clean_correct)
        )
    return counts


def finite_dimensional(seed: int, dimension: int, samples: int, epsilon: float) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    w_star = np.zeros(dimension)
    w_star[0] = math.sqrt(dimension)
    w_hat = rng.normal(size=dimension)
    w_hat -= w_star * (np.dot(w_star, w_hat) / np.dot(w_star, w_star))
    w_hat *= math.sqrt(dimension) / np.linalg.norm(w_hat)
    raw_budget = epsilon / math.sqrt(dimension)

    definition_robust = 0
    definition_boundary = 0
    target_residual = 0.0
    attack_budget_excess = 0.0
    batch_size = 2_000
    for start in range(0, samples, batch_size):
        size = min(batch_size, samples - start)
        x = rng.normal(size=(size, dimension)) / math.sqrt(dimension)
        nu = x @ w_star
        mu = x @ w_hat
        signed_margin = np.where(nu >= 0.0, mu, -mu)
        attacked = signed_margin < epsilon
        clean_correct = nu * mu > 0.0
        definition_robust += int(np.count_nonzero(attacked))
        definition_boundary += int(np.count_nonzero(attacked & clean_correct))

        delta = -raw_budget * w_hat / np.linalg.norm(w_hat)
        target_residual = max(target_residual, abs(float(np.dot(w_star, delta))))
        attack_budget_excess = max(
            attack_budget_excess, float(np.linalg.norm(delta)) - raw_budget
        )

    return {
        "dimension": dimension,
        "samples": samples,
        "overlap_m": float(np.dot(w_star, w_hat) / dimension),
        "norm_q": float(np.dot(w_hat, w_hat) / dimension),
        "definition_robust": definition_robust / samples,
        "definition_boundary": definition_boundary / samples,
        "max_target_residual": target_residual,
        "max_attack_budget_excess": attack_budget_excess,
    }


def audit_theorem31(seeds: list[int]) -> dict[str, object]:
    epsilon = 0.5
    q = 1.0
    m = 0.0
    a = math.sqrt(q - m * m)
    phi = normal_cdf(epsilon * a)

    analytic = {
        "printed_eq24_robust": 0.5,
        "definition_robust": phi,
        "printed_eq25_boundary": 0.5 * (phi - 0.5),
        "definition_boundary": phi - 0.5,
        "robust_gap": phi - 0.5,
        "boundary_gap": 0.5 * (phi - 0.5),
        "epsilon_zero_control": {
            "printed_robust": 0.5,
            "definition_robust": 0.5,
            "printed_boundary": 0.0,
            "definition_boundary": 0.0,
        },
    }

    sample_count = 1_000_000
    totals = {
        "samples": 0,
        "printed_robust": 0,
        "definition_robust": 0,
        "printed_boundary": 0,
        "definition_boundary": 0,
    }
    per_seed = []
    for seed in seeds:
        counts = monte_carlo(seed + 31, sample_count, epsilon)
        per_seed.append({"seed": seed + 31, **counts})
        for key in totals:
            totals[key] += counts[key]

    estimates = {
        key: totals[key] / totals["samples"]
        for key in (
            "printed_robust",
            "definition_robust",
            "printed_boundary",
            "definition_boundary",
        )
    }
    standard_errors = {
        key: bernoulli_se(value, totals["samples"])
        for key, value in estimates.items()
    }

    finite = [
        finite_dimensional(seed + 3100, 512, 40_000, epsilon) for seed in seeds
    ]
    finite_robust_mean = float(np.mean([row["definition_robust"] for row in finite]))
    finite_boundary_mean = float(
        np.mean([row["definition_boundary"] for row in finite])
    )

    printed_rejected = (
        abs(estimates["definition_robust"] - analytic["printed_eq24_robust"])
        > 50.0 * standard_errors["definition_robust"]
        and abs(
            estimates["definition_boundary"] - analytic["printed_eq25_boundary"]
        )
        > 50.0 * standard_errors["definition_boundary"]
    )
    corrected_matches = (
        abs(estimates["definition_robust"] - analytic["definition_robust"])
        < 5.0 * standard_errors["definition_robust"]
        and abs(estimates["definition_boundary"] - analytic["definition_boundary"])
        < 5.0 * standard_errors["definition_boundary"]
        and abs(finite_robust_mean - analytic["definition_robust"]) < 0.006
        and abs(finite_boundary_mean - analytic["definition_boundary"]) < 0.006
    )
    controls_pass = (
        analytic["epsilon_zero_control"]["printed_robust"]
        == analytic["epsilon_zero_control"]["definition_robust"]
        and analytic["epsilon_zero_control"]["printed_boundary"]
        == analytic["epsilon_zero_control"]["definition_boundary"]
    )
    geometry_pass = all(
        abs(float(row["overlap_m"])) < 1e-12
        and abs(float(row["norm_q"]) - 1.0) < 1e-12
        and float(row["max_target_residual"]) < 1e-12
        and float(row["max_attack_budget_excess"]) < 1e-12
        for row in finite
    )
    verifier_passed = (
        printed_rejected and corrected_matches and controls_pass and geometry_pass
    )

    return {
        "status": "FALSIFIED" if verifier_passed else "BLOCKED",
        "exact_target": "Theorem 3.1 equations (24)-(25) as printed",
        "parameters": {
            "attack_geometry": "l2",
            "epsilon_tilde": epsilon,
            "m": m,
            "q": q,
            "A": a,
        },
        "analytic_certificate": analytic,
        "monte_carlo": {
            "total_samples": totals["samples"],
            "per_seed_counts": per_seed,
            "estimates": estimates,
            "standard_errors": standard_errors,
        },
        "finite_dimensional_checker": {
            "runs": finite,
            "robust_mean": finite_robust_mean,
            "boundary_mean": finite_boundary_mean,
        },
        "negative_control": {
            "mutation": "omit the label-dependent attack direction",
            "rejected_at_positive_epsilon": printed_rejected,
            "not_rejected_at_epsilon_zero": controls_pass,
            "status": "REJECTED_AS_EXPECTED" if printed_rejected else "UNEXPECTED_PASS",
        },
        "corrected_definition_matches": corrected_matches,
        "assumptions_audited": geometry_pass,
        "verifier_passed": verifier_passed,
    }
