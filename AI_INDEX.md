# AI index: reciprocal Mittag-Leffler functions, complete monotonicity (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with [README.md](README.md) and the paper [manuscript.pdf](manuscript.pdf) (source [manuscript.md](manuscript.md)).
Version DOI 10.5281/zenodo.23934934; concept DOI 10.5281/zenodo.23934933.

## Notation

E_{a,b}(z) = sum_k z^k / Gamma(a k + b). Q = Gamma(b) E_{a,b}, Phi = log Q. C_a = {b > 0 : 1/E_{a,b} completely monotone on (0,inf)}.
GGPS25 = Garrappa, Gerhold, Popolizio, Simon, JMAA 551 (2025) 129588, arXiv:2410.11852v4. Conjecture 25: for 1<a<2, band b in [a-1,a] <=> 1/E CM <=> global |E(z)| >= E(Re z).

## Claims and where they are proved

| ID | Claim | Location in [manuscript.md](manuscript.md) | Evidence type |
|---|---|---|---|
| C1 | Theorem A: for 1<a<2 and 0<b<=a, Phi is Bernstein; Q^{-r} is an infinitely divisible probability Laplace transform | Section 2 (Lemmas 2.1, 2.2, recurrence (2.1)) | proof; band case b in [a-1,a] is GGPS25 Remark 4(a) |
| C2 | Dilation ratios F(cq)/F(q) are probability Laplace transforms for seeds on the band | Lemma 2.2 | proof from the GGPS25 Prop. 3 construction (cited input) |
| C3 | Corollary 2.3: for 0<b<a-1, 1/E CM but global modulus inequality fails | Corollary 2.3; Appendix | proof + exact rational certificate at (3/2, 1/4, -60+i) |
| C4 | Theorem B: C_a = (0, b(a)] for a near 2, b analytic, b(2)=3; self-decomposable laws | Sections 3-9 | proof (uses the order-two zero theorem cited from GGPS25) |
| C5 | b'(2) = 1 + a Si(a)/(2 I(a)), a = 2 pi, = 2.82768173110428... | Section 10 | proof; 90-digit series check |
| C6 | C_2 = (0,3] | Lemma 5.1 | proof |
| C7 | Numerical double-zero curve on 1.5<=a<=2.5; b(a)>a on computed a<2 | Section 12 | numerics only (mpmath, 40 digits) |
| C8 | Conjecture 12.1: C_a = (0,b(a)] for all 1<a<2 | Section 12 | conjecture |

## Verification artefacts

- [verify.py](verify.py) -> [verification_results.json](verification_results.json): runs [code/verify_mittag_boundary.py](code/verify_mittag_boundary.py) (exact coefficients, tangent), [code/certify_example.py](code/certify_example.py) (exact rational certificate), [code/boundary_curve.py](code/boundary_curve.py) (curve, compared with [code/boundary_curve.json](code/boundary_curve.json)) and a negative control. Explicit failures, valid under python -O. Scope: finite checks only.
- Pinned packages: [requirements.txt](requirements.txt). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml).

## Sources, novelty and review record

- [refs.bib](refs.bib), [refs/crossref_records.jsonl](refs/crossref_records.jsonl): bibliography and registry records.
- [novelty_report_boundary.md](novelty_report_boundary.md), [novelty_report_lower_parameter.md](novelty_report_lower_parameter.md): dated bounded prior-art audits of the two merged drafts; [target_boundary.yaml](target_boundary.yaml), [target_lower_parameter.yaml](target_lower_parameter.yaml).
- [RESEARCH_GATES.json](RESEARCH_GATES.json); [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md); [MANIFEST.sha256](MANIFEST.sha256); [LICENSE.md](LICENSE.md); [CITATION.cff](CITATION.cff); [.zenodo.json](.zenodo.json).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or proof-assistant formalisation. Theorem B's neighbourhood is not quantified. The band <=> modulus-inequality leg of Conjecture 25 is not addressed. Priority holds only within a bounded search (Polson 2026, SSRN, abstract only).
