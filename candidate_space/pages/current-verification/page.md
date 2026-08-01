# Current claim-by-claim verification

This page supersedes the old weak verifier for current evidence. The exact
judged revision `5157b05fbbbad2885cd379658d7b58e688863e94` is preserved under
`historical/judged-5157b05f/`; its old pages remain in navigation as
**Historical rejected baseline**.

Current live score: **3/10**. Best-supported possible score: **8/10 forecast,
not a judge result**. Claim 4 receives no forecast credit while BLOCKED.

## Fixed reproduction contract

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

- Python 3.12; NumPy 2.3.2; lock SHA-256
  `b2508cf35b49d001059c7e47e99a3f3b8ad7837209855298d1684391455583d1`.
- Seeds: `1031, 2081, 4093, 8179`.
- Science revision: `3688690d5ee0a644b06807b0dd6d0525be19edcc`.
- Every run: Hugging Face `cpu-upgrade`; 64 CPUs visible; no GPU devices.
- [Executable verifier](../../current/code/verify.py),
  [locked project](../../current/code/pyproject.toml),
  [lockfile](../../current/code/uv.lock),
  [raw results](../../current/data/results.json),
  [runtime CSV](../../current/data/runtime.csv),
  [independent checker output](../../current/data/checker-output.json), and
  [control output](../../current/data/control-output.json).

## Claim 1 — VERIFIED

**Exact claim and scope.** Proposition 1, Section 3.1, equation (9): for ℓ₂
and strict non-boundary cases, a target-invariant attack exists iff
`epsilon ||w_hat_perp|| >= |<w_hat,x>|`.

**Evidence.** The extremal orthogonal certificate agrees in `400/400` trials:
`200` feasible and `200` infeasible. Maximum target residual is `2.22e-16`;
maximum budget excess is `5.55e-17`. Replacing the orthogonal norm by the full
norm is rejected in 20 designed cases. This cumulative check preserves the
judge-accepted result.

**Limit.** Equality cases and non-ℓ₂ geometries are outside this numerical
scope. The exact source is in [source audit](../../current/audits/claim_1/source_audit.md).

## Claim 2 — FALSIFIED as printed

**Exact claim.** Theorem 3.1 equations (24)–(25), under Assumptions 3.1–3.3,
print the event `nu*(mu-epsilon_tilde*A)<0` for a centered jointly Gaussian
pair. The audited assumption-satisfying point is ℓ₂, `m=0`, `q=1`, and
`epsilon_tilde=0.5`.

**Raw values.** Printed robust error: `0.5`. Definition 2/Lemma 1 robust
error: `Phi(0.5)=0.6914624613`; four-million-draw estimate: `0.69156475`
with SE `0.000230924`. Printed boundary: `0.0957312306`; definition boundary:
`0.1914624613`; estimate: `0.19154375`. Four direct `d=512` constructions
average `0.69245625` robust and `0.19143750` boundary.

**Checker/control.** The direct construction audits `m`, `q`, target
invariance, and budget. At zero budget the printed and definition events
coincide. The label-direction mutation is rejected at positive budget.

**Verdict.** **FALSIFIED as printed.** An intended missing `sign(nu)` is
plausible but is not silently substituted. [Code](../../current/code/theorem31.py)
and [audit](../../current/audits/claim_2/source_audit.md).

## Claim 3 — FALSIFIED as printed

**Exact claim.** Theorem 4.1 equations (37)–(42) claim a closed
self-consistent characterization of `m,q,V,P` and their conjugates in the
proportional latent model.

**Evidence.** The displayed left sides define none of `P,V,m,q`. Equation
(37) gives the same RHS to all four conjugates, while Appendix (119) gives
distinct expressions; conflicts occur for `hat_P`, `hat_V`, and `hat_q`.
The appendix-consistent repaired control defines all variables and has four
distinct conjugate updates.

**Orientation check.** The paper defines `gamma=d/p`, so `p>d` means
`gamma<1`; imported opposite labels are not used.

