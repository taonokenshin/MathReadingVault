# Three mechanisms behind partition identities

## Public reader preface

**Learning question and project role.** Context and hypothesis guidance, rather than a repetition of the partition identity proof. A selective analysis/analytic-number-theory support lane. Its durable records connect convergence, integral interchange, character sums, products, and generating functions across two books. The historical queue is maintenance-gated; this release does not reopen it.

**Preparation.** Power-series coefficients, infinite products, roots of unity, and the distinction between finite Fourier filters and analytic theta transformations.

**Historical scope and status.** Historical explanatory synthesis. The partition identity and its prior proof are reused; the note explicitly adds context rather than claiming another proof. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Three mechanisms behind partition identities. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The prior partition-identity derivation, Jacobi/Euler product identities, and Poisson/theta results are dependencies outside this excerpt. The comparison does not identify the finite filtering proof with a modular-transformation proof.

**Source and editorial treatment.** Case ID: `APOSTOL-N1`. Historical source date: 2026-06-30. Original project record: `2026-06-30-ramanujan-modular-theta-context.md`. Original-note SHA256: `74d730f561ad4224a8d2fadc79e3006ce4acf6220ec045d09e2b1cd1a3666005`. The short historical excerpts use source lines 13–31, 113–133; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 13–31

## 直觉图像

Ch. 14 的证明可以想成有限 Fourier 分析。若要抽出 $4\pmod 5$ 的系数，最自然的工具是五次单位根：
$$
\frac15\sum_{h=0}^{4}\alpha^{-4h}F(\alpha^h x),
\qquad \alpha=e^{2\pi i/5}.
$$
这一步只是在有限循环群 $\mathbb Z/5\mathbb Z$ 上做投影。它不需要把 $x=e^{-2\pi t}$ 送到 $e^{-2\pi/t}$，也不需要知道 modular transformations。

但恒等式右侧
$$
\frac{\varphi(x^5)^5}{\varphi(x)^6}
$$
已经很像 modular theory 中的 eta-quotient。若写 $x=e^{2\pi i\tau}$，Dedekind eta function 满足
$$
\eta(\tau)=x^{1/24}\varphi(x).
$$
于是上式等价于一个由 $\eta(5\tau)$ 和 $\eta(\tau)$ 组成的 eta-quotient，再乘上一个简单的 $x$-幂。这个观察解释了为什么 Ramanujan 分拆恒等式后来会自然进入 modular forms；但在 Apostol 这条证明里，它只是背景，不是逻辑输入。

### Source lines 113–133

## 隐藏假设和反驳点

第一，若把这些公式当解析恒等式使用，必须保持 $|x|<1$。这样无穷乘积的拆分、有限单位根乘积后的逐项重组、以及系数比较都有绝对收敛或局部一致收敛支撑。

第二，也可以在形式幂级数环中理解这些等式，但要换一种合法性说明：每个固定次数的系数只依赖有限多个低阶因子。不要在形式幂级数语言里随意使用需要解析收敛的极限操作。

第三，$I_0I_2=-I_1^2$ 不是从符号上“看出来”的。它来自 $\varphi(x)^3$ 的 type $2$ 部分为零，并且使用 $I_0$ 的常数项为 $1$，所以 $I_0$ 在幂级数环中可逆。

第四，这条证明没有证明任何 modular transformation。它只显示了一个 modular 现象的初等影子：eta-product 形状、level $5$ 的同余过滤、以及 theta/product identities 同时出现。

## 与当前学习目标的关联

paired lane 现在有三种 Fourier/生成函数工具：

第一，Dirichlet series 和 Perron/Mellin kernels 服务于素数分布，核心变量是 $n^{-s}$。

第二，Poisson/theta transformation 服务于 completed zeta 和函数方程，核心动作是 Fourier transform 与尺度倒易。

第三，ordinary generating functions 与 roots-of-unity filters 服务于 partitions，核心变量是 $x^n$ 和同余类抽取。

当前 Ch. 14 的首轮证明已经闭合。2026-06-30 后续已经用 reciprocal Gamma product 和 sine product 笔记补齐当时提到的 complex Gamma / Weierstrass support。若以后继续这条背景线，应明确是新的 modular forms / eta function 背景或 paired-lane closure audit，不是重复 Ch. 14 Ramanujan proof 或 Gamma product 支撑。
