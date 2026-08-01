# Route 4 — mandatory falsification search

## Exact claim

For the optimally tuned robust-ERM setup used in Section 4.3/Figure 5, in an
unstated “large psi” interval, `E_bnd_cns` increases with features while
`E_rob_cns` decreases. The stated setup uses the structured latent Gaussian
model, proportional `n,p,d`, `s=infinity`, Appendix A.1's `r=2`, `d=500`, and
ten finite-dimensional realizations.

## Counterexample eligibility

A falsification must preserve the model, estimator, positive evaluation
budget, loss/link, hyperparameter optimization, `psi` domain, and uncertainty
rule. Four candidates were sought: the historical judged sweep, each of the
two contradictory latent-noise scalings, and a zero-budget construction.
Every candidate is rejected for a recorded assumption mismatch. In
particular, a zero-budget check is vacuous, and choosing either noise scaling
silently contradicts another source definition.

An independent eligibility checker accepts a synthetic fully pinned
opposite-trend certificate, proving that the checker does not reject all
counterexamples.

References consulted for interpretation: the paper's cited ridgeless
least-squares overparameterization work (Hastie et al., 2022) and the cited
empirical adversarial-robustness overview (Chen et al., arXiv:2406.10090).
Neither supplies the missing Figure 5 contract.

Falsification did not succeed. Final status: **BLOCKED**. Author code/raw data
or the missing loss, link, budget, tuning domain, seeds, large-psi threshold,
and uncertainty rule would unblock the claim.
