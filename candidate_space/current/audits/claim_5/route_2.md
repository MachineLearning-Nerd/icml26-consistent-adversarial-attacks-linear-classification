# Route 2 — general indicator proof

Let `c=epsilon_tilde*A^(1/s_star)>0`. For the centered nondegenerate joint
Gaussian pair declared by Theorem 4.2, equation (43) prints

`{nu>0, mu<c} union {nu<0, mu>c}`.

Definition 2 and the latent attack geometry require

`{nu>0, mu<c} union {nu<0, mu>-c}`.

The printed formula omits `{nu<0, -c<mu<=c}`, an open-region event with
strictly positive probability. For boundary error, central symmetry makes the
positive- and negative-label attacked-correct regions equiprobable, while
equation (44) retains only the positive-label region.

The checker tests correlations `-0.75`, `-0.25`, `0.25`, and `0.75` with two
million samples total. At `c=0` the expressions must coincide, preventing a
checker that rejects every formula.
