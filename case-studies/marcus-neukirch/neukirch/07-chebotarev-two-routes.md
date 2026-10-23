# From One-Dimensional Nonvanishing to Chebotarev Density

## Public reader preface

**Learning question and purpose.** Compare cyclic-subgroup reduction with a character-expansion route, keeping the analytic input explicit. This case belongs to Neukirch VII §13. It is part of a user-directed, Codex-assisted study project; it presents reader exposition and supplementary reasoning about established mathematics, without claiming a new theorem or priority.

**Preparation.** Prime-ideal Euler products, Dirichlet density, finite group characters, Frobenius conjugacy classes, one-dimensional Hecke nonvanishing, and the cited Artin–Hecke formalism.

**Argument route.** Extract the logarithmic prime divergence; compare density notions; use character orthogonality; reduce to a cyclic subgroup and count centralizer fibres; compare the stronger character-expansion route.

**Historical scope and qualification.** The historical project records closed-pass1/source-checked-with-coefficient-caveat, unreviewed. The residue-coefficient qualification remains explicit. Source records closed-pass1/source-checked-with-coefficient-caveat, unreviewed. Preserve the residue-coefficient caveat and the distinction between Dirichlet and natural density.

**Source and provenance.** The mathematical body is adapted from English study-edition article `NA0535`, originally recorded on 2026-08-27, in the preserved 20 October 2026 snapshot. The textbook reference is Neukirch VII §13; printed-page locators below belong to the source edition and are not a universal PDF offset. Underlying original-note SHA256: `7e5e1fc5d6795664a0e7d7f0ac31f0f45a35ca09d103d1bbea27d9bdbc81ca87`. English source-article SHA256: `544d43f7150c25e6721f72826b2d9a78a60f1d989fb8235ae3670443bb7b67d4`. Textbooks and private source files are not bundled with this case.

**How to read the historical body.** The exposition below retains its original mathematical content and source-specific qualifications. A reference to a “run,” “review,” or next exercise describes the dated project history, not an instruction to operate an automation or a new proof audit. Public editing removes private archive links and obsolete operational continuation wording; no proof is re-verified and no status is upgraded. Unbundled article IDs identify provenance rather than working links.

**Reader choice.** Use the parts that serve your own course or research preparation. The optional, unfinished NM-HR-073 branch is not a prerequisite for this case. [Return to the case-study index](../INDEX.md).

## Historical mathematical exposition

After logarithms of Euler products, first powers of prime ideals carry all logarithmic divergence and higher powers leave an analytic error. Character orthogonality extracts each ray class's proportion from that divergence. For nonabelian groups, place a specified Frobenius element inside its cyclic subgroup and count prime fibers after base change. The factor comes from a centralizer index, not a guess of uniformity among elements.

Before reading the author's p. 555 proof, this run derived 13.2 independently from finite-order Hecke nonvanishing and orthogonality. Before p. 557, it also reconstructed cyclic-subgroup reduction, degree-one primes, and centralizer fibers. A separate Brauer character-expansion proof is included for comparison. The functional equation itself is not a density-proof hypothesis; both branches share Artin–Hecke formalism and one-dimensional analytic input.

## Definition 13.1 and exact normalization of divergence

Let $M$ be a set of finite prime ideals of number field $K$. Its Dirichlet density is, as real $s\downarrow1$, the limit of $\sum_{\mathfrak p\in M}(N\mathfrak p)^{-s}$ divided by the corresponding sum over all prime ideals, when that limit exists.

Take the Euler logarithm of $\operatorname{Re}s>1$. The sum $R(s)=\sum_{\mathfrak p}\sum_{j\ge2}(j(N\mathfrak p)^{js})^{-1}$ outside first powers converges absolutely and locally uniformly on $\operatorname{Re}s>1/2$, bounded on each compact sub-half-plane by a constant times $\sum_{\mathfrak p}(N\mathfrak p)^{-2\sigma}$. Thus $R$ is analytic at one.

The precise residue expansion is $\zeta_K(s)=\kappa_K/(s-1)+h(s)$ with $\kappa_K>0$ and $h$ holomorphic at one. Hence

$$
\sum_{\mathfrak p}(N\mathfrak p)^{-s}
=\log\frac1{s-1}+O(1).
$$

More strongly, after choosing logarithms on the positive real direction, their difference extends holomorphically at one: the extra term is $\log(\kappa_K+(s-1)h(s))-R(s)$. The density denominator can therefore be replaced by $\log(1/(s-1))$.

