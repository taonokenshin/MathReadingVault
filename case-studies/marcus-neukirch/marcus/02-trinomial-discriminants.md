# Deriving Two Families of Trinomial Discriminants

## Public reader preface

**Learning question and purpose.** Show extended algebraic computation rather than a final discriminant formula alone. This case belongs to Marcus Chapter 2. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Power bases, derivatives, the discriminant-resultant identity, multiplicativity of resultants, and evaluation at polynomial roots.

**Argument route.** Start from the derivative resultant; treat the first trinomial family; track critical-point factors and the sign; repeat for the second family; compare the quintic checks.

**Historical scope and qualification.** The original record reports the Exercise 45 derivation complete within its stated scope. This public selection neither rechecks it nor turns that statement into whole-book completion. Retitle as a standalone derivation; reference the original exercise context without distributing a full printed exercise sheet.

**Source and provenance.** The mathematical body is adapted from English study-edition article `MA0066`, originally recorded on 2026-06-29, in the preserved 20 October 2026 snapshot. The textbook reference is Marcus Chapter 2; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `d075c49f7da6548b4f26e3296889eef83d4a1863e595dd8a1e0ca2b025023621`. English source-article SHA256: `43fd4c14a20222fefd670dd5d4b27e8755ee3b7c627ad54e0c6fa3c18bab6bc2`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

## Reader preface

This article generalizes the Marcus Chapter 2 Exercises 43–44 quintic computations to two families of trinomial power-basis discriminants. It records the Exercise 45 template rather than expanding a new Sylvester determinant for every degree.

Prerequisites actually used: the derivative formula for a power-basis discriminant, resultants, their multiplicativity, and evaluation at derivative roots. The route through the article is the first trinomial family, its critical-point equation and sign computation, then the second family, whose derivative exposes a high-multiplicity zero. Each derivation is checked against the preceding quintic formula.

Scope and status: all degree parameters, signs, and displayed identities are retained. The historical next exercise concerns divisibility and computation using the derivative; it is not folded into this derivation.

## Preserved reading article

Scope: 

- Marcus, Chapter 2 Exercise 45, book p. 38 / PDF p. 55.
- Objective: generalize Exercises 43–44 by computing
  $$
  x^n+ax+b
  $$
  and
  $$
  x^n+ax^{n-1}+b
  $$
  their power-basis discriminants.

## Intuition

The quintic formulas in the preceding two exercises come from the same principle:

$$
\operatorname{disc}(\alpha)
=(-1)^{n(n-1)/2}\operatorname{Res}(f,f').
$$

The derivative of the first family $x^n+ax+b$ gives a single critical-point equation

$$
nx^{n-1}+a=0.
$$

The derivative of the second family $x^n+ax^{n-1}+b$ factors off

$$
x^{n-2}(nx+a(n-1)),
$$

so the high multiplicity of $0$ contributes $b^{n-2}$ directly.

## 1. $f(x)=x^n+ax+b$

Let

$$
f(x)=x^n+ax+b,
$$

and let $\alpha$ be a root. Its derivative is

$$
f'(x)=nx^{n-1}+a.
$$

Let $r_1,\dots,r_{n-1}$ be the roots of $f'$; then

$$
r_i^{n-1}=-\frac an.
$$

At these points,

$$
f(r_i)=r_i^n+ar_i+b
=r_i\left(-\frac an+a\right)+b
=b+\frac{(n-1)a}{n}r_i.
$$

Put

$$
\lambda=\frac{(n-1)a}{n}.
$$

Since $r_i$ is a root of

$$
x^{n-1}+\frac an
$$

, we have

$$
\prod_i(b+\lambda r_i)
=b^{n-1}+(-1)^{n-1}\frac{(n-1)^{n-1}a^n}{n^n}.
$$

Thus

$$
\operatorname{Res}(f,f')
=n^n\prod_i f(r_i)
=n^n b^{n-1}+(-1)^{n-1}(n-1)^{n-1}a^n.
$$

Therefore

$$
\boxed{
\operatorname{disc}(\alpha)
=(-1)^{n(n-1)/2}
\left(n^n b^{n-1}+(-1)^{n-1}(n-1)^{n-1}a^n\right).
}
$$

Checking $n=5$ gives

$$
4^4a^5+5^5b^4,
$$

exactly Exercise 43.

## 2. $f(x)=x^n+ax^{n-1}+b$

Now put

$$
f(x)=x^n+ax^{n-1}+b.
$$

The derivative is

$$
f'(x)=nx^{n-1}+a(n-1)x^{n-2}
=x^{n-2}(nx+a(n-1)).
$$

Multiplicativity of the resultant gives

$$
\operatorname{Res}(f,f')
=\operatorname{Res}(f,x)^{n-2}
\operatorname{Res}(f,nx+a(n-1)).
$$

First,

$$
\operatorname{Res}(f,x)=(-1)^n b.
$$

Next put

$$
c=\frac{a(n-1)}{n}.
$$

then

$$
\operatorname{Res}(f,nx+a(n-1))
=n^n\prod_i(\alpha_i+c)
=(-1)^n n^n f(-c).
$$

Compute

$$
f(-c)=(-c)^n+a(-c)^{n-1}+b
=(-c)^{n-1}\frac an+b
=(-1)^{n-1}\frac{(n-1)^{n-1}a^n}{n^n}+b.
$$

Combining signs gives

$$
\operatorname{Res}(f,f')
=b^{n-2}\left(n^n b+(-1)^{n+1}(n-1)^{n-1}a^n\right).
$$

Therefore

$$
\boxed{
\operatorname{disc}(\alpha)
=(-1)^{n(n-1)/2}
b^{n-2}\left(n^n b+(-1)^{n+1}(n-1)^{n-1}a^n\right).
}
$$

Checking $n=5$ gives

$$
b^3(5^5b+4^4a^5),
$$

exactly Exercise 44(a).

## Current connection

Exercise 45 unifies the computations of Exercises 43–44 into one template. For later trinomial power-basis discriminants, identifying the derivative structure gives the resultant without a fresh Sylvester determinant expansion.

## Historical stopping marker

Exercise 45 is complete in the original record. Continue with Exercise 46: it gives a method using integer or rational roots of $f'$ to test divisibility of $\operatorname{disc}(\alpha)$ quickly, then proposes a discriminant procedure using $g(x)f'(x)\equiv h(x)\pmod{f(x)}$.
