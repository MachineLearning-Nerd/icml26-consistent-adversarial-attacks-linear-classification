# Current verification

## Claim 1 — VERIFIED by cumulative regression

The current verifier supersedes the historical weak multi-claim verifier for
new evidence. Historical pages remain preserved at the judged revision
`5157b05fbbbad2885cd379658d7b58e688863e94`.

- Exact claim: Proposition 1, Section 3.1, equation (9), scoped here to ℓ₂ and
  strict non-boundary cases.
- Code: `repro/src/verify.py` and `repro/src/core.py`.
- Fixed command: `uv sync --frozen && .venv/bin/python repro/src/verify.py`.
- Pinned environment: `pyproject.toml` and `uv.lock`.
- Raw result: 400/400 exact agreement, including 200 feasible and 200
  infeasible cases; full-norm mutation rejected.
- Independent checker: extremal orthogonal feasibility certificate.
- Negative control: full-norm mutation must be rejected.
- Limitations: equality and non-ℓ₂ geometries are excluded from the numerical
  scope; Claims 2–5 remain unresolved in the baseline.

## Claim 2 — FALSIFIED as printed

Theorem 3.1 equations (24)–(25) are tested exactly as printed. At `m=0`, the
printed Gaussian integral is analytically `0.5` for all positive attack budgets,
while Definition 2 plus Lemma 1 gives `Phi(epsilon_tilde)`. The candidate
verifier includes four million bivariate-Gaussian samples, four dense
dimension-512 constructions, an epsilon-zero non-falsification control, and a
label-direction mutation control. The printed robust error is exactly `0.5` at
the audited parameters, while the definition-faithful value is
`0.6914624613`; four million samples and dimension-512 constructions recover
the latter.

## Claim 3 — source-integrity audit pending

Theorem 4.1 equations (37)–(42) are checked as a displayed self-consistent
system and compared field-by-field with Appendix D equation (119). The checker
requires all four primal variables to be defined, detects three conflicting
conjugate updates, and accepts an appendix-consistent repaired control.

## Claim 5 — BLOCKED, route 1

Theorem 4.2 consumes `m` and `q`, but the displayed Theorem 4.1 system does not
define them. Route 1 reports this concrete dependency blocker and the repeated
label-direction mismatch without silently choosing a corrected theorem.

## Claim 4 — BLOCKED, route 1

Figure 5 does not publish enough settings or quantifiers to define a unique
reproduction: the evaluation budget, loss/link, tuning domain, seeds, numeric
table, large-psi threshold, and acceptance rule are absent. Equation (28) and
Assumption 4.2 also disagree on latent-noise scaling.

## Claim 5 — general event proof pending

For every positive effective threshold and nondegenerate centered joint
Gaussian, equation (43) omits the positive-probability half-strip
`nu<0, -c<mu<=c`; equation (44) retains only one of two symmetry-related
boundary regions. A correlated-Gaussian checker and `c=0` control are pending
remote execution.
