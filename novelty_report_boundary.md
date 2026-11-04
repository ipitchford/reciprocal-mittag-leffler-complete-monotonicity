# Formula-first novelty and object-identity report

Date: 2 November 2026. This is a bounded literature search, not a proof of historical priority. The inspected manuscript supplies new analytic arguments; whether the resulting statements have appeared elsewhere remains subject to the limits below.

## 1. Frozen contribution units

The principal proposed contribution is the classification, **local in alpha and global in positive beta**, recorded in `target.yaml`. A second contribution is the analytic double-zero boundary and its exact first derivative. A third is the positive and strictly decreasing inverse-logarithmic-derivative kernel, giving infinite divisibility and self-decomposability throughout the admissible region. The complete proofs, numerical consistency checks and explanatory material are separate contribution units.

The classical identities at alpha=2, the use of Hadamard products to obtain Bernstein logarithms when all zeros are negative, the known beta=alpha probability law, and the beta=0 recurrence are **not** proposed as new. A separate extension in the manuscript establishes a positive-beta interval for every fixed alpha in (1,2); it is not a full classification away from order two.

The originating statement is Conjecture 25 in arXiv:2410.11852v4, dated 11 May 2025, corresponding to the published JMAA paper. Version 3 numbers the relevant statement Conjecture 24. The result concerns the reciprocal at a **positive argument**. It is different from complete monotonicity of E_{alpha,beta}(-s), which has another parameter range.

## 2. Normalisation and fingerprints

The parameter beta is strictly positive in all probability-law conclusions. Multiplication by Gamma(beta) ensures that the entire function equals one at zero and its reciprocal is a probability Laplace transform. Constants do not affect complete monotonicity but do affect probability normalisation. For the inverse kernel, L=E'/E and F=-L' are invariant under that constant normalisation.

Three exact anchors were used: E_{2,2}=sinh(sqrt(z))/sqrt(z); E_{2,3}=(cosh(sqrt(z))-1)/z; and E_{2,0}=sqrt(z)sinh(sqrt(z)). The seven coefficient values for the first two normalised reciprocals are recorded in the target file and independently reproduced by exact fraction arithmetic. These anchors are familiar objects and deliberately register as identity collisions.

The literal reciprocal coefficient search returned the classical cosecant/sinh series and OEIS A036281/A036282. After the substitution z=x^2 and alternating signs, these agree with x/sinh(x). This confirms that the elementary alpha=2 function is old; it does not identify the new parameter-stability or boundary statement. There is no rational/algebraic generating function to canonicalise for general alpha,beta. Finite-matrix invariants are not applicable to this scalar entire-function target.

The proposed boundary is characterised by E=E'=0 near z=-4*pi^2. Its slope has the exact integral expression in the target file. The literal numerical-slope search found no matching Mittag-Leffler result. The mathematical statement is the exact integral identity, not its decimal expansion.

## 3. Actual query record

Both available live web search engines were used in separate calls. Primary repositories were arXiv and Numdam; publisher and author pages supplied further records. Relevant queries, including searches repeated after the logarithmic-derivative and boundary simplifications, were:

- `"2410.11852" "conjecture"`
- `"Mittag-Leffler" "Conjecture 25" "monotone"`
- `"Mittag-Leffler" "reciprocal" "2026" completely monotone`
- `"logarithm" "Mittag-Leffler" "Bernstein" "2"`
- `"logarithmically completely monotonic" "Mittag-Leffler" reciprocal`
- `"Mittag-Leffler" "Conjecture 25" counterexample`
- `"Mittag-Leffler" "infinite divisibility" "beta"`
- `"Mittag-Leffler" "Bernstein" "stability"`
- `"Mittag-Leffler" "reciprocal" "beta" "2" "Bernstein"`
- `"Nonasymptotic results on distribution of zeros" Peresyolkova`
- `"Thorin Quantisation" "Mittag"`
- `"Mittag-Leffler" "Bernstein" "near" "2"`
- `"Mittag-Leffler" "log" "alpha" "Conjecture 25"`
- `"reciprocal" "Mittag-Leffler" "self-decomposable"`
- `"Konstantopoulos" "Patie" "Sarkar" "van Dantzig" Mittag Leffler`
- `"Mittag-Leffler" "complete monotonicity" "double zero"`
- `"Mittag-Leffler" "reciprocal" "boundary"`
- `"Mittag-Leffler" "Bernstein" "2,3"`
- `"Mittag-Leffler" "reciprocal" "zeros" "Bernstein" "2026"`
- `"Mittag-Leffler" "complete monotonicity" "boundary curve"`
- `"Mittag-Leffler" "2.827681"`
- `"Mittag-Leffler" "reciprocal" "first zero" complete monotonicity`
- `"Mittag-Leffler" "small beta" "reciprocal"`
- `"Mittag-Leffler" "small" "beta" "infinite divisibility"`
- `"1/6" "7/360" "31/15120" sinh`
- `"Turán Inequalities and Complete Monotonicity for a Class of Entire Functions"`
- `"reciprocal entire" "completely monotone" zeros`
- `"Mittag-Leffler" "self-decomposable" "stability"`
- `"Patie" "Bartholme" pdf Turan`
- `"Turán" "Patie" "Mittag" "alpha"`
- `"Turán Inequalities" "Complete Monotonicity" arxiv`

