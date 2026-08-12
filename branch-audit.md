# Branch audit — consistent adversarial attacks

This ledger records the branch cleanup for the high-dimensional linear-classification reproduction.

## Initial remote snapshot

- Repository: MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea
- Default branch: main
- Main before cleanup: 14e7f57c87c53c6345117ef9fddcdf04542d053c
- Reachable commits before cleanup: 10
- Remote branches before cleanup: main plus 8 ORX branches
- Current scientific evidence tip: 3688690d5ee0a644b06807b0dd6d0525be19edcc

## Identity policy

Every reachable commit will use this exact author and committer identity:

    MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>

The pre-cleanup history contains Dinesh Jinjala author/committer records and one GitHub noreply committer. The rewrite changes identity metadata only; file content and branch roles are preserved.

## Branch rename map

| Old remote branch | New remote branch | Purpose |
| --- | --- | --- |
| main | main | Canonical documentation, reports, evidence, and evaluator surface |
| orx/judged-baseline-regression | audit/proposition-1-baseline | Proposition 1 baseline and regression |
| orx/claim-2-printed-formula-audit | audit/theorem-3-1-printed-formula | Theorem 3.1 sign audit |
| orx/latent-theorem-integrity-audit | audit/latent-theorem-integrity | Theorem 4.1 main/appendix comparison |
| orx/metric-quantifier-and-specification-audit | audit/metric-quantifier-specification | Figure 5 contract and Theorem 4.2 event audit |
| orx/claim-4-scaling-ambiguity | audit/claim-4-scaling-ambiguity | Conflicting latent-noise scaling route |
| orx/claim-4-mechanism-decomposition | audit/claim-4-mechanism-decomposition | Exact clean-plus-boundary decomposition |
| orx/claim-4-falsification-eligibility | audit/claim-4-falsification-eligibility | Mandatory source-faithful counterexample eligibility route |
| orx/evaluator-visible-release-candidate | release/evaluator-visible-candidate | Current release and visibility gates |

## Cleanup checks

Before publication:

- [x] README explains the paper, claims, evidence paths, branches, citation, and thank-you note.
- [x] STATUS.md records the scientific and publication checkpoints.
- [x] AUTONOMOUS_STATE.json records the next action and pinned sources.
- [x] Target repository name is available.
- [ ] Rewrite reachable commit identities.
- [ ] Rename the GitHub repository.
- [ ] Push descriptive branches and remove old ORX names.
- [ ] Verify remote main, branch inventory, README blob, JSON parsing, and commit identities.

The final published state will be appended below after remote verification.
