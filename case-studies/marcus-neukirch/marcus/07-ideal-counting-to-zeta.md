# From Ideal Counting to Dedekind Zeta

## Public reader preface

**Learning question and purpose.** Explain Abel summation, convergence, continuation, the Euler product, and the role of the counting error. This case belongs to Marcus Chapter 7. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Ideal norms and unique ideal factorization, asymptotic ideal counting, Abel summation, and locally uniform convergence of holomorphic series.

**Argument route.** Control partial sums; apply Abel summation; isolate the ideal-counting main term; continue the remaining Dirichlet series; justify the Euler product.

**Historical scope and qualification.** The source is a dated first-reading exposition of the Chapter 7 opening. Its source-specific continuation half-plane and analytic prerequisites are retained without a new audit. Keep the continuation half-plane and the distinction between formal and absolutely convergent rearrangement.

**Source and provenance.** The mathematical body is adapted from English study-edition article `MA0140`, originally recorded on 2026-06-30, in the preserved 20 October 2026 snapshot. The textbook reference is Marcus Chapter 7; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `f890cb614a92e8f51b9c50d7cc2ecdcf4ec1d95a3d75af462911769b2d236a6b`. English source-article SHA256: `6b91bf61459d674d9ea71654e268d26857ffb9522934a74e336a166954f50af9`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

Scope: Chapter 7 opening through Theorem 42, book pp. 129–133 / PDF pp. 144–148.

## Intuitive picture

Chapter 6 established the ideal count:

$$
i(t)=h\kappa t+O(t^{1-1/d}),
\qquad d=[K:\mathbb Q].
$$

Chapter 7 places it in a Dirichlet series:

$$
\zeta_K(s)=\sum_I\frac1{\|I\|^s}
=\sum_{n\ge1}\frac{j_n}{n^s},
$$

Here $j_n$ counts ideals of norm $n$. Controlled partial sums give convergence in a half-plane. Subtracting the main term $h\kappa$ from $j_n$ leaves a smaller error, extending $\zeta_K$ farther and revealing a simple pole at $s=1$.

## Lemma 1: Dirichlet series convergence from partial sums

Consider

$$
\sum_{n=1}^{\infty}\frac{a_n}{n^s},
\qquad s=x+iy.
$$

If the partial sums satisfy

$$
A(t)=\sum_{n\le t}a_n=O(t^\rho),
\qquad \rho\ge0,
$$

the Dirichlet series converges on

$$
x>\rho
$$

and is holomorphic there.

Use discrete Abel summation. Put

$$
A_k=\sum_{n=1}^k a_n.
$$

For a partial tail,

$$
\sum_{n=m}^{M}\frac{a_n}{n^s}
=
\frac{A_M}{M^s}
-\frac{A_{m-1}}{m^s}
+
\sum_{n=m}^{M-1}
A_n\left(\frac1{n^s}-\frac1{(n+1)^s}\right).
$$

If $|A_n|\le Bn^\rho$, use

$$
\frac1{n^s}-\frac1{(n+1)^s}
=
s\int_n^{n+1}\frac{dt}{t^{s+1}},
$$

to obtain

$$
\left|
\sum_{n=m}^{M}\frac{a_n}{n^s}
\right|
\le
B\left(
M^{\rho-x}+m^{\rho-x}
 + |s|\sum_{n=m}^{M-1}n^{\rho-x-1}
\right).
$$

When $x>\rho$, the tail tends to zero with $m,M\to\infty$. On compact subsets of $x>\rho$, the quantity $|s|$ is uniformly bounded and $x-\rho$ stays uniformly away from $0$. Convergence is locally uniform, hence the sum is holomorphic.

## Dedekind zeta convergence

Put

$$
j_n=\#\{I\subset R:\ \|I\|=n\}.
$$

Then

$$
\zeta_K(s)=\sum_{n=1}^{\infty}\frac{j_n}{n^s}
$$

for $x>1$, because

$$
\sum_{n\le t}j_n=i(t)=O(t)
$$

by Chapter 6, Lemma 1 gives convergence and analyticity for $x>1$. 

More strongly, Chapter 6 gives

$$
i(t)=h\kappa t+O(t^{1-1/d}).
$$

Hence

$$
\sum_{n\le t}(j_n-h\kappa)
=
i(t)-h\kappa\lfloor t\rfloor
=O(t^{1-1/d}).
$$

