# A square class does not preserve a fixed divisor representative

## Public reader preface

**Learning question and project role.** Reader counterexample and repaired scope, not an official publisher erratum or a rejection of two-descent. An arithmetic certification and hypothesis-tracking example from Cohen Volume I, Chapter 8. The larger first pass remains unfinished, and Volume II remains gated.

**Preparation.** Two-isogeny descent, square classes, quartic coverings, primitive integer solutions, and common-factor cancellation.

**Historical scope and status.** The covering and primitive-normalization arguments are recorded reader closed-pass1. A fixed-divisor literal equivalence is recorded as refuted/source-caveat; the repaired formulations are project arguments, not official publisher errata. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** A square class does not preserve a fixed divisor representative. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The distinction is between a square class and an already-fixed divisor representative. The case does not refute two-descent itself. The reader repairs preserve their stated coefficient and coprimality assumptions, and official errata were not checked for this public edition.

**Source and editorial treatment.** Case ID: `COHEN-N2`. Historical source date: 2026-10-15. Original project record: `2026-10-15-ch8-quartic-fixed-divisor-caveat.md`. Original-note SHA256: `8afefc090a4f9e6a2cec4d2a3ae82d407e5c7a58bfa973288d15393064e9635a`. The short historical excerpts use source lines 17–35; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 17–35

**Prop11的固定参数反例。** 取$a=12,b=12,b_1=4$，其平方自由部分$s(b_1)=1$。平方自由方程$Y^2=X^4+12X^2Z^2+12Z^4$有$(X,Y,Z)=(1,5,1)$，满足$XZ\ne0,\gcd(X,Z)=1$。原固定参数方程却是$Y^2=4X^4+12X^2Z^2+3Z^4$：$Z$奇时右端模4为3，不可能平方；$Z$偶时$Y$也偶，不能两两互素。因此固定$b_1=4$的iff不成立。曲线判别因子$a^2-4b=96\ne0$，不是退化反例。

原书逆向proof令$f=\gcd(X,Y)$后构造的是$b_1'=s(b_1)f^2$，并未证明$b_1'=b_1$；本例恰有$f=1$，返回$b_1'=1$。不能把这次系数更新从结论中省掉。

**准确的平方类版本。** 给平方自由有符号约数$s\mid b$，方程$Y^2=sX^4+aX^2Z^2+(b/s)Z^4$有$XZ\ne0,\gcd(X,Z)=1$的整解，当且仅当同一平方类中的某个约数$b_1'=sf^2\mid b$的覆盖有两两互素解。

证明：先由$s$平方自由和$\gcd(X,Z)=1$推出$\gcd(Y,Z)=1$。若$p\mid Y,Z$，则$p\nmid X$；模$p$先迫$p\mid s$，随后$sX^4$赋值恰1、其他项至少2，矛盾。令$f=\gcd(X,Y)>0$，则$\gcd(f,Z)=1$；方程模$f^2$给$f^2\mid b/s$。除去$f^2$，取$X'=X/f,Y'=Y/f$，得到$b_1'=sf^2$的覆盖，且三变量两两互素。反向写$b_1'=sf^2$，将$(X',Y',Z)$送到$(fX',fY',Z)$即可；Thm9的$\gcd(b_1',Z)=1$保证新$X$仍与$Z$互素。

**准确的固定参数版本。** 若原先固定$b_1=su^2$、$u>0$，则平方自由方程还必须要求

$$
\gcd(X,Y)=u.
$$

前向转换$(X_0,Y_0,Z_0)\mapsto(uX_0,uY_0,Z_0)$恰使共同因子为$u$；逆向除以同一个$u$，才会回到原来的$b_1$。这是缺失的精确条件，而非可随便再选的一次参数。

$Y=0$也不例外：此时$f=|X|>0$，上述$\gcd(Y,Z)=1$迫$|Z|=1$。Cor12在$b_1,b/b_1$都平方自由时成立：$f^2\mid b/b_1$迫$f=1$，所以仅$\gcd(X,Z)=1$便足够两两互素。

用于下降时，合法做法是在平方类层面问“是否有某个代表的全局覆盖点”，而不是把某个固定约数的本原点许可搬给同类另一约数。局部可解性仍只提供上界；上述global witness与精确本原化没有证明一般四次曲线的Hasse原则。
