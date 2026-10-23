# From Trace Duality to the Different

## Public reader preface

**Learning question and purpose.** Connect module duality, fractional ideals, localization, completion, and later ramification calculations. This case belongs to Neukirch III §2. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Finite separable extensions, Dedekind domains, fractional ideals, the trace pairing, localization, and completion.

**Argument route.** Define trace duals and the inverse different; follow the local comparisons; keep residue separability visible; connect these objects with later discriminant and ramification arguments.

**Historical scope and qualification.** The source is an opening trace-duality exposition with explicit standing hypotheses. Placement does not certify all subsequent different or discriminant results. Retain separability and residue-separability hypotheses; opening exposition is not a claim to prove all of Chapter III.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0141`, originally recorded on 2026-07-05, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch III §2; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `6609167650a8a2ad69455950a44a090fcf2f4999dbd209d1812c526ae6abaa07`. English source-article SHA256: `0bcaf96b3b79ae676716c373d92d64d19b24778bc6d54d72cb2933093d137fad`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

## Reader preface

This opening article introduces the different through trace duality and follows its behavior under passage to local rings and completions. It supplies the ideal-theoretic language behind later ramification and discriminant calculations.

**Textbook placement.** This article follows the specific chapter, section, and source window recorded below; those references are inherited from the original note and have not been newly verified for this edition.

**Prerequisites actually used.** A finite separable field extension; Dedekind domains and integral closure; fractional ideals; the nondegenerate trace pairing; localization and completion. The section-wide separability of residue extensions is an explicit standing hypothesis.

**Argument route and dependencies.** Begin with the trace dual of a fractional ideal, specialize to the inverse different, and follow the existing local comparisons. The exposition links the dual-module viewpoint to the later ramification correction in Riemann-Roch without opening that theory.

**Scope and status.** The scope is the opening of Chapter III §2 at the recorded source pages. All standing residue-separability assumptions and the original local behavior statements are retained. This edition translates and organizes the existing record. It does not independently verify proofs, repair mathematical arguments, or upgrade any recorded proof status. Historical next-step instructions and limitations remain part of the article.

Source location: Chapter III §2, book pp. 194-196 / PDF pp. 208-210 (corrected from rendered pages on 2026-10-04).

Intuition. Chapter III §1 views a number field as a curve with infinite points; §2 introduces the different and discriminant, which provide the ramification correction term in the later Riemann-Roch theory. Whereas Chapter I starts by computing a discriminant determinant, the present approach begins with the dual module for the trace pairing: ramification is measured by how far $\mathcal O$ is from being self-dual under trace.

Setup. Let $L/K$ be finite separable, let $\mathfrak o\subset K$ be a Dedekind domain with fraction field $K$, and let $\mathcal O$ be the integral closure of $\mathfrak o$ in $L$. Neukirch assumes throughout this section that the residue extensions $\lambda/\kappa$ of $\mathcal O/\mathfrak o$ are separable. This hypothesis must stay visible, especially when localizing and completing.

For a fractional ideal $\mathfrak A$ of $L$, define the trace dual

$$
{}^*\mathfrak A=\{x\in L:\operatorname{Tr}_{L/K}(x\mathfrak A)\subset\mathfrak o\}.
$$

It is again a fractional ideal. To see boundedness, choose a $K$-basis $a_1,\dots,a_n\in\mathcal O$ of $L$ and let $d=\det(\operatorname{Tr}(a_i a_j))\ne0$. After multiplying $\mathfrak A$ by a nonzero element of $K$, we may test $x=\sum x_i a_i$ against elements of $\mathfrak A$ that contain a scaled copy of the basis. The linear equations with coefficient matrix $(\operatorname{Tr}(a_i a_j))$ force $d$ times the scaled coordinates into $\mathfrak o$. Thus ${}^*\mathfrak A$ is contained in a finite $\mathfrak o$-module after clearing one denominator, hence is fractional.

The trace pairing also gives the conceptual identification

$$
{}^*\mathfrak A\simeq\operatorname{Hom}_\mathfrak o(\mathfrak A,\mathfrak o),
\qquad
x\mapsto(y\mapsto\operatorname{Tr}(xy)).
$$

Every $\mathfrak o$-homomorphism $\mathfrak A\to\mathfrak o$ extends uniquely to a $K$-linear map $L\to K$ because $\mathfrak A K=L$, and the nondegenerate trace form identifies $L$ with $\operatorname{Hom}_K(L,K)$. 

Definition 2.1. Dedekind's complementary module, or inverse different, is

$$
\mathfrak D_{\mathcal O/\mathfrak o}^{-1}={}^*\mathcal O
=\{x\in L:\operatorname{Tr}_{L/K}(x\mathcal O)\subset\mathfrak o\}.
$$

Its inverse ideal

$$
\mathfrak D_{\mathcal O/\mathfrak o}=({}^*\mathcal O)^{-1}
$$

is the different. Since ${}^*\mathcal O\supset\mathcal O$, the different is an integral ideal of $\mathcal O$. When $\mathfrak o,\mathcal O$ are clear, write $\mathfrak D_{L/K}$ and $\mathfrak D_{L/K}^{-1}$. 

Proposition 2.2 records functorial behavior.

First, in a tower $K\subset L\subset M$, with integral closures $A\subset B\subset C$, the different satisfies

$$
\mathfrak D_{C/A}=\mathfrak D_{C/B}\mathfrak D_{B/A}.
$$

Equivalently for complementary modules,

$$
\mathfrak D_{C/A}^{-1}=\mathfrak D_{C/B}^{-1}\mathfrak D_{B/A}^{-1}.
$$

The proof is just trace transitivity. One inclusion follows from

$$
\operatorname{Tr}_{M/K}
(\mathfrak D_{C/B}^{-1}\mathfrak D_{B/A}^{-1}C)
=\operatorname{Tr}_{L/K}\operatorname{Tr}_{M/L}
(\mathfrak D_{C/B}^{-1}C)\mathfrak D_{B/A}^{-1}
\subset A.
$$

For the reverse inclusion, if $x\in\mathfrak D_{C/A}^{-1}$, then $\operatorname{Tr}_{M/L}(xC)\subset\mathfrak D_{B/A}^{-1}$; multiplying by $\mathfrak D_{B/A}$ forces the trace into $B$, hence $\mathfrak D_{B/A}x\in\mathfrak D_{C/B}^{-1}$. 

Second, localization commutes with the different:

$$
\mathfrak D_{S^{-1}\mathcal O/S^{-1}\mathfrak o}=S^{-1}\mathfrak D_{\mathcal O/\mathfrak o}.
$$

This is immediate from the trace-dual definition after inverting $S$. 

Third, completion is local:

$$
\mathfrak D_{\mathcal O_\mathfrak P/\mathfrak o_\mathfrak p}
=\mathfrak D_{\mathcal O/\mathfrak o}\mathcal O_\mathfrak P.
$$

For the inverse different, Neukirch proves equality after reducing by localization to the DVR case. The key input is the local trace decomposition

$$
\operatorname{Tr}_{L/K}=\sum_{\mathfrak P|\mathfrak p}\operatorname{Tr}_{L_\mathfrak P/K_\mathfrak p}
$$

from Chapter II §8. To show the global complementary module localizes into the local one, approximate a test element at the chosen $\mathfrak P$ and by $0$ at the other primes above $\mathfrak p$; the other local trace terms become small/integral. Conversely, approximate a local dual element by a global element that is close at $\mathfrak P$ and close to $0$ at all other $\mathfrak P'|\mathfrak p$. This is exactly where the Approximation Theorem is used inside the proof.

Corollary 2.3. If $\mathfrak D=\mathfrak D_{L/K}$ and $\mathfrak D_\mathfrak P=\mathfrak D_{L_\mathfrak P/K_\mathfrak p}$ is viewed as an ideal of $\mathcal O$ by contraction/local support, then

$$
\mathfrak D=\prod_\mathfrak P\mathfrak D_\mathfrak P.
$$

Thus the global different is assembled prime by prime from local differents. This is the precise bridge to Marcus's different computations: local ramification exponents determine the global different ideal.

Hidden boundaries. The trace-dual construction needs $L/K$ separable so the trace form is nondegenerate. The standing separable residue-extension assumption is part of Neukirch's §2 setup and should not be silently dropped in completion/localization statements. Finally, the tower formula multiplies ideals after extension to the top ring; it is not an equality of ideals living in different rings without extension.

Next boundary. Continue at Proposition 2.4, book p. 197 / PDF p. 212: if $\mathcal O=\mathfrak o[\alpha]$, prove $\mathfrak D_{L/K}=(f'(\alpha))$ using the trace-dual basis of the power basis. Do not open Theorem 2.5 until the monogenic formula is clean.