By Lemma 1,

$$
\sum_{n=1}^{\infty}\frac{j_n-h\kappa}{n^s}
$$

In

$$
x>1-\frac1d
$$

is holomorphic on this domain.

## Riemann zeta extension used by Marcus

Marcus first uses the alternating series

$$
f(s)=1-\frac1{2^s}+\frac1{3^s}-\frac1{4^s}+\cdots
$$

to extend $\zeta(s)$ to $x>0$. The partial sums of $a_n=(-1)^{n-1}$ are bounded, so Lemma 1 makes $f$ holomorphic on $x>0$. For $x>1$,

$$
f(s)=(1-2^{1-s})\zeta(s).
$$

Therefore

$$
\zeta(s)=\frac{f(s)}{1-2^{1-s}}
$$

gives meromorphic continuation. To remove possible poles at the points of $1-2^{1-s}=0$ other than $s=1$, also use

$$
g(s)=1+\frac1{2^s}-\frac2{3^s}+\frac1{4^s}+\frac1{5^s}-\frac2{6^s}+\cdots
$$

where

$$
g(s)=(1-3^{1-s})\zeta(s)
$$

for $x>1$. The two denominators have no common zero away from $1$, excluding genuine poles of $f(s)/(1-2^{1-s})$ there. Thus $\zeta$ is meromorphic on $x>0$ with a unique simple pole at $s=1$.

PDF extraction may flatten the $\ne0$ signs. The expression needed is

$$
f(1)\ne0
$$

because $f(1)=1-\frac12+\frac13-\frac14+\cdots=\log2$. This makes $s=1$ a genuine pole of $\zeta$.

## Extending $\zeta_K$

For $x>1$, write

$$
\zeta_K(s)
=
\sum_{n=1}^{\infty}\frac{j_n-h\kappa}{n^s}
+
h\kappa\,\zeta(s).
$$

The first term is holomorphic on

$$
x>1-\frac1d
$$

The second is meromorphic on $x>0$ with only a simple pole at $s=1$. Thus $\zeta_K$ is meromorphic on

$$
x>1-\frac1d
$$

holomorphic away from $s=1$, with a simple pole at $s=1$.

This is where Chapter 6's counting theorem enters analysis: the error $O(t^{1-1/d})$ determines how far continuation crosses $x=1$.

## Euler product

For $x>1$, absolute convergence gives

$$
\zeta_K(s)=\sum_I\frac1{\|I\|^s},
$$

summed over all nonzero ideals. Unique prime ideal factorization and multiplicative norms formally give

$$
\zeta_K(s)=
\prod_P
\left(1+\frac1{\|P\|^s}+\frac1{\|P\|^{2s}}+\cdots\right)
=
\prod_P
\left(1-\frac1{\|P\|^s}\right)^{-1}.
$$

Infinite-product Lemma 2 justifies the expansion: if $\sum |a_i|<\infty$, then

$$
\prod_i(1-a_i)^{-1}
$$

converges absolutely and has the indicated expansion. Take

$$
a_P=\|P\|^{-s}.
$$

Since

$$
\sum_P\|P\|^{-x}
\le
\sum_I\|I\|^{-x}
=\zeta_K(x)<\infty
$$

for $x>1$ to justify the Euler product.

## Theorem 42

Theorem 42 states:

1. $\zeta_K$ extends meromorphically to
   $$
   x>1-\frac1{[K:\mathbb Q]},
   $$
   with a single simple pole at $s=1$. 
2. For $x>1$,
   $$
   \zeta_K(s)
   =
   \sum_I\frac1{\|I\|^s}
   =
   \prod_P
   \left(1-\frac1{\|P\|^s}\right)^{-1}.
   $$

## Relation to the learning goals

Chapter 7 collects the arithmetic of the first six chapters into an analytic object:

- Ideals and norms give Dirichlet coefficients $j_n$.
- Chapter 6 gives their partial-sum asymptotic.
- Unique ideal factorization gives the Euler product.
- The residue at the pole $s=1$ encodes $h$, $\operatorname{reg}(R)$, $w$, and $\operatorname{disc}(R)$.

The recorded next step is the material after Theorem 42: use $\zeta_K$ to obtain prime densities, then proceed toward the class-number formula.
