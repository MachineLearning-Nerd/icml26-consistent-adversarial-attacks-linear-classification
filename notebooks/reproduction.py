import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Consistent adversarial attacks: an evidence-first reproduction

    **Observed outcomes:** Claim 1 is VERIFIED; Claims 2, 3, and 5 are
    FALSIFIED as printed; Claim 4 is BLOCKED after four routes. The best
    supported score is 8/10 only as a forecast—the live score remains 3/10.

    The central geometric question is whether an attack can flip the learned
    classifier while remaining orthogonal to the ground-truth direction.
    """)
    return


@app.cell
def _():
    evidence = {
        "claim_1": {"status": "VERIFIED", "agreement": "400/400"},
        "claim_2": {"status": "FALSIFIED", "printed": 0.5, "definition": 0.6914624613},
        "claim_3": {"status": "FALSIFIED", "missing": ["m", "q", "V", "P"]},
        "claim_4": {"status": "BLOCKED", "routes": 4},
        "claim_5": {"status": "FALSIFIED", "boundary_ratio": "1.9945–2.0079"},
    }
    return (evidence,)


@app.cell
def _(evidence, mo):
    mo.md(f"""
    ## Headline numerical discrepancy

    At `m=0`, `q=1`, and rescaled budget `0.5`, Theorem 3.1 prints robust
    error **{evidence['claim_2']['printed']}**. The definition and attack
    geometry give **{evidence['claim_2']['definition']}**. Four million draws
    measured `0.69156475`, and four direct dimension-512 checks averaged
    `0.69245625`.

    The difference comes from a missing label-dependent sign. For negative
    ground-truth margin, the worst-case direction must reverse.
    """)
    return


@app.cell
def _(mo):
    correlation = mo.ui.slider(-0.9, 0.9, value=0.0, step=0.05, label="Correlation ρ")
    correlation
    return (correlation,)


@app.cell
def _(correlation, mo):
    mo.md(f"""
    ## Bounded interactive interpretation

    Selected correlation: **{correlation.value:.2f}**.

    For every nondegenerate correlation and every positive threshold `c`, the
    printed Theorem 4.2 event omits `nu<0, -c<mu<=c`. This notebook embeds the
    completed evidence; changing the slider does not rerun formal experiments.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Why one claim is blocked

    Figure 5 omits the evaluation budget, loss/link, tuning domain, seeds,
    numerical large-ψ threshold, and uncertainty rule. Worse, equation (28)
    uses noise covariance `I/p` while Assumption 4.2 uses `I`. At fixed `p/d`,
    these give SNR slopes 0 and −1. Choosing either silently would replace the
    paper's claim with a nearby experiment.

    Formal reproduction command:

    ```bash
    uv sync --frozen && .venv/bin/python repro/src/verify.py
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
