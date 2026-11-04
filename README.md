# Reciprocal Mittag–Leffler functions: complete monotonicity below the parameter band, and the exact boundary near order two

Author: Anonymous. Text CC0-1.0; code MIT (see `LICENSE.md`). This is an unrefereed research candidate. Its review was internal and AI-assisted (see `REVIEW_SUMMARY.md`), not human peer review.

## In one paragraph

The Mittag–Leffler function $E_{\alpha,\beta}(z)=\sum_k z^k/\Gamma(\alpha k+\beta)$ generalises the exponential and appears in fractional differential equations, anomalous relaxation and the hitting times of self-similar Markov processes. When its reciprocal $1/E_{\alpha,\beta}$ is *completely monotone* (derivatives alternate in sign), it is, after normalisation, the Laplace transform of a probability distribution. Garrappa, Gerhold, Popolizio and Simon (2025, Conjecture 25) proposed that for $1<\alpha<2$ this happens exactly when $\beta\in[\alpha-1,\alpha]$. **This paper shows the band is too small, on both sides.**

## Main results

- **Theorem A (all orders $1<\alpha<2$).** For $0<\beta\le\alpha$, $\log[\Gamma(\beta)E_{\alpha,\beta}]$ is a Bernstein function, so every positive power of the normalised reciprocal is the Laplace transform of an infinitely divisible law. This covers the whole triangle $0<\beta<\alpha-1$ below the band. The proof is short: a dilation-ratio identity contained in the proof of Garrappa et al.'s Proposition 3, plus the recurrence $E_{\alpha,\beta}=\beta E_{\alpha,\beta+1}+\alpha zE'_{\alpha,\beta+1}$.
- **Theorem B (near $\alpha=2$).** For $\alpha$ in a neighbourhood of 2 the admissible set is exactly $(0,b(\alpha)]$, with $b$ real analytic, $b(2)=3$ and
  $b'(2)=1+\dfrac{2\pi\,\mathrm{Si}(2\pi)}{2\int_0^{2\pi}(1-\cos u)\,du/u}=2.8276817311\ldots$
  The boundary is where two negative zeros near $-4\pi^2$ collide; the laws are self-decomposable. Since $b(\alpha)>\alpha$ just below 2, the band also fails above.
- **Numerics (not proof).** A 40-digit continuation of the double-zero curve over $1.5\le\alpha\le2.5$, and a replacement conjecture $\mathcal C_\alpha=(0,b(\alpha)]$ for $1<\alpha<2$.
- **Certificate.** Exact rational arithmetic shows the global modulus inequality fails at $(\alpha,\beta,z)=(3/2,1/4,-60+i)$, where Theorem A gives complete monotonicity.

## What is not proved

The size of the neighbourhood in Theorem B (no specific pair above the band is certified); the classification away from $\alpha=2$; whether the band is exactly where the global modulus inequality holds. Two inputs are cited, not reproved: the hitting-time construction of Garrappa et al. and the order-two zero theorem. Historical priority is not established (an SSRN preprint by Polson, 2026, was readable only at abstract level).

## Files

| File | Contents |
| --- | --- |
| `manuscript.pdf`, `manuscript.md` | The paper with all proofs (PDF built by `build_pdf.py`, pandoc + tectonic; `build/header.tex`). |
| `verify.py` | Runs all finite checks; explicit failures (valid under `python -O`); includes a negative control. |
| `verification_results.json` | Output of the final run. |
| `code/verify_mittag_boundary.py` | Exact reciprocal coefficients at order two; 90-digit check of the tangent $b'(2)$ (standard library). |
| `code/certify_example.py` | Exact rational certificate of the modulus-inequality failure (standard library). |
| `code/boundary_curve.py`, `code/boundary_curve.json` | Numerical continuation of the boundary curve (mpmath). |
| `requirements.txt` | Pinned dependency (mpmath 1.4.1). |
| `novelty_report_boundary.md`, `novelty_report_lower_parameter.md`, `target_*.yaml` | Dated, bounded prior-art audits and machine-readable targets of the two source drafts merged here. |
| `REVIEW_SUMMARY.md` | Review findings and what changed. |
| `AI_INDEX.md`, `RESEARCH_GATES.json`, `MANIFEST.sha256` | Package index, gate record, checksums. |
| `refs.bib`, `refs/crossref_records.jsonl` | Bibliography and the Crossref/arXiv records it was copied from. |
| `CITATION.cff`, `.zenodo.json` | Citation and archive metadata. |
| `.github/workflows/replay.yml` | CI replay (with and without `-O`). |

## Reproduce

```bash
python -m pip install -r requirements.txt
python -I -B -O verify.py --output verification_results.json
```

The run takes a few minutes (the curve continuation dominates). **The theorems rest on the written proofs, not on these finite checks.**

## How to cite

Anonymous (2026). *Reciprocal Mittag–Leffler functions: complete monotonicity below the parameter band, and the exact boundary near order two*. Version 0.1.0-candidate. Evidence Press, unrefereed candidate. https://doi.org/10.5281/zenodo.23934934

- Version DOI: [10.5281/zenodo.23934934](https://doi.org/10.5281/zenodo.23934934); concept DOI (all versions): [10.5281/zenodo.23934933](https://doi.org/10.5281/zenodo.23934933)
- Repository: <https://github.com/ipitchford/reciprocal-mittag-leffler-complete-monotonicity>; release page: <https://evidencepress.org/releases/reciprocal-mittag-leffler-complete-monotonicity/>