Within the opened newer Ferreira-Simon paper, text searches for `Bernstein`, `conjecture`, and `completely monotone` gave no matches; `reciprocal` led to a different self-reciprocal random variable. This is a targeted exclusion check, not a claim to have audited every proof in that paper.

## 4. Inspected sources and verified translations

### Originating conjecture and known anchors

Garrappa, Gerhold, Popolizio and Simon (2025), arXiv v4, was inspected in full-text HTML. The decisive locators are the proof of Theorem 1 (simple negative zeros at alpha=2, 0<beta<3), Proposition 3 and Remark 4(a) (known reciprocal/Bernstein range), Proposition 14 (necessity of the original interval for the global modulus inequality), and Conjectures 25 and 26. The new theorem contradicts the reciprocal necessity implication of Conjecture 25 for **strictly positive** beta. It does not contradict Proposition 14 or resolve Conjecture 26.

The beta=0 identity E_{alpha,0}(s)=s E_{alpha,alpha}(s) already gives a completely monotone reciprocal for 1<alpha<2. Thus the literal nonnegative-beta reading of the conjecture has an elementary endpoint defect. The manuscript does not count that endpoint observation as a research contribution.

### Earlier probability constructions

Patie (2009) was opened as a full Numdam PDF. Section 4.2.1 and Corollary 4.1 contain the beta=alpha example. The positive probability normalisation is Gamma(alpha)E_{alpha,alpha}; the manuscript retains this factor. Corollary 4.2 uses a more general function with coefficients formed from products of **differences** of Pochhammer symbols. Those coefficients are not the defining coefficients 1/Gamma(alpha*n+beta) for arbitrary beta. A broad title similarity therefore does not establish identity with the present theorem.

Bartholmé and Patie (2021) was inspected in an author-uploaded full-text copy on ResearchGate. Section 1.2.4 identifies I_phi=Gamma(alpha)E_{alpha,alpha}. Theorem 2.5(ii) establishes a Bernstein logarithm with a decreasing kernel. Its differentiated examples in that section carry an additional rising-factorial coefficient and are Fox-Wright functions, rather than generic E_{alpha,beta}. This is a known anchor and method context, not a verified collision with the beta-boundary theorem.

Konstantopoulos, Patie and Sarkar (2024) was opened as a full Numdam PDF. Section 4.2.4, printed p.399, explicitly uses 1<alpha<2 and alpha-1<beta<alpha, with normalised E_{alpha,beta}(-t^2). The general theory provides related self-decomposable clocks. The inspected example stays in the older interval and does not establish the new region or its boundary.

### Newer material and access limits

Ferreira and Simon (2025), arXiv:2512.04940, was opened as a full PDF; the abstract, main-results context and targeted passages were inspected. Its parameter-monotonicity and convex-order results concern different assertions. No duplicate of the present classification was found in this bounded inspection.

Polson's 2026 *Thorin Quantisation* was accessible only through an indexed SSRN abstract. Direct page/PDF access was blocked. The abstract concerns reciprocal entire functions, self-decomposable clocks and the Thorin class; it is relevant enough that its unavailable full text is an explicit priority limitation. No conclusion about its uninspected theorems is drawn. A second related SSRN abstract, *A Riemann Thorin-van Dantzig principle*, was surfaced; it also does not supply a verified formula-level collision from the inspected abstract.

