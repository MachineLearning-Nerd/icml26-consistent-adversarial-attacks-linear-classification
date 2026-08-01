# Claims


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_305bf98bbdfb", "created_at": "2026-07-31T05:03:35+00:00", "title": "Claims to reproduce"}
-->
## Claims to reproduce

1. Proposition 1 gives the geometric existence condition for a consistent (label-preserving) adversarial attack: ε·d*_q*(ŵ_⊥) ≥ |⟨ŵ,x⟩|, where ŵ_⊥ is the component of the classifier orthogonal to the ground-truth direction (Section 3.1, Proposition 1).
2. Theorem 3.1 shows that, for the well-specified Gaussian model, the consistent robust-error and consistent boundary-error metrics concentrate to closed-form integrals depending on √(q-m²), in contrast to the standard (inconsistent) robust error which depends on √q, formally explaining why consistent attacks are less effective at fixed perturbation budget (Section 3.3, Theorem 3.1).
3. Theorem 4.1 characterizes the asymptotic robust-ERM performance in a latent-space (misspecified) linear classification model via a system of self-consistent equations in the proportional limit n,p,d→∞, distinguishing underparameterized (γ≤1) from overparameterized (γ>1) regimes (Section 4.2, Theorem 4.1).
4. Section 4.3 shows overparameterization has a dual effect: the consistent boundary error E_bnd^cns increases with overparameterization (greater vulnerability to label-preserving attacks), while the aggregate consistent robust error E_rob^cns decreases because overparameterization improves clean generalization (Section 4.3).
5. Theorem 4.2 gives the exact asymptotic characterization of the consistent error metrics (E_rob^cns and E_bnd^cns) for the latent-variable classification model under misspecification (Section 4.2, Theorem 4.2).
