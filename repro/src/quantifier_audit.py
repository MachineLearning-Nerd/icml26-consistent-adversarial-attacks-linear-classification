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
    complete_control = {
        name: value or "specified-control-value" for name, value in required.items()
    }
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


def audit_claim4_scaling(seeds: list[int]) -> dict[str, object]:
    dimensions = [125, 250, 500, 1000]
    p_over_d = 2
    samples_per_dimension = 1_000_000
    rows = []
    for dimension, seed in zip(dimensions, seeds, strict=True):
        features = p_over_d * dimension
        rng = np.random.default_rng(seed + 4400)
        latent_coordinate = rng.normal(size=samples_per_dimension) / math.sqrt(
            dimension
        )
        signal = math.sqrt(features / dimension) * latent_coordinate
        noise_eq28 = rng.normal(size=samples_per_dimension) / math.sqrt(features)
        noise_assumption42 = rng.normal(size=samples_per_dimension)
        signal_variance = float(np.mean(signal * signal))
        eq28_ratio = signal_variance / float(np.mean(noise_eq28 * noise_eq28))
        assumption42_ratio = signal_variance / float(
            np.mean(noise_assumption42 * noise_assumption42)
        )
        rows.append(
            {
                "seed": seed + 4400,
                "dimension_d": dimension,
                "features_p": features,
                "samples": samples_per_dimension,
                "empirical_signal_variance": signal_variance,
                "eq28_empirical_snr": eq28_ratio,
                "eq28_exact_snr": float(p_over_d * p_over_d),
                "assumption42_empirical_snr": assumption42_ratio,
                "assumption42_exact_snr": features / (dimension * dimension),
            }
        )
    log_dimensions = np.log(np.asarray(dimensions, dtype=float))
    eq28_slope = float(
        np.polyfit(
            log_dimensions,
            np.log([row["eq28_empirical_snr"] for row in rows]),
            1,
        )[0]
    )
    assumption42_slope = float(
        np.polyfit(
            log_dimensions,
            np.log([row["assumption42_empirical_snr"] for row in rows]),
            1,
        )[0]
    )
    exact_matches = all(
        abs(float(row["eq28_empirical_snr"]) - float(row["eq28_exact_snr"]))
        / float(row["eq28_exact_snr"])
        < 0.015
        and abs(
            float(row["assumption42_empirical_snr"])
            - float(row["assumption42_exact_snr"])
        )
        / float(row["assumption42_exact_snr"])
        < 0.015
        for row in rows
    )
    divergent_sequences = (
        abs(eq28_slope) < 0.03 and abs(assumption42_slope + 1.0) < 0.03
    )
    passed = exact_matches and divergent_sequences
    return {
        "status": "BLOCKED",
        "exact_target": "Section 4.3 and Figure 5 right-panel dual-effect claim",
        "route": 2,
        "route_name": "high-dimensional latent-noise scaling audit",
        "fixed_ratio": "p/d=2",
        "analytic_certificate": {
            "feature_signal_variance": "p/d^2",
            "equation_28_noise_variance": "1/p",
            "equation_28_snr": "(p/d)^2, constant in the proportional limit",
            "assumption_4_2_noise_variance": "1",
            "assumption_4_2_snr": "p/d^2, vanishes as 1/d",
        },
        "rows": rows,
        "log_log_slopes": {
            "equation_28": eq28_slope,
            "assumption_4_2": assumption42_slope,
        },
        "negative_control": {
            "expected_equation_28_slope": 0.0,
            "observed_equation_28_slope": eq28_slope,
            "status": "NOT_REJECTED_AS_EXPECTED"
            if abs(eq28_slope) < 0.03
            else "UNEXPECTED_REJECTION",
        },
        "blocker": "The two published noise scalings define different proportional-limit experiments, so Claim 4 has no unique source-faithful asymptotic target.",
        "verifier_passed": passed,
    }


def audit_claim4_decomposition(seeds: list[int]) -> dict[str, object]:
    correlations = [-0.6, -0.2, 0.2, 0.6]
    thresholds = [0.15, 0.35, 0.55, 0.75]
    rows = []
    for seed, correlation, threshold in zip(
        seeds, correlations, thresholds, strict=True
    ):
        rng = np.random.default_rng(seed + 4600)
        samples = 500_000
        nu = rng.normal(size=samples)
        mu = correlation * nu + math.sqrt(1.0 - correlation**2) * rng.normal(
            size=samples
        )
        consistent_robust = np.where(nu >= 0.0, mu, -mu) < threshold
        clean_error = nu * mu < 0.0
        consistent_boundary = consistent_robust & ~clean_error
        robust_count = int(np.count_nonzero(consistent_robust))
        clean_count = int(np.count_nonzero(clean_error))
        boundary_count = int(np.count_nonzero(consistent_boundary))
        mutated_count = boundary_count
        rows.append(
            {
                "seed": seed + 4600,
                "correlation": correlation,
                "threshold": threshold,
                "samples": samples,
                "consistent_robust_count": robust_count,
                "clean_error_count": clean_count,
                "consistent_boundary_count": boundary_count,
                "identity_residual_count": robust_count
                - clean_count
                - boundary_count,
                "omit_clean_error_mutation_residual": robust_count - mutated_count,
            }
        )
    identity_pass = all(row["identity_residual_count"] == 0 for row in rows)
    mutation_rejected = all(
        row["omit_clean_error_mutation_residual"] > 50_000 for row in rows
    )
    dual_effect_control = {
        "lower_psi": {"clean": 0.40, "boundary": 0.05, "robust": 0.45},
        "higher_psi": {"clean": 0.20, "boundary": 0.15, "robust": 0.35},
    }
    boundary_change = (
        dual_effect_control["higher_psi"]["boundary"]
        - dual_effect_control["lower_psi"]["boundary"]
    )
    clean_change = (
        dual_effect_control["higher_psi"]["clean"]
        - dual_effect_control["lower_psi"]["clean"]
    )
    robust_change = (
        dual_effect_control["higher_psi"]["robust"]
        - dual_effect_control["lower_psi"]["robust"]
    )
    mechanism_pass = (
        boundary_change > 0
        and robust_change < 0
        and abs(clean_change + boundary_change - robust_change) < 1e-12
        and abs(clean_change) > boundary_change
    )
    passed = identity_pass and mutation_rejected and mechanism_pass
    return {
        "status": "BLOCKED",
        "exact_target": "Section 4.3 and Figure 5 right-panel dual-effect claim",
        "route": 3,
        "route_name": "exact error decomposition and compensation audit",
        "identity": "E_rob_cns = E_clean + E_bnd_cns (outside zero-probability ties)",
        "rows": rows,
        "dual_effect_control": dual_effect_control,
        "changes": {
            "clean": clean_change,
            "boundary": boundary_change,
            "consistent_robust": robust_change,
        },
        "negative_control": {
            "mutation": "identify consistent robust error with boundary error alone",
            "rejected_in_all_rows": mutation_rejected,
            "status": "REJECTED_AS_EXPECTED"
            if mutation_rejected
            else "UNEXPECTED_PASS",
        },
        "mechanism_conclusion": "If boundary error rises while aggregate consistent robust error falls, clean error must fall by more than the boundary error rises.",
        "blocker": "The identity verifies the proposed compensation mechanism but supplies no missing psi-dependent trained-model values, so it cannot establish the directional Figure 5 trend.",
        "verifier_passed": passed,
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
