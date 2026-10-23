# A Reader Correction Dossier for Hecke Theta Normalizations

## Public reader preface

**Learning question and purpose.** Expose a substantive cycle of convention tracking, counterexample construction, formula repair, and later source comparison. This case belongs to Neukirch VII §7. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Ideal-number coordinates, conjugation conventions, ideal-class characters, trace-dual lattices, Poisson summation, and finite Gauss sums. The article identifies the narrower dependencies it actually uses.

**Argument route.** Separate the three conjugations; identify the ordinary class-character phase; retain the ordinary and exceptional zero-term branches separately; follow the two counterexamples and the double-transformation consistency check.

**Historical scope and qualification.** The historical project records closed-pass1/reader-corrected, including a source-statement diagnosis and counterexamples. A later note explicitly says no matching formal erratum was obtained. This release neither claims publisher confirmation nor independently audits the diagnosis. Publish as dated reader corrections. The source reports closed-pass1/reader-corrected and no matching formal erratum; do not claim publisher confirmation, novelty, or a new independent audit. Replace excluded artifact links honestly.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0506`, originally recorded on 2026-08-26, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch VII §7; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `4128b24a14cea08ea073a629b899161def410764e3a1ee9573056bd2d0609173`. English source-article SHA256: `8828d328c4d7d1b68b88aaf00940abb80058877a1d57f6ef2005c3f0b3326dd8`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

First-pass verification note for Theorem 7.7, 2026-10-04: PDF 501–503 through the 7.7 square were visually rechecked. The earlier phase and zero-term corrections and both exact counterexamples are reliable; mathematical counterarguments suffice to retain book-statement-error, but this session obtained no matching formal erratum and does not claim publisher confirmation. The reviewed synthesis (archived article NA0505; outside this curated selection) of 2026-08-26 21:31 is reused, while this component remains pass-1. “This session,” “awaiting review,” and the closing exercise successor are August 26 snapshots. The present window verifies only 7.7, with 7.8 left for later; the historical live-state continuation is outside this public case study. See the current verification (archived article NA0710; outside this curated selection).

Ideal-class decomposition, Poisson duality, and finite Gauss sums should combine into a transformation constant of modulus $1$. Continuing from the Gauss/lattice preparation chain (archived article NA0502; outside this curated selection), independent assembly of constants found that ideal numbers allowed by the book can be nonreal at real places, so coordinate conjugation cannot be conflated with permutation of embeddings. Also, at modulus $1$ and weight $0$, adding a fixed $1$ to each partial theta is incompatible with a nontrivial class character.

**Layered verdict.** The preparation chain Definition 7.4–Lemma 7.6 is closed-pass1/source-checked. Theorem 7.7 at its printed generality is **book-statement-error**; Corollary 7.8 is likewise affected in models allowing nontrivial real-place phases. The corrected formulas, proofs, and two counterexamples below are **closed-pass1/reader-corrected**, without silently upgrading the incorrect book statement or claiming reviewed status. The corrected chain has no remaining proof gap; later Hecke $L$-series applications must still continue through the actual character interface.

Source order: the first p. 501 image exposed the theorem and proof opening; before opening pp. 502–503 the independent argument had reached the dual-lattice substitution and a suspected remaining phase. Pp. 501–502 were then checked at r240 and p. 503 at r160, with returns to the three involutions on p. 455, admissibility on p. 459, and ideal-number root choices on pp. 496–497. The full source proof is not claimed to have remained entirely unexposed.

## 1. Three conjugations must remain distinct

In $\mathbf C=\prod_\tau\mathbb{C}$ the book's notation is: $z^*$ permutes $\tau\leftrightarrow\bar\tau$; ${}^*z$ takes ordinary complex conjugation in each coordinate; $\bar z={}^*(z^*)$ composes the two. The Minkowski real form is $\mathbf R=\{z:\bar z=z\}$. The Hermitian pairing is

$$
\langle x,y\rangle=\sum_\tau x_\tau\overline{y_\tau}
=\operatorname{Tr}(x\,{}^*y).
$$

Thus ${}^*z$ is the adjoint multiplication operator. On $\mathbf R$, ${}^*z=z^*$, but not on general $\mathbf C$. Proposition 7.1 requires conjugate root choices only for **nonreal embedding pairs**; real embeddings allow arbitrary complex roots, so $\widehat K^*$ need not lie in $\mathbf R$. This is not a definition change in this session but freedom explicitly given by the construction on p. 496.

Here $p$ is a nonnegative integral admissible weight: real places use only 0 or 1, and at most one coordinate of a complex pair is nonzero. The character $\chi$ is on the finite group $G=(\widehat{\mathcal O}/\mathfrak m)^*$, primitive meaning conductor $\mathfrak m$ on the ordinary residue-unit group. Modulus 1 still permits nontrivial ordinary class characters. The parameter $z\in\mathbf H$ satisfies $z=z^*$, equality of coordinates on conjugate embedding pairs; none of these conditions is extended to arbitrary weights or complex coordinates.

Write $P_p(a)=N(a^p)$, $\bar p_\tau=p_{\bar\tau}$, $T=\operatorname{Tr}(p)$. For $r\in\mathbf R$,

$$
P_p({}^*r)=P_{\bar p}(r).
$$

For a general ideal number $a$ this identity can fail. That is precisely the risk in the book's separate conjugation cancellations for $g$ on p. 502 and $a$ on p. 503.

## 2. The omitted quantity is an ordinary class character

Let $C=J/P$, $D=[\mathfrak m\mathfrak d]$, and $A'=DA^{-1}$. For class $A$ and any ideal number $a$ in it define

$$
\eta_p(A)=\frac{P_p(a)P_{\bar p}(a)}{N(|a|^{2p})}.
$$

The denominator is positive, and $|a|$ agrees on conjugate pairs, so this number has modulus $1$. It is a homomorphism under ideal-number multiplication. If $a\in K^*$, then $a\in\mathbf R$ and the numerator equals $|P_p(a)|^2=N(|a|^{2p})$; it is therefore trivial on $K^*$ and descends to a character of the finite class group. Changing the representative in the same class leaves it unchanged. Also $\eta_{\bar p}=\eta_p$.

Complex-pair contributions always cancel; a possible defect comes only from the complex roots at real places used by $p$. In particular, if $p$ vanishes at all real places, or every real-place coordinate in the ideal-number model is real, then $\eta_p=1$. These are sufficient conditions, not hypotheses already stated in the book, and no claim is made that every number field admits an arbitrarily chosen model satisfying the latter condition.

## 3. Exact correction in the ordinary branch

First assume $\mathfrak m\ne1$ or $p\ne0$, so the zero term vanishes. Let $\chi$ be primitive, $q=md/|md|$, and define

$$
J_p(z)=N((z/i)^{p+\frac{1}{2}}),
\qquad
W(\chi,\bar p)=\frac{\tau(\chi)}{i^T P_{\bar p}(q)\sqrt{\mathrm N\mathfrak m}}.
$$

The constant $W$ is exactly as printed. Half-powers use the principal branch in the right half-plane of $z/i$ for each upper-half-space coordinate and then multiply; no arbitrary new square root may be taken of the final scalar product. The corrected partial-theta transformation is

$$
\theta^p(A,\chi,-1/z)
=\eta_p(A)W(\chi,\bar p)J_p(z)
\theta^{\bar p}(A',\bar\chi,z).
$$

The additional factor is $\eta_p(A)$, not a patch depending on $z$. The Gauss modulus gives exactly $|W(\chi,\bar p)|=1$, making the constant $\eta_p(A)W(\chi,\bar p)$ have modulus $1$; $J_p(z)$ still carries its weight varying with $z$.

**Dual and covolume.** Take $(a)=\mathfrak a\in A$ with $\mathfrak a$ coprime to the modulus. Let $\Gamma=\mathfrak m\mathfrak a^{-1}$ and let $\Gamma'$ be its Euclidean dual. Lemma 5.7 and the discriminant volume formula give

$$
{}^*\Gamma'=\mathfrak a(\mathfrak m\mathfrak d)^{-1},
\qquad
\operatorname{vol}(\Gamma)=\frac{\mathrm N\mathfrak m}{\mathrm N\mathfrak a}\sqrt{|d_K|}.
$$

Set $R=|md/a^2|$. Proposition 3.6 transforms every lattice theta in Lemma 7.6 to its dual-lattice theta, with factor

$$
A(z)=\frac{P_p(R)}{i^T\sqrt{\mathrm N\mathfrak m}}J_p(z).
$$

The exact general transformation used here is

$$
\theta_\Gamma^p(x,0,-1/(zR))
=A(z)\theta_{\Gamma'}^p(0,x,zR).
$$

The characteristic goes from $(x,0)$ to $(0,x)$ with fixed phase $e^{-2\pi i\langle x,0\rangle}=1$, so no extra translation constant is missing.

The square-root constant can be checked directly: $N(R^{1/2})=\sqrt{\mathrm N\mathfrak m\,|d_K|}/\mathrm N\mathfrak a$; division by $\operatorname{vol}(\Gamma)$ gives exactly $1/\sqrt{\mathrm N\mathfrak m}$. No additional complex-place $2$ is inserted, since self-dual measure already includes it.

**Dual lattice points return to ideal integers.** For $g'\in\Gamma'$ set $b=(md/a){}^*g'$. Its values are exactly the ideal integers in class $A'$ together with zero. Conversely $r=ab/(md)\in K$, $g'={}^*r$, so

$$
\langle x,g'\rangle=\operatorname{Tr}(axb/(md)),
\qquad
P_p(g')=P_{\bar p}(a/md)P_{\bar p}(b).
$$

The correct reason for the second identity is that **the quotient $r$ belongs to $K$**. One cannot separately claim $P_p({}^*b)=P_{\bar p}(b)$ and the corresponding denominator identity for arbitrary ideal numbers. The separate intermediate assertion on p. 502 fails, but its final formula (3) is repaired by this quotient argument.

For nonzero $b$, both $|a|,|b|,|md|$ lie in the positive cone, giving the following quadratic identity coordinatewise; for $b=0$ both sides are directly zero:

$$
\langle g'zR,g'\rangle=\langle bz/|md|,b\rangle.
$$

**Finite Fourier transform and remaining phase.** Incorporating $\chi(a)$ from Lemma 7.6 into the finite sum makes the inner sum exactly

$$
\sum_{x\in U}\chi(ax)e^{2\pi i\operatorname{Tr}(axb/(md))}
=\tau(\chi,b)=\overline{\chi(b)}\tau(\chi).
$$

For noncoprime $b$ the final equality still follows from the noncoprime branch of Proposition 7.5. At $b=0$ the primitive finite character for a proper modulus is nontrivial, so the finite sum vanishes; if $p\ne0$, the polynomial itself vanishes. Gaussian normal convergence from the preceding note permits interchange of summation.

The remaining polynomial constant is $P_p(a)P_{\bar p}(a/md)P_p(R)$. Since $|md|$, $|a|$ agree on embedding pairs, exactly

$$
P_p(a)P_{\bar p}(a/md)P_p(R)
=\eta_p(A)P_{\bar p}(q)^{-1}.
$$

This gives the correction. On p. 503 the book cancels $\eta_p(A)$ to $1$; this needs the corresponding additional condition. The preceding dual lattice, covolume, and Gauss modulus remain unchanged.

## 4. Immediate consequence and another unambiguous form

Occurrence-11 verification note, 2026-10-04: the finite class-sum verification of 7.8 (archived article NA0703; outside this curated selection) checked the lower part of PDF 503 and the author's motivation. The formulas, phase, and ordinary-branch conditions below are reliable; preservation of the finite conductor uses only triviality of a class twist on the ordinary residue-unit group. There is no new independent proof, error confirmation, or status upgrade; the old component pass-1 and existing reviewed synthesis are reused separately. “7.8 left for later” in the opening 7.7 note is the preceding window's snapshot.

Pull $\eta_p$ back to $G=(\widehat{\mathcal O}/\mathfrak m)^*$. Since $\eta_p(A)\eta_p(A')=\eta_p(D)$, summing over the finite ideal classes gives the corrected Corollary 7.8:

$$
\theta^p(\chi,-1/z)=\eta_p(D)W(\chi,\bar p)J_p(z)
\theta^{\bar p}(\bar\chi\eta_p^{-1},z).
$$

The twist changes only the ordinary class-character part; the finite residue character remains $\bar\chi|_U$, preserving primitivity. Under $\eta_p=1$ this directly recovers the source, but in general the class character cannot be deleted. Retain $\mathfrak m\ne1$ or $p\ne0$ here as well; neither next section's Mellin conclusions nor $L$-series conclusions are counted as closed.

One may instead never rewrite coordinate conjugation as embedding permutation. Writing the transformed weight directly as $\overline{P_p(b)}$ gives constant

$$
\widetilde W(\chi,p)=\frac{P_p(q)\tau(\chi)}{i^T\sqrt{\mathrm N\mathfrak m}}.
$$

Since $\overline{P_p(b)}=\eta_p(A')^{-1}P_{\bar p}(b)$, this agrees exactly with the correction above. It shows that the correction comes from the actual Fourier weight rather than fitting a constant to examples.

## 5. Real-quadratic counterexample: the missing phase changes nonzero theta

Take $K=\mathbb{Q}(s)$, $s=\sqrt{10}$, $\mathfrak b=(3,1+s)$. The existing ideal-number preparation note independently proved $\mathrm{Cl}_K=C_2$ and $\mathfrak b^2=(1+s)$. In real-embedding order $(s,-s)$ choose

$$
b=(B_1,iB_2),\qquad B_1=\sqrt{1+s},\quad B_2=\sqrt{s-1}.
$$

This fully satisfies Proposition 7.1, and $b^2=(1+s,1-s)$. Take $\mathfrak m=1$, $\chi=1$, $d=2s$, $p=(1,1)$. This is the ordinary branch $p\ne0$, unrelated to the later zero-term issue; $p$ is admissible, $\bar p=p$, and $P_p(b)=3i$. Thus

$$
\eta_p([\mathfrak b])=\frac{(3i)^2}{9}=-1.
$$

To exclude the escape that theta happens to vanish identically, list all ideal integers in class $A=[\mathfrak b]$:

$$
b\left(u+v\frac{1-s}{3}\right),\qquad (u,v)\in\mathbb{Z}^2\setminus\{(0,0)\}.
$$

The second basis vector is $c=-3/b=(-B_2,iB_1)$. Take $z=(it,2it)$; the Gaussian exponent is $-\pi tQ(u,v)$, where

$$
Q(u,v)=\frac{3s-1}{2s}u^2+\frac{3}{s}uv+\frac{3s+1}{2s}v^2.
$$

The real symmetric quadratic form has matrix trace $3$ and determinant $2$, hence eigenvalues exactly $1,2$ and therefore $Q(u,v)\ge u^2+v^2$. Also $Q(1,0)<Q(0,1)<2$; all points with $u^2+v^2\ge2$ are longer. The unique shortest point is thus $\pm b$ with first-term coefficient $2P_p(b)=6i\ne0$. Normal Gaussian convergence makes all remaining exponents strictly larger, so theta is not identically zero; no numerical sum or new finite character is needed.

In this example $D=1$, $A'=A$, $q=(1,-1)$, $\tau(1)=1$. The source gives $W=[i^2P_p(q)]^{-1}=1$, whereas the correct coefficient is $-1$. This is a counterexample to the theorem statement, not merely an unexplained proof line. Direct substitution into the first line of the constant simplification on p. 503 also gives $(-1)(40/9)(9/40)=-1$; only the final line after the invalid phase cancellation becomes $1$.

This class group consists only of the principal class and $A$, with phases $1,-1$ respectively. The difference between the source's two sides for total theta is therefore $-2J_p(z)\theta^p(A,1,z)$, also not identically zero; the same counterexample detects the error in Corollary 7.8.

A different entirely real model might remove this specific phase but does not repair the printed generality for an arbitrary fixed model allowed by Proposition 7.1. The counterexample does not claim this field has no entirely real model.

## 6. Exceptional branch: class characters and the zero term

Now let $\mathfrak m=1$, $p=0$. Then $G=C$, and every ordinary class character has finite conductor $1$, so the principal character alone is insufficient. Let $\Theta_A(z)$ denote **unweighted by a character** theta for the same class lattice, including zero term $1$. The definition on p. 500 actually gives

$$
\theta^0(A,\chi,z)=\chi(A)\Theta_A(z)+1-\chi(A).
$$

The unweighted Poisson formula is $\Theta_A(-1/z)=J_0(z)\Theta_{A'}(z)$. Here $D=[\mathfrak d]$ and Proposition 7.5 gives $\tau(\chi)=\chi(D)$. Termwise substitution gives the correct relation

$$
\theta^0(A,\chi,-1/z)
=\chi(D)J_0(z)\theta^0(A',\bar\chi,z)+R_A(z),
$$

where

$$
R_A(z)=1-\chi(A)-J_0(z)(\chi(D)-\chi(A)).
$$

On p. 502 the book directly drops $\chi(A)$ and treats this branch as unweighted theta for $\chi=1$; that fails for general class characters. A homogeneous repair instead changes the zero term of each partial theta to $\chi(A)$, giving $\chi(A)\Theta_A$; then the homogeneous formula with coefficient $\chi(D)$ holds. The alternatives “retain the original definition and add $R_A$” and “change the zero-term definition” are explicitly distinguished, without silent switching.

An exact counterexample requires no numerical summation. Take $K=\mathbb{Q}(\sqrt{-5})$ with class group $C_2$: the Minkowski bound is less than $3$ and the ideal of norm $2$ is nonprincipal but has principal square. Take nonprincipal class $A$ and its quadratic class character $\chi(A)=-1$. The different is the principal ideal $(2\sqrt{-5})$, so $D=1$, $A'=A$, $\chi(D)=1$. The single complex place at $z=it$ gives $J_0(z)=t$, making the exact difference between the source's sides

$$
R_A(it)=2(1-t).
$$

At $t=2$ the difference is $-2$. This field has no real places, so $\eta_p=1$: the zero-term error is independent of the preceding real-place phase error. Only quadratic-ideal intuition supported by Marcus is reused; proof permission still comes from Neukirch's ideal-number, trace-dual, and Poisson chain.

## 7. Internal consistency and reusable boundaries

Replacing $a$ by same-class $a\alpha$, $\alpha\in K^*$, leaves $\eta_p(A)$ unchanged, so the correction is independent of a temporary class representative. Also $|W|=|\eta_p(A)W|=1$; the normalization factor $(\mathrm N\mathfrak m)^{-1/2}$ comes from covolume and is canceled by the Gauss modulus.

After two transformations in the ordinary zero-term-free branch, Gauss sums satisfy $\tau(\chi)\tau(\bar\chi)=\chi(-1)\mathrm N\mathfrak m$ and $\eta_p(A)\eta_p(A')=\eta_p(D)$, with product of corrected constants $(-1)^T\chi(-1)$. Nonzero theta must satisfy $\chi(-1)=(-1)^T$ because terms pair under $a,-a$; this is necessary, not a guarantee of nonvanishing. The relation $z=z^*$ gives $J_p=J_{\bar p}$, and reciprocal half-power branches in the right half-plane cancel, so the double transformation returns to the original formula. The exceptional branch must carry $R_A$ through both transformations; it cannot drop the additive remainder and use the homogeneous check. Double transformation checks internal consistency only, without determining the phase sign alone; its actual sign still comes from the Fourier constant and nonzero counterexample above.

The safest later interface is to retain the coordinate-conjugate weight first and only then determine whether it can be rewritten as $\bar p$; retain the exceptional zero term until the class-group values of the character are known. Passing all customary principal-ideal examples does not license dropping these two conditions. The author's closing motivation remains valid: ideal factorization, the different, discriminant, Gauss sums, and Poisson each supply a part of the same transformation chain.

Self-test: why can $\eta_p$ be trivial on $K^*$ yet nontrivial on the ideal class group? Why can the quotient formula on p. 502 be repaired while the final phase on p. 503 cannot simply be dropped? Retaining the original zero-term definition, how can $R_A(z)$ be written without repeating Poisson?

The seven printed §7 exercises on PDF p. 504 were verified; this session then independently completed Exercises 1–3, see the ideal-arithmetic note (archived article NA0500; outside this curated selection). The exact successor is Exercise 4 on the same page; Exercises 4–7 remain unattempted, the §8 heading and definition are page-boundary exposure only, and p. 505 remains unopened. Both source errors remain durable caveats; the correction layer awaits later concentrated review, without rewriting earlier pass-1/reviewed layers.
