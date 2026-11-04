# Novelty-gate report: lower-parameter extension for reciprocal Mittag–Leffler functions

**Search date:** 2 November 2026.  
**Researcher/agent:** Analysis scout in a multi-agent research session.  
**Corpus boundary:** Live primary-source web searches with two search engines; arXiv, Numdam, author webpages, publisher records, NIST DLMF and SSRN abstract metadata. No MathSciNet or zbMATH subscription search; no author enquiry.  
**Intended contribution unit:** A positive-parameter extension of a complete-monotonicity theorem and refutation of one equivalence in an explicitly numbered published conjecture; a separate finite certificate.

## 1. Frozen claim

### Exact statement

For every real 1<alpha<2 and every real 0<beta<=alpha, log[Gamma(beta) E_{alpha,beta}(q)] is Bernstein for all q>0. Thus every positive power of its reciprocal is completely monotone. For beta=0, all positive powers of the unnormalised reciprocal remain completely monotone. The proposed extension is the open triangle 0<beta<alpha-1.

### Exclusions

No full beta>alpha classification; no resolution of the remaining global-modulus conjecture within beta in [alpha-1,alpha]; no resolution of Conjecture 26; no novelty claim for the Mittag–Leffler recurrence, self-decomposability criterion, Bernstein closure facts, or passage from dilation ratios to qF'/F; no proof-assistant certification; no historical-priority assertion.

### Permitted claim language before the gate

“The following argument extends the published parameter region; this exact extension was not found in the bounded search described here.”

## 2. Normalisation and translation table

| Original notation | Canonical notation | Transformation checked |
|---|---|---|
| E_{alpha,beta}(z)=sum z^n/Gamma(alpha n+beta) | Same E | Source definition, arXiv v4 equation (1.1) |
| Source equation (2.2) prints Gamma(alpha)E_{alpha,beta} with constant coefficient one | F_beta=Gamma(beta)E_{alpha,beta} | Constant coefficient E(0)=1/Gamma(beta) forces the latter. Ratio identity unaffected. |
| Hitting transform E_x exp(-qT_a)=F_q(x)/F_q(a) | R_c(q)=F(cq)/F(q) | Set a=1, x=c, with source’s 1-self-similar normalisation |
| Laplace exponent of reciprocal law | Phi=log F | Reciprocal normalised transform equals exp(-Phi) |
| Self-decomposable reciprocal | B=qF'/F Bernstein | Standard correspondence; also proved directly through (1-R_c)/(1-c) |
| Parameter shift beta+1 to beta | G=beta F+alpha qF' | Exact coefficient equality, (alpha n+beta)/Gamma(alpha n+beta+1)=1/Gamma(alpha n+beta) |

## 3. Fingerprints

### Sequences

The defining coefficient sequence is a_n=1/Gamma(alpha n+beta). Three exact parameter instances in the proposed new region are (alpha,beta)=(3/2,1/4), (4/3,1/6), and (7/4,1/2); their seed parameters gamma=beta+1 are 5/4, 7/6 and 3/2. These coefficients are transcendental in general and have no natural common integer scaling. No claim concerns a newly discovered sequence. An OEIS fingerprint search would identify gamma constants rather than the complete-monotonicity statement, so none was treated as decisive.

For the explicit (3/2,1/4) example, splitting n into even and odd indices gives rational recurrences after factoring out Gamma(1/4) and Gamma(7/4): each same-parity term is multiplied by z^2/[v(v+1)(v+2)], with v increasing by 3. This fingerprint was used in the exact certificate.

### Generating functions

The object is the classical entire Mittag–Leffler function, not a rational or algebraic generating function. Its order is below one in the target range. No new object identity is claimed.

### Small matrices/kernels

Not applicable: the theorem concerns an entire special-function family. The finite certificate evaluates it at the exact complex argument -60+i.

### Invariants and recurrences

E_{alpha,beta}=beta E_{alpha,beta+1}+alpha q E'_{alpha,beta+1}; E_{alpha,0}=q E_{alpha,alpha}; normalised F_beta(0)=1 for beta>0; B(0)=0; the target is closure of positivity of all signed derivatives, not mere log-convexity.

## 4. Alias map

| Analysis | Probability | Combinatorics | Mathematical physics | Other |
|---|---|---|---|---|
| Complete monotonicity; logarithmic complete monotonicity; Bernstein logarithm | Infinite divisibility; self-decomposable hitting times; spectrally negative positive self-similar process | Gamma-ratio coefficients; Euler differential transform | van Dantzig pairs; Laguerre–Pólya functions; fractional differential equations | Generalised gamma convolutions; parameter lowering; reciprocal special functions |

The combinatorial language concerns coefficients only; no claim that the new reciprocal is a characteristic function after the van Dantzig substitution was made. Such a claim would require additional positivity.

## 5. Search log

All searches below ran on 2 November 2026.

