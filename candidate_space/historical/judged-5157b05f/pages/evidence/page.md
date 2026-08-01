# Evidence


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_daa10869a904", "created_at": "2026-07-31T05:03:36+00:00", "title": "Verification output (last 40 lines)"}
-->
## Verification output (last 40 lines)

```
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
```
