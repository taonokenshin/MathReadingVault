# Minkowski Space and Two Measure Conventions

## Public reader preface

**Learning question and purpose.** Explain the real-coordinate metric and reconcile the complex-place factor between the two textbooks. This case belongs to Neukirch I §5. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Field embeddings, discriminants, complete lattices, Gram determinants, and the convex-body form of Minkowski’s theorem.

**Argument route.** Build the real form from conjugate embeddings; compute its metric; compare canonical and coordinate measures; derive the ideal-lattice covolume; apply a convex body.

**Historical scope and qualification.** The source treats the opening Minkowski-space propositions and coordinate bound. It historically stops before the later class-group finiteness argument. Preserve both normalization conventions and the limited opening-section scope.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0044`, originally recorded on 2026-07-01, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch I §5; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `a7f6961bb1bb6508d2cc9c95e9e67fa3b81f52b1d67687fe8cb5f908fec455e1`. English source-article SHA256: `136b9d47afa363696aa401b0c0c108cae0514a4f357db7f816af3c11f82cd251`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

## Reader preface

This article constructs Minkowski space, computes ideal-lattice covolumes, and applies the lattice theorem to embedding-coordinate bounds. It retains the real-coordinate and Gram-matrix conventions and the canonical-versus-Lebesgue measure comparison before the later class-group finiteness proof.

This is a full editorial translation of the original article. Its source references, qualifications, historical frontier, and proof-status markers are preserved; no new proof verification is implied.

Source: Neukirch, Chapter I §5, book pp. 28-32 / PDF pp. 44-48. This article treats only the Minkowski-space opening, Propositions 5.1-5.2, and Theorem 5.3. The §6 class-number proof is not opened.

## Intuition

The lattice theorem in §4 is geometric. Section §5 embeds a number field $K$ in a real Euclidean space where algebraic integers and ideals form complete lattices. The space is not an arbitrary $\mathbb R^n$; it comes from all complex embeddings

$$
\tau:K\hookrightarrow\mathbb C.
$$

Each $\alpha\in K$ becomes its tuple of conjugate values $(\tau\alpha)_\tau$. Real embeddings give real coordinates; conjugate pairs of complex embeddings contribute two real coordinates. The discriminant thereby becomes the covolume of an arithmetic lattice, beyond being a trace-matrix determinant.

## $K_{\mathbb C}$ and $K_{\mathbb R}$

Set

$$
K_{\mathbb C}=\prod_{\tau:K\hookrightarrow\mathbb C}\mathbb C.
$$

The canonical embedding is

$$
j:K\longrightarrow K_{\mathbb C},\qquad
\alpha\longmapsto(\tau\alpha)_\tau.
$$

Complex conjugation acts on both coordinate values and embedding indices, giving an involution $F$. Its fixed space

$$
K_{\mathbb R}=K_{\mathbb C}^{F=1}
$$

is a real vector space of dimension $n=[K:\mathbb Q]$, with $j(K)\subset K_{\mathbb R}$.

Restricting the canonical hermitian metric to $K_{\mathbb R}$ gives a Euclidean metric. If $K$ has $r$ real embeddings and $s$ conjugate complex pairs, with $n=r+2s$, choose one $\sigma$ from each pair to obtain the explicit isomorphism

$$
K_{\mathbb R}\cong\mathbb R^{r+2s},
$$

with coordinates

$$
z_\rho=x_\rho\quad(\rho\text{ real}),\qquad
z_\sigma=x_\sigma+i x_{\bar\sigma}\quad(\sigma\text{ complex}).
$$

Here $x_{\bar\sigma}$ denotes the imaginary part with the source's real-coordinate indexing and is real-valued; it is not the complex coordinate $z_{\bar\sigma}$. In these coordinates $x,y$ are real-coordinate vectors, and the canonical metric becomes

$$
(x,y)=
\sum_{\rho\text{ real}}x_\rho y_\rho
+2\sum_{\sigma\text{ complex}}(x_\sigma y_\sigma+x_{\bar\sigma}y_{\bar\sigma}).
$$

Thus canonical measure differs from ordinary Lebesgue measure by a factor $2^s$:

$$
\operatorname{vol}_{\mathrm{can}}(X)
=2^s\operatorname{vol}_{\mathrm{Leb}}(f(X)).
$$

This normalization is an especially easy place to misalign Neukirch and Marcus.

## Proposition 5.1

The proposition gives the explicit coordinates for $K_{\mathbb R}$ and explains that in $\mathbb R^{r+2s}$ the canonical metric weights complex coordinates by $2$.

A conjugate embedding pair $\sigma,\bar\sigma$ starts as two complex coordinates in $K_{\mathbb C}$, but the fixed condition makes the second the conjugate of the first. The real degrees of freedom are therefore $\operatorname{Re}$ and $\operatorname{Im}$. The metric factor $2$ adds the contributions of both conjugate coordinates.

## Proposition 5.2: ideal lattices and covolume

If $\mathfrak a\ne0$ is an integral ideal of $\mathcal O_K$, then

$$
j\mathfrak a\subset K_{\mathbb R}
$$

is a complete lattice, with

$$
\operatorname{vol}(j\mathfrak a)
=\sqrt{|d_K|}\,(\mathcal O_K:\mathfrak a).
$$

The proof combines discriminant scaling in I §2 with the Gram determinant in §4.

For $\mathfrak a$ choose a $\mathbb Z$-basis $\alpha_1,\dots,\alpha_n$ and let $A=(\tau_i\alpha_j)$ be the embedding matrix. Then

$$
d(\alpha_1,\dots,\alpha_n)=(\det A)^2
=(\mathcal O_K:\mathfrak a)^2d_K.
$$

On the other hand, the Gram matrix of $j\alpha_i$ is

$$
\big((j\alpha_i,j\alpha_j)\big)=A^t\overline{A}.
$$

The convention is $A=(\tau_i\alpha_j)$, with embeddings as rows and basis elements as columns, so Gram inner products are taken between columns. The source uses basis elements as rows and $A\overline A^t$ for that other convention. Both determinants are $|\det A|^2$. Hence

$$
\operatorname{vol}(j\mathfrak a)
=|\det A|
=\sqrt{|d_K|}\,(\mathcal O_K:\mathfrak a).
$$

This uses Neukirch's canonical measure. Marcus's real-coordinate Lebesgue covolume is

$$
2^{-s}\sqrt{|d_K|}\,N(\mathfrak a),
$$

The difference is exactly the canonical-measure factor $2^s$.

## Theorem 5.3: coordinate bound from Minkowski

Let $\mathfrak a\ne0$ be an integral ideal. For each embedding $\tau$ choose a positive number $c_\tau>0$ satisfying

$$
c_\tau=c_{\bar\tau}.
$$

If

$$
\prod_\tau c_\tau
>
\left(\frac2\pi\right)^s
\sqrt{|d_K|}\,(\mathcal O_K:\mathfrak a),
$$

there is $0\ne\alpha\in\mathfrak a$ such that for every embedding $\tau$,

$$
|\tau\alpha|<c_\tau.
$$

For the proof take the symmetric convex body

$$
X=\{(z_\tau)\in K_{\mathbb R}: |z_\tau|<c_\tau\}.
$$

Its canonical volume is

$$
\operatorname{vol}(X)
=2^s
\left(\prod_{\rho\text{ real}}2c_\rho\right)
\left(\prod_{\sigma\text{ complex}}\pi c_\sigma^2\right)
=2^{r+s}\pi^s\prod_\tau c_\tau.
$$

The hypothesis and Proposition 5.2 give

$$
\operatorname{vol}(X)>2^{r+2s}\operatorname{vol}(j\mathfrak a)
=2^n\operatorname{vol}(j\mathfrak a).
$$

Theorem 4.4 then supplies a nonzero lattice point $j\alpha\in X$, giving the required $\alpha$.

## Comparison with Marcus

Marcus Chapter 5 Theorem 36 uses real-coordinate Lebesgue measure, so its covolume contains

$$
2^{-s}\sqrt{|\operatorname{disc}(R)|}.
$$

Neukirch uses the canonical metric and measure on $K_{\mathbb R}$, so Proposition 5.2 has no $2^{-s}$. The two expressions agree after accounting for their different normalizations.

Theorem 5.3 is upstream of Marcus Theorem 37: it first bounds the coordinate at each embedding. A convex body adapted to the norm and the arithmetic-geometric mean inequality then yield the usual Minkowski bound

$$
\frac{n!}{n^n}\left(\frac4\pi\right)^s\sqrt{|d_K|}.
$$

## Historical next step

This article stops before §6. The natural continuation has two stages:

1. Complete §5 Exercises 1-3, passing from Theorem 5.3 to the explicit norm/Minkowski bound.
2. Enter §6 and use the bound to prove the class group finite.

Retain the boundary: $\operatorname{Cl}_K$ has been defined, but its finiteness has not yet been formally proved.
