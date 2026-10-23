# Equal orders and indices can hide different quotients

## Public reader preface

**Learning question and project role.** Compact project-authored counterexample retaining the actual carry and marked embedding. A Chapter 8 reader investigation beside Serre’s finite-groups material. It concentrates on actual integral embeddings and marked tensor data, where dimension and order alone can discard essential information.

**Preparation.** Finite abelian groups, cyclic presentations, quotient maps, tensor products over the integers, and reduction modulo three.

**Historical scope and status.** Recorded as closed-pass1-reader-problem. The compact counterexample is a project-created boundary test, not a printed exercise or a new reviewed item. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Equal orders and indices can hide different quotients. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** Earlier joint-image calculations are named reuse. The point is that equal orders, element orders, and indices do not determine the marked quotient. No general classification or new source-exercise completion follows.

**Source and editorial treatment.** Case ID: `SERRE-N1`. Historical source date: 2026-10-07. Original project record: `2026-10-07-ch8-marked-quotient-equal-index-counterexample.md`. Original-note SHA256: `50e2f897a6ba04fb5183bcdc8cd7853e334207c9c1b21356de0d6030a9e413d9`. The short historical excerpts use source lines 3–17; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–17

本条从本轮亲自处理的五重/四重 joint 问题提取一个可复用边界，`closed-pass1-reader-problem`；不是原书题面，也不新增reviewed。与 2026-10-07-ch8-fifth-raw-joint-image (source record: `2026-10-07-ch8-fifth-raw-joint-image`; not bundled)、2026-10-07-ch8-gap-four-fourfold-marked-completion (source record: `2026-10-07-ch8-gap-four-fourfold-marked-completion`; not bundled) 配合阅读。Ex15的有理化结构可以看自由部，但本轮整数目标要保留真正标记嵌入，不能从群阶或秩认商。

**一个有区分力的二副本例。** 取 $F=C_{81}w\oplus C_3s$，实际标记 $\zeta=9w+s$ 阶九。两副本先加入正确旧pair关系 $\zeta_1+\zeta_2=0$，得到Q。真实cube母群换基给 $Q=F\oplus(F/\langle\zeta\rangle)$；消s后 $F/\langle\zeta\rangle=C_{27}$。所以Q阶为 $3^8$，每个真实ζ的像仍九阶。

现在加真实新列ζ1=0；旧pair同时给ζ2=0，因此商是 $C_{27}^2$，阶 $3^6$。若把ζ1的三阶carry漏掉、误加9w1=0，结果不同：w1变九阶；旧pair可用单位系数消 $s_2=-9w_2-s_1$，旧 $3s_2=0$ 给 $27w_2=0$。没有剩余混合关系，商是 $C_9\oplus C_{27}\oplus C_3$，仍阶 $3^6$。

两条新列都九阶，指数都九，但末商的模三维数分别为2和3。漏carry的错误因此逃过“原始元阶、总指数、有限 valuation”三项检查。它能被完整marked mother位置与quotient-copy坐标查出：在 $F/\langle\zeta\rangle$ 中，9w的像是−s，真三阶，故错误新列在该副本坐标非零；真实ζ在所有quotient-copy坐标都零。

**本轮可复用的证明链。** 先在原始整基中建立输入的加权中心化与Boolean差分；再逐列分类旧关系，证明它保持root/centered支撑或固定inner子集；随后构造落在完整C27/C81等母块的兼容投影，检查新列在母块中的实际graph位置；最后同步母群与mark做cube/树换基。每一步都给一个反向包含，才从必要关系走到完整像。普通整数张量对已给定直和分配，无需flatness；但只知道商群型不能反推出原始嵌入。

对范数九除还要另问自由投影是否原始。本轮的 $\lambda(G)=1$ 是正确启动证据；norm的增广27或等式W=9G均不足。对带carry的自由关系则只规范化free向量，carry仍用原P(v)，不能跟随除三/除九。固定总槽数的closure与抽象h/r引理的适用条件也分开，r2的primitive trace与pure顶点删图均有真实例外。

两个可自测的小问题：为何不能把完整C27母群回缩到九倍C3子群？任何从C27到C3的同态在9倍元上为零，所以本轮投影必须保留C27母群；只在joint image内部才可投影到其中的C3因子。为何奇偶cube没有twist门可以偷省？一条边把和误换成差，C9/3C9的square会把剩余C9降成C3，说明同一N群型及各边秩不决定全cube商。

该反例是对本轮实际carry/projection问题的数学检验；不以此宣称已复盘全章或已审核作者的integer tensor定理。后继仍是source161四重的实际outer Hh(27)与raw mark同步门。
