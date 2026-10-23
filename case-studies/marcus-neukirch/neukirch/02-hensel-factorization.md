# Hensel Lifting as Iterative Factor Correction

## Public reader preface

**Learning question and purpose.** Make the linearized correction, shrinking error, degree control, and completeness step visible. This case belongs to Neukirch II §4. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** A complete nonarchimedean valued field, its valuation ring and residue field, polynomial coprimality, Bézout identities, and coefficientwise convergence.

**Argument route.** State the factorization problem with its hypotheses; choose initial lifts; solve the correction equation with degree bounds; take the complete-ring limit; inspect the roots-of-unity example.

**Historical scope and qualification.** The source preserves a factorization-form proof with explicit hidden checks. No new proof-status label is assigned here. Retain primitive-polynomial, coprimality, completeness, and error-parameter qualifications.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0087`, originally recorded on 2026-07-02, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch II §4; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `2404c0b8b13dd85bf43eb8baa42315cb8eff2bc1669ec4c966486f22f7c7fc76`. English source-article SHA256: `54c464c3a0867eca4692f17ef91950a46e45b1befe143bc000ece704521821a4`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

## Reader preface

This article presents Hensel lifting for a coprime factorization of a primitive polynomial. The reader should track the linear correction equation and the shrinking error before passing to the complete-ring limit.

**Textbook placement.** Neukirch, Chapter II §4, Hensel's Lemma 4.6, as identified by the source title. The article supplies no further page window.

**Prerequisites actually used.** A complete nonarchimedean valued field; its valuation ring, maximal ideal, and residue field; primitive polynomials; coprimality and Bezout identities for residue polynomials; coefficientwise convergence.

**Argument route and dependencies.** After defining primitive polynomials and stating the lemma, choose initial lifts, normalize the error, solve the inductive correction equation, and take limits of the two factor sequences. The roots-of-unity example illustrates the lifting procedure, and the final checks preserve its hypotheses.

**Scope and status.** The existing factorization proof, example, and hidden checks are preserved without substituting a derivative-only version of Hensel's lemma. This edition translates and organizes the existing record. It does not independently verify proofs, repair mathematical arguments, or upgrade any recorded proof status. Historical next-step instructions and limitations remain part of the article.

## Intuition

Hensel's lemma is the factorization form of "Newton lifting" in a complete nonarchimedean ring. If a primitive polynomial factors modulo the maximal ideal into two coprime pieces, then the factorization is not an accident of the residue field: completeness lets us correct the two lifted factors by smaller and smaller error terms until their product is exactly the original polynomial.

The coprimality condition is the algebraic substitute for an invertible derivative. It lets one solve the linearized correction equation at each stage.

## Primitive polynomials

Let $K$ be complete for a nonarchimedean valuation, with valuation ring $\mathfrak o$, maximal ideal $\mathfrak p$, and residue field $\kappa=\mathfrak o/\mathfrak p$. For $f(x)=a_0+\cdots+a_nx^n\in\mathfrak o[x]$, Neukirch calls $f$ primitive if its reduction is not zero:

$$
f\not\equiv0\pmod{\mathfrak p}.
$$

Equivalently,

$$
|f|=\max\{|a_0|,\dots,|a_n|\}=1.
$$

This is the polynomial analogue of having at least one unit coefficient.

## Statement

Suppose $f\in\mathfrak o[x]$ is primitive and admits a residue factorization

$$
\bar f=\bar g\,\bar h
$$

in $\kappa[x]$, where $\bar g$ and $\bar h$ are relatively prime. Then there are $g,h\in\mathfrak o[x]$ such that

$$
f=gh,
$$

with

$$
g\equiv\bar g\pmod{\mathfrak p},
\qquad
h\equiv\bar h\pmod{\mathfrak p},
$$

and $\deg g=\deg\bar g$. 

## Initial lifts and the error parameter

Let $d=\deg f$ and $m=\deg\bar g$. Choose lifts $g_0,h_0\in\mathfrak o[x]$ such that

$$
g_0\equiv\bar g\pmod{\mathfrak p},
\qquad
h_0\equiv\bar h\pmod{\mathfrak p},
$$

with $\deg g_0=m$ and $\deg h_0\le d-m$. Since $\bar g$ and $\bar h$ are coprime, choose $a,b\in\mathfrak o[x]$ with

$$
a g_0+b h_0\equiv1\pmod{\mathfrak p}.
$$

The two initial errors are

$$
f-g_0h_0,
\qquad
a g_0+b h_0-1,
$$

both in $\mathfrak p[x]$. Neukirch chooses an element $\pi\in\mathfrak p$ from the error coefficients so that all these error coefficients lie in $\pi\mathfrak o$. This $\pi$ is an error-size parameter, not necessarily a uniformizer and not a generator of $\mathfrak p$. 

Thus the initial congruence is

$$
f\equiv g_0h_0\pmod{\pi}.
$$

## Inductive correction

Seek

$$
g=g_0+p_1\pi+p_2\pi^2+\cdots,
$$

$$
h=h_0+q_1\pi+q_2\pi^2+\cdots,
$$

where $\deg p_i<m$ and $\deg q_i\le d-m$. Assume $g_{n-1}$ and $h_{n-1}$ have been constructed so that

$$
f\equiv g_{n-1}h_{n-1}\pmod{\pi^n}.
$$

Write

$$
I_n=\pi^{-n}(f-g_{n-1}h_{n-1})\in\mathfrak o[x].
$$

We want to choose $p_n,q_n$ so that

$$
g_n=g_{n-1}+p_n\pi^n,
\qquad
h_n=h_{n-1}+q_n\pi^n
$$

satisfy the congruence modulo $\pi^{n+1}$. Ignoring the higher product term $p_nq_n\pi^{2n}$ modulo $\pi^{n+1}$, the required condition becomes

$$
g_0q_n+h_0p_n\equiv I_n\pmod{\pi}.
$$

The Bezout congruence gives a formal solution $q_n=aI_n$, $p_n=bI_n$ modulo $\pi$, but degrees may be too large. To fix this, divide

$$
bI_n=qg_0+p_n
$$

with $\deg p_n<m$. This division is valid in $\mathfrak o[x]$ because the leading coefficient of $g_0$ is a unit. Then

$$
g_0(aI_n+h_0q)+h_0p_n\equiv I_n\pmod{\pi}.
$$

Reduce $aI_n+h_0q$ modulo $\pi$ coefficientwise and discard coefficients divisible by $\pi$ to get a representative $q_n$ of degree $\le d-m$. This gives the desired congruence and preserves the degree bounds.

## Passing to the limit

Because $\pi^n\to0$ in the nonarchimedean topology, the coefficientwise series defining $g$ and $h$ converge in $\mathfrak o[x]$ with the stated degree bounds. The congruences

$$
f\equiv g_nh_n\pmod{\pi^{n+1}}
$$

force $f=gh$ in the limit by completeness. The reductions of $g,h$ are the original $\bar g,\bar h$ because all correction terms are divisible by $\pi\in\mathfrak p$. 

## Example: Teichmuller roots of unity

For odd $p$, the polynomial $x^{p-1}-1\in\mathbb Z_p[x]$ splits over $\mathbb F_p$ into distinct linear factors. Repeated Hensel lifting gives all $(p-1)$-st roots of unity in $\mathbb Z_p$. Together with $0$, these roots form a multiplicatively closed system of representatives for the residue field.

This is the structural version of the Teichmuller representatives already seen in Chapter II §2.

## Boundaries and hidden checks

- The lemma needs completeness; the iterative corrections only become an exact factorization after taking limits.
- The residual factors must be relatively prime. Without coprimality, the linearized correction equation need not be solvable.
- The $\pi$ used in the proof is an error parameter, not necessarily a prime element of a discrete valuation ring.
- This note stops before Corollary 4.7 on irreducible polynomials over complete nonarchimedean fields.