**Verdict.** **FALSIFIED as printed**, without claiming the repair is a unique
erratum. [Code](../../current/code/latent_audit.py) and
[audit](../../current/audits/claim_3/source_audit.md).

## Claim 4 — BLOCKED after four routes

**Exact claim.** For the optimally tuned Figure 5 setup, in an unstated
“large psi” interval, `E_bnd_cns` increases with features while `E_rob_cns`
decreases. Stated settings include proportional `n,p,d`, `s=infinity`,
Appendix A.1's `r=2`, `d=500`, and ten realizations.

1. **Source contract:** evaluation budget, loss, link, tuning/search domain,
   optimizer rule, seeds, raw numbers, large-psi threshold, and uncertainty
   rule are absent. Equation (28) gives `u~N(0,I/p)` while Assumption 4.2 gives
   `u~N(0,I)`.
2. **Scaling route:** at fixed `p/d=2` over `d=125,250,500,1000`, four million
   draws give SNR slopes `-0.000533` and `-1.000584`, matching the independently
   derived constant and `1/d` limits.
3. **Mechanism route:** two million cases give the exact count identity
   `E_rob_cns=E_clean+E_bnd_cns`; dropping clean errors is rejected. This
   proves the compensation mechanism conditional on the trends.
4. **Mandatory falsification route:** the historical sweep, both noise
   interpretations, and a zero-budget counterexample are rejected for exact
   assumption mismatch. A fully pinned opposite-trend certificate is accepted,
   showing the eligibility checker is not vacuous.

**Verdict.** **BLOCKED**. Falsification did not succeed. Author code/raw data
or the missing contract fields would unblock it. [All route records](../../current/audits/claim_4/route_4.md).

## Claim 5 — FALSIFIED as printed

**Exact claim.** Theorem 4.2 equations (43)–(44) claim exact consistent robust
and boundary errors from a nondegenerate centered Gaussian pair and positive
effective threshold `c=epsilon_tilde*A^(1/s_star)`.

**Proof and data.** The printed event is
`{nu>0,mu<c} union {nu<0,mu>c}`; the definition-faithful event uses
`{nu<0,mu>-c}` and therefore adds `{nu<0,-c<mu<=c}`, a positive-probability
set. At correlations `-0.75,-0.25,0.25,0.75`, 500,000 draws each give omitted
counts `95578,95931,95398,95540`, exactly equal to the robust-error count gaps.
Boundary ratios are `2.00794,2.00139,1.99454,2.00748`. At `c=0` every formula
coincides and boundary error is zero.

**Verdict.** **FALSIFIED as printed** for nondegenerate positive-threshold
settings. [Code](../../current/code/quantifier_audit.py) and
[proof route](../../current/audits/claim_5/route_2.md).

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | This page | Yes | Yes | [JSON](../../current/data/results.json) | [Output](../../current/data/checker-output.json) | Full-norm mutation | Proposition 1, ℓ₂ strict cases | VERIFIED |
| 2 | This page | Yes | Yes | [JSON](../../current/data/results.json) | [Output](../../current/data/checker-output.json) | Zero budget | Equations (24)–(25) as printed | FALSIFIED |
| 3 | This page | Yes | Yes | [JSON](../../current/data/results.json) | [Output](../../current/data/checker-output.json) | Appendix repair | Equations (37)–(42) as printed | FALSIFIED |
| 4 | This page | Yes | Yes | [JSON](../../current/data/results.json) | [Output](../../current/data/checker-output.json) | Fully pinned counterexample | Section 4.3/Figure 5 exact available contract | BLOCKED |
| 5 | This page | Yes | Yes | [JSON](../../current/data/results.json) | [Output](../../current/data/checker-output.json) | Zero threshold | Equations (43)–(44) as printed | FALSIFIED |

## Historical safety and deviations

The historical pages are retained unchanged and explicitly labeled in
navigation as **Historical rejected baseline**. They are not the current
verifier. The exact judged tree is mirrored byte-for-byte under
`historical/judged-5157b05f/`. No toy result is described as full-scale;
Claim 4 remains blocked despite substantial mechanism evidence.
