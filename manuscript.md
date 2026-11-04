# Reciprocal Mittag–Leffler functions: complete monotonicity below the parameter band, and the exact boundary near order two

## Abstract

For which parameters is the reciprocal $1/E_{\alpha,\beta}$ of the two-parameter Mittag–Leffler function completely monotone on $(0,\infty)$? For $1<\alpha<2$, Garrappa, Gerhold, Popolizio and Simon (2025) conjectured that this happens exactly when $\beta\in[\alpha-1,\alpha]$. We prove two results that together show this parameter band is not the right answer.

**Theorem A (every order between one and two).** If $1<\alpha<2$ and $0<\beta\le\alpha$, then $\log[\Gamma(\beta)E_{\alpha,\beta}]$ is a Bernstein function. Hence every positive power of $1/[\Gamma(\beta)E_{\alpha,\beta}]$ is the Laplace transform of an infinitely divisible probability law. This includes the whole triangle $0<\beta<\alpha-1$ lying below the band. The proof is short. It combines a dilation-ratio identity contained in the proof of Garrappa et al.'s Proposition 3 with the classical recurrence $E_{\alpha,\beta}=\beta E_{\alpha,\beta+1}+\alpha zE'_{\alpha,\beta+1}$.

**Theorem B (exact classification near order two).** There is a real analytic function $b$, with $b(2)=3$, such that for every $\alpha$ in some two-sided neighbourhood of $2$ the set of admissible $\beta>0$ is exactly the interval $(0,b(\alpha)]$. On this set the normalised logarithm is Bernstein with a decreasing Lévy density, so the associated laws are self-decomposable. The boundary is where the two zeros of $E_{\alpha,\beta}$ near $-4\pi^2$ collide, and
\[
b'(2)=1+\frac{2\pi\operatorname{Si}(2\pi)}{2\int_0^{2\pi}(1-\cos u)\,du/u}=2.82768173110428\ldots .
\]
For $\alpha<2$ close to $2$, $b(\alpha)>\alpha$, so the band also fails above.

Theorem A disproves the lower half of the proposed necessity for every $\alpha\in(1,2)$; Theorem B disproves the upper half for $\alpha$ near $2$ and gives the correct answer there. The remaining assertion of the conjecture, that the band is exactly where a global complex modulus inequality holds, is untouched. A high-precision continuation, which is numerical evidence and not proof, traces the double-zero curve $b(\alpha)$ over $1.5\le\alpha\le2.5$ and suggests the replacement conjecture $\mathcal C_\alpha=(0,b(\alpha)]$ for all $1<\alpha<2$.

*Status.* Version 0.1.0-candidate (4 November 2026), archived at https://doi.org/10.5281/zenodo.23934934 . AI-assisted research paper, not externally refereed. The proofs received several internal AI-assisted audits; finite checks are supplied as scripts. No proof-assistant verification has been done.

## Reader's guide

**Why this question matters.** Mittag–Leffler functions generalise the exponential. They appear wherever relaxation or waiting times are "anomalous": fractional differential equations, viscoelastic models, and the hitting times of self-similar Markov processes. A function $f$ on $(0,\infty)$ is *completely monotone* if its derivatives alternate in sign, $(-1)^nf^{(n)}\ge0$. By Bernstein's theorem this means $f$ is the Laplace transform of a positive measure. So when $1/E_{\alpha,\beta}$ is completely monotone, it is (after normalisation) the Laplace transform of a probability distribution. A *Bernstein function* is a nonnegative function with completely monotone derivative. When $\log$ of the normalised function is Bernstein, every power of the reciprocal is also a Laplace transform, so the distribution is *infinitely divisible*. If in addition the Lévy density is decreasing in a suitable sense, the law is *self-decomposable*.

**What was known.** Garrappa, Gerhold, Popolizio and Simon [GGPS25] proved complete monotonicity on the band $\alpha-1\le\beta\le\alpha$ for $1\le\alpha\le2$ (their Proposition 3), with a Bernstein logarithm (their Remark 4(a)). The diagonal $\beta=\alpha$ goes back to Patie [P09]. Their Conjecture 25 asserts that, for $1<\alpha<2$, three conditions are equivalent: (i) $\beta\in[\alpha-1,\alpha]$; (ii) $1/E_{\alpha,\beta}$ is completely monotone; (iii) $|E_{\alpha,\beta}(z)|\ge E_{\alpha,\beta}(\operatorname{Re}z)$ for all complex $z$. Their Proposition 14 proves that (iii) forces (i).

**What is new here.** (ii) does *not* force (i). Theorem A shows this below the band for every order. Theorem B shows it above the band near order two and finds the true answer there. Combined with [GGPS25, Proposition 14], our examples also show that (ii) does not imply (iii).

**Where to find things.**

| Part | Content |
|---|---|
| §1 | Notation and precise statements |
| §2 | Proof of Theorem A (short, self-contained apart from one cited identity) |
| §3–§10 | Proof of Theorem B: complex asymptotics (§3), the inverse kernel (§4), the order-two anchors (§5), interior stability (§6), the small-$\beta$ end (§7), the exact boundary (§8), assembly (§9), the tangent $b'(2)$ (§10) |
| §11 | Scope, limits and consistency checks |
| §12 | Numerical boundary curve and an open conjecture |
| Appendix | A certified failure of the modulus inequality |

Readers who want only the main ideas can read §1, §2, the opening of §8, and §11.

## 1. Notation and statements

For $\alpha>0$ and $\beta\ge0$,
\[
E_{\alpha,\beta}(z)=\sum_{k=0}^{\infty}\frac{z^k}{\Gamma(\alpha k+\beta)} .
\]
The reciprocal gamma function makes this meaningful at $\beta=0$. For $\beta>0$ the coefficients are positive and $E_{\alpha,\beta}(0)=1/\Gamma(\beta)$. We normalise
\[
Q_{\alpha,\beta}(s)=\Gamma(\beta)E_{\alpha,\beta}(s),\qquad
\Phi_{\alpha,\beta}(s)=\log Q_{\alpha,\beta}(s),\qquad s\ge0,
\]
so $\Phi_{\alpha,\beta}(0)=0$. Multiplying by the constant $\Gamma(\beta)$ does not affect complete monotonicity. Write
\[
\mathcal C_\alpha=\{\beta>0:\ 1/E_{\alpha,\beta}\ \text{is completely monotone on }(0,\infty)\}.
\]

**Theorem A.** Let $1<\alpha<2$ and $0<\beta\le\alpha$. Then $\Phi_{\alpha,\beta}$ is a Bernstein function. Consequently $Q_{\alpha,\beta}^{-r}$ is the Laplace transform of an infinitely divisible probability law for every $r>0$, and $(0,\alpha]\subseteq\mathcal C_\alpha$.

