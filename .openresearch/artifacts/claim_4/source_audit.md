# Claim 4 source audit — route 1

Section 4.3 confines the directional statement to an undefined “large psi
regime.” Figure 5 specifies `d=500`, ten realizations, `s=infinity`, `r=2`,
and plotted alpha/psi values. It does not give the evaluation perturbation
budget, loss, link, hyperparameter search domain, optimizer tolerance, seeds,
raw values, a large-psi threshold, or an effect-size/uncertainty criterion.

The latent model is also internally ambiguous: equation (28) specifies
`u~N(0,I_p/p)`, while Assumption 4.2 specifies `u~N(0,I_p)`. These sequences
have different high-dimensional signal-to-noise scaling.

The figure caption calls the curves solutions of malformed equations (37),
(39), and (40). Route 1 therefore cannot derive a unique executable contract
without silently selecting corrections and experimental settings.
