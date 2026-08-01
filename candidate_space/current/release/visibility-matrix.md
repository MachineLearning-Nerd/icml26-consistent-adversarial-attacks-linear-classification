# Evaluator-visible audit

Traversal entrypoint: `candidate_space/README.md` → logbook navigation →
`pages/current-verification/page.md`. Repository knowledge and OpenResearch
logs are not needed to locate the evidence below.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current verification | Yes | Yes | Yes | Yes | Yes | Proposition 1 ℓ₂ strict scope | VERIFIED |
| 2 | Current verification | Yes | Yes | Yes | Yes | Yes | Theorem 3.1 eqs. (24)–(25) as printed | FALSIFIED |
| 3 | Current verification | Yes | Yes | Yes | Yes | Yes | Theorem 4.1 eqs. (37)–(42) as printed | FALSIFIED |
| 4 | Current verification | Yes | Yes | Yes | Yes | Yes | Section 4.3/Figure 5 exact available contract | BLOCKED |
| 5 | Current verification | Yes | Yes | Yes | Yes | Yes | Theorem 4.2 eqs. (43)–(44) as printed | FALSIFIED |

The two-pass evaluator-blind review, including every file opened and the first
round's rejected conclusion, is recorded in [red-team.md](red-team.md). No
conclusion requires an unpublished branch or hidden dashboard artifact. The
old Verification run is visibly labeled Historical rejected baseline and is
not the default.
