# Source audit

## Paper identity

| Field | Record |
| --- | --- |
| Title | On the existence of consistent adversarial attacks in high-dimensional linear classification |
| Authors | Matteo Vilucchio; Lenka Zdeborová; Bruno Loureiro |
| Primary paper | [arXiv:2506.12454v1](https://arxiv.org/abs/2506.12454) |
| OpenReview record | [PUIivg3GrO](https://openreview.net/forum?id=PUIivg3GrO) |
| Submitted | 14 June 2025 |
| Venue record | ICML 2026, as listed by arXiv |
| HTML source | https://ar5iv.labs.arxiv.org/html/2506.12454 |
| HTML SHA-256 | 83b475d685ce1c7b0988d027f3ad3d8e0ff95afeeb583bdd58f0a31bca7f8696 |
| PDF source | https://arxiv.org/pdf/2506.12454 |
| PDF SHA-256 | d57224430f16e29eca731470f2a756428aa2f53b2c9001dfb3a04ccd1d4f23ce |
| Retrieval | 2026-08-02, Asia/Kolkata |
| User-Agent | OpenResearch-Reproduction/1.0 |

The source version used by the evidence is arXiv v1. The original source audit
under .openresearch/artifacts/claim_1/source_audit.md records the same hashes
and the explicit retrieval boundary.

## Claim anchors

| Claim | Anchor | Scope used by this repository |
| --- | --- | --- |
| C1 | Section 3.1, Proposition 1, equations (9)–(12) | l2, dimension 64, strict non-boundary numerical certificate. |
| C2 | Theorem 3.1 equations (24)–(27), Definition 2, Lemma 1 | Literal printed indicator versus definition-faithful signed-margin condition. |
| C3 | Theorem 4.1 equations (37)–(42), Appendix D equation (119) | Closure and appendix consistency of the displayed latent system. |
| C4 | Section 4.3 and Figure 5 right panel | Source completeness, scaling ambiguity, decomposition, and counterexample eligibility. |
| C5 | Theorem 4.2 equations (43)–(44) | Dependency and printed-indicator consistency for latent error metrics. |

## Literal-versus-intended boundary

The repository reports a literal verdict when the displayed equation or
system fails its stated contract. A plausible sign repair in Theorem 3.1, an
appendix-consistent repair in Theorem 4.1, or a guessed Figure 5 setting is
documented as a control or possible interpretation, never silently promoted
to the paper's claim.

## Implementation provenance

No separate author implementation is pinned in the source audit. The
repository contains an independent verifier and a committed evidence package.
The historical judged revision is preserved under
candidate_space/historical/judged-5157b05f/.

## Repository identity

- Former repository:
  icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea
- Canonical repository:
  [MachineLearning-Nerd/icml26-consistent-adversarial-attacks-linear-classification](https://github.com/MachineLearning-Nerd/icml26-consistent-adversarial-attacks-linear-classification)
- Canonical branch: main
- Repository homepage: https://arxiv.org/abs/2506.12454