**Source coefficient caveat.** PDF p. 554 defines $f\sim g$ as equality modulo a difference analytic at one, then writes $\zeta_K(s)\sim1/(s-1)$. Under that definition residue $\kappa_K$ must remain and cannot generally be replaced by one. The logarithmic equivalence that follows remains correct because constant $\log\kappa_K$ is absorbed into the analytic term. This proof-line correction changes neither density definition nor conclusion.

Primes of absolute residue degree at least two contribute only analytic error too: at most $[K:\mathbb Q]$ primes lie above a rational prime and each has norm at least $p^2$. Their sum converges on $\operatorname{Re}s>1/2$. Finite additions/deletions preserve density; prime ideals of absolute degree greater than one have density zero.

## Why natural density implies Dirichlet density

Let $A(x)$ count primes in $M$ of norm at most $x$, and $B(x)$ all primes. If $A(x)/B(x)\to\delta$, Abel summation writes both Dirichlet series as $s\int_1^\infty A(t)t^{-s-1}dt$, $s\int_1^\infty B(t)t^{-s-1}dt$.

Given $\epsilon>0$, sufficiently large $T$ gives $|A(t)-\delta B(t)|\le\epsilon B(t)$. The integral over $[1,T]$ stays bounded as $s\downarrow1$ while the denominator diverges. The quotient error is at most $\epsilon+o(1)$, giving Dirichlet density $\delta$ without a prime-ideal theorem.

The source's failure of the converse has an explicit check. Let $p_n$ be rational prime number $n$, put $N_j=\lceil\exp(\exp(j^2))\rceil$, and take all primes with indices in $[N_j,2N_j]$ into $M$. Before block $j$ the natural proportion tends to zero; at its end it tends to $1/2$ because earlier blocks are negligible relative to $N_j$. Natural density fails.

On the other hand $p_n\ge n$. Write $s=1+\eta$; each block's weighted sum is at most $2\exp(-\eta\log N_j)$. Put $J=\lceil\sqrt{\log(1/\eta)}\rceil$. The first $J$ terms are at most $2J$; subsequent term $J+k$ is at most $2e^{-e^k}$. The total is $O(\sqrt{\log(1/\eta)})$, and division by the full-prime sum's $\log(1/\eta)+O(1)$ tends to zero. The set has Dirichlet density zero but no natural density, without prime asymptotics or enumeration.

The following theorems establish only **Dirichlet density**, not natural density or a counting asymptotic with $\operatorname{Li}(x)$.

## Lemma 13.3: one-dimensional characters are nonzero at one

Let $\theta$ be a nontrivial one-dimensional ray-class character. First take its primitive version and faithful cyclic class field $E/K$. The nontrivial Hecke functions are entire, and $\zeta_E/\zeta_K$ is the product of all nontrivial Artin-character factors. At one, the left side is a ratio of nonzero residues; every right-side factor is finite, hence nonzero.

Enlarging primitive modulus to the original adds only finitely many factors $1-\theta(\mathfrak p)(N\mathfrak p)^{-s}$, nonzero at one because $|\theta(\mathfrak p)|\le1<N\mathfrak p$. Thus original-modulus $L(\theta,1)$ is nonzero too. PDF p. 555 uses a ray field and the same regular-character decomposition; the faithful quotient here isolates extra Euler factors first.

This is the same one-dimensional nonvanishing lemma as this run's §12 zero audit, which independently also proves boundary nonvanishing of $1+it$. Density needs only $t=0$, without a stronger prime theorem.

## Theorem 13.2: character orthogonality on the correct finite quotient

Let $A=J^{\mathfrak m}/H^{\mathfrak m}$ have order $h$, with $P^{\mathfrak m}\subseteq H^{\mathfrak m}\subseteq J^{\mathfrak m}$. For $a\in A$, one-dimensional orthogonality gives

$$
1_{[\mathfrak p]=a}=\frac1h\sum_{\theta\in\widehat A}\overline{\theta(a)}\theta([\mathfrak p]).
$$

Take weighted prime sums. The Euler logarithm of each $\theta$ differs from $\sum_{\mathfrak p\nmid\mathfrak m}\theta([\mathfrak p])(N\mathfrak p)^{-s}$ by a function analytic at one, by the higher-power estimate above, since character magnitudes are at most one.

The principal L-function is Dedekind zeta with finitely many factors removed, with logarithm $\log(1/(s-1))+O(1)$. By 13.3, nonprincipal factors are finite nonzero at one and have local analytic logarithms contributing bounded terms. Euler and local logarithms differ at most by a fixed integer multiple of $2\pi i$, irrelevant to the limit.

