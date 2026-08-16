# Claim-to-evidence map

This dossier records how each paper claim is produced. The common production
graph is:

    paper anchor -> literal contract -> executable producer
                 -> committed raw result -> independent checker/control
                 -> scoped verdict

The fixed cumulative producer is repro/src/verify.py. Its machine-readable
result is evidence/results.json, with checker-output.json and control-output.json
beside it. candidate_space/current/data contains the evaluator-visible copy of
the same evidence package.

## Evidence boundary

- The source claims are tested literally before any possible author-intended
  correction is considered.
- Raw results, checker results, negative controls, runtime records, and claim
  contracts are committed under .openresearch/artifacts and evidence.
- The scientific evidence was generated at revision
  3688690d5ee0a644b06807b0dd6d0525be19edcc. Later commits in main are
  documentation, metadata, and publication-state changes; they do not
  represent a new scientific rerun.
- Claim 1 is a finite l2, dimension-64, strict non-boundary certificate.
  Claims 2, 3, and 5 are verdicts on the displayed equations. Claim 4 is
  blocked because its Figure 5 contract is not uniquely executable.
- The historical judge score and forecast remain provenance only. No new score,
  official author implementation, or author endorsement is claimed.

## C1 — Proposition 1: existence geometry

Paper anchor: Section 3.1, Proposition 1, equation (9).

Producer path:

1. repro/src/core.py computes the target-orthogonal component of the model
   predictor and the paper's lq condition.
2. repro/src/verify.py::run_proposition_trials constructs the extremal
   target-preserving perturbation and checks feasibility, attack budget,
   target-invariance residual, and attacked margin.
3. Four deterministic seeds generate 100 Gaussian instances each in dimension
   64. The budget factors are 0.25, 0.75, 1.25, and 2 times the exact
   threshold, so equality is not used.
4. The full predictor-norm mutation is required to disagree with the
   independent certificate.

Committed result:

- 400/400 condition-certificate agreements.
- 200 feasible and 200 infeasible cases.
- 20 designed mutation disagreements.
- Maximum target-invariance residual below 2.22e-16 and maximum budget excess
  below 5.55e-17 in the recorded result.

Verdict: VERIFIED in the disclosed l2, dimension-64, strict non-boundary
scope. This finite certificate does not replace the proof for every lq
geometry or settle the source's equality convention.

Evidence: evidence/results.json, evidence/checker-output.json,
evidence/control-output.json, and .openresearch/artifacts/claim_1/.

## C2 — Theorem 3.1: well-specified asymptotic integrals

Paper anchors: Assumptions 3.1–3.3, Theorem 3.1 equations (24)–(27),
Definition 2, and Lemma 1.

Producer path:

1. repro/src/theorem31.py evaluates the printed indicator and the
   definition-faithful label-dependent indicator independently.
2. At m = 0, q = 1, l2 geometry, and rescaled budget 0.5, symmetry makes the
   printed robust value 0.5.
3. Definition 2 and Lemma 1 give Phi(0.5) = 0.6914624613 and boundary error
   0.1914624613.
4. The committed result uses four million bivariate-Gaussian samples and four
   direct dimension-512 constructions. The zero-budget case is a
   non-falsification control.

Committed result:

- Printed robust value: 0.5.
- Definition-faithful robust value: 0.6914624612740131.
- Monte Carlo definition-faithful robust value: 0.69156475.
- Printed boundary: 0.09573123063700656.
- Definition-faithful boundary: 0.19146246127401312.
- Four million samples and finite dimension 512 are recorded in the result.

Verdict: FALSIFIED as printed. A missing sign of nu is a plausible intended
correction, but this repository does not silently substitute it.

Evidence: evidence/results.json, evidence/checker-output.json,
evidence/control-output.json, and .openresearch/artifacts/claim_2/.

## C3 — Theorem 4.1: latent self-consistent system

Paper anchors: Section 4.2, Theorem 4.1 equations (37)–(42), and Appendix D
equation (119).

Producer path:

1. repro/src/latent_audit.py transcribes the displayed left-side variable sets
   and right-side expression signatures.
2. The literal system is checked for defining equations for m, q, V, and P.
3. The four displayed conjugate updates are compared with the distinct
   Appendix (119) updates.
4. The only accepted negative control is an appendix-consistent repair that
   adds the missing primal left sides and distinct conjugate updates.
5. The gamma = d/p orientation is checked independently; p > d means
   gamma < 1.

Committed result:

- Missing primal definitions: P, V, m, and q.
- Appendix conflicts: hat_P, hat_V, and hat_q.
- The literal system is not closed.
- The appendix-consistent repair control is closed and accepted as a control.

Verdict: FALSIFIED as printed. This is not a claim that the appendix repair is
the authors' unique intended erratum.

Evidence: evidence/results.json, evidence/checker-output.json,
evidence/control-output.json, and .openresearch/artifacts/claim_3/.

## C4 — Section 4.3 and Figure 5: overparameterization dual effect

Paper anchor: Section 4.3 and the right panel of Figure 5.

Producer path:

1. repro/src/quantifier_audit.py::audit_claim4_specification inventories the
   missing executable fields: evaluation budget, loss, link, tuning domain,
   optimizer stopping rule, seeds, large-psi threshold, and uncertainty rule.
2. The scaling route compares equation (28) with Assumption 4.2 at p/d = 2
   over d = 125, 250, 500, and 1000.
3. The decomposition route checks
   E_rob_cns = E_clean + E_bnd_cns over two million cases.
4. The falsification-eligibility route searches for a
   source-faithful assumption-satisfying counterexample. A fully pinned
   opposite-trend synthetic specification is a control, not paper evidence.

Committed result:

- Four routes completed.
- Equation (28) signal-to-noise slope: approximately -0.00053328.
- Assumption 4.2 signal-to-noise slope: approximately -1.00058364.
- Decomposition cases: 2,000,000, with residual 0.
- Eligible source-faithful counterexamples: 0.
- Unblocker: author code/raw data, or exact loss, link, evaluation budget,
  tuning domain, seeds, large-psi threshold, uncertainty rule, and noise
  scaling.

Verdict: BLOCKED. The mechanism identity is checked, but the source does not
specify one executable Figure 5 experiment. No guessed settings are promoted
to evidence.

Evidence: evidence/results.json, evidence/checker-output.json,
evidence/control-output.json, .openresearch/artifacts/claim_4/, and
candidate_space/current/release/visibility-matrix.md.

## C5 — Theorem 4.2: latent consistent-error metrics

Paper anchors: Section 4.2, Theorem 4.2 equations (43)–(44), with Definition 2
and Lemma 1 as the definition-faithful reference.

Producer path:

1. The dependency route checks whether Theorem 4.1 defines m, q, and
   A = sqrt(q - m^2) before Theorem 4.2 uses them.
2. The indicator route compares the printed
   nu times (mu minus epsilon times A) condition with the
   sign(nu) times mu condition.
3. Two million samples across correlations -0.75, -0.25, 0.25, and 0.75
   count the omitted positive-probability half-strip.
4. The zero-threshold control verifies that the formulas coincide at the
   boundary.

Committed result:

- Omitted half-strip counts: 95,578; 95,931; 95,398; and 95,540.
- Boundary ratios: approximately 2.00794, 2.00139, 1.99454, and 2.00748.
- Two million samples and all four correlations are recorded.

Verdict: FALSIFIED as printed for nondegenerate positive-threshold settings.
This route does not solve a guessed repaired Theorem 4.1 system.

Evidence: evidence/results.json, evidence/checker-output.json,
evidence/control-output.json, and .openresearch/artifacts/claim_5/.

## Overall decision

Claim 1 is VERIFIED in its disclosed finite scope; Claims 2, 3, and 5 are
FALSIFIED as printed; Claim 4 is BLOCKED. Literal equations, likely intended
corrections, and historical evaluation provenance remain separate.