**Theorem B.** There exist $\delta>0$ and a real analytic $b:(2-\delta,2+\delta)\to(0,\infty)$ such that for every $|\alpha-2|<\delta$,
\[
\boxed{\mathcal C_\alpha=(0,b(\alpha)].}
\]
For each admissible $(\alpha,\beta)$ there is a continuous, strictly positive, strictly decreasing $g_{\alpha,\beta}$ on $(0,\infty)$ with
\[
\Phi_{\alpha,\beta}(s)=\int_0^\infty(1-e^{-st})\frac{g_{\alpha,\beta}(t)}t\,dt,
\]
so $Q_{\alpha,\beta}^{-r}$ is the Laplace transform of a self-decomposable probability law for every $r>0$. The boundary satisfies $b(2)=3$ and is locally characterised by a double real zero,
\[
E_{\alpha,b(\alpha)}(x(\alpha))=\partial_zE_{\alpha,b(\alpha)}(x(\alpha))=0,\qquad x(2)=-4\pi^2 .
\]
With $a=2\pi$, $I(a)=\int_0^a(1-\cos u)\,du/u$ and $\operatorname{Si}(a)=\int_0^a\sin u\,du/u$,
\[
\boxed{b'(2)=1+\frac{a\operatorname{Si}(a)}{2I(a)}=2.827681731104280866705425238445\ldots}
\]

**How the two theorems fit together.** Near $\alpha=2$, Theorem A's range $(0,\alpha]$ sits inside Theorem B's $(0,b(\alpha)]$, since $b(\alpha)\to3$. Theorem A is global in $\alpha\in(1,2)$ but says nothing above $\beta=\alpha$ and gives only infinite divisibility. Theorem B is local in $\alpha$ but exact in $\beta$, and gives self-decomposability. For $\alpha<2$ close to $2$, for example, both $\beta=1/2<\alpha-1$ and $\beta=2>\alpha$ are admissible. The size of $\delta$ is not quantified; §12 reports numerics but certifies no specific pair above the band.

**Endpoint $\beta=0$.** The identity $E_{\alpha,0}(s)=sE_{\alpha,\alpha}(s)$ makes $1/E_{\alpha,0}$ completely monotone, as a product of $1/s$ and $1/E_{\alpha,\alpha}$. This observation is elementary and is not claimed as a contribution. It is used below only as an analytic anchor.

## 2. Proof of Theorem A

### 2.1. A transform of functions with completely monotone dilation ratios

**Lemma 2.1.** Let $F$ be a positive function on $[0,\infty)$, real analytic on a neighbourhood of $[0,\infty)$, with $F(0)=1$. Suppose that for every $0<c<1$ the ratio $R_c(q)=F(cq)/F(q)$ is completely monotone on $(0,\infty)$. Then $\log F$ and $B(q)=qF'(q)/F(q)$ are Bernstein functions. Moreover, for $a>0$ and $b\ge0$, the function $G=aF+bqF'$ has $\log[G/a]$ Bernstein, so $G^{-t}$ is completely monotone for every $t>0$.

**Proof.** Since $R_c$ is completely monotone and $R_c(0)=1$, we have $0<R_c\le1$, and $1-R_c$ is nonnegative with completely monotone derivative $-R_c'$; so $1-R_c$ is Bernstein, and so is $B_c=(1-R_c)/(1-c)$. Because $F(cq)$ is real analytic jointly in $(c,q)$ near $c=1$, $B_c$ and each of its $q$-derivatives converge locally uniformly on $(0,\infty)$, as $c\uparrow1$, to the corresponding derivatives of $qF'(q)/F(q)$. The Bernstein class is closed under pointwise limits that are finite [SSV12, Chapter 3], so $B$ is Bernstein.

Also $F(cq)\le F(q)$, so $F$ is nondecreasing and $\log F\ge0$. Since $B(0)=0$,
\[
\log F(q)=\int_0^1\frac{B(sq)}s\,ds .
\]
For each $s\in(0,1]$, $q\mapsto B(sq)/s$ is Bernstein. The integral is a pointwise limit of Riemann sums of Bernstein functions with nonnegative weights, and it is finite; hence it is Bernstein, again by [SSV12, Chapter 3].

For $a>0$, write $\log(G/a)=\log F+\log(1+(b/a)B)$. The function $x\mapsto\log(1+x)$ is Bernstein, compositions of Bernstein functions are Bernstein [SSV12, Chapter 3], and sums of Bernstein functions are Bernstein. Finally $e^{-t\psi}$ is completely monotone whenever $\psi$ is Bernstein and $t>0$. $\square$

The hypothesis of Lemma 2.1 says that the law with Laplace transform $1/F$ is self-decomposable. The conclusion gives only infinite divisibility for $G$. This is why the lemma cannot simply be iterated, and why Theorem A does not claim self-decomposability.

### 2.2. The dilation-ratio identity on the band

**Lemma 2.2.** Let $1<\alpha<2$, $\gamma\in[\alpha-1,\alpha]$ with $\gamma>0$, and $F_\gamma(q)=\Gamma(\gamma)E_{\alpha,\gamma}(q)$. For every $0<c<1$ there is a random variable $T\ge0$ (depending on $\alpha,\gamma,c$) with
\[
\frac{F_\gamma(cq)}{F_\gamma(q)}=\mathbb E\big[e^{-qT}\big],\qquad q>0 .
\]
In particular the ratio is completely monotone.

**Source and proof.** This is contained in the proof of [GGPS25, Proposition 3] (arXiv v4, Section 2). For $\gamma=\alpha$, the authors display the identity $\mathbb E_x[e^{-qT_a}]=F_q(x)/F_q(a)$ for $a>x>0$, where $F_q(x)=F_\gamma(qx)$, $X$ is a positive self-similar Markov process without positive jumps and $T_a$ is its first passage time above $a$. Taking $x=c$ and $a=1$ gives the claim. For $\alpha-1\le\gamma<\alpha$, they construct a recurrent extension of the corresponding process, still without positive jumps, whose generator satisfies $\mathcal L F_q=qF_q$ (just after their (2.2)), and state that "reasoning exactly as above" gives the hitting-time formula. For completeness, here is that step. Fix $0<x<a$. Up to time $T_a$ the process stays in $[0,a]$, where $F_q$ is bounded. By Dynkin's formula, $e^{-q(t\wedge T_a)}F_q(X_{t\wedge T_a})-F_q(x)$ has zero mean. Recurrence gives $T_a<\infty$ almost surely, and because there are no positive jumps $X_{T_a}=a$. Letting $t\to\infty$ by dominated convergence gives $\mathbb E_x[e^{-qT_a}]F_q(a)=F_q(x)$. (Their equation (2.2) prints the normalising factor as $\Gamma(\alpha)$; the factor consistent with constant coefficient one is $\Gamma(\gamma)$. The constant cancels from the ratio.) $\square$

The band restriction on the seed is essential: Lemma 2.2 is not claimed for $\gamma>\alpha$, and the parameter-lowering step below only ever uses seeds strictly inside the band.

### 2.3. Lowering the parameter

The defining series gives, for every $\beta\ge0$,
\[
E_{\alpha,\beta}(q)=\beta E_{\alpha,\beta+1}(q)+\alpha qE'_{\alpha,\beta+1}(q),
\tag{2.1}
\]
since the coefficient of $q^n$ on the right is $(\beta+\alpha n)/\Gamma(\alpha n+\beta+1)=1/\Gamma(\alpha n+\beta)$.

**Proof of Theorem A.** If $\alpha-1\le\beta\le\alpha$, Lemmas 2.1 and 2.2 with $F=F_\beta$ give the result (this case is [GGPS25, Remark 4(a)]). Suppose $0<\beta<\alpha-1$ and put $\gamma=\beta+1$. Then $\alpha-1<1<\gamma<\alpha$, so Lemma 2.2 applies to $F_\gamma$. Multiplying (2.1) by $\Gamma(\beta)$ and using $\Gamma(\beta+1)=\beta\Gamma(\beta)$,
\[
\Gamma(\beta)E_{\alpha,\beta}(q)=F_\gamma(q)+\frac\alpha\beta\,qF'_\gamma(q).
\]
This is $G=aF_\gamma+bqF_\gamma'$ with $a=1$, $b=\alpha/\beta$. Lemma 2.1 shows that $\Phi_{\alpha,\beta}=\log G$ is Bernstein. $\square$

**Corollary 2.3.** For every $1<\alpha<2$ and $0<\beta<\alpha-1$, $1/E_{\alpha,\beta}$ is completely monotone but the modulus inequality $|E_{\alpha,\beta}(z)|\ge E_{\alpha,\beta}(\operatorname{Re}z)$ fails for some $z$.

**Proof.** The first part is Theorem A; the second is [GGPS25, Proposition 14]. A direct reason: $E_{\alpha,\beta}(-x)\sim1/[x\Gamma(\beta-\alpha)]$ as $x\to\infty$, with $\Gamma(\beta-\alpha)>0$ because $\beta-\alpha\in(-2,-1)$. Differentiating the expansion gives $(E')^2-EE''\sim-C^2x^{-4}<0$ at $-x$, and expanding $|E(-x+iy)|^2$ to second order in $y$ shows that small $y\neq0$ violates the inequality. The Appendix gives an exactly certified instance. $\square$

## Proof of Theorem B: overview

The proof constructs the inverse Laplace transform $g$ of the logarithmic derivative and shows it is positive and decreasing for all $t>0$. Three regimes are handled separately. Uniform complex asymptotics (§3) control small times. The zeros of $E_{\alpha,\beta}$ nearest the origin control large times (§4). At $\alpha=2$ everything is explicit, through products of sines and hyperbolic sines (§5), and continuity carries strict signs on the compact middle time range to nearby $\alpha$. Sections 6 and 7 cover the interior and the small-$\beta$ end. Section 8 analyses the boundary, where two negative zeros collide and become complex, and proves necessity with Pringsheim's theorem. Section 9 assembles the pieces and Section 10 computes $b'(2)$.


## 3. Uniform complex estimates

Throughout the proof it is enough to use the fixed compact rectangle

\[K=[19/10,21/10]\times[0,10].
\]

Put

\[p=1/\alpha,\qquad q=(\beta-1)/\alpha,
\qquad
L_{\alpha,\beta}(z)=\frac{E'_{\alpha,\beta}(z)}{E_{\alpha,\beta}(z)},
\qquad
F_{\alpha,\beta}(z)=-L'_{\alpha,\beta}(z).
\]

Primes denote differentiation in the complex argument. The functions $L$ and $F$ are meromorphic. The parameters $p$ remain in a compact subinterval of $(0,1)$, and $q$ remains bounded. All complex powers below use the principal branch.

**Lemma 3.1.** Uniformly for parameters in $K$ and $|\arg z|\le5\pi/9$,

\[E_{\alpha,\beta}(z)
=\alpha^{-1}z^{-q}e^{z^p}+O(|z|^{-1}),\qquad |z|\to\infty.
\]

On the smaller sector $|\arg z|\le19\pi/36$,

\[L(z)=pz^{p-1}-qz^{-1}
+O\bigl(|z|^N e^{-\kappa|z|^p}\bigr),
\]

\[F(z)=p(1-p)z^{p-2}-qz^{-2}
+O\bigl(|z|^N e^{-\kappa|z|^p}\bigr).
\]

The same type of exponentially small bound holds after any fixed finite number of argument derivatives. The constants can be chosen uniformly on $K$. Outside a sufficiently large disk, $E$ has no zeros in these sectors.

**Proof.** Start with the Hankel formula for reciprocal gamma [DLMF, Equation 5.9.2] on rays $\arg u=\pm2\pi/3$. Join the rays by a circular arc through the right side. Initially take its radius larger than $|z|^{1/\alpha}$. Expanding the denominator geometrically and integrating term by term gives the Hankel representation for $E$. Deform the circular arc to radius one, keeping the rays fixed.

For $\alpha\in[1.9,2.1]$, the unreduced arguments $\alpha(\pm120^\circ)$ run from $\pm228^\circ$ to $\pm252^\circ$. Their principal absolute arguments lie between $108^\circ$ and $132^\circ$. They are therefore separated by at least $8^\circ$ from the allowed $100^\circ$ sector for $z$. On the rays,

\[|u^\alpha-z|\ge c\bigl(|u|^\alpha+|z|\bigr)
\]

with a uniform $c>0$. On the unit arc the denominator also has magnitude bounded below by a fixed multiple of $|z|$ for large $|z|$.

The principal root $u=z^{1/\alpha}$ has argument of absolute value at most $100^\circ/1.9<53^\circ$. Every other root on the principal $u$-plane has argument of absolute value at least $260^\circ/2.1>123^\circ$. The deformation consequently crosses exactly the principal pole. Its residue gives

\[E_{\alpha,\beta}(z)
=\alpha^{-1}z^{-q}e^{z^p}
+\frac1{2\pi i}\int_{\mathcal H_1}
\frac{e^u u^{\alpha-\beta}}{u^\alpha-z}\,du,
\]

where $\mathcal H_1$ is the fixed-radius contour. Along its rays, $|e^u|=e^{-|u|/2}$. Since the rays start at radius one, no integrability condition at $u=0$ is required. The integral is uniformly $O(1/|z|)$ for every $\beta\in[0,10]$.

Write $E=M(1+h)$ with $M=\alpha^{-1}z^{-q}e^{z^p}$. In the larger sector, $\operatorname{Re}z^p$ is bounded below by a positive uniform multiple of $|z|^p$. Thus $h$ is exponentially small, uniformly. For large enough $|z|$, $|h|<1/2$, proving zero exclusion. Cauchy's estimates on disks of radius $\eta|z|$ contained in the larger sector, with the fixed value $\eta=\tfrac12\sin(\pi/36)$ (the two sectors differ in half-angle by $\pi/36$, and $\arcsin\eta<\pi/36$, so each disk of radius $\eta|z|$ centred in the smaller sector lies in the larger one), give the asserted bounds for derivatives of $\log(1+h)$. Finally,

\[M'/M=pz^{p-1}-q/z,
\]

and differentiation proves the formulas for $L$ and $F$. The same argument gives any fixed finite number of derivatives. $\square$

## 4. The inverse kernel and its signs

Choose $c>0$ sufficiently large that Lemma 3.1 makes $E$ zero-free on $\operatorname{Re}z\ge c$, uniformly on $K$. Define

\[g_{\alpha,\beta}(t)
=\frac1{2\pi i\,t}
\int_{c-i\infty}^{c+i\infty}e^{zt}F_{\alpha,\beta}(z)\,dz,
\qquad t>0.
\]

The integral converges absolutely: its leading vertical order is $|z|^{p-2}$, whose exponent is uniformly less than $-1$. Contour rectangles show independence of the sufficiently large choice of $c$. Conjugation symmetry makes $g$ real. Dominated convergence gives joint continuity in the parameters and in positive $t$.

To differentiate without introducing a conditionally convergent integral, set

\[h(t)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}e^{zt}L''(z)\,dz.
\]

Both $L''(z)=O(|z|^{p-3})$ and $zL''(z)=O(|z|^{p-2})$ are absolutely integrable on this line. Integration by parts, using $L''=-F'$, gives $h=t^2g$. Moreover $h'$ is the inverse of $zL''$. Hence

\[g'(t)=\frac{th'(t)-2h(t)}{t^3}
\]

exists and is jointly continuous.

**Lemma 4.1: small times.** Uniformly on $K$,

\[g(t)=\frac p{\Gamma(1-p)}t^{-p}-q
+O\bigl(t^{-N_1}e^{-\kappa_1t^{-p}}\bigr),
\]

\[g'(t)=-\frac{p^2}{\Gamma(1-p)}t^{-p-1}
+O\bigl(t^{-N_2}e^{-\kappa_2t^{-p}}\bigr),
\qquad t\downarrow0.
\]

Consequently $g>0$ and $g'<0$ for all sufficiently small positive times, uniformly on $K$.

**Proof.** Move the inversion line to $\operatorname{Re}z=1/t$. Inverting the two explicit terms of $F$ gives

\[\frac1t\mathcal L^{-1}\{p(1-p)z^{p-2}-qz^{-2}\}(t)
=\frac{p(1-p)}{\Gamma(2-p)}t^{-p}-q
=\frac p{\Gamma(1-p)}t^{-p}-q.
\]

For the remainder, split the vertical integral at $|\operatorname{Im}z|=1/t$. The central segment contributes a power of $1/t$ times $e^{-\kappa t^{-p}}$. In the tails, substitute $|\operatorname{Im}z|=v/t$ and absorb every power of $v$ into the exponential. This proves the displayed uniform error bound. Applying the same procedure to $L''$ and $zL''$ and using the formula for $g'$ proves the derivative estimate; the constant $-q$ cancels exactly. The leading coefficient has a positive uniform lower bound and $q$ is bounded, so the signs follow. $\square$

**Lemma 4.2: isolated real zeros.** Suppose that, throughout a compact parameter set, the only zeros in $\operatorname{Re}z>-B$ are a fixed finite number of real zeros $-\lambda_j$, counted with multiplicity, and the line $\operatorname{Re}z=-B$ remains zero-free. Suppose also that their positions stay in a compact subset of $[0,B)$. Then, uniformly for $t\ge1$,

\[g(t)=\sum_j e^{-\lambda_jt}+O(t^{-1}e^{-Bt}),
\]

\[g'(t)=-\sum_j\lambda_j e^{-\lambda_jt}
+O(t^{-2}e^{-Bt}).
\]

The formulas remain uniform when zeros coalesce.

**Proof.** A zero of multiplicity $d$ contributes $d/(z+\lambda)$ to $L$, $d/(z+\lambda)^2$ to $F$, and $2d/(z+\lambda)^3$ to $L''$. Shift the inversion contours for $g$, $h$ and $h'$ to $\operatorname{Re}z=-B$. Residues give the displayed sums. On a bounded part of the new line, compactness and zero exclusion give a uniform bound. On its tails, Lemma 3.1 gives uniform absolute integrability. Horizontal integrals vanish by the same estimates.

For $h$, a zero of multiplicity $d$ contributes $dt^2e^{-\lambda t}$, and for $h'$ it contributes $d(2t-\lambda t^2)e^{-\lambda t}$. Combining them gives the formula for $g'$. No coefficient involves $1/E'$ at a zero: coefficients are multiplicities. They therefore remain bounded at a collision. $\square$

The first formula in Lemma 4.2 is uniformly positive for sufficiently large times whenever there is at least one retained real zero. The derivative is uniformly negative if at least one retained $\lambda_j$ stays in a fixed compact subinterval of $(0,B)$; other retained zeros may approach zero.

**Lemma 4.3: recovery of the transform.** Suppose $\beta>0$ and that the hypotheses of Lemma 4.2 hold: every zero of $E_{\alpha,\beta}$ in $\operatorname{Re}z>-B$ is real and these zeros are $-\lambda_j$ with $0<\lambda_j<B$ (strictly negative, since $\beta>0$). Suppose also $g>0$ and $g'<0$ on $(0,\infty)$. Then

\[L(s)=\int_0^\infty e^{-st}g(t)\,dt,
\qquad
\Phi(s)=\int_0^\infty(1-e^{-st})\frac{g(t)}t\,dt.
\]

The function $\Phi$ is Bernstein and every $Q^{-r}$, $r>0$, is a self-decomposable probability Laplace transform.

**Proof.** Put $k(t)=tg(t)$. For $s>c$, absolute convergence permits Fubini, and Cauchy's formula in the right half-plane gives

\[\int_0^\infty e^{-st}k(t)\,dt
=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
\frac{F(z)}{s-z}\,dz=F(s).
\]

The closing integrals vanish because $F(z)=O(|z|^{p-2})$ there. Lemmas 4.1 and 4.2 make the transform analytic to the right of the rightmost negative zero. The meromorphic side is analytic there as well, so the equality extends to every $s>0$. Lemma 3.1 gives $L(s)\to0$ as $s\to\infty$. Integrating $F=-L'$ gives the representation for $L$. Integrating once more and using $\Phi(0)=0$ gives the representation for $\Phi$.

The measure $g(t)dt/t$ satisfies

\[\int_0^\infty\min(1,t)\frac{g(t)}t\,dt<\infty,
\]

because $p<1$ at zero and the tail is exponentially integrable. Thus $\Phi$ has a Lévy–Khintchine representation with nonnegative Lévy measure, zero killing and zero drift. By the standard Bernstein correspondence recalled in [BP21, Section 1.1], it is Bernstein, and $e^{-r\Phi}$ is a probability Laplace transform for every $r>0$. One can also obtain this conclusion by truncating the measure at $t=\varepsilon$, recognising compound Poisson transforms and passing to the limit.

Finally, if $0<d<1$, substitution in the integral gives

\[\Phi(s)-\Phi(ds)
=\int_0^\infty(1-e^{-st})\frac{g(t)-g(t/d)}t\,dt.
\]

The new density is nonnegative because $g$ decreases and is bounded above by the original Lévy density. Therefore $e^{-r\Phi(s)}/e^{-r\Phi(ds)}$ is a probability Laplace transform. This is the defining factorisation for self-decomposability. $\square$

## 5. The order-two anchors and a uniform upper bound

We use one established zero theorem: for $0<\beta<3$, all zeros of $E_{2,\beta}$ are simple and negative. This is explicitly invoked in [GGPS25, proof of Theorem 1], with references to the underlying zero-distribution results. Write them as $-\lambda_n(\beta)$, with increasing positive $\lambda_n$. The function has order $1/2$, so its genus-zero Hadamard product is

\[\Gamma(\beta)E_{2,\beta}(z)
=\prod_{n\ge1}\left(1+\frac z{\lambda_n(\beta)}\right),
\qquad \sum_n\lambda_n(\beta)^{-1}<\infty.
\]

Logarithmic differentiation and Laplace inversion yield

\[g_{2,\beta}(t)=\sum_{n\ge1}e^{-\lambda_n(\beta)t}>0,
\qquad
g'_{2,\beta}(t)=-\sum_{n\ge1}\lambda_n(\beta)e^{-\lambda_n(\beta)t}<0.
\]

Both sums converge for positive $t$: their summands are bounded by suitable constants times $1/\lambda_n$. At the endpoints we have explicit products:

\[E_{2,0}(z)=\sqrt z\sinh\sqrt z
=z\prod_{n\ge1}\left(1+\frac z{\pi^2n^2}\right),
\]

\[\Gamma(3)E_{2,3}(z)
=\left(\frac{\sinh(\sqrt z/2)}{\sqrt z/2}\right)^2
=\prod_{n\ge1}\left(1+\frac z{4\pi^2n^2}\right)^2.
\]

Their kernels are respectively

\[g_{2,0}(t)=1+\sum_{n\ge1}e^{-\pi^2n^2t},
\qquad
g_{2,3}(t)=2\sum_{n\ge1}e^{-4\pi^2n^2t}.
\]

Both are strictly positive and strictly decreasing.

**Lemma 5.1.** $\mathcal C_2=(0,3]$.

**Proof.** The products prove admissibility for $0<\beta\le3$. For $\beta>3$, a beta integral gives

\[E_{2,\beta}(-x)
=\frac1{\Gamma(\beta-3)}
\int_0^1t^2(1-t)^{\beta-4}E_{2,3}(-xt^2)\,dt
\]

and hence, for $x>0$,

\[E_{2,\beta}(-x)
=\frac1{x\Gamma(\beta-3)}
\int_0^1(1-t)^{\beta-4}\bigl(1-\cos(t\sqrt x)\bigr)\,dt>0.
\]

The identity follows term by term from the defining series. The integral is finite for $\beta>3$, and its integrand is positive on a set of positive measure. Thus $E_{2,\beta}$ has no negative real zero. Positive coefficients exclude nonnegative real zeros.

The function is non-polynomial and entire of order $1/2$, so Hadamard factorisation implies that it has zeros. Consequently the Taylor series at zero of $1/E_{2,\beta}(-z)$ has a finite convergence radius. If the reciprocal were completely monotone, all coefficients of that series would be nonnegative, by passing its derivative signs to zero. Pringsheim's theorem [FS09, Theorem IV.6] would force a singularity at the positive real endpoint of the convergence disk. This contradicts the strict positivity of $E_{2,\beta}(-x)$ for every $x>0$. $\square$

**Lemma 5.2.** For every $\varepsilon>0$, there is a two-sided neighbourhood of $\alpha=2$ in which $\mathcal C_\alpha\subset(0,3+\varepsilon)$.

**Proof.** First prevent $\beta$ from escaping to infinity. A positive completely monotone function is log-convex. For $1/E_{\alpha,\beta}$, its log-convexity at zero implies

\[R(\alpha,\beta):=
\frac{\Gamma(\beta)\Gamma(\beta+2\alpha)}{\Gamma(\beta+\alpha)^2}\ge2.
\]

This follows directly from $E'(0)^2\ge E(0)E''(0)$ and the first three series coefficients. The decreasing trigamma function gives

\[\log R(\alpha,\beta)
=\int_0^\alpha\int_0^\alpha\psi'(\beta+u+v)\,du\,dv
\le\alpha^2\psi'(\beta)
\le4.41\left(\frac1\beta+\frac1{\beta^2}\right)
\]

for $\alpha\in[1.9,2.1]$. The last bound follows from

\[\psi'(\beta)=\sum_{n\ge0}(\beta+n)^{-2}
\le\beta^{-2}+\int_0^\infty(\beta+x)^{-2}dx.
\]

If $\beta\ge10$, this is at most $0.4851<\log2$, contradicting $R\ge2$. Thus $\mathcal C_\alpha\subset(0,10)$ uniformly.

If the lemma failed, there would be $\alpha_n\to2$ and $\beta_n\in[3+\varepsilon,10]$ with completely monotone reciprocals. Pass to a subsequence with $\beta_n\to\beta_*>3$. The series for $E$ and all its argument derivatives depend continuously on the parameters on compact sets. On the positive real axis the denominators are positive, so every reciprocal derivative converges. Its alternating sign persists in the limit, making $1/E_{2,\beta_*}$ completely monotone, contrary to Lemma 5.1. $\square$

## 6. Stability on compact subsets of the interior

**Proposition 6.1.** For every nonempty compact $J\subset(0,3)$, there exists $\delta_J>0$ such that $g_{\alpha,\beta}>0$ and $g'_{\alpha,\beta}<0$ whenever $|\alpha-2|<\delta_J$ and $\beta\in J$.

**Proof.** Fix $\beta_*\in J$ and choose $B$ strictly between the first two positive zero magnitudes of $E_{2,\beta_*}$. The outer-sector estimate in Lemma 3.1 excludes zeros at large modulus in $\operatorname{Re}z\ge-B$, uniformly for parameters near $(2,\beta_*)$. On the remaining compact rectangle, Rouché's theorem preserves exactly one zero in that half-plane and leaves the boundary zero-free. A small circle around the anchor zero isolates it. The perturbed zero is simple and real, because non-real zeros would occur in a conjugate pair. It remains negative and a positive distance from both zero and the line $\operatorname{Re}z=-B$.

Lemma 4.2 gives $g>0$ and $g'<0$ for sufficiently large times, uniformly in a small parameter neighbourhood. Cover $J$ by finitely many such neighbourhoods, using the smallest permitted $\alpha$-width and the largest large-time cutoff. Lemma 4.1 supplies a uniform small-time cutoff. On the intervening compact time interval, the order-two kernels and their derivatives have strict signs by Section 5. Joint continuity and compactness preserve both signs when $\alpha$ is sufficiently close to two. $\square$

For positive $\beta$, the retained zero is strictly negative, so Lemma 4.3 gives the Bernstein and self-decomposability conclusions throughout this region.

## 7. Uniform stability at the lower endpoint

**Proposition 7.1.** There exist $\eta_0>0$ and $\delta_0>0$ such that $g>0$ and $g'<0$ for every $t>0$ when $|\alpha-2|<\delta_0$ and $0\le\beta\le\eta_0$. For $\beta>0$, the Bernstein and self-decomposability conclusions hold.

**Proof.** At $(2,0)$ retain the two simple zeros zero and $-\pi^2$, and put $B=2\pi^2$. Lemma 3.1 excludes large zeros in $\operatorname{Re}z\ge-B$. Rouché's theorem on a compact rectangle and on two disjoint small circles preserves exactly two simple real zeros in the half-plane. Write them as $-\lambda_0$ and $-\lambda_1$, with $\lambda_1$ near $\pi^2$.

The identity $E_{\alpha,0}(z)=zE_{\alpha,\alpha}(z)$ shows that the first zero is exactly zero when $\beta=0$. When $\beta>0$, positive coefficients exclude every nonnegative real zero; hence this real root near zero must be strictly negative. After shrinking the parameter rectangle, there are constants $0<a_1<a_2<B$ such that

\[0\le\lambda_0<a_1,\qquad a_1\le\lambda_1\le a_2<B,
\]

with $\lambda_0>0$ for $\beta>0$. Lemma 4.2 gives

\[g(t)=e^{-\lambda_0t}+e^{-\lambda_1t}+O(t^{-1}e^{-Bt}),
\]

\[g'(t)=-\lambda_0e^{-\lambda_0t}-\lambda_1e^{-\lambda_1t}
+O(t^{-2}e^{-Bt}).
\]

These imply the required large-time signs uniformly up to $\beta=0$. Retaining the second zero is essential for the derivative: the first negative term can vanish as $\lambda_0\to0$, but

\[\lambda_1e^{-\lambda_1t}\ge a_1e^{-a_2t}
\]

still dominates the remainder. Small-time signs follow from Lemma 4.1. On the intervening compact interval they follow from continuity and the explicit strictly signed anchor $g_{2,0}$ in Section 5.

For each $\beta>0$, $\lambda_0>0$, and the kernel is exponentially integrable at infinity. Lemma 4.3 applies. Uniform integrability as $\beta\downarrow0$ is neither true nor needed, and no normalised probability law at $\beta=0$ is asserted. $\square$

## 8. The exact boundary near $(2,3)$

Put $a=2\pi$, $z_0=-a^2$ and $B=2a^2$. At the anchor,

\[E_{2,3}(z)=\frac{\cosh\sqrt z-1}{z},
\]

whose zeros are $-a^2n^2$, each of multiplicity two. Exactly two zeros, counted with multiplicity, lie both in the disk $|z|<B$ and in the half-plane $\operatorname{Re}z>-B$.

**Lemma 8.1.** In a neighbourhood of $(2,3)$, these two zeros stay close to $z_0$, and every other zero lies outside the disk $|z|<B$ and to the left of $\operatorname{Re}z=-B$.

**Proof.** Rouché's theorem preserves the disk count and the count on a small circle around $z_0$. For the unbounded half-plane, first use Lemma 3.1 to exclude large zeros uniformly, then apply Rouché on the remaining compact rectangle. All chosen boundaries are zero-free at the anchor and remain so after shrinking the neighbourhood. $\square$

The disk and half-plane statements have distinct roles: the former identifies the zeros of smallest modulus, while the latter controls the large-time inverse transform.

At the double zero,

\[E_{2,3}(z_0)=E'_{2,3}(z_0)=0,
\qquad E''_{2,3}(z_0)=\frac1{4a^4}>0.
\]

The implicit function theorem gives a real analytic critical point $\xi(\alpha,\beta)$ near $z_0$. On a fixed sufficiently small real interval around $z_0$, $E$ remains strictly convex and has positive endpoint values. Define the local minimum

\[m(\alpha,\beta)=E_{\alpha,\beta}(\xi(\alpha,\beta)).
\]

Section 10 calculates

\[\partial_\beta m(2,3)
=\partial_\beta E_{2,3}(z_0)=I(a)/a^2>0.
\]

The implicit function theorem therefore provides a unique real analytic curve $\beta=b(\alpha)$, with $b(2)=3$, on which $m=0$. Locally $m$ increases with $\beta$. Strict convexity shows that the isolated pair consists of two simple real zeros when $\beta<b(\alpha)$, a double real zero when $\beta=b(\alpha)$, and a non-real conjugate pair when $\beta>b(\alpha)$.

**Proposition 8.2.** In a neighbourhood of $(2,3)$, reciprocal complete monotonicity holds exactly when $\beta\le b(\alpha)$. On the admissible side, $g>0$, $g'<0$, and all conclusions of Lemma 4.3 hold, including at the double-zero boundary.

**Proof of sufficiency.** When the two zeros are real, write them as $-\lambda_1,-\lambda_2$, repeating a double zero. Their magnitudes stay in a compact subinterval of $(0,B)$. Lemma 4.2 gives positive and negative large-time signs for $g$ and $g'$, uniformly even at coalescence. Its coefficients are one per zero, or two for a double zero; there is no divergent simple-pole residue.

Lemma 4.1 supplies the small-time signs uniformly. On the intermediate compact interval, both signs persist from the explicit anchor

\[g_{2,3}(t)=2\sum_{n\ge1}e^{-4\pi^2n^2t},
\qquad
g'_{2,3}(t)=-8\pi^2\sum_{n\ge1}n^2e^{-4\pi^2n^2t}.
\]

Lemma 4.3 now applies.

**Proof of necessity.** If $\beta>b(\alpha)$, the pair is non-real and, by Lemma 8.1, consists of the zeros of smallest modulus. Let their common modulus be $\rho<B$. If $1/E$ were completely monotone, the Taylor coefficients at zero of $1/E(-z)$ would all be nonnegative. The radius of this series is exactly $\rho$, since the nearest singularities are the two non-real poles. Pringsheim's theorem forces a singularity at the positive real point $z=\rho$. But $E(-\rho)\ne0$: the only zeros inside $|z|<B$ are the non-real pair. The reciprocal is analytic there, a contradiction. $\square$

## 9. Proof of the global parameter classification

We now combine the parameter regions without assuming in advance that $\mathcal C_\alpha$ is an interval.

Proposition 7.1 gives admissibility and the stronger distributional conclusions for $0<\beta\le\eta_0$ when $\alpha$ is close to two. Reduce $\eta_0$ if necessary so that $\eta_0<1$. Choose $0<\eta_3<1$ so that Proposition 8.2 applies whenever $|\beta-3|<\eta_3$, and shrink the $\alpha$-neighbourhood so that $|b(\alpha)-3|<\eta_3/4$. Proposition 6.1 applies to the compact interval

\[[\eta_0/2,\;3-\eta_3/2]\subset(0,3).
\]

These three regions overlap. Together they establish the Bernstein and self-decomposability conclusions for every $0<\beta\le b(\alpha)$.

Lemma 5.2, with $\varepsilon=\eta_3/2$, excludes every $\beta\ge3+\eta_3/2$ uniformly near order two. Every remaining candidate $\beta>b(\alpha)$ lies in the neighbourhood covered by Proposition 8.2 and is excluded there. Taking the minimum of the finitely many required $\alpha$-widths proves

\[\mathcal C_\alpha=(0,b(\alpha)]
\]

on a two-sided neighbourhood of two, with all stated probabilistic conclusions. This proves Theorem B apart from the derivative formula. $\square$

## 10. The tangent to the boundary

For $\eta>0$, a beta integral yields

\[E_{2,3+\eta}(-x^2)
=\frac1{x^2\Gamma(\eta)}
\int_0^1(1-t)^{\eta-1}(1-\cos(xt))\,dt,
\qquad x>0.
\]

Let $D(z)=\partial_\beta E_{2,\beta}(z)|_{\beta=3}$. Subtract the endpoint value $1-\cos x$ inside the integral and use $1/\Gamma(\eta)=\eta+\gamma\eta^2+O(\eta^3)$. This gives

\[D(-x^2)=\frac1{x^2}\left[
\gamma(1-\cos x)
+\int_0^1\frac{\cos x-\cos(xt)}{1-t}\,dt
\right].
\]

The subtracted integrand is regular at $t=1$ and can be differentiated in $x$ on compact sets. The right parameter derivative agrees with the analytic derivative supplied by the entire defining series.

At $a=2\pi$, a change of variable $t\mapsto1-t$ gives

\[D(-a^2)=\frac{I(a)}{a^2},
\qquad I(a)=\int_0^a\frac{1-\cos u}{u}\,du>0.
\]

Differentiating in $x$ gives

\[\left.\frac d{dx}D(-x^2)\right|_{x=a}
=-\frac{2I(a)}{a^3}-\frac{\operatorname{Si}(a)}{a^2}.
\]

Here

\[\int_0^1\frac{t\sin(at)}{1-t}\,dt=-\operatorname{Si}(a),
\]

as follows by writing $t/(1-t)=1/(1-t)-1$ and using $\sin(a-u)=-\sin u$ and $\cos a=1$.

Termwise parameter differentiation gives the exact identity

\[\partial_\alpha E_{\alpha,\beta}(z)
=z\partial_z\partial_\beta E_{\alpha,\beta}(z).
\]

Since $z=-x^2$, the preceding formulas imply

\[\partial_\alpha E_{2,3}(-a^2)
=-\frac{I(a)}{a^2}-\frac{\operatorname{Si}(a)}{2a}.
\]

Along the double-zero curve, differentiation of $E_{\alpha,b(\alpha)}(x(\alpha))=0$ gives no $x'$ term at the anchor because $E'=0$. Therefore

\[b'(2)=-\frac{\partial_\alpha E_{2,3}(-a^2)}{\partial_\beta E_{2,3}(-a^2)}
=1+\frac{a\operatorname{Si}(a)}{2I(a)}.
\]

This proves the derivative assertion in Theorem B. Positivity of $\operatorname{Si}(2\pi)$ follows by pairing the positive integral over $(0,\pi)$ with the smaller-in-magnitude negative integral over $(\pi,2\pi)$.

For numerical orientation,

\[I(2\pi)=2.437653393057224411810710341436684144412\ldots,
\]

\[\operatorname{Si}(2\pi)=1.418151576132628450245780162299749429142\ldots.
\]

Independent summation and differentiation of the defining series at 90-digit working precision in the supplied independent check script give

\[\partial_\beta E_{2,3}(-4\pi^2)
=0.0617464817735797030375322568988971256331\ldots,
\]

\[\partial_\alpha E_{2,3}(-4\pi^2)
=-0.1745993984711147813869948041372633002418\ldots.
\]

They agree with the exact formulas. The numerical values check algebra and sign conventions; the analytic identities prove the result.

## 11. Consequences, limitations and consistency checks

### 11.1. What the conjecture resolution covers

Conjecture 25 of [GGPS25] asserts, for $1<\alpha<2$, the equivalence of three conditions: the parameter band $\beta\in[\alpha-1,\alpha]$, complete monotonicity of $1/E_{\alpha,\beta}$, and the global modulus inequality. The present paper settles one link. Theorem A shows that complete monotonicity holds on the whole triangle $0<\beta<\alpha-1$ for **every** $\alpha\in(1,2)$. Theorem B shows that for $1<\alpha<2$ close to two it also holds on $(\alpha,b(\alpha)]$, with $b(\alpha)\to3$, and fails beyond $b(\alpha)$. Thus the band is not necessary for complete monotonicity, on either side.

What is *not* settled: whether the band is exactly where the global modulus inequality holds. The band's own Bernstein-logarithm property is [GGPS25, Remark 4(a)]; Theorem A adds only the triangle below it. For $\alpha\ge2$, [GGPS25, Remark 4(b)] gives complete monotonicity whenever all zeros are negative, in particular for $\beta\in[0,2\alpha-1]$; near $\alpha=2^+$, Theorem B gives the larger exact range $(0,b(\alpha)]$, since $b'(2)>2$. On the band itself, Lemma 2.2 also gives self-decomposability of the law with Laplace transform $1/F_\gamma$, since $F_\gamma(cq)/F_\gamma(q)$ is a probability Laplace transform. Below the band, our argument gives self-decomposability only in Theorem B's neighbourhood; elsewhere Theorem A gives infinite divisibility.

The necessary condition for the global complex modulus inequality proved in [GGPS25, Proposition 14] is not challenged. At the counterexample parameters, namely $\beta\in(0,\alpha-1)$ for every $1<\alpha<2$ and $\beta\in(\alpha,b(\alpha)]$ for $\alpha<2$ near two, our Bernstein and complete-monotonicity properties hold while that global inequality fails. The asserted equivalence between the properties is what the theorem disproves.

Theorem B is local in order and global in the positive second parameter. It does not determine $\mathcal C_\alpha$ when $\alpha$ stays away from two. It does not provide a numerical radius for the guaranteed neighbourhood. In particular, the decimal tangent does not certify any arbitrarily chosen finite parameter pair.

### 11.2. Bernstein versus complete Bernstein

For $\beta=2$ and $\alpha<2$ sufficiently close to two, the Bernstein function in Theorem B is not a complete Bernstein function. Indeed,

\[E_{\alpha,2}(-x)\sim\frac1{x\Gamma(2-\alpha)}>0
\qquad(x\to\infty).
\]

It has only finitely many negative real zeros. Positive coefficients exclude nonnegative real zeros. As a non-polynomial entire function of order $1/\alpha<1$, it has infinitely many zeros by Hadamard factorisation, hence non-real zeros. Its logarithmic derivative has genuine poles at those zeros. A complete Bernstein function and its derivative extend holomorphically to the slit plane $\mathbb C$ minus $(-\infty,0]$; such poles prevent that extension.

For $\alpha>2$, the present argument does not assert that all zeros are real or that the logarithm is complete Bernstein. It therefore does not resolve the separate global-modulus and real-zero conjecture [GGPS25, Conjecture 26].

### 11.3. Checks on normalisation and endpoint behaviour

At $(\alpha,\beta)=(2,2)$, the small-time formula becomes

\[g(t)=\frac1{2\sqrt{\pi t}}-\frac12+o(1),
\]

in agreement with the theta sum $\sum_{n\ge1}e^{-\pi^2n^2t}$. At $(2,0)$ it becomes $1/(2\sqrt{\pi t})+1/2+o(1)$, agreeing with the additional zero-mode contribution one. At $(2,3)$ it becomes $1/(2\sqrt{\pi t})-1+o(1)$, agreeing with $2\sum_{n\ge1}e^{-4\pi^2n^2t}$.

For admissible positive parameters,

\[\int_0^\infty g(t)\,dt
=\Phi'(0)=\frac{\Gamma(\beta)}{\Gamma(\alpha+\beta)}.
\]

At $(2,2)$ this is $1/6$, matching $\sum_{n\ge1}1/(\pi^2n^2)$. Near $\beta=0$, the first zero has magnitude

\[\lambda_0(\alpha,\beta)=\Gamma(\alpha)\beta+O(\beta^2),
\]

because $E(0)=\beta+O(\beta^2)$ and $E'(0)=1/\Gamma(\alpha+\beta)$. The mean $\Gamma(\beta)/\Gamma(\alpha+\beta)$ diverges like $1/[\Gamma(\alpha)\beta]$, consistent with this slow first-zero contribution. The proof deliberately requires exponential integrability for each positive $\beta$, not uniformly at the anchor $\beta=0$.

Finally, $Q(0)=1$ is essential for the probability-law statement. The unnormalised reciprocal has value $\Gamma(\beta)$ at zero and is a positive constant multiple of the probability Laplace transform.


### 11.4. Literature and verification boundary

A dated literature search (recorded in the accompanying novelty report) found no earlier statement of Theorem A on the triangle $0<\beta<\alpha-1$, of the exact interval in Theorem B, or of the boundary tangent. Semantic Scholar listed four works citing [GGPS25] at the time of the search; none addresses Conjecture 25. The SSRN preprint of Polson [Pol26], whose abstract discusses related hitting-time distributions, could be inspected only at abstract level and remains a priority uncertainty. No guarantee of historical priority is made.

Two inputs are taken from the literature and not reproved: the hitting-time construction behind Lemma 2.2 [GGPS25, proof of Proposition 3], and the order-two zero theorem used in §5 (all zeros of $E_{2,\beta}$ are simple and negative for $0<\beta<3$), cited from [GGPS25, proof of Theorem 1]. The boundary analysis of §8 uses only the explicit anchor at $(2,3)$ and does not depend on that zero theorem. At $\alpha=2$, the sufficiency half of Lemma 5.1 is also [GGPS25, Remark 4(b)].

The supplied scripts check exact reciprocal coefficients, the tangent formula against direct series differentiation, the certified modulus failure of the Appendix, and the numerical curve of §12. They do not prove positivity over unbounded time intervals or certify a numerical neighbourhood; those assertions rest on the analytic proofs.

## 12. The boundary curve numerically, and a replacement conjecture

*This section is numerical exploration, not proof.*

The double-zero system $E_{\alpha,\beta}(x)=\partial_xE_{\alpha,\beta}(x)=0$ can be continued in $\alpha$ from $(\alpha,\beta,x)=(2,3,-4\pi^2)$ by Newton's method with 40-digit arithmetic and direct series summation (script `boundary_curve.py`). At every computed point the solution is a local minimum of $E_{\alpha,\beta}$ on the real axis ($E''>0$). A central difference at $\alpha=2\pm0.01$ gives slope $2.82768$, matching the exact $b'(2)$ to the expected $O(10^{-6})$.

| $\alpha$ | $b(\alpha)$ | $b(\alpha)-\alpha$ | collision point $-x(\alpha)$ |
|---|---|---|---|
| 1.5 | 1.7937 | 0.2937 | 11.40 |
| 1.6 | 2.0019 | 0.4019 | 14.04 |
| 1.7 | 2.2266 | 0.5266 | 17.68 |
| 1.8 | 2.4678 | 0.6678 | 22.73 |
| 1.9 | 2.7256 | 0.8256 | 29.72 |
| 1.95 | 2.8607 | 0.9107 | 34.19 |
| 1.99 | 2.9718 | 0.9818 | 38.35 |
| 2 (exact) | 3 | 1.0000 | $4\pi^2=39.48$ |
| 2.05 | 3.1435 | 1.0935 | 45.74 |
| 2.1 | 3.2911 | 1.1911 | 53.18 |
| 2.2 | 3.5990 | 1.3990 | 72.56 |
| 2.3 | 3.9237 | 1.6237 | 100.20 |
| 2.5 | 4.6235 | 2.1235 | 197.34 |

Two features stand out. First, $b(\alpha)>\alpha$ on the whole computed range $1.5\le\alpha<2$, with $b(\alpha)-\alpha$ shrinking from about $0.83$ at $\alpha=1.9$ to about $0.29$ at $\alpha=1.5$. Second, the curve is smooth and close to linear near $2$. This suggests:

**Conjecture 12.1.** The local double-zero branch through $(\alpha,\beta,x)=(2,3,-4\pi^2)$ extends uniquely as a real analytic graph $(b(\alpha),x(\alpha))$ throughout $1<\alpha<2$, and $\mathcal C_\alpha=(0,b(\alpha)]$ for every such $\alpha$.

The numerical evidence covers only $1.5\le\alpha<2$, and we have not checked numerically that this pair remains the zero set nearest the origin; the conjecture for $\alpha$ close to $1$ is correspondingly more speculative.

Theorem A gives $(0,\alpha]\subseteq\mathcal C_\alpha$ unconditionally; the conjecture would add $(\alpha,b(\alpha)]$ and exclude everything above. Proving it would require global continuation of the branch with control of where the other zeros lie, positivity and monotonicity of the kernel $g$ below the boundary on all time ranges (at $\alpha=2$ the middle range is controlled by explicit products), and exclusion of every parameter above $b(\alpha)$, not only those near it. For $\alpha>2$ the curve continues, but Theorem B is claimed only on its neighbourhood of $2$, and the separate real-zero question there is [GGPS25, Conjecture 26].

## Appendix. A certified failure of the modulus inequality below the band

Take $(\alpha,\beta,z)=(3/2,1/4,-60+i)$, a point of the triangle covered by Theorem A, so $1/E_{3/2,1/4}$ is completely monotone. The script `certify_example.py` computes with exact rational arithmetic only: it bounds $\pi$ by Machin's formula with alternating arctangent series, bounds $\Gamma(1/4)$ through the arithmetic–geometric mean identity, and sums the series split into even and odd indices (which gives rational recurrences after two gamma constants are factored out). One hundred terms of each subseries suffice; each tail is bounded by $10^{-240}$. Outward rounding preserves every inequality. The enclosures are:

| Quantity | Certified enclosure (shared digits, then the last digits of the lower and upper endpoints) |
|---|---|
| $E_{3/2,1/4}(-60)$ | $0.00133487672100398060813\,[0,1]$ |
| $\operatorname{Re}E_{3/2,1/4}(-60+i)$ | $0.0012657163197546662746\,[19,20]$ |
| $\operatorname{Im}E_{3/2,1/4}(-60+i)$ | $0.00037788597189713938741\,[2,3]$ |
| $E(-60)^2-\lvert E(-60+i)\rvert^2$ | $0.00000003706025042839686\,[4,5]$ |

Since $E(-60)>0$ and $|E(-60+i)|<E(-60)=E(\operatorname{Re}z)$, the inequality fails strictly at this point. This is one finite instance of Corollary 2.3, which follows in general from [GGPS25, Proposition 14].

## References

[BP21] Bartholmé, C., & Patie, P. (2021). Turán inequalities and complete monotonicity for a class of entire functions. *Analysis Mathematica, 47*(3), 507–527. https://doi.org/10.1007/s10476-021-0088-4

[DLMF] NIST Digital Library of Mathematical Functions, Equation 5.9.2 (Hankel's loop integral for the reciprocal gamma function). https://dlmf.nist.gov/5.9.E2 (accessed 2 November 2026).

[FS09] Flajolet, P., & Sedgewick, R. (2009). *Analytic Combinatorics*. Cambridge University Press. https://doi.org/10.1017/CBO9780511801655 . Theorem IV.6 (Pringsheim's theorem).

[GGPS25] Garrappa, R., Gerhold, S., Popolizio, M., & Simon, T. (2025). On some inequalities for the two-parameter Mittag-Leffler function in the complex plane. *Journal of Mathematical Analysis and Applications, 551*(1), 129588. https://doi.org/10.1016/j.jmaa.2025.129588 . Preprint version inspected: arXiv:2410.11852v4. Locators: Proposition 3 and its proof (including equation (2.2)); Remark 4(a),(b); proof of Theorem 1; Proposition 14; Conjectures 25 and 26.

[KPS24] Konstantopoulos, T., Patie, P., & Sarkar, R. (2024). A new class of solutions to the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis. *Annales de l'Institut Fourier, 74*(1), 377–421. https://doi.org/10.5802/aif.3600 . Section 4.2.4 (Mittag–Leffler examples).

[P09] Patie, P. (2009). Infinite divisibility of solutions to some self-similar integro-differential equations and exponential functionals of Lévy processes. *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques, 45*(3), 667–684. https://doi.org/10.1214/08-AIHP182 . Corollary 4.1 (the diagonal case $\beta=\alpha$).

[Pol26] Polson, N. G. (2026). Thorin quantisation [Preprint]. SSRN. https://doi.org/10.2139/ssrn.7277540 . Abstract only inspected.

[SSV12] Schilling, R. L., Song, R., & Vondraček, Z. (2012). *Bernstein Functions: Theory and Applications* (2nd ed.). De Gruyter. https://doi.org/10.1515/9783110269338 . Chapter 3 (closure properties of Bernstein and completely monotone functions).
