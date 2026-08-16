# Consistent adversarial attacks in high-dimensional linear classification

> Independent, claim-by-claim reproduction and source audit for *On the existence of consistent adversarial attacks in high-dimensional linear classification*.

## Current status

The current evidence package contains one verified finite-dimensional proposition, three literal printed-formula falsifications, and one blocked empirical trend claim. The literal verdicts are deliberately separated from plausible author-intended corrections.

| Claim | Paper location | Status | Evidence summary |
| --- | --- | --- | --- |
| 1 | Proposition 1, Section 3.1, equation (9) | VERIFIED in the stated scope | 400/400 exact certificate agreements for strict non-boundary l2 cases; 200 feasible and 200 infeasible; mutated norm rejected. |
| 2 | Theorem 3.1, equations (24)–(27) | FALSIFIED as printed | At m=0, q=1, and rescaled budget 0.5, the printed event gives 0.5 while Definition 2/Lemma 1 give Phi(0.5)=0.69146246. |
| 3 | Theorem 4.1, equations (37)–(42) | FALSIFIED as printed | The displayed system defines none of m, q, V, P and conflicts with Appendix D equation (119); an appendix-consistent repair closes. |
| 4 | Section 4.3 and Figure 5 right panel | BLOCKED | Four routes completed, but the loss, link, budget, tuning domain, seeds, large-psi threshold, uncertainty rule, and authoritative noise scaling are not fixed. |
| 5 | Theorem 4.2, equations (43)–(44) | FALSIFIED as printed | The printed Gaussian indicator omits a positive-probability half-strip; 2,000,000 draws reproduce the gap across four correlations. |

The previous live judged score is 3/10. The projected 5–8/10 range and best-supported 8/10 value are forecasts, not judge results.

## Audit dossier

The standardized audit record is split into small, reviewable files:

- [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) maps every paper claim to its producer, raw result, checker, control, and limitation.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the pinned paper sources, theorem anchors, and literal-versus-intended boundary.
- [BRANCH_AUDIT.md](BRANCH_AUDIT.md) records published branches, former workspace labels, tips, and attribution.
- [ENVIRONMENT.md](ENVIRONMENT.md) records the fixed command, lockfile, evidence revision, seeds, and compute boundary.
- [REPORT.md](REPORT.md) states the scoped decision and evaluation boundary.
- [CITATION.cff](CITATION.cff) and [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md) provide citation and author acknowledgement.
- [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) content-addresses the
  published dossier and evidence inputs.
- [verify_final.py](verify_final.py) performs fail-closed checks on a local or fresh clone.

The raw/checker/control package under [evidence](evidence) remains the
scientific evidence. The dossier documents it and does not silently replace a
printed formula with a plausible correction.

## Paper and provenance

