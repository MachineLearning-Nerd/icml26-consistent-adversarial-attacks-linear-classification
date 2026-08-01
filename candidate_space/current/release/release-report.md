# Release forecast and gate report

- Previous live judged score: `3/10`
- Conservative projected score range after the proposed change: `5–8/10`
- Best-supported possible new score: `8/10` (**forecast, not a judge result**)

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 2 | 2 | HIGH | VERIFIED | 400/400 geometry certificates; cumulative regression. |
| 2 | 1 | 2 | HIGH | FALSIFIED | Printed sign counterexample, 4M draws, `d=512`; intended-typo interpretation risk. |
| 3 | 0 | 2 | HIGH | FALSIFIED | Displayed system unclosed and conflicts with Appendix (119); erratum interpretation risk. |
| 4 | 0 | 0 | LOW | BLOCKED | Four routes complete; exact Figure 5 contract cannot be reconstructed or falsified. |
| 5 | 0 | 2 | HIGH | FALSIFIED | General event proof and 2M draws; intended-typo interpretation risk. |

Current total score: `3/10`. Conservative projected total: `5–8/10`.
Best-supported possible total: `8/10` forecast.

Claims 2, 3, and 5 changed since the previous judge result. Claim 4 remains
BLOCKED because its loss, link, evaluation budget, tuning domain, seeds,
large-`psi` threshold, uncertainty rule, and authoritative noise scaling are
not published.

The exact publication action, only after all gates pass, is a text-only update
to the existing `DineshAI/PUIivg3GrO` Space, followed by a fresh download and
hash/navigation audit, then a mirror of the published text paths to GitHub
`main`. No second Space will be created. The live score must remain reported as
3/10 until the evaluator records a new verdict.

## Final pre-upload summary

| Claim | Status | Expected points | Confidence | Expected evaluator status |
| --- | --- | ---: | --- | --- |
| 1 | VERIFIED | 2 | HIGH | Full credit retained |
| 2 | FALSIFIED as printed | 2 | HIGH | Full credit possible; interpretation risk |
| 3 | FALSIFIED as printed | 2 | HIGH | Full credit possible; interpretation risk |
| 4 | BLOCKED | 0 | LOW | No credit requested |
| 5 | FALSIFIED as printed | 2 | HIGH | Full credit possible; interpretation risk |

Conservative projected total: `5–8/10`; best-supported possible: `8/10`.
Remaining risk is concentrated in whether the evaluator scores literal printed
statements or silently intended corrections.

## Compute and lineage

The experiment tree is a single descending stack from the Claim 1 baseline
through Claims 2/3/5 and four Claim 4 routes to the release candidate. The
winning scientific branch is `orx/claim-4-falsification-eligibility`, SHA
`3688690d5ee0a644b06807b0dd6d0525be19edcc`.

All seven completed scientific runs used Hugging Face `cpu-upgrade`, reported
64 CPUs and no GPUs, and consumed 198 seconds of provider runtime before the
release-candidate run. Monetary cost is unavailable in the OpenResearch/HF
logs and is not estimated.

The exact judged Space revision is
`5157b05fbbbad2885cd379658d7b58e688863e94`; its original file set remains a
subset of the candidate. Historical evidence pages remain reachable and are
labeled **Historical rejected baseline** in navigation.
