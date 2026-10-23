# Tame Hilbert Symbols: Valuation, Units, and Frobenius

## Public reader preface

**Learning question and purpose.** Track how bilinearity, residue units, roots of unity, and Frobenius normalization determine the formula. This case belongs to Neukirch V §3. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Local reciprocity with the stated Frobenius convention, discrete valuations, residue-field units, Teichmüller lifts, and roots of unity in the local field.

**Argument route.** Define the candidate pairing; reduce comparison by bilinear generation; compute the unramified Frobenius case; use injective root-of-unity reduction; derive the residue-power criterion.

**Historical scope and qualification.** The historical project records closed-reviewed at its D2 level. That is an attributed historical label, not an additional public-review certification. Preserve the tame condition, root-of-unity assumptions, and original closed-reviewed label as dated provenance.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0242`, originally recorded on 2026-07-13, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch V §3; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `fae2b36820e8760386866698ac7d103119939e698a4726c43183d464696830ae`. English source-article SHA256: `53c63f6cccc57ff51eba418c1e84ba3aaf37513d3ddb0ea71ff42d6a030d61f8`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

## Reader preface

This article treats Neukirch Chapter V §3 Propositions 3.4–3.5, book pp. 335–337 / PDF pp. 348–350. It proves the tame Hilbert-symbol formula by bilinear generation, the unramified arithmetic-Frobenius case, and injective reduction on roots of unity, then formulates the power residue symbol criterion. Its original closed-reviewed status, measure of the finite checks, and separation of Marcus examples from reciprocity proof inputs are preserved.

## Preserved reading article

Scope: book pp. 335–337 / PDF pp. 348–350. Status: `closed-reviewed` at D2 proof level. The original visual check of PDF p. 349 confirmed numerator $b^\alpha$, denominator $a^\beta$, and outer exponent $(q-1)/n$. Retain the section's hypotheses: $K$ is a nonarchimedean local field with residue field $k$ of cardinality $q$ and residue characteristic $p$, with $\mu_n\subset K$ and $(n,p)=1$.

## Intuition: the tame pairing sees valuation and residue units

In the tame case the $n$-th power map is an automorphism on principal units, leaving only two coordinates in $K^*/K^{*n}$: a uniformizer valuation class and a residue-field unit class. The explicit Hilbert symbol pairs one variable's valuation with the other's residue unit. The sign $(-1)^{\alpha\beta}$ handles the uniformizer–uniformizer direction and ensures compatibility with $(a,-a)_n=1$.

The conditions $\mu_n\subset K$ and $(n,p)=1$ also imply that reduction is injective on $\mu_n$, hence $n\mid q-1$. Let $\omega:U_K\to\mu_{q-1}$ be the Teichmüller representative map, a multiplicative section of reduction $\mu_{q-1}\simeq k^*$.

## Proposition 3.4: exact formula

For $a,b\in K^*$ write $\alpha=v_K(a)$ and $\beta=v_K(b)$. Then

$$
(a,b)_n=
\omega\left((-1)^{\alpha\beta}\frac{b^\alpha}{a^\beta}\right)^{(q-1)/n}.
$$

The element in parentheses is a unit because its valuation is $\alpha\beta-\beta\alpha=0$. The right side lies in $\mu_n$: put $m=(q-1)/n$; its $n$-th power is a Teichmüller unit's $(q-1)$-st power, equal to $1$.

## Step 1: regard the right side as a second pairing

Define the candidate pairing

$$
\langle a,b\rangle=
\omega\left((-1)^{\alpha\beta}\frac{b^\alpha}{a^\beta}\right)^m.
$$

Additivity of valuation, multiplicativity of the unit expression, and multiplicativity of $\omega$ make it multiplicative in each variable. Replacing $a$ by $aa'$, for example, makes the new unit expression the product of the original two expressions; the second variable is similar.

The book then reduces to $a,b$ being prime elements. The omitted generation argument is that a unit $u$ is a quotient of prime elements, for example $u=(\pi u)/\pi$. Prime elements therefore generate $K^*$ multiplicatively. Both the Hilbert symbol and the candidate are bilinear, so it suffices to compare pairs of prime elements.

Fix the first prime element $\pi$. Every second one is $-\pi u$ with $u\in U_K$. Proposition 3.2 gives $(\pi,-\pi)_n=1$; the candidate's corresponding unit expression is also $1$, so $\langle\pi,-\pi\rangle=1$. Bilinearity therefore reduces comparison to the single core case

$$
(\pi,u)_n\stackrel{?}{=}\omega(u)^m.
$$

This also explains the sign: omitting $(-1)^{\alpha\beta}$ would prevent the uniformizer–uniformizer direction from automatically satisfying $(\pi,-\pi)_n=1$.

## Step 2: unramified Frobenius computation of the core case

Choose $y^n=u$ and put $K'=K(y)$. Lemma 3.3 makes $K'/K$ unramified. Under Neukirch's arithmetic-Frobenius reciprocity convention, Chapter IV Proposition 5.7 gives the norm residue image of a prime element

$$
(\pi,K'/K)=\varphi_{K'/K},
$$

with residue action $\bar z\mapsto\bar z^q$. Proposition 3.1 gives

$$
(\pi,u)_n=\frac{\varphi(y)}{y}.
$$

Reducing modulo $\mathfrak p_{K'}$, arithmetic Frobenius gives

$$
\frac{\varphi(y)}{y}
\equiv y^{q-1}
=u^m
\equiv\omega(u)^m.
$$

Both sides lie in $\mu_n\subset\mu_{q-1}$, and reduction $\mu_{q-1}\to k^*$ is injective, so equality modulo the prime ideal lifts to exact equality in $K$. This proves Proposition 3.4.

Warning layer: geometric Frobenius inverts all of $\varphi(y)/y$; one cannot simply change one exponent in the final formula. This article consistently uses Neukirch's arithmetic-Frobenius convention.

## Proposition 3.5: power residue criterion

Define the $n$-th power residue symbol

$$
\left(\frac{u}{\mathfrak p_K}\right)_n
=(\pi,u)_n
=\omega(u)^m.
$$

It is independent of the prime element $\pi$. To prove the criterion, choose a primitive $(q-1)$-st root $\xi$. Since $m=(q-1)/n$, the map $z\mapsto z^m$ on the cyclic group $\mu_{q-1}$ has kernel the order-$m$ subgroup

$$
\mu_m=\langle\xi^n\rangle.
$$

so

$$
\omega(u)^m=1
\quad\Longleftrightarrow\quad
\omega(u)=(\xi^i)^n
$$

for some $i$. Reduction gives at once that $\bar u$ is, in $k^*$, an $n$-th power. Conversely, if $\bar u=\bar v^n$, take the Teichmüller lift of $\bar v$ to obtain $\omega(u)=\omega(v)^n$, so the symbol is $1$.

Thus the exact conclusion is

$$
\left(\frac{u}{\mathfrak p_K}\right)_n=1
\quad\Longleftrightarrow\quad
\bar u\in k^{*n}.
$$

In the tame case Hensel lifts a residue root to a root in $K$, so for units also $\bar u\in k^{*n}$ if and only if $u\in U_K^n$. Proposition 3.5 itself needs only the residue-field formulation.

## Sanity checks, difficulty, and the relationship between the books

- Take $K=\mathbb Q_5$, $n=2$, $a=5$, and $b=2$. The formula gives $(5,2)_2\equiv2^2\equiv-1\pmod5$, consistent with $2$ not being a square residue.
- If $u\in U_K^{(1)}$, then $\omega(u)=1$, hence $(\pi,u)_n=1$. This agrees with principal units being $n$-th powers in the tame case.
- For $a=b=\pi$ the formula leaves only $\omega(-1)^m$, compatible with $(\pi,-\pi)_n=1$ and skew symmetry. The sign is substantive.
- Finite-residue check: for $(q,n)=(5,2),(7,3),(13,3),(13,4)$, enumeration of valuation classes and nonzero residue units verifies bilinearity, skew symmetry, and $\langle a,-a\rangle=1$ for the candidate. This checks the algebraic signs and does not replace the Frobenius proof.
- Proof layer: Neukirch local reciprocity, Lemma 3.3, arithmetic Frobenius, Teichmüller reduction, and cyclic finite-field units.
- Example layer: Marcus's Legendre symbols, prime splitting, and norm forms check the residue direction of $n=2$ but do not prove reciprocity normalization, uniformizer independence, or the general $n$ pairing.
- Difficulty: D2 conceptual dependency. The delicate points are the bilinear generation reduction, Frobenius convention, injectivity of reduction on roots of unity, and first establishing that the unit expression is a unit. No D3/D4 proof gap is recorded.

Review question: why does checking $(\pi,u)_n$ suffice to compare the pairings? Which prime-element case is repaired by $(-1)^{\alpha\beta}$? Which injectivity lifts the congruence modulo $\mathfrak p$ to an equality of roots of unity?

Exact historical continuation: Propositions 3.4–3.5 are `closed-reviewed`. The historical further-reading plan was Theorem 3.6: the odd-$p$ branch specializes this formula; the $p=2$ branch checks that $\{-1,5\}$ generates $\mathbb Z_2^*/\mathbb Z_2^{*2}$, the four norm-form values, multiplicativity, and the exponential argument for $U^{(3)}\subset U^2$. That historical unit stopped before Theorem 3.7 and Chapter V §4; the later hard-review topics were recorded separately.
