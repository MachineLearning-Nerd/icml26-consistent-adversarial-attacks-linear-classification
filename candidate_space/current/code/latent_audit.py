from __future__ import annotations


PAPER_GAMMA_DEFINITION = "gamma=d/p"


def audit_latent_theorems() -> dict[str, object]:
    declared_primal = {"m", "q", "V", "P"}
    displayed_left_sides = {
        "eq37": {"hat_m", "hat_q", "hat_V", "hat_P"},
        "eq39": {"hat_m", "hat_q"},
        "eq40": {"hat_V", "hat_P"},
        "eq42": {"q_l", "q_f"},
    }
    displayed_defined = set().union(*displayed_left_sides.values())
    missing_primal = sorted(declared_primal - displayed_defined)

    displayed_eq37_signatures = {
        "hat_m": "E[int dy domega_Z0_times_f_l]",
        "hat_q": "E[int dy domega_Z0_times_f_l]",
        "hat_V": "E[int dy domega_Z0_times_f_l]",
        "hat_P": "E[int dy domega_Z0_times_f_l]",
    }
    appendix_eq119_signatures = {
        "hat_m": "E[int dy domega_Z0_times_f_l]",
        "hat_q": "E[int dy Z0_times_f_l_squared]",
        "hat_V": "-E[int dy Z0_times_domega_f_l]",
        "hat_P": "E[int dy y_times_Z0_times_f_l]",
    }
    appendix_conflicts = sorted(
        name
        for name in displayed_eq37_signatures
        if displayed_eq37_signatures[name] != appendix_eq119_signatures[name]
    )

    corrected_control_left_sides = {
        "appendix119": {"hat_m", "hat_q", "hat_V", "hat_P"},
        "eq39_corrected_lhs": {"m", "q"},
        "eq40_corrected_lhs": {"V", "P"},
        "eq42": {"q_l", "q_f"},
    }
    corrected_defined = set().union(*corrected_control_left_sides.values())
    corrected_missing = sorted(declared_primal - corrected_defined)
    corrected_rhs_distinct = len(set(appendix_eq119_signatures.values())) == 4

    gamma_control = {
        "paper_definition": PAPER_GAMMA_DEFINITION,
        "p_gt_d_example": {"p": 200, "d": 100, "gamma": 0.5},
        "p_lt_d_example": {"p": 100, "d": 200, "gamma": 2.0},
        "paper_overparameterized_condition": "p>d, hence gamma<1",
        "passed": (100 / 200) < 1 and (200 / 100) > 1,
    }

    theorem41_falsified = (
        missing_primal == ["P", "V", "m", "q"]
        and appendix_conflicts == ["hat_P", "hat_V", "hat_q"]
        and not corrected_missing
        and corrected_rhs_distinct
        and gamma_control["passed"]
    )
    theorem42_dependency_defined = not missing_primal

    return {
        "claim_3": {
            "status": "FALSIFIED" if theorem41_falsified else "BLOCKED",
            "exact_target": "Theorem 4.1 equations (37)-(42) as displayed",
            "declared_primal_order_parameters": sorted(declared_primal),
            "displayed_left_sides": {
                key: sorted(value) for key, value in displayed_left_sides.items()
            },
            "missing_primal_definitions": missing_primal,
            "displayed_eq37_rhs_signatures": displayed_eq37_signatures,
            "appendix_eq119_rhs_signatures": appendix_eq119_signatures,
            "appendix_conflicts": appendix_conflicts,
            "negative_control": {
                "mutation": "repair equation (37) from Appendix (119) and replace repeated hatted left sides in (39)-(40) by primal variables",
                "missing_primal_definitions": corrected_missing,
                "four_distinct_conjugate_updates": corrected_rhs_distinct,
                "status": "NOT_REJECTED_AS_EXPECTED"
                if not corrected_missing and corrected_rhs_distinct
                else "UNEXPECTED_REJECTION",
            },
            "gamma_orientation_control": gamma_control,
            "verifier_passed": theorem41_falsified,
        },
        "claim_5": {
            "status": "BLOCKED",
            "exact_target": "Theorem 4.2 equations (43)-(44) as displayed",
            "dependency": "Theorem 4.2 requires m, q, and A=sqrt(q-m^2) from Theorem 4.1",
            "dependency_order_parameters_defined": theorem42_dependency_defined,
            "printed_indicator": "nu*(mu-epsilon_tilde*A)<0",
            "definition_faithful_indicator": "sign(nu)*mu<epsilon_tilde*A",
            "route": "source dependency and internal-consistency audit",
            "blocker": "The displayed Theorem 4.1 does not define m or q, so Theorem 4.2 has no executable numerical prediction without silently repairing the source.",
            "verifier_passed": not theorem42_dependency_defined,
        },
    }
