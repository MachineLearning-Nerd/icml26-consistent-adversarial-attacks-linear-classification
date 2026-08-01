# Claim 1 source audit

- Retrieved: 2026-08-02 with explicit `OpenResearch-Reproduction/1.0` User-Agent.
- ar5iv HTML: `https://ar5iv.labs.arxiv.org/html/2506.12454`
- ar5iv HTML SHA-256: `83b475d685ce1c7b0988d027f3ad3d8e0ff95afeeb583bdd58f0a31bca7f8696`
- arXiv PDF: `https://arxiv.org/pdf/2506.12454`
- arXiv PDF SHA-256: `d57224430f16e29eca731470f2a756428aa2f53b2c9001dfb3a04ccd1d4f23ce`
- Version: arXiv `2506.12454v1`, dated 14 June 2025.
- Anchor: Section 3.1, Proposition 1, equations (9)–(12).

The proposition quantifies over two linear classifiers, a covariate with
nonzero model margin, and a perturbation in a closed ℓq ball. The baseline
checks ℓ₂ only, where Remark 3 reduces the metric projection to
`||w_hat_perp||_2`. It avoids the equality boundary because the paper states
`>=` in equation (9), uses `>` in its proof, and does not define the decision
rule at zero margin. This deviation is explicit and prevents a convention at
zero from deciding the numerical result.