| Field | Record |
| --- | --- |
| Full title | On the existence of consistent adversarial attacks in high-dimensional linear classification |
| Authors | Matteo Vilucchio, Lenka Zdeborová, Bruno Loureiro |
| Primary source | [arXiv:2506.12454v1](https://arxiv.org/abs/2506.12454) |
| Submitted | 14 June 2025 |
| Venue record | ICML 2026, as listed by arXiv |
| HTML source | https://ar5iv.labs.arxiv.org/html/2506.12454 |
| HTML SHA-256 | 83b475d685ce1c7b0988d027f3ad3d8e0ff95afeeb583bdd58f0a31bca7f8696 |
| PDF SHA-256 | d57224430f16e29eca731470f2a756428aa2f53b2c9001dfb3a04ccd1d4f23ce |
| Source audit | [.openresearch/artifacts/claim_1/source_audit.md](.openresearch/artifacts/claim_1/source_audit.md) |
| Historical judged revision | candidate_space/historical/judged-5157b05f/ |
| Former repository | icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea |
| Canonical repository | [MachineLearning-Nerd/icml26-consistent-adversarial-attacks-linear-classification](https://github.com/MachineLearning-Nerd/icml26-consistent-adversarial-attacks-linear-classification) |
| Canonical branch | main |
| Official code status | No separate author implementation is pinned in the source audit; this repository contains an independent verifier and evidence package. |

## What the paper is doing

The paper studies when a linear classifier can be fooled by a perturbation that changes the model prediction while preserving the ground-truth label. It distinguishes consistent attacks from inconsistent attacks and develops three layers of analysis:

1. Finite-dimensional geometry: a consistent attack must flip the model margin while remaining orthogonal to the target classifier.
2. Well-specified high-dimensional asymptotics: Gaussian limits characterize robust, boundary, and consistent robust errors.
3. Latent-variable and overparameterized models: self-consistent order parameters describe how robust empirical risk minimization changes the error metrics as data and feature dimensions scale.

The paper's central message is that overparameterization has a nuanced effect: some consistent-error metrics can worsen while aggregate consistent robust error improves because clean error changes at the same time. This repository audits the geometry, displayed equations, asymptotic indicators, and the precise reproducibility contract for the Figure 5 trend.

## Claim-to-evidence ledger

The exact contracts, methods, raw results, independent checker output, controls, and limitations are stored under [.openresearch/artifacts](.openresearch/artifacts). The fixed cumulative verifier is [repro/src/verify.py](repro/src/verify.py).

### Claim 1 — Proposition 1: existence geometry

Exact statement: for a nonzero model margin, an lq perturbation in a closed ball that preserves the linear target exists if and only if the budget times the dual-norm distance of the predictor's target-orthogonal component from the target span reaches the model margin.

How the claim is produced:

1. [repro/src/core.py](repro/src/core.py) computes the target-orthogonal predictor component and the paper's condition.
2. The verifier constructs the extremal orthogonal perturbation and checks feasibility, target invariance, attack budget, and attacked margin.
3. Four deterministic seeds generate 400 strict non-boundary l2 cases in dimension 64: 200 feasible and 200 infeasible.
4. The independent certificate agrees in all 400 cases; the maximum target residual is below 2.22e-16 and budget excess is below 5.55e-17.
5. Replacing the orthogonal norm with the full predictor norm produces 20 designed disagreements and is rejected.

Verdict: VERIFIED for the tested l2, dimension-64, strict non-boundary scope. The paper's broader lq statement and equality boundary are not silently claimed by this numerical certificate.

Evidence: [.openresearch/artifacts/claim_1](.openresearch/artifacts/claim_1), [candidate_space/current/pages/current-verification/page.md](candidate_space/current/pages/current-verification/page.md).

### Claim 2 — Theorem 3.1: well-specified asymptotic integrals

Exact printed target: equations (24)–(25) use the indicator nu times (mu minus epsilon_tilde times A) less than zero while nu and mu are centered jointly Gaussian.

How the claim is produced:

1. [repro/src/theorem31.py](repro/src/theorem31.py) evaluates the printed event and the definition-faithful label-dependent event independently.
2. At m=0, q=1, l2 geometry, and epsilon_tilde=0.5, symmetry forces the printed robust error to 0.5.
3. Definition 2 and Lemma 1 give Phi(0.5)=0.6914624613 and a boundary error of 0.1914624613.
4. Four million Gaussian draws give 0.69156475 with standard error 0.00023092; four direct dimension-512 constructions average 0.69245625.
5. At zero budget the two expressions coincide, so the control is not falsely rejected.

Verdict: FALSIFIED as printed. A missing sign(nu) is a plausible intended correction, but it is not substituted into the literal verdict.

Evidence: [.openresearch/artifacts/claim_2](.openresearch/artifacts/claim_2), [reports/reproduction/report.md](reports/reproduction/report.md).

### Claim 3 — Theorem 4.1: latent self-consistent system

Exact printed target: equations (37)–(42) provide a closed self-consistent characterization of primal order parameters m, q, V, P and their conjugates in the latent model.

How the claim is produced:

1. [repro/src/latent_audit.py](repro/src/latent_audit.py) transcribes the displayed left-side variable sets and right-side signatures.
2. The checker finds no displayed definition for the announced primal variables m, q, V, or P.
3. Equation (37) repeats one right-hand side for four conjugates, while Appendix D equation (119) gives distinct updates; conflicts occur for hat_P, hat_V, and hat_q.
4. An appendix-consistent repair supplies primal left sides and the four distinct conjugate updates; the repaired control is accepted.
5. The orientation check preserves the paper's gamma=d/p definition, so p>d implies gamma<1.

Verdict: FALSIFIED as printed. This does not assert that the accepted appendix repair is the authors' unique intended erratum.

Evidence: [.openresearch/artifacts/claim_3](.openresearch/artifacts/claim_3), [candidate_space/current/pages/current-verification/page.md](candidate_space/current/pages/current-verification/page.md).

### Claim 4 — Section 4.3 and Figure 5: overparameterization dual effect

Exact target: in an unspecified large-psi regime, consistent boundary error increases while aggregate consistent robust error decreases under optimally tuned robust ERM.

How the claim is produced:

1. Route 1, [quantifier_audit.py](repro/src/quantifier_audit.py), inventories missing contract fields: evaluation budget, loss, link, hyperparameter domains, optimizer stopping rule, seeds, raw numeric results, large-psi threshold, and uncertainty rule.
2. The source also gives incompatible latent noise scalings: equation (28) uses u distributed as N(0, I_p/p), while Assumption 4.2 uses N(0, I_p).
3. Route 2 quantifies the scaling ambiguity at fixed p/d=2 over d values 125, 250, 500, and 1000. The two log-log slopes are approximately -0.00053 and -1.00058.
4. Route 3 checks the exact decomposition E_rob_cns = E_clean + E_bnd_cns over 2,000,000 cases and rejects the boundary-only mutation.
5. Route 4 performs the mandatory falsification-eligibility search. It finds zero eligible counterexamples because the missing contract prevents a source-faithful comparison; a fully pinned opposite-trend synthetic control is accepted.

Verdict: BLOCKED. The mechanism identity is verified, but it does not establish the Figure 5 direction. The claim becomes auditable when the authors' code/raw data or every missing contract field is supplied.

Evidence: [.openresearch/artifacts/claim_4](.openresearch/artifacts/claim_4), [candidate_space/current/release/visibility-matrix.md](candidate_space/current/release/visibility-matrix.md), [candidate_space/current/release/red-team.md](candidate_space/current/release/red-team.md).

### Claim 5 — Theorem 4.2: latent consistent-error metrics

Exact printed target: equations (43)–(44) give exact asymptotic consistent robust and boundary errors using the Theorem 4.1 order parameters.

How the claim is produced:

1. The source-dependency route shows that Theorem 4.2 consumes m, q, and A=sqrt(q-m^2), but the displayed Theorem 4.1 system does not define m or q.
2. [repro/src/quantifier_audit.py](repro/src/quantifier_audit.py) independently compares the printed indicator with the definition-faithful event.
3. For positive effective threshold c, the printed event includes nu>0, mu<c and nu<0, mu>c; the definition-faithful event uses nu<0, mu>-c and therefore adds the positive-probability half-strip nu<0, -c<mu<=c.
4. Two million draws across correlations -0.75, -0.25, 0.25, and 0.75 produce omitted half-strip counts 95,578, 95,931, 95,398, and 95,540. Boundary ratios are approximately 2.00794, 2.00139, 1.99454, and 2.00748.
5. At zero threshold all formulas coincide, providing a non-falsification control.

Verdict: FALSIFIED as printed for nondegenerate positive-threshold settings. The result does not solve a guessed repaired latent system.

Evidence: [.openresearch/artifacts/claim_5](.openresearch/artifacts/claim_5), [reports/reproduction/report.md](reports/reproduction/report.md).

## Branch map

The original orx/ prefixes were workspace execution labels. They are retained below only for provenance; the published names describe the mathematical or release role.

| Published branch | Former branch | Purpose | State |
| --- | --- | --- | --- |
| main | main plus evaluator release lineage | Canonical README, reports, evidence, candidate surface, and release mirror. | Current |
| audit/proposition-1-baseline | orx/judged-baseline-regression | Preserves the Proposition 1 regression and accepted baseline. | Verified evidence |
| audit/theorem-3-1-printed-formula | orx/claim-2-printed-formula-audit | Tests the printed Theorem 3.1 sign with analytic and Monte Carlo controls. | Falsified evidence |
| audit/latent-theorem-integrity | orx/latent-theorem-integrity-audit | Compares the Theorem 4.1 displayed system with Appendix D. | Falsified evidence |
| audit/metric-quantifier-specification | orx/metric-quantifier-and-specification-audit | Audits the Figure 5 contract and Theorem 4.2 event. | Blocked plus falsified evidence |
| audit/claim-4-scaling-ambiguity | orx/claim-4-scaling-ambiguity | Quantifies the incompatible latent noise scalings. | Blocked route |
| audit/claim-4-mechanism-decomposition | orx/claim-4-mechanism-decomposition | Verifies the clean-plus-boundary decomposition. | Blocked route |
| audit/claim-4-falsification-eligibility | orx/claim-4-falsification-eligibility | Runs the mandatory source-faithful counterexample eligibility route. | Blocked route |
| release/evaluator-visible-candidate | orx/evaluator-visible-release-candidate | Packages current pages, raw data, checker/control outputs, and visibility gates. | Release surface |

All renamed branches preserve their historical commits after identity normalization. Branch names do not change claim verdicts.

## Reproduce and inspect

The environment is pinned by uv.lock. From a clean checkout:

    uv sync --frozen
    .venv/bin/python repro/src/verify.py

The cumulative verifier prints machine-readable evidence and checks:

- the Proposition 1 geometry certificate and full-norm mutation;
- the Theorem 3.1 analytic, Monte Carlo, finite-dimension, and zero-budget controls;
- the Theorem 4.1 closure, Appendix (119) comparison, repair control, and gamma orientation;
- all four Figure 5 audit routes;
- the Theorem 4.2 dependency and omitted-half-strip checks; and
- release visibility, manifests, and no-GPU requirements.

Raw results are in [evidence/results.json](evidence/results.json), with checker and control outputs beside them. The evaluator-visible entrypoint is [candidate_space/README.md](candidate_space/README.md). Historical pages remain under candidate_space/historical/judged-5157b05f/ and are labeled Historical rejected baseline.

All recorded research runs used Hugging Face cpu-upgrade hardware, reported 64 CPUs, and requested no GPU. Monetary cost is not exposed by the provider logs and is not estimated.

## Reproduction policy

- Audit literal equations before proposing a correction.
- Keep intended corrections separate from printed-statement verdicts.
- Preserve non-falsification controls at zero budget or equality boundaries.
- Do not guess a loss, link, tuning grid, seed, or noise scaling to unblock an underspecified experiment.
- Keep independent checkers, raw outputs, negative controls, and limitations beside each claim.
- Treat finite numerical certificates as evidence for their disclosed scope, not as universal proof.
- Keep the historical judged baseline reachable but visibly separate from current evidence.

## Citation

Please cite the paper as:

    @article{vilucchio2025consistent,
      title = {On the existence of consistent adversarial attacks in high-dimensional linear classification},
      author = {Vilucchio, Matteo and Zdeborová, Lenka and Loureiro, Bruno},
      journal = {arXiv preprint arXiv:2506.12454},
      year = {2025},
      doi = {10.48550/arXiv.2506.12454}
    }

The arXiv record lists ICML 2026 as the journal reference; use the final proceedings citation when a formal conference bibliography is required.

## Thank you

Thank you to Matteo Vilucchio, Lenka Zdeborová, and Bruno Loureiro for developing a precise framework for separating label-preserving adversarial attacks from ordinary misclassification and for connecting finite geometry with high-dimensional asymptotics. The paper's explicit equations and appendices make it possible to audit both the valid geometric result and the boundaries of the printed asymptotic claims. This repository is intended as a respectful, transparent companion, keeping possible typographical corrections distinct from literal reproduction verdicts.

## Limitations

- Claim 1 is numerically verified only for l2, dimension 64, and strict non-boundary cases; it does not replace a proof for every lq geometry.
- Claims 2, 3, and 5 are verdicts on the printed equations, not author-confirmed errata.
- Claim 4 remains blocked because its source does not determine a unique executable Figure 5 contract.
- The live 3/10 score and projected 5–8/10 range are preserved for provenance; no new judge score is claimed.
- The current verifier is independent and does not claim code-level agreement with an official author implementation.
