# Review record (public, AI-assisted)

**What this is.** This release merges two independent drafts written in November 2026 that both addressed Conjecture 25 of Garrappa, Gerhold, Popolizio and Simon (2025): one proving the exact boundary near order two (now Theorem B), and one proving the lower-parameter extension for every order in (1,2) (now Theorem A, replacing the first draft's weaker small-β appendix). Neither draft cited the other; this single release carries one priority statement. Before release the merged candidate went through an internal, AI-assisted review: five reviewer roles (editor, methodology, domain, perspective, devil's advocate) run as AI agents, a separate-model adversarial review, a clean replay of every shipped script, one revision round, a re-review, a targeted proof audit and a separate-model audit of every new or rewritten proof. **None of this is human peer review or independent reproduction.**

## Findings and what changed

| Finding | Severity | Resolution |
| --- | --- | --- |
| The dilation-ratio identity F(cq)/F(q) = E[e^{-qT}] was attributed to Garrappa et al. Proposition 3, whose proof displays it only for β = α and says "reasoning exactly as above" for the rest of the band. | Major | New Lemma 2.2 quotes the source locations and writes out the Dynkin/optional-stopping step for the recurrent extension (no positive jumps, so the process hits the level exactly). Reviewers and both audits confirmed it holds on the whole closed band. The source's Γ(α) normalisation misprint in its (2.2) is noted; the constant cancels. |
| Priority framing: the two drafts claimed overlapping refutations. | Major | Two-theorem abstract: Theorem A refutes the lower side for every α in (1,2); Theorem B refutes the upper side near α = 2 and gives the exact answer there. The band's own Bernstein property is credited to Garrappa et al. Remark 4(a); their Remark 4(b) (all-negative zeros, α ≥ 2) is discussed. The unaddressed modulus-inequality equivalence is stated. |
| Self-decomposability scope was blurred between the two results. | Major | Stated precisely: on the band (Lemma 2.2), near order two (Theorem B); below the band elsewhere only infinite divisibility. |
| The neighbourhood of α = 2 is not quantified; no pair above the band is certified. | Major (scope) | Not tractable in this revision (needs interval-certified kernel positivity on a middle time range). Stated plainly; added a numerical boundary curve and a replacement conjecture as evidence, labelled as numerics. |
| Lemma 2.1's limit step needed its smoothness and closure facts stated. | Minor | Real analyticity assumed explicitly; closure of Bernstein functions cited (Schilling–Song–Vondraček). |
| The kernel-recovery lemma left its zero-location hypotheses implicit; Cauchy-estimate radius implicit. | Minor | Hypotheses listed; explicit radius η = sin(π/36)/2 with the geometric reason. |
| Readability for non-specialists. | Minor | Added a reader's guide (why it matters, what was known, what is new, a section map) and a proof overview. |
| Shipped scripts relied on `assert`. | Minor | Replaced by explicit checks; `verify.py` adds a negative control and runs under `python -O`. |
| Conjecture wording presupposed global continuation. | Minor | Reworded; the missing ingredients for a proof are listed. |

## Checks that came back clean

The tangent b'(2) was recomputed independently (to 40-60 digits) by several reviewers; the sector-angle bookkeeping, Rouché counts, Pringsheim necessity argument, the log-convexity bound excluding β ≥ 10, and the compactness step were checked line by line; both shipped scripts replayed identically from a fresh copy.
