# Affine monodromy requires an explicit path-order convention

## Public reader preface

**Learning question and project role.** Reader-created warning about path order and cover universality; retain the rectangular-lattice scope. A reader extension of the Complex Analysis lane. It uses established local mechanisms to test when a proposed global interpretation is justified, while keeping the Fourier book and earlier proof grades separate.

**Preparation.** Elliptic functions for a rectangular period lattice, local inverse germs, continuation along based loops, and composition of affine maps.

**Historical scope and status.** Recorded as reader independently proved / proof-audited / closed-pass1 / D3. This is a local convention guard, not a new theorem attributed to the textbook. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Affine monodromy requires an explicit path-order convention. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The already-established rectangular-lattice inverse is reused. The excerpt does not establish an arbitrary cubic period lattice, a global square-root branch on the three-root complement, or universality of the inverse cover.

**Source and editorial treatment.** Case ID: `STEIN-N2`. Historical source date: 2026-10-14. Original project record: `2026-10-14-elliptic-affine-monodromy-order-guard.md`. Original-note SHA256: `15b4ec36fbcd6279035036d903bc33560a2d305bfadfa2052d081705d73b714b`. The short historical excerpts use source lines 21–41; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 21–41

## 两个相反的单路反例

$\gamma_1^2$ 对第一根绕数为二，对其余根为零；但 $T_1^2=\mathrm{id}$，积分坐标没有位移。这说明单条路径的非零 individual winding 不必给非零 affine monodromy。

再看 commutator，按上述 first-path 约定走 $\gamma_1\gamma_2\gamma_1^{-1}\gamma_2^{-1}$。各根绕数都为零，但 meridian inverse 的反射仍为 $T_j$，故写出的 affine map 是 $T_1T_2T_1T_2$，即 $z\mapsto z-2\tau$。它恢复根号号，却没有恢复积分坐标。这说明单条路径的零 individual winding 也不必消去 affine monodromy。

这里的 $-2\tau$ 是沿**多值根号的连续分支**积分所得位移，不是 $Y$ 上某条全局 holomorphic differential 的普通 period。若某平面域已有全局 $q$，闭路积分是加性 homomorphism，自然杀掉 commutators；它不可能同时包含上述两个 odd meridians 的全部轨迹，因为各小圈已经违反平方根门。

## 回到整域判据

前页“每条闭路对每根绕数均零”量化整个域。在平面域中，任一闭路可有限分解为域内 simple polygons；它们分别不围根，因而可匹配根号延入各内部、逐项用 Cauchy。这个过程证明整域的普通 periods 为零，不是把 affine monodromy 当作单路 winding 的线性函数。

不同 corridors 会共轭或改变半周期代表，从而改写 generators 的 affine 常数。上面的具体 $1,\tau,-2\tau$ 只在给定 lower-corridor 规范中断言；整个群的两族结构、根号门与单值积分门不依赖这种命名选择。自测：为什么 continuation 的 written affine product 顺序容易误读？为什么 commutator 例不能放进一个已有全局 $q$ 的域？为什么整域判据必须写“每条”而非只给当前路径的三个整数？

## 解析逆所在的 cover 不必 universal

令 $E=\mathbb C\setminus(\frac12\Lambda)$；删去的半格点同时包括 poles 和三个有限 critical fibers。已有 degree-two covering 在环面上删去四个 branch values 后无分歧；再把其两个局部 inverse charts 作 lattice lift，就给 $\wp:E\to Y$ 的 evenly-covered neighborhoods。因此这是连通无分歧 covering，不只是沿单条路径可解微分方程。

同值点恰为 $\pm z+\lambda$，故这些 affine maps 是作用自由且在纤维上传递的 deck transformations。没有额外 deck map：在一个 inverse chart 内它必须等于某个 $z\mapsto\pm z+\lambda$，全纯恒等原理延到连通的 $E$。所以前面的 affine 群正是这份 regular cover 的 deck group。

但 $E$ 不是单连通。围任一不属于 $\Lambda$ 的 half-period 的小圈对该删点的绕数一，不能在 $E$ 内收缩；其 $\wp$ 像却是对应 root meridian 走两次。沿该像路 inverse 坐标回到原值，对应 $T_j^2=\mathrm{id}$，同时 lifted loop 仍非平凡。若围的是 lattice pole，其像则绕无穷远两次，不把它称为有限根 meridian。因此“解析延拓的 affine map 为恒等”不等于“原闭路可收缩”，这份具体 inverse surface 也不等于 universal cover。这里只说明明确的 kernel 元，不声称已经给出 kernel 的完整 presentation。