The prime sum in class $a$ is therefore $h^{-1}\log(1/(s-1))+O(1)$, giving density $1/h$.

PDF p. 555 actually sums over the full ray quotient $J^{\mathfrak m}/P^{\mathfrak m}$. For general $H^{\mathfrak m}$, merge full ray classes lying in one $H$ class, or use only characters trivial on $H$ as here. Use $h=(J^{\mathfrak m}:H^{\mathfrak m})$ consistently rather than mix both quotient orders. This supplies the compressed merging step without changing the statement.

For $K=\mathbb Q$ this recovers for coprime class $a\bmod m$ its prime Dirichlet density $1/\varphi(m)$. Noncoprime classes are excluded.

## Theorem 13.4: independently reconstruct cyclic-subgroup reduction first

Let $L/K$ be finite Galois with group $G$. Fix $\sigma\in G$ with conjugacy class $C_\sigma$, and put $H=\langle\sigma\rangle$, $F=L^H$, $h=|H|$. The extension $L/F$ is cyclic. By 13.2, Frobenius exactly $\sigma$ occurs at $F$-primes forming a set $Q_\sigma$ of density $1/h$.

Require relative residue degree one over $K$ and unramifiedness in $L/K$, keeping only such $\mathfrak q$. Ramified primes removed are finite; relative degree greater than one gives absolute degree at least two over $\mathbb Q$ and density zero. The retained set $Q'_\sigma$ still has density $1/h$.

The image of $\mathfrak q\mapsto\mathfrak p=\mathfrak q\cap K$ is precisely $P_{L/K}(\sigma)$. Relative degree one preserves norms and prevents additional powers of local Frobenius. Both conditions are essential.

Fix an image prime $\mathfrak p$ and choose $\mathfrak P$ above it with Frobenius $\sigma$. Unramifiedness makes its decomposition group exactly $H$. All upper primes are $g\mathfrak P$ with Frobenius $g\sigma g^{-1}$; this still equals $\sigma$ exactly when $g\in Z_G(\sigma)$. They give the same prime exactly when differing by $H$, so fiber size is

$$
r=[Z_G(\sigma):H]=\frac{|Z_G(\sigma)|}{h}.
$$

These biject with primes of $Q'_\sigma$: in cyclic $L/F$, the element $\sigma$ generates the whole group. The associated decomposition group is full, leaving only one upper prime.

Norms agree and fiber size is constant $r$, so both Dirichlet prime sums differ by that factor. Their denominators over either base are $\log(1/(s-1))+O(1)$. Hence

$$
d_K(P_{L/K}(\sigma))=\frac{1/h}{r}
=\frac1{|Z_G(\sigma)|}=\frac{|C_\sigma|}{|G|}.
$$

This agrees term by term with PDF pp. 556–557. At $\sigma=1$, we have $F=L$, $h=1$ and fiber size $|G|$, recovering density $1/[L:K]$ of completely split primes. This boundary checks the denominator direction.

## Second proof: Artin character expansion

For independent comparison let $\rho$ range over irreducible characters. At unramified primes the first Euler-log term is $\rho(\operatorname{Frob}_{\mathfrak p})(N\mathfrak p)^{-s}$, and higher terms are analytic at one since $|\rho(g)|\le\rho(1)$. This run's §12 used one-dimensional nonvanishing and integral Brauer induction to prove every nontrivial irreducible Artin L-function finite nonzero at one, with only the principal character having a simple pole.

The conjugacy-class indicator has character expansion

$$
1_{C_\sigma}(g)=\frac{|C_\sigma|}{|G|}
\sum_\rho\overline{\rho(\sigma)}\rho(g).
$$

After weighted prime summation, only the principal term gives logarithmic divergence with coefficient exactly $|C_\sigma|/|G|$; the rest stay bounded. This proves Chebotarev too, with stronger Brauer input. The author's cyclic-subgroup route needs only one-dimensional nonvanishing and finite-group counting. Neither uses general Artin holomorphy.

## Source and status

Results 13.1–13.4 and natural-density comparison are closed-pass1/source-checked, unreviewed. The p. 554 residue-coefficient caveat remains; explicit merging above closes the general-quotient interface of 13.2. Adjacent degree-one primes, the Galois criterion, and Bauer's theorem continue by the same conjugacy mechanism; see this run's second-half §13 note.
