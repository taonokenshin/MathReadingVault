# Why Class Fields Enter Prime Distribution

## Public reader preface

**Learning question and purpose.** Show how distribution, character nonvanishing, and principal primes meet in the Hilbert class field. This case belongs to Marcus Chapter 8. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Ideal classes, Frobenius elements, elementary finite character theory, Dirichlet series, and the preceding class-number/distribution results.

**Argument route.** Start from the abstract character-distribution mechanism; obtain the cyclotomic case; identify the principal-prime obstruction; state the cited Hilbert-class-field input; compare narrow and ray variants.

**Historical scope and qualification.** The source distinguishes locally explained distribution arguments from cited class-field existence. Its printed limit-point observation remains a reader diagnosis. Hilbert-class-field existence remains a cited textbook input. The printed limit-point diagnosis is a dated reader observation, not a publisher erratum.

**Source and provenance.** The mathematical body is adapted from English study-edition article `MA0170`, originally recorded on 2026-06-30, in the preserved 20 October 2026 snapshot. The textbook reference is Marcus Chapter 8; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `090d0a521f63686b4444b4b7200b0a8bbb95afb21de0db897a2311909291a424`. English source-article SHA256: `a6793ed839fcec7fabf3d764989c8c9f303d5e0236019c1b2b0060482ae5cca5`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

Scope: Chapter 8, after Theorem 48 through the ray-class-field overview, book pp. 164–170 / PDF pp. 179–185.

## Intuition

Theorem 48 is an abstract distribution principle: nonvanishing of nontrivial character $L(s,\chi)$ at $s=1$ gives uniform prime distribution in a finite abelian group. The following text makes two applications.

First, apply it to

$$
G=(\mathbb Z/m\mathbb Z)^\*
$$

to obtain Dirichlet's theorem on arithmetic progressions.

Second, apply it to the ideal class group. The nonvanishing argument needs sufficiently many principal primes. The Hilbert class field $H/K$ supplies them: its completely split primes are precisely the principal primes.

## Theorem 49: Dirichlet theorem as cyclotomic Frobenius

Choose

$$
X=\{p:p\nmid m\},\qquad G=(\mathbb Z/m\mathbb Z)^\*,\qquad \phi(p)=\bar p.
$$

The function $L(s,\chi)$ is the Dirichlet $L$-series from Chapter 7. Before Theorem 44, Marcus showed that nontrivial $\chi\ne1$ extend analytically to $\operatorname{Re}(s)>0$. For the trivial character,

$$
L(s,1)=\zeta(s)\prod_{p\mid m}\left(1-\frac1{p^s}\right),
$$

there is a simple pole at $s=1$.

It remains to show

$$
L(1,\chi)\ne0,\qquad \chi\ne1.
$$

Marcus gives two arguments.

First use the abelian class-number formula in Theorem 44. Taking $K=\mathbb Q(\zeta_m)$,

$$
\prod_{\chi\ne1}L(1,\chi)
$$

equals a nonzero constant times $\rho=h\kappa>0$, so no nontrivial factor can be $0$.

The second argument explains the density mechanism. If some $L(1,\chi)=0$, then

$$
\prod_{\chi\in\widehat G}L(s,\chi)
$$

has a zero canceling the simple pole of $L(s,1)$, giving a finite limit at $s=1$. Combining Euler factors over characters gives

$$
\prod_p\left(1-\frac1{p^{f_p s}}\right)^{-r_p},
$$

where $f_p$ is the order of $p$ in $(\mathbb Z/m\mathbb Z)^\*$, and $r_p=\varphi(m)/f_p$. For real $s>1$ every factor is $>1$. A finite limit for the product remains after deleting any collection of $>1$ factors. Retaining those with $p\equiv1\pmod m$ gives

$$
\prod_{p\equiv1\pmod m}
\left(1-\frac1{p^s}\right)^{-\varphi(m)}
$$

a finite limit at $s=1$. This excludes positive polar density for $p\equiv1\pmod m$, but these are exactly the primes splitting completely in $\mathbb Q(\zeta_m)$, with positive density $1/\varphi(m)$ by Theorem 43. Contradiction.

Theorem 48 therefore gives, for each $a\in(\mathbb Z/m\mathbb Z)^\*$,

$$
\sum_{p\equiv a\pmod m}\frac1{p^s}
-
\frac1{\varphi(m)}
\sum_p\frac1{p^s}
$$

as $s\downarrow1$ has a finite limit. 

## Ideal class group case: why Hilbert class field enters

Let $G$ be the ideal class group of $K$, with $\phi(P)=[P]$. Then

$$
L(s,1)=\zeta_K(s),
$$

Theorem 42 determines the trivial-character pole.

For $\chi\ne1$, use Theorem 39's classwise ideal counts. Equal leading terms cancel after nontrivial character weighting:

$$
\sum_{g\in G}\chi(g)=0.
$$

