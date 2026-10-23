# Embeddings, Trace, and Norm

## Public reader preface

**Learning question and purpose.** Connect conjugates, linear algebra, relative trace/norm, and a higher-degree counterexample. This case belongs to Marcus Chapter 2. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Finite field extensions, minimal polynomials, linear algebra, and the definition of an algebraic integer.

**Argument route.** Distinguish embeddings from automorphisms; derive trace and norm; test the quadratic and higher-degree examples; pass to relative operations and transitivity.

**Historical scope and qualification.** The source is a dated explanatory study note. No independent-proof completion or new review label is assigned by this public edition. A reader exposition of classical theory; do not describe the formulas as new research.

**Source and provenance.** The mathematical body is adapted from English study-edition article `MA0060`, originally recorded on 2026-06-29, in the preserved 20 October 2026 snapshot. The textbook reference is Marcus Chapter 2; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `54ac3b1430ac0ce8cec979f8afd97b17345a7069c6464345745e4c7baa2c7635`. English source-article SHA256: `1791869cd257aabe23cf03c667292a0ea84b58f2205b9fdc25530f6313c225e1`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

Scope:

- Marcus, Chapter 2, book pp. 14–16 / PDF pp. 31–33.
- Compare the linear-algebra definitions of trace and norm in Neukirch I, §2.

## Intuition

An element $\alpha$ of a number field $K$ has more than one numerical image. Every embedding

$$
\sigma:K\hookrightarrow\mathbb{C}
$$

gives an image $\sigma(\alpha)$. The trace adds these images, and the norm multiplies them:

$$
T_K(\alpha)=\sum_\sigma\sigma(\alpha),\qquad
N_K(\alpha)=\prod_\sigma\sigma(\alpha).
$$

These quantities bring problems in $K$ down to $ \mathbb{Q}$, and for algebraic integers further down to $ \mathbb{Z}$. They immediately control units and irreducibility, and later the discriminant.

## Embeddings need not be automorphisms

If $K=\mathbb{Q}(\alpha)$ and $[K:\mathbb{Q}]=n$, the $n$ embeddings of $K$ correspond to the $n$ conjugates of $\alpha$:

$$
\alpha\mapsto\beta.
$$

An embedding need not be an automorphism of $K$. For example,

$$
K=\mathbb{Q}(\sqrt[3]{2})
$$

has three embeddings, corresponding to

$$
\sqrt[3]{2},\quad \omega\sqrt[3]{2},\quad \omega^2\sqrt[3]{2},
$$

where $\omega=e^{2\pi i/3}$. The last two images do not lie in the real field $K$, so these are not automorphisms of $K$.

This differs from a cyclotomic field. If $K=\mathbb{Q}(\omega)$, then $K$ already contains all roots of $x^m-1$, so its embeddings are automorphisms.

## Basic properties of trace and norm

Let $[K:\mathbb{Q}]=n$ have embeddings $\sigma_1,\dots,\sigma_n$. Define

$$
T_K(\alpha)=\sigma_1(\alpha)+\cdots+\sigma_n(\alpha),
$$

$$
N_K(\alpha)=\sigma_1(\alpha)\cdots\sigma_n(\alpha).
$$

Immediately,

$$
T_K(\alpha+\beta)=T_K(\alpha)+T_K(\beta),
$$

$$
N_K(\alpha\beta)=N_K(\alpha)N_K(\beta).
$$

For a rational number $r\in\mathbb{Q}$, every embedding fixes $r$, so

$$
T_K(r)=nr,\qquad N_K(r)=r^n.
$$

This reminds us that trace and norm depend on the ambient field $K$, not only on the element.

## Theorem 4

If $\alpha\in K$ has degree $d$ over $ \mathbb{Q}$, let $t(\alpha)$ be the sum of the $d$ conjugates of $\alpha$ and $n(\alpha)$ their product. Each embedding of $ \mathbb{Q}(\alpha)$ extends to

$$
[K:\mathbb{Q}(\alpha)]=\frac nd
$$

embeddings of $K$. Thus each conjugate appears $n/d$ times in the trace or norm in $K$:

$$
T_K(\alpha)=\frac nd\,t(\alpha),
$$

$$
N_K(\alpha)=n(\alpha)^{n/d}.
$$

Since $t(\alpha)$ and $n(\alpha)$ are coefficients of the minimal polynomial, both lie in $ \mathbb{Q}$. Hence

$$
T_K(\alpha),N_K(\alpha)\in\mathbb{Q}.
$$

If $\alpha$ is an algebraic integer, its minimal polynomial lies in $ \mathbb{Z}[x]$, so

$$
T_K(\alpha),N_K(\alpha)\in\mathbb{Z}.
$$

## Quadratic fields

In

$$
K=\mathbb{Q}(\sqrt m)
$$

the two embeddings are

$$
\sqrt m\mapsto\sqrt m,\qquad \sqrt m\mapsto-\sqrt m.
$$

Therefore

$$
T(a+b\sqrt m)=2a,
$$

$$
N(a+b\sqrt m)=a^2-mb^2.
$$

