# Three Mechanisms Behind Hilbert 90

## Public reader preface

**Learning question and purpose.** Present multiplicative weighted sums, additive trace-one integration, and Witt filtered lifting with failure boundaries. This case belongs to Neukirch IV §3. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Finite Galois groups, right actions and cocycles, automorphism independence, a normal basis, cyclic norm/difference operators, and the additive Witt filtration.

**Argument route.** Construct a nonzero multiplicative weighted sum; integrate an additive cocycle with trace one; lift norm-kernel elements through a nonsplit Witt filtration; compare the failure tests.

**Historical scope and qualification.** The historical project records closed-reviewed/source-checked/reader-proof-expanded for this focused synthesis; the linked component arguments retain their original provenance. Queue totals near the end are a dated snapshot. The source records closed-reviewed/source-checked/reader-proof-expanded. This is historical provenance, not a new audit; omit or explicitly date obsolete queue totals.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0559`, originally recorded on 2026-08-30, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch IV §3; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `6a6a3bd3e42a13d439dff1bf684ab129afe017acb7ee3dba1c54179a3bccfc10`. English source-article SHA256: `7fac5288065a30d51d6ccaaffa710f9f5417900cbe07127c05e6638feaa468df`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

Status: **closed-reviewed / source-checked / reader-proof-expanded**. This page is a focused review of Proposition 3.8 and Exercises 1–2; the three existing pass-1 artifacts retain first-closure provenance and are not individually relabeled reviewed. Source verification is limited to Neukirch PDF p. 297 / printed p. 283, p. 292 / printed p. 278, and p. 149 / printed p. 134, all checked with `source_window.py` text and original-detail page images, fingerprint `149c6dc1146884357366`. Exercise 3 is same-page boundary exposure only.

## Intuition: Three Ways to Eliminate the Same Obstruction

All three proofs answer the same question: given a Galois difference that appears locally solvable, how can a global witness be constructed? The multiplicative layer has no linear averaging, so cocycle values become automorphism coefficients, and Artin independence selects a nonzero twisted sum. The additive layer has a trace-one element, allowing simultaneous integration of all cocycle components. Witt addition has carries and cannot be copied coordinatewise; the first coordinate and Verschiebung nevertheless supply a filtration, so the obstruction is first eliminated at length one and then lifted, subtracted, and descended layer by layer.

When a cyclic group $C=\langle\sigma\rangle$ acts on an additive group $M$, write $d=\sigma-1$ and $N=1+\sigma+\cdots+\sigma^{m-1}$. One always has $Nd=dN=0$; the substantive assertion is the reverse inclusion

$$
\ker N\subseteq dM.
$$

Proposition 3.8 first eliminates multiplicative $H^1$ for any finite Galois group; Exercise 1 handles additive $H^1$; Exercise 2 lifts its cyclic $H^{-1}$ form through the Witt filtration. This uses the special field-module and Witt-filtration structures, rather than automatic vanishing of finite-group cohomology.

The cyclic bridge is directly visible from cocycles. If a multiplicative cocycle has generator value $a=f(\sigma)$, then

$$
f(\sigma^j)=\prod_{i=0}^{j-1}a^{\sigma^i}.
$$

The relation $\sigma^m=1$ requires precisely $Na=1$; the generator value comes from a coboundary precisely when $a=b^{\sigma-1}$. Replacing products by sums gives $Na=0$ and $a=(\sigma-1)b$ in exactly the same way. Thus identification of cyclic $H^1$ with $H^{-1}$ is evaluation at $\sigma$, rather than an additional black box; Exercise 2 performs filtered lifting precisely at this generator-value level.

## First Layer: Noether's Multiplicative Weighted Sum

Let $L/K$ be finite Galois, $G=\operatorname{Gal}(L/K)$, and use the right action. A multiplicative $1$-cocycle satisfies

$$
f(\sigma\tau)=f(\sigma)^\tau f(\tau).
$$

The closed-book reconstruction first follows the book's direction. For $c\in L^*$ define

$$
T(c)=\sum_{\sigma\in G}f(\sigma)c^\sigma.
$$

Distinct automorphisms are linearly independent as $L$-valued functions, and every coefficient $f(\sigma)$ is nonzero, so $T$ is not the zero function. Thus there exists $c$ with $\alpha=T(c)\ne0$. This guarantees a good choice exists, without saying that every $c$ works.

This independence was also checked closed-book during review. Suppose $\sum_{i=1}^r a_i\sigma_i=0$ is a nonzero relation with the fewest terms. Choose $u$ such that $\sigma_1(u)\ne\sigma_r(u)$. Apply the relation to $ux$ and subtract $\sigma_r(u)$ times the original relation applied to $x$. This eliminates term $r$ while retaining at least one nonzero coefficient, producing a shorter relation, a contradiction. Thus the weighted operator is indeed nonzero as a function, although it can vanish at a fixed $c$.

The cocycle identity gives $f(\sigma)^\tau=f(\sigma\tau)f(\tau)^{-1}$. Right multiplication by $\tau$ permutes the indices, hence

$$
\alpha^\tau=f(\tau)^{-1}\alpha.
$$

Thus $\alpha$ gives the inverse cocycle. Only after setting $\beta=\alpha^{-1}$ does one obtain

$$
f(\tau)=\beta^{\tau-1}.
$$

This is the step most liable to reversal in the whole proof. In noncommutative $G$, reindexing must use $\sigma\mapsto\sigma\tau$; it cannot silently be replaced by left multiplication.

An equivalent direct-witness version inverts the coefficients from the outset:

$$
S(c)=\sum_{\sigma\in G}f(\sigma)^{-1}c^\sigma.
$$

Choose $c$ such that $b=S(c)\ne0$. Then $b^\tau=f(\tau)b$, hence $f(\tau)=b^{\tau-1}$. This can also be read as one-dimensional semilinear descent: twisting the action to $x*\tau=f(\tau)^{-1}x^\tau$ makes $S(c)$ a fixed vector that can be chosen nonzero. The ratio of two witnesses lies in $K^*$, so the ambiguity of solutions is exactly a base-field scalar.

## Second Layer: Additive Trace-One Integration

Now let $f:G\to L^+$ satisfy

$$
f(\sigma\tau)=f(\sigma)^\tau+f(\tau).
$$

By the normal basis theorem choose $\theta$ such that $\{\theta^\sigma\}_{\sigma\in G}$ is a basis over $K$. Its trace cannot vanish, since that would give a linear relation among these basis vectors with all coefficients $1$. Scaling produces $c$ satisfying $\operatorname{Tr}_{L/K}(c)=1$.

Define

$$
\alpha=\sum_{\sigma\in G}f(\sigma)c^\sigma.
$$

Since $f(\sigma)^\tau=f(\sigma\tau)-f(\tau)$, right-multiplication reindexing gives

$$
\alpha^\tau=\alpha-f(\tau)\operatorname{Tr}(c)=\alpha-f(\tau).
$$

Taking $b=-\alpha$ yields $f(\tau)=b^\tau-b$. The proof never divides by $|G|$, so it retains the branch $\operatorname{char}K\mid |G|$. If $G=C$ is cyclic, evaluation at $\sigma$ expresses this as the familiar exactness:

$$
\ker\operatorname{Tr}_{L/K}=(\sigma-1)L.
$$

Normal-basis coefficients give a second closed-book route: trace zero means that the coefficients sum to zero, and cyclic adjacent differences span precisely this hyperplane. This shows that the decisive input is the permutation-module structure, rather than formal averaging.

## Third Layer: Witt Filtered Lifting

Let $k$ be a field of characteristic $p$ and $k_s$ a separable closure. The Galois group acts coordinatewise on $W_n(k_s)$; every finite tuple of coordinates lies in a finite separable extension, so this is a discrete continuous module, with

$$
W_n(k_s)^{G_L}=W_n(L).
$$

Fix a finite cyclic $L/K\subseteq k_s$ and $C=\langle\sigma\rangle$. For $r\ge2$, the first coordinate and Verschiebung give an equivariant additive short exact sequence for $C$:

$$
0\longrightarrow W_{r-1}(L)\xrightarrow{V}W_r(L)\xrightarrow{\pi_0}L\longrightarrow0.
$$

Suppose $x\in W_r(L)$ and $Nx=0$. First project to the first coordinate: $\operatorname{Tr}(\pi_0x)=0$. Length-one additive Hilbert 90 gives $a\in L$ with $\pi_0x=(\sigma-1)a$. Choose any $y\in W_r(L)$ satisfying $\pi_0y=a$; no additive Teichmüller section is needed or may be assumed for this lift. Then

$$
x-(\sigma-1)y=Vz
$$

holds for a unique $z\in W_{r-1}(L)$. From $N(\sigma-1)=0$, $NV=VN$, and injectivity of $V$, obtain $Nz=0$. Induction gives $z=(\sigma-1)w$, hence

$$
x=(\sigma-1)(y+Vw).
$$

The reverse inclusion follows by telescoping, so $\ker N=(\sigma-1)W_r(L)$. Taking $r=n$ gives exactly the requirement of Axiom (3.1) at every finite cyclic layer.

The extracted filtered lifting lemma is independently reusable: if $0\to M'\to M\to M''\to0$ is a short exact sequence of cyclic modules and both $M'$ and $M''$ satisfy $\ker N=\operatorname{im}(\sigma-1)$, then $M$ does too. The proof solves the obstruction in the quotient, lifts, subtracts, and solves again in the submodule; it needs neither a split filtration nor surjectivity of the norm onto the fixed part.

An independent consistency route for any finite Galois $G$ proves $H^1(G,W_n(L))=0$ along the same filtration. Project a Witt-valued cocycle to the first coordinate, use Exercise 1 to solve it as an additive coboundary, then lift its witness and subtract. The remaining cocycle lies uniquely in $V W_{n-1}(L)$, and induction applies. In the cyclic case, evaluation at a generator converts this $H^1$ vanishing into the required $H^{-1}$ exactness. This strengthening is only a proof check and does not inflate Exercise 2 into vanishing of all Tate degrees.

Nonuniqueness of witnesses is parallel in all three layers. Multiplicative witnesses form an $K^*$-torsor; additive witnesses differ by an element of $K$; two solutions of a Witt difference equation differ by a fixed vector in $W_n(K)$. Hilbert 90 eliminates the existence obstruction, without producing or needing a canonical witness.

## Decisive Guards

**The same $\mathbb Q(i)$ model checks both signs.** Let $s$ be conjugation. Take multiplicative cocycle $f(s)=-1$: the book's weighted sum vanishes for $c=1$, whereas for $c=i$ it gives $\alpha=2i$; the actual witness is $\alpha^{-1}$, satisfying $\beta^s/\beta=-1$. Take additive cocycle $f(s)=i$ and trace-one element $c=(1+i)/2$; then $\alpha=i c^s=(1+i)/2$, while $b=-\alpha$ satisfies $b^s-b=i$. This fixes both the multiplicative inverse and the additive minus sign.

**Characteristic dividing the group order does not invalidate the additive proof.** For $\mathbb F_4/\mathbb F_2$, one can take normal-basis element $\omega$ of trace $1$. Although $|G|=\operatorname{char}K=2$, a trace-one witness still exists; division by the group order is therefore not a valid alternative route.

A fresh enumeration over the same field also covered all three norm-one multiplicative cocycles of $\mathbb F_4^*$. Each cocycle admits a nonzero source weighted sum, and termwise checking shows that its inverse gives precisely the original cocycle. This also extends the wild-characteristic guard to Proposition 3.8.

**The Witt norm is not coordinatewise trace.** In $W_2(\mathbb F_4)$, write $\omega^2+\omega+1=0$. Then

$$
(a,b)+(c,d)=(a+c,b+d+ac).
$$

The norm given by squaring Frobenius is

$$
N(a,b)=(a+a^2,b+b^2+a^3).
$$

Therefore

$$
\ker N=\{(0,0),(0,1),(1,\omega),(1,\omega^2)\}=\operatorname{im}(\sigma-1).
$$

Using coordinatewise trace would incorrectly give $(1,0),(1,1)$ for the last two terms. This smallest carry guard shows that the filtration proof really uses Witt addition, rather than silently replacing $W_2(L)$ by $L^2$.

The same example directly rules out additive splitting. The Teichmüller-shaped lift satisfies $(1,0)+(1,0)=(0,1)=V(1)\ne0$; indeed $W_2(\mathbb F_4)^+$ has an element of order $4$, whereas the submodule and quotient are both exponent-$2$ groups, so this short exact sequence cannot split as additive groups. The lift–subtract argument in this round is therefore strictly stronger than choosing a section.

**The assertion fails for arbitrary modules.** If $C_p$ acts trivially on $\mathbb F_p^+$, a nonzero homomorphism $C_p\to\mathbb F_p^+$ is a cocycle, while all coboundaries vanish. Vanishing in all three layers depends on the respective field-theoretic inputs.

Three common failed routes can therefore be remembered together. In the multiplicative layer one cannot fix $c=1$, since the weighted sum may vanish. In the additive layer one cannot replace a trace-one element by $1/|G|$, since wild characteristic makes the group order vanish. In the Witt layer one cannot choose an imaginary additive Teichmüller splitting, since that erases precisely the carry structure. The correct replacements are automorphism independence, a normal basis, and nonsplit filtered lifting, respectively.

## Review Conclusion, Boundaries, and Next Goal

The closed-book proofs agree point by point with the source and existing pass-1 artifacts. This round confirms the sum, right-action reindexing, inverse witness, and exercise boundaries of Proposition 3.8. Axiom (3.1) on p. 292 indeed quantifies over all finite cyclic extensions; p. 149 supplies only the additive $V$ input needed here. The existing Frobenius ghost-index source warning for Exercise 4 remains isolated and does not affect the $V$-filtration.

The three-layer package is therefore promoted to **closed-reviewed/source-checked/reader-proof-expanded**; component artifacts retain current-line pass-1 provenance. The historical review recorded no new book error, proof gap, or hard-review packet. Its former queue totals are omitted because they do not describe the 20 October snapshot.

There are two interfaces with the main line of the book. Proposition 3.8 is later used only in VI §2.5 to eliminate the scalar cocycle of a fixed idele class and obtain an actual fixed representative. Witt filtered lifting supplies only Axiom (3.1) for the §3 Kummer formalism, preparing the cohomological input for the immediately following Artin–Schreier–Witt operator. Neither can replace the other.

Historical continuation recorded on 30 August 2026: Exercise 3 / PDF p. 297, first prove that $F-1$ is an additive homomorphism on $W_n(k_s)$, then prove surjectivity by triangular coordinate lifting and identify its kernel as a cyclic group of order $p^n$. These operator/kernel conclusions cannot be inferred automatically from Axiom (3.1) in this round. Marcus remains support/example/pass-2 only, with no Chapter 9; the whole-book inventory and terminal hard-review reconciliation remain unfinished.

Self-test: why does automorphism independence guarantee only that some weighted sum is nonzero? Why must the book's witness be inverted for the right action? Why can a normal-basis element not have trace zero? Why does a Witt lift need no additive section? Where does the filtered lifting lemma use injection of the submodule? Which three separate gates—operator, surjectivity, and kernel—remain for Exercise 3 beyond this round?