The coefficient partial sums are therefore of error-term size. Lemma 1 for Theorem 42 makes $L(s,\chi)$ analytic in a half-plane extending to the left of $1$.

The remaining issue is nonvanishing:

$$
L(1,\chi)\ne0.
$$

If some $L(1,\chi)=0$, the character-product Euler factors would make the principal-prime Euler product have a finite limit at $s=1$, excluding positive polar density.

If there is an extension $H/K$ with

$$
P\text{ splits completely in }H
\quad\Longleftrightarrow\quad
P\text{ is principal in }K,
$$

Theorem 43 instead gives principal primes positive density. The Hilbert class field supplies exactly such an extension.

## Fact 1: Hilbert class field

Marcus marks the required class-field-theory input with a dagger:

For each number field $K$, there is an unramified abelian extension $H/K$ whose Artin kernel consists of the nonzero principal ideals of $K$.

Unramifiedness of $H/K$ defines Artin on all nonzero ideals:

$$
\phi:\Gamma\to\operatorname{Gal}(H/K).
$$

Its principal kernel makes the induced ideal-class map

$$
\operatorname{Cl}(K)
$$

into $\operatorname{Gal}(H/K)$ well-defined and injective. Corollary 4 to Theorem 43 gives surjectivity. Thus

$$
\operatorname{Cl}(K)\simeq\operatorname{Gal}(H/K).
$$

Uniformity in ideal classes is therefore equivalent to uniformity in the Frobenius group of the Hilbert class field.

This is the first class-field dictionary:

$$
\text{ideal class}
\quad\leftrightarrow\quad
\text{Frobenius element in } \operatorname{Gal}(H/K).
$$

## Examples and the Hilbert $+$ class field

If $\mathcal O_K$ is a PID, then $H=K$; imaginary quadratic fields of class number $1$ illustrate this.

Marcus gives

$$
K=\mathbb Q(\sqrt{-5}).
$$

Its known class number $2$ predicts degree $2$ for the Hilbert class field over $K$. The candidate is

$$
\mathbb Q(\sqrt{-5},i).
$$

It is unramified over $K$. Only potential ramification from $2,5$ needs attention, and the ramification in $\mathbb Q(i)$ and $\mathbb Q(\sqrt5)$ excludes new ramification over $K$. Imaginary quadratic fields have no real embeddings, so total positivity is vacuous and this Hilbert class field is the largest unramified abelian extension.

For real fields, total positivity matters. Fact 2 says that a closed semigroup $S$ is an unramified abelian Artin kernel exactly when it contains every principal ideal generated by a totally positive element.

Write

$$
P^+=\{(\alpha):\alpha\text{ totally positive}\}.
$$

The corresponding maximal unramified abelian extension is the Hilbert $+$ class field $H^+$, with narrow class group as Galois group:

$$
G^+.
$$

This connects with Chapter 6's narrow class group.

## Ray class fields

Finally, fix a finite prime set $T$ and consider abelian extensions unramified outside $T$. For a modulus ideal $M$, define

$$
P_M^+
=
\{(\alpha):\alpha\equiv1\pmod M,\ \alpha\text{ totally positive}\}.
$$

Fact 3 characterizes an Artin kernel of a $T$-ramified abelian extension: the closed semigroup $S\subset\Gamma_T$ must contain some $P_M^+$, where the prime divisors of $M$ are exactly $T$.

The associated extension $H_M^+$ is a ray class field, with

$$
G_M^+\simeq\operatorname{Gal}(H_M^+/K).
$$

This generalizes:

- Hilbert $+$ class fields when $M=R$.
- Cyclotomic fields when $K=\mathbb Q$.

Every abelian extension of $K$ thus embeds in a ray class field. Theorem 48 gives uniform distribution; the class field's completely split primes supply nonvanishing.

## Cautions

First, the limit point in Theorem 49 is read as $s\downarrow1$. The local PDF shows $0$, while the source note identifies $1$ as required by context. This records its diagnosis without a new source audit.

Second, nonvanishing for class-group characters is not obtained without further input: Marcus uses Hilbert-class-field existence to identify principal primes with completely split primes and invoke Theorem 43.

Third, inclusion of Artin kernels reverses inclusion of extensions: larger kernel means a larger fixed subgroup and a smaller field.

## Relation to the learning goals

This is Marcus's first explicit statement of the central class-field dictionary:

$$
\text{abelian extensions}
\quad\leftrightarrow\quad
\text{ideal-theoretic congruence data / Artin kernels}.
$$

Neukirch develops it systematically through ideles, conductors, ray classes, and Artin reciprocity. Marcus supplies the facts needed for distribution theorems while already displaying the structure.

## Recorded continuation

The introductory reading reaches book p. 170 / PDF p. 185, where the exercises begin. Its next unit is Exercises 1–3: determination of normal extensions by split-prime sets up to density $0$, Artin surjectivity outside a density-zero set, and the closed-semigroup/subgroup correspondence.
