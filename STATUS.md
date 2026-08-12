# Status — consistent adversarial attacks

## Identification

- Paper: On the existence of consistent adversarial attacks in high-dimensional linear classification
- Authors: Matteo Vilucchio, Lenka Zdeborová, Bruno Loureiro
- Source: arXiv:2506.12454v1
- Venue record: ICML 2026
- Former repository: icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea
- Current repository: icml26-consistent-adversarial-attacks-linear-classification
- Canonical branch: main
- Historical judged revision: 5157b05fbbbad2885cd379658d7b58e688863e94
- Paper HTML SHA-256: 83b475d685ce1c7b0988d027f3ad3d8e0ff95afeeb583bdd58f0a31bca7f8696
- Paper PDF SHA-256: d57224430f16e29eca731470f2a756428aa2f53b2c9001dfb3a04ccd1d4f23ce

## Scientific checkpoint

| Claim | Verdict | Evidence checkpoint |
| --- | --- | --- |
| 1 / Proposition 1 | VERIFIED in scope | 400/400 l2 strict non-boundary cases, 200 feasible and 200 infeasible, full-norm mutation rejected. |
| 2 / Theorem 3.1 | FALSIFIED as printed | Printed robust value 0.5 versus definition-faithful Phi(0.5)=0.69146246; 4M draws and d=512 checks agree. |
| 3 / Theorem 4.1 | FALSIFIED as printed | Primal m, q, V, P are not defined; displayed conjugate updates conflict with Appendix (119); repair control closes. |
| 4 / Figure 5 trend | BLOCKED | Four routes complete; source contract and noise scaling are not uniquely specified; no eligible counterexample. |
| 5 / Theorem 4.2 | FALSIFIED as printed | Positive-threshold indicator omits a half-strip; 2M draws across four correlations reproduce the gap. |

Historical live score: 3/10. Projected 5–8/10 and best-supported 8/10 are forecasts only.

## Reproduction checkpoint

- Fixed command: uv sync --frozen && .venv/bin/python repro/src/verify.py
- Seeds: 1031, 2081, 4093, 8179
- Python/lock: pinned by uv.lock; current evidence records NumPy 2.3.2
- Compute: Hugging Face cpu-upgrade, 64 CPUs visible, no GPU devices
- Evidence revision: 3688690d5ee0a644b06807b0dd6d0525be19edcc
- Claim 4 route count: four
- Claim 4 eligible counterexamples: zero

## Publication checkpoint

- Main contains the current claim-by-claim README, reports, evidence, evaluator surface, and historical baseline.
- Per-claim contracts, raw outputs, checker outputs, controls, methods, source audits, and limitations are committed.
- Literal printed claims are kept distinct from possible intended corrections.
- Historical ORX branches are preserved under descriptive audit/release names after cleanup.