| Corpus/database | Query family | Results inspected | Consequence |
|---|---|---|---|
| Web engine 1 and arXiv | “Mittag-Leffler” “Conjecture 25” complete monotonicity; “Garrappa” “Conjecture 25” “false” | GGPS full arXiv v4 §2, §3, §4 | Exact conjecture and seed representation verified; no matching resolution returned |
| Web engine 1 | “reciprocal” “Mittag-Leffler” “monotone” beta; “1/E” “Mittag-Leffler” “2026” | GGPS and general complete-monotonicity papers | Distinguished reciprocal function from E(-q), avoiding a common collision |
| Web engines 1 and 2 | “Mittag-Leffler” “self-decomposable” “beta”; “Mittag-Leffler” “reciprocal” “self-decomposable”; “Patie” “Mittag-Leffler” “self-decomposable” functions | Patie 2009 full text, Theorem 2.6, Lemma 3.3, Corollary 4.1 | qI'/I Bernstein and seed SD are established prior work |
| Web engine 2 and Numdam | “Mittag-Leffler” “beta” “van Dantzig”; exact KPS title | KPS 2024 full text §4.2.4, Theorem 4.1, derivative-closure context | Explicit ML parameter domain remains alpha-1<beta<alpha; no target-region extension located |
| Web engine 2 | “Mittag-Leffler” “beta+1” “completely monotone”; “Mittag-Leffler” “parameter lowering” monotonicity | No matching claim returned | Negative evidence only; search terms may miss unnamed derivations |
| Web engines 1 and 2 | “Mittag-Leffler” “logarithmically completely monotonic” reciprocal; “self-decomposable” “F” “derivative” “reciprocal” Bernstein; “Bernstein” “Euler operator” “reciprocal” | Bernstein-function literature and unrelated special-function studies | General transform is a short standard consequence; novelty language withheld for lemma |
| Web engine 2 and SSRN | “Thorin Quantisation” “Mittag”; “Thorin Quantisation” “beta”; exact title plus pdf | Polson 2026 abstract, not full text; exact PDF returned 403 | Related recent priority uncertainty remains |
| Author webpage | Gerhold publications and linked Addenda and Corrigenda | Errata PDF dated 22 September 2025 | No relevant correction listed; date limits evidential value |
| NIST DLMF | AGM, K(1/sqrt(2)), Gamma(1/4) identities | §§19.8, 22.20, 5.4 | Certificate constants independently sourced |

## 6. Verified collisions or bridges

**Known seed region.** GGPS Proposition 3 explicitly proves complete monotonicity for alpha in [1,2] and beta in [alpha-1,alpha]. The proof’s hitting-time ratio supplies our seed. This is a collision for any purported novelty claim on that region.

**Known probabilistic mechanism.** Patie (2009), Theorem 2.6, gives self-decomposability of reciprocals of its I-functions and infinite divisibility of exp[-qI'/I]. Theorem 2.1 gives a hitting-time ratio; Lemma 3.3 explains the self-similar additive structure. These statements contain the mechanism behind our Lemma 2. Our direct limiting argument is an exposition of this known mechanism, not a new discovery.

**KPS family.** KPS (2024), §4.2.4 p.399, writes the normalised ML series with alpha in (1,2) and beta in (alpha-1,alpha). Setting q=-t^2 matches our seed function after their variable change. It does not directly cover the proposed new triangle. The inspection is local to the relevant results, not a claim that every consequence of the 46-page article was exhausted.

**Classical recurrence.** The parameter shift follows from Gamma(u+1)=u Gamma(u). It is known and is not independently novel.

**Proposed combination.** The Bernstein-logarithm extension to 0<beta<alpha-1 was not found in the inspected sources or returned searches. This is bounded negative evidence, not proof of historical priority.

## 7. Negative evidence and missingness audit

The searches are not exhaustive. MathSciNet and zbMATH were not searched directly. No author was contacted; contacting authors requires separate user authorisation. No Russian-language or other non-English full-text search was performed. Polson (2026) was available only at abstract level because the full PDF endpoint returned 403; its precise ML parameter domain could not be checked. General operator results could imply the extension without naming the target function, and that risk remains. Published-source typographical issues were checked through normalisation rather than repeated literally. The theorem’s validity and its priority are distinct questions.

## 8. Outcome by contribution unit

| Unit | Outcome | Confidence | Allowed wording | Forbidden wording |
|---|---|---|---|---|
| Seed CM and self-decomposability statements | COLLISION | High | Established prior work used as an ingredient | New proof of previously open seed region |
| General qF'/F Bernstein mechanism | COLLISION / standard consequence | High | Elementary consequence of a known ratio property | New probabilistic principle |
| Target positive-beta extension | BOUNDED UNCERTAINTY | Moderate | Exact extension not found in recorded search | First proof; proved novel; universal priority |
| Complete proof of extension | CLEAR TO PROVE within boundary | Moderate | Complete written derivation from published identity | Formally verified unrestricted theorem |
| Cross-identification | Not a contribution | High | Translation of standard normalisations | New bridge between distinct objects |
| Finite rational certificate | CLEAR within boundary | High about construction | Executable exact enclosure for specified values | Proof of all derivatives/all parameters |

## 9. Decision

**BOUNDED UNCERTAINTY.** The mathematical argument is ready for independent review. The precise extension survived this bounded search, but the available evidence does not establish historical priority.

## 10. Rerun triggers

Rerun on obtaining Polson’s full text; identifying an established name for the derivative transform; finding a theorem that directly covers gamma-ratio parameter lowering; extending beta above alpha; or discovering a direct stochastic realisation for the new beta region.
