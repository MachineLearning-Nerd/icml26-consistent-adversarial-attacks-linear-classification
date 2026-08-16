# Branch audit

Published branch names describe their mathematical or release role. Former
orx/ names are retained only as migration provenance; no final remote branch
uses that prefix.

## Pre-dossier snapshot

- Repository: MachineLearning-Nerd/icml26-consistent-adversarial-attacks-linear-classification
- Former repository:
  MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea
- Default branch: main
- Main tip before this dossier: 48cdacb0831167e621f8c999f08c210b40f720c8
- Reachable commits before this dossier: 13 unique commits
- Remote branches before this dossier: 9
- Recovery bundle:
  /tmp/icml-adversarial-before-dossier.aBJ6Ya/adversarial-before-dossier.bundle
- Recovery bundle SHA-256:
  71f83eaf283004a9b1c356521a9a5ea2b2039381ba752a0a7a8d36e89991a0d2
- The bundle was verified complete and contained 20 local/remote refs.

## Final branch map

| Final branch | Former branch | Evidence role | Pre-dossier tip |
| --- | --- | --- | --- |
| main | main plus evaluator release lineage | Canonical README, reports, evidence, candidate surface, and dossier | 48cdacb0831167e621f8c999f08c210b40f720c8 |
| audit/proposition-1-baseline | orx/judged-baseline-regression | Proposition 1 baseline and regression | dd29c7fa8a2bb59d61d931229948943520c7cd09 |
| audit/theorem-3-1-printed-formula | orx/claim-2-printed-formula-audit | Theorem 3.1 sign audit | b8b521ea65653cf75736d213eef5f47511cfa873 |
| audit/latent-theorem-integrity | orx/latent-theorem-integrity-audit | Theorem 4.1 main/appendix comparison | ddfdec33ef2c5c0a1bfcd191a9d68fccf77b310b |
| audit/metric-quantifier-specification | orx/metric-quantifier-and-specification-audit | Figure 5 contract and Theorem 4.2 event audit | 6cfb2cb7e7a365d6ace53445c3c5127f2fedc74f |
| audit/claim-4-scaling-ambiguity | orx/claim-4-scaling-ambiguity | Conflicting latent-noise scaling route | 1e1234052b2e6aafc01f47777ea830e0c576fcb2 |
| audit/claim-4-mechanism-decomposition | orx/claim-4-mechanism-decomposition | Exact clean-plus-boundary decomposition | ad3ba3a1bece9d8f0c0b3d1f3cde84f1d4891390 |
| audit/claim-4-falsification-eligibility | orx/claim-4-falsification-eligibility | Source-faithful counterexample eligibility route | e770b5d6254a5c2fed943b3c355577d402b2bf96 |
| release/evaluator-visible-candidate | orx/evaluator-visible-release-candidate | Current release and visibility gates | bb4fae0ff373e56e0a67db50b49a8e01d8b73ab3 |

## Attribution and safety record

Every reachable pre-dossier commit has both author and committer set to:

    MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>

The dossier and checkpoint commits use the same identity. Co-author trailers
are not used. The final verifier checks that no refs/original, legacy orx
reference, or unexpected branch remains after a fresh clone.

Branch names preserve provenance only. They do not change the literal claim
verdicts or turn the evaluator release branch into an official author release.