The original 1997 zero-distribution paper by Ostrovskii and Peresyolkova was checked at the publisher-metadata level; its full text was not obtained. The specific zero theorem is explicitly stated and used in the inspected 2025 paper. The core beta=2 counterexample and the local boundary theorem use elementary anchors and do not require this general zero theorem. The full all-beta classification does use it for the middle beta interval.

## 5. Outcomes by contribution unit

| Unit | Outcome | Basis and permitted claim |
|---|---|---|
| Elementary alpha=2 identities and heat sums | COLLISION | Classical sine/sinh products; explicitly recognised and cited as anchors. |
| beta=alpha Bernstein/self-decomposable law | COLLISION | Patie 2009; Bartholmé-Patie 2021; Garrappa et al. 2025. |
| beta=0 reciprocal complete monotonicity | COLLISION / elementary consequence | Recurrence and the known beta=alpha law. No novelty claimed. |
| Full positive-beta classification for alpha near 2 | BOUNDED UNCERTAINTY; clear to develop within inspected corpus | No duplicate found in inspected primary sources; inaccessible 2026 material prevents universal priority language. |
| Double-zero boundary and exact slope | BOUNDED UNCERTAINTY | Exact formula and zero-transition searches found no matching result. |
| Positive/decreasing kernel on the expanded region | BOUNDED UNCERTAINTY | Known on older parameter bands; expanded region not found in inspected sources. |
| Positive small-beta interval for each order in (1,2), uniformly on compact order sets | BOUNDED UNCERTAINTY | Extends the elementary beta=0 anchor to positive beta using a proved uniform stability argument; no matching positive-beta existence theorem was found in inspected sources. |
| Reproducible proof/check exposition | Completed work product | Exact checks and recorded analytic derivation are supplied; not a novelty certificate. |

Permitted wording: "We prove the following theorem" and "This refutes the stated reciprocal implication for positive beta, assuming the displayed proof is correct." For priority: "No matching result was found in the bounded search described here." Forbidden wording: "first-ever", "proved novel", "the conjecture is still universally open as of today", or "world-leading" solely because a paper called a statement a conjecture.

No author enquiries were sent. Contacting authors was not authorised. The missing full-text priority checks and external specialist assessment remain appropriate before submission; they do not invalidate an independently inspectable proof.

## 6. References actually consulted

### Main problem and probability context

Garrappa, R., Gerhold, S., Popolizio, M., & Simon, T. (2025). On some inequalities for the two-parameter Mittag-Leffler function in the complex plane. *Journal of Mathematical Analysis and Applications, 551*(1), 129588. https://doi.org/10.1016/j.jmaa.2025.129588 . Full text: https://arxiv.org/html/2410.11852v4

Patie, P. (2009). Infinite divisibility of solutions to some self-similar integro-differential equations and exponential functionals of Lévy processes. *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques, 45*(3), 667-684. https://doi.org/10.1214/08-AIHP182 . https://www.numdam.org/item/10.1214/08-AIHP182.pdf

Bartholmé, C., & Patie, P. (2021). Turán inequalities and complete monotonicity for a class of entire functions. *Analysis Mathematica, 47*, 507-527. https://doi.org/10.1007/s10476-021-0088-4 . Author full-text upload: https://www.researchgate.net/publication/346205543_Turan_Inequalities_and_Complete_Monotonicity_for_a_Class_of_Entire_Functions

Konstantopoulos, T., Patie, P., & Sarkar, R. (2024). A new class of solutions to the van Dantzig problem, the Lee-Yang property, and the Riemann hypothesis. *Annales de l'Institut Fourier, 74*(1), 377-421. https://doi.org/10.5802/aif.3600 . https://www.numdam.org/item/10.5802/aif.3600.pdf

### Recent checks and explicit limitations

Ferreira, R. A. C., & Simon, T. (2025). *Mittag-Leffler functions and convex ordering* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2512.04940

Polson, N. G. (2026). *Thorin quantisation* [Preprint; abstract inspected only]. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7277540

Ostrovskii, I. V., & Peresyolkova, I. N. (1997). Nonasymptotic results on distribution of zeros of the function E_rho(z,mu). *Analysis Mathematica, 23*, 283-296. https://doi.org/10.1007/BF02789843 . Metadata inspected; zero result used through Garrappa et al. (2025).

### Fingerprint only

OEIS Foundation Inc. (n.d.). *A036281; A036282*. The On-Line Encyclopedia of Integer Sequences. Retrieved November 2, 2026, from https://oeis.org/A036281 and https://oeis.org/A036282