In a quadratic field, $\alpha$ is an algebraic integer if and only if its trace and norm are integers, because its minimal polynomial is

$$
x^2-T(\alpha)x+N(\alpha).
$$

This criterion applies only in degree two.

## A higher-degree counterexample

Marcus gives the polynomial

$$
x^3+\frac12x+1.
$$

It has no rational root and is therefore irreducible in $ \mathbb{Q}[x]$. If $\alpha$ is one of its roots, this is the minimal polynomial of $\alpha$.

Vieta's formulas give

$$
T_{\mathbb{Q}(\alpha)}(\alpha)=0,
$$

$$
N_{\mathbb{Q}(\alpha)}(\alpha)=-1.
$$

The trace and norm are integers, but $\alpha$ is not an algebraic integer, because its minimal polynomial does not belong to $ \mathbb{Z}[x]$.

In higher degree, trace and norm control only the coefficient immediately below the leading term and the constant coefficient; intermediate coefficients can still have denominators.

## Units and irreducibility

If $\alpha\in\mathcal{O}_K$ is a unit, then

$$
N_K(\alpha)N_K(\alpha^{-1})=1.
$$

Both sides are integers, so

$$
N_K(\alpha)=\pm1.
$$

Conversely, if $N_K(\alpha)=\pm1$, the constant coefficient of the minimal polynomial of $\alpha$ is $\pm1$. Dividing its equation by the appropriate power of $\alpha$ gives a monic integral equation for $\alpha^{-1}$; hence $\alpha^{-1}\in\mathcal{O}_K$. Thus

$$
\mathcal{O}_K^*=\{\alpha\in\mathcal{O}_K:N_K(\alpha)=\pm1\}.
$$

Likewise, if $|N_K(\alpha)|$ is an ordinary prime, every factorization

$$
\alpha=\beta\gamma
$$

gives

$$
N_K(\alpha)=N_K(\beta)N_K(\gamma).
$$

Therefore $N_K(\beta)$ or $N_K(\gamma)$ must equal $\pm1$, and the corresponding factor is a unit. Thus $\alpha$ is irreducible.

This extends the use of the Gaussian or Eisenstein norm to prove irreducibility in Chapter 1.

## Relative trace/norm

Marcus next replaces the ground field $ \mathbb{Q}$ by an arbitrary number field. If

$$
K\subset L,\qquad [L:K]=n,
$$

consider only the embeddings fixing $K$,

$$
\sigma_i:L\hookrightarrow\mathbb{C}.
$$

and define

$$
T_{L/K}(\alpha)=\sum_i\sigma_i(\alpha),\qquad
N_{L/K}(\alpha)=\prod_i\sigma_i(\alpha).
$$

If $\delta\in K$, all these embeddings fix $\delta$, so

$$
T_{L/K}(\delta)=n\delta,\qquad N_{L/K}(\delta)=\delta^n.
$$

As in the absolute case, if $\alpha$ has degree $d$ over $K$ and the sum and product of its conjugates are $t(\alpha)$ and $n(\alpha)$, then

$$
T_{L/K}(\alpha)=\frac nd\,t(\alpha),
\qquad
N_{L/K}(\alpha)=n(\alpha)^{n/d}.
$$

Consequently

$$
T_{L/K}(\alpha),N_{L/K}(\alpha)\in K.
$$

If $\alpha$ is an algebraic integer in $L$, its relative trace and norm are still algebraic integers in $K$.

## Transitivity

For a tower

$$
K\subset L\subset M,
$$

descending in stages equals descending in one step:

$$
T_{L/K}(T_{M/L}(\alpha))=T_{M/K}(\alpha),
$$

$$
N_{L/K}(N_{M/L}(\alpha))=N_{M/K}(\alpha).
$$

The idea of the proof is to take all embeddings of $M/L$ and then all embeddings of $L/K$; their combinations give exactly all embeddings of $M/K$.

A technical point is that the original embeddings map into $ \mathbb{C}$ and cannot be composed directly. Marcus places all number fields inside a normal extension $N/\mathbb{Q}$, extends the embeddings to automorphisms of $N$, and then composes.

It remains to check that these composites

$$
\sigma_i\tau_j
$$

are distinct on restriction to $M$. If two composites agree on $M$, restricting first to $L$ shows that their corresponding $\sigma_i$ agree. Fixing that same $\sigma_i$ and comparing the $M/L$ parts then gives equal $\tau_j$. This is precisely the detail supplied by Marcus Exercise 18.

## Comparison with Neukirch

Marcus defines trace and norm through embeddings. Neukirch I, §2, begins with linear algebra: for a finite extension $L/K$, let $T_x$ be the $K$-linear map on $L$

$$
y\mapsto xy.
$$

Then

$$
\operatorname{Tr}_{L/K}(x)=\operatorname{trace}(T_x),
\qquad
N_{L/K}(x)=\det(T_x).
$$

In the separable case, this agrees with the embedding formulas. Neukirch's definition is better suited to relative extensions, localization, and discriminants; Marcus's definition is convenient for first calculations.
