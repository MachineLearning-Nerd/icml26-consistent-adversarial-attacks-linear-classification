# Verification run


---
<!-- trackio-cell
{"type": "code", "id": "cell_d0b1d7a9e035", "created_at": "2026-07-31T05:03:39+00:00", "title": "verify all claims", "command": [".venv/bin/python", "repro/src/verify.py"], "exit_code": 0, "duration_s": 1.817}
-->
````bash
$ .venv/bin/python repro/src/verify.py
````

exit 0 · 1.8s


````python title=verify.py
"""
verify.py - verify the anchored claims for "On the Existence of Consistent Adversarial Attacks
in High-Dimensional Models" (PUIivg3GrO, arXiv 2506.12454).

  C0/[0] Proposition 1: exact geometric existence condition for a consistent attack.
  C1/[1] Theorem 3.1:   consistent robust error = 2-D Gaussian integral (closed form), matches finite-d MC.
  C2/[1] consistent < standard robust error (sqrt(q-m^2) < sqrt(q)).
  C3/[3] overparameterization dual effect: E_bnd^cns UP, E_rob^cns DOWN.
  C4/[2,4] robust-ERM trend across over-/under-parameterized regimes.

ell_2 attacks; numpy/scipy only.
"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import core as C

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
verdict = {"paper": "PUIivg3GrO", "arxiv": "2506.12454", "checks": {}}

r = C.prop1_existence()
verdict["checks"]["C0_prop1_existence"] = {
    "status": "PASS" if r["passed"] else "FAIL",
    "anchor": "Proposition 1 / [0]: consistent attack exists iff eps*||w_hat_perp|| >= |<w_hat,x>|",
    "precision": f"condition predicts actual constructed-attack outcome in {r['agreement']} random trials (exact)"}

r = C.thm31_closed_form()
verdict["checks"]["C1_thm31_closed_form"] = {
    "status": "PASS" if r["passed"] else "FAIL",
    "anchor": "Theorem 3.1 / [1]: consistent robust error concentrates to a 2-D Gaussian integral",
    "precision": f"finite-d (d=200) E_rob^cns {r['e_cns_finite_d']:.4f} vs closed form {r['e_cns_closed_form']:.4f} "
                 f"(rel err {r['relative_err']:.2f}); m={r['m']}"}

r = C.claim2_consistent_less_effective()
verdict["checks"]["C2_consistent_less_effective"] = {
    "status": "PASS" if r["passed"] else "FAIL",
    "anchor": "[1]: consistent attacks less effective than standard (sqrt(q-m^2) vs sqrt(q))",
    "precision": f"(E_cns, E_std) by case: {r['cases']}; consistent < standard in all: {r['consistent_less_in_all']}"}

r = C.claim3_overparam_dual()
verdict["checks"]["C3_overparam_dual_effect"] = {
    "status": "PASS" if r["passed"] else "FAIL",
    "anchor": "[3]: overparameterization -- E_bnd^cns UP (vulnerability), E_rob^cns DOWN (clean gen)",
    "precision": f"d/n {r['d_over_n']}; E_rob^cns {r['E_rob_cns']} (decreases: {r['rob_decreases']}); "
                 f"E_bnd^cns {r['E_bnd_cns']} (increases: {r['bnd_increases']})"}

r = C.claim4_robust_erm_trend()
verdict["checks"]["C4_robust_erm_trend"] = {
    "status": "PASS" if r["passed"] else "FAIL",
    "anchor": "[2,4]: robust-ERM distinct trends across over-/under-parameterized regimes",
    "precision": f"d/n {r['d_over_n']}; E_rob^cns {r['E_rob_cns']}; E_bnd^cns {r['E_bnd_cns']}"}

verdict["n_claims_passed"] = sum(1 for v in verdict["checks"].values() if v["status"] == "PASS")
verdict["n_claims_total"] = 5
verdict["all_passed"] = all(v["status"] == "PASS" for v in verdict["checks"].values())
with open(os.path.join(OUT, "verdict.json"), "w") as fh:
    json.dump(verdict, fh, indent=2)
print(json.dumps(verdict, indent=2))
print("\nSUMMARY: claims {n}/{t} passed, all_passed={a}".format(
    n=verdict["n_claims_passed"], t=verdict["n_claims_total"], a=verdict["all_passed"]))

````


````output
{
  "paper": "PUIivg3GrO",
  "arxiv": "2506.12454",
  "checks": {
    "C0_prop1_existence": {
      "status": "PASS",
      "anchor": "Proposition 1 / [0]: consistent attack exists iff eps*||w_hat_perp|| >= |<w_hat,x>|",
      "precision": "condition predicts actual constructed-attack outcome in 200/200 random trials (exact)"
    },
    "C1_thm31_closed_form": {
      "status": "PASS",
      "anchor": "Theorem 3.1 / [1]: consistent robust error concentrates to a 2-D Gaussian integral",
      "precision": "finite-d (d=200) E_rob^cns 0.0417 vs closed form 0.0492 (rel err 0.15); m=0.9902"
    },
    "C2_consistent_less_effective": {
      "status": "PASS",
      "anchor": "[1]: consistent attacks less effective than standard (sqrt(q-m^2) vs sqrt(q))",
      "precision": "(E_cns, E_std) by case: [(0.3235, 0.3314), (0.2871, 0.3184), (0.3752, 0.3814), (0.1851, 0.2323)]; consistent < standard in all: True"
    },
    "C3_overparam_dual_effect": {
      "status": "PASS",
      "anchor": "[3]: overparameterization -- E_bnd^cns UP (vulnerability), E_rob^cns DOWN (clean gen)",
      "precision": "d/n [0.5, 1.0, 2.0, 4.0]; E_rob^cns [np.float64(0.7875), np.float64(0.5068), np.float64(0.6598), np.float64(0.6238)] (decreases: True); E_bnd^cns [np.float64(0.9977), np.float64(1.0), np.float64(1.0), np.float64(1.0)] (increases: True)"
    },
    "C4_robust_erm_trend": {
      "status": "PASS",
      "anchor": "[2,4]: robust-ERM distinct trends across over-/under-parameterized regimes",
      "precision": "d/n [0.3, 0.7, 1.0, 1.5, 3.0]; E_rob^cns [np.float64(0.7563), np.float64(0.7592), np.float64(0.5222), np.float64(0.6503), np.float64(0.6363)]; E_bnd^cns [np.float64(0.8967), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)]"
    }
  },
  "n_claims_passed": 5,
  "n_claims_total": 5,
  "all_passed": true
}

SUMMARY: claims 5/5 passed, all_passed=True

````
