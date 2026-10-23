# Rounding correlated data can introduce a first-order penalty

## Public reader preface

**Learning question and project role.** Reader-only comparison on named admissible finite packets; prior domain/root/transport inputs are dependencies, not re-proved here. A Chapter XV reader extension on rigorous approximation with correlated admissible data. It is useful as a methodological case study in error geometry; it is not a claim of a new textbook theorem or generally available numerical accuracy.

**Preparation.** Complex moduli, interval enclosures, correlated errors, implicit roots, and the distinction between a common-data comparison and subtraction of independent broad boxes.

**Historical scope and status.** The 12 October source records reader-only-proof-chain-closed-pass1, restricted to the named rational and finite-digit packets and their own actual minima. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Rounding correlated data can introduce a first-order penalty. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The previously licensed packets, root tubes, contact bounds, common derivative field, and transport estimates are dependencies. No different parameter receives an inherited root license, and the comparison does not cancel uncertainty from unrelated data.

**Source and editorial treatment.** Case ID: `DIEUDONNE-N1`. Historical source date: 2026-10-12. Original project record: `chapter_15_euler_second_finite_gap_amplitude_penalty.md`. Original-note SHA256: `82be6de4abeec07073d6db0c17d333fb347e8c5d03f92e702d1c8f4212ff1e81`. The short historical excerpts use source lines 11–67; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 11–67

直觉：几乎最优的两份等半径数据，主要缺陷是极小的方向失配，损失为二阶。分别舍入两个复数之后，两份模长可能不再相等，新增的一阶幅差费反而先出现。要比较舍入前后的gap，必须以各包自己的根为中心；共同导数字段的来源误差应相关保留，而不从两个宽gap盒盲减。

固定 chapter_15_euler_second_balanced_finite_precision (source record: `chapter_15_euler_second_balanced_finite_precision`; not bundled) 的准确有理包 Q 与既有164位有限包 D；其合法性、唯一根图、两个自身根 $p_Q,p_D$、辅助圆与全局极小识别已经先付。$\widehat r=|\eta_Q|=|v_Q|$，而 D 满足 $A_D=|\eta_D|<V_D=|v_D|$。本篇比较 $\Gamma_Q=\widehat r-R(p_Q)$ 与 $\Gamma_D=V_D-R(p_D)$；公共半径及极小半径始终指各自的根，没有把 D 当作同 pT 的函数定义数据。

## 1. 不等模的准确平方恒等式

在任一真实端点场 C，令 $q=|C|>0$、$A=|\eta|>0,V=|v|>0$。定义 $W=\eta/A+(C/q)v/V$，以及 $c=\eta-Cv$。直接展开给 $(A+qV)^2-|c|^2=qAV|W|^2$。若 $V\ge A$，仿射模型的损失准确分成幅差与方向两项：

$$
V-\frac{|c|}{1+q}=\frac{V-A}{1+q}+\Psi.
$$

其中 $\Psi=qAV|W|^2/[(1+q)(A+qV+|c|)]\ge0$。令 $S=|W|^2$，再定义 $P=qAV/[(1+q)(A+qV)]$、$b=qAV/(A+qV)^2$ 与 $\beta=bS$，便有 $\Psi=PS h(\beta)$，$h(\beta)=1/(1+\sqrt{1-\beta})$。AM–GM 给 $0\le b\le1/4$，故小 W 的平方根分母始终远离0；这是准确有理化，不直接相减两个近等模长。

Q 的幅差项为0；D 的幅差项由准确有限数平方及真实 qD 盒给出，约 $1.21944011864\times10^{-165}$。真实 $A_D-V_D\approx-3.66988170507\times10^{-165}$。两包的方向损失仍约 $5.42142\times10^{-158}$，比幅差大七个数量级；即便如此，方向损失的变化可以更小。

## 2. 各自根的共同场运输

两包的准确复数据差满足 $|\eta_D-\eta_Q|,|v_D-v_Q|<10^{-164}$。已有自身根运输给 $|p_D-p_Q|<4.482\times10^{-123}$；这里使用的是旧真根间上界，不重新生成点中心。共同联合管上已付 $|C_p|<.05$、$|C_\delta|<M$，$M=1.124\times10^8$。于是

$$
|C_D-C_Q|\le .05|p_D-p_Q|+M|v_D-v_Q|<3\times10^{-124}.
$$

这同时包住 $|q_D-q_Q|$。实际C运输先在固定 $\delta_D$ 沿 $p_D\to p_Q$，再在固定 $p_Q$ 沿 $\delta_D\to\delta_Q$；旧联合管许可覆盖两段。后面A,V,q,W的标量凸段只用于代数函数Lipschitz估计，不能替代这条物理场路径。不能把端点的 $2.066\times10^{-63}$ 来源圈相互独立相减来替代这条短段许可。两端 $2<q_Q,q_D<3$；单位化恒等式给场相位差至多 $2|C_D-C_Q|/\min(q_Q,q_D)$。数据单位向量也用准确幅长归一化：$|\eta_D/A_D-\eta_Q/\widehat r|\le2|\eta_D-\eta_Q|/A_D$，v 同理。三项相加给 $|W_D-W_Q|<10^{-114}$。

旧数据及新端点许可还给 $|W_Q|,|W_D|<10^{-50}$；这是故意宽松的解析门，实际尺度约 $10^{-54}$。整个比较区间保持 $\widehat r/2<A,V<2\widehat r$、$1<q<3$；并未要求两根互异。

## 3. 方向费的变化先保留相关性

在上述正区域，$P\le\widehat r$，且 $|P_A|<1,|P_V|<1,|P_q|<3\widehat r$。例如 $P_A=q^2V^2/[(1+q)(A+qV)^2]$，而 $P_V=qA^2/[(1+q)(A+qV)^2]$；第三项可从 $\partial_q\log P=1/q-1/(1+q)-V/(A+qV)$ 得到。

$b\le1/4$，其三项导数分别可外包为 $1/\widehat r,2/\widehat r,2$。$\beta<10^{-100}/4$ 使 $h,h'<1$。沿 A,V,q 和复 W 的直段，这些界仍成立；W 的模不超过两个端点的较大者，所以没有独立外包产生不属于许可域的新角点。

令 $e_A,e_V,e_q,e_W$ 分别包住两端幅长、q及W的差，$w$ 包住两端 $|W|$。则 $\Delta P$ 的费用可取 $e_A+e_V+3\widehat r e_q$，$\Delta S$ 的费用可取 $2we_W$。再付 $\Delta\beta\le\Delta S/4+w^2[(e_A+2e_V)/\widehat r+2e_q]$，三次乘积拆分给

$$
|\Psi_D-\Psi_Q|\le w^2\Delta P+\widehat r\Delta S+\widehat r w^2\Delta\beta.
$$

有向标量预算小于 $3\times10^{-213}$。决定性项是 $\widehat r\,w\,e_W$；共同场的绝对来源宽没有被加两次。独立两gap盒也已能证明正差，外包为 $[8.70295581,15.6858466]\times10^{-166}$；相关推导则解释正差为何来自一阶幅差。

## 4. 非线性极小点仍各自付款

仿射损失与真实 $\Gamma$ 的差，沿用每包的仿射试点和真实极小点两份 $M|\Delta v|^2/2$ 费用。真实步长先由旧接触收缩除以 $1-Q$，因此不是把冻结极小点当作真实极小点。每包绝对非线性费约 $3.033\times10^{-199}$；两包相加连同方向费，小于 $6.3\times10^{-199}$。旧合法路径、辅助 $|v|\le1.001\rho$ 与全局局部极小识别先给域，细费没有反过来证明自己的许可。

最终准确关系为 $\Gamma_D-\Gamma_Q=(V_D-A_D)/(1+q_D)+E$，其中 $|E|<6.3\times10^{-199}$。主幅差费严格正，故有限164包的自身gap严格大于有理母包的自身gap；这只是这两份既有数据的结论，不推广为任意舍入都变差。receipt 的 `correlated_finite164_minus_rational_own_gap` 保存实际更紧方向费、两根非线性费和差盒；`two_minimizer_Taylor_feesD` 明列 D 的两份付款。两包的成员资格与严格非极小性均保持，未生成新包。

## 5. 两个小模型与当前学习目标

取实 $C=-q$、$\eta=v=r>0$，方向费为0。若只把 $\eta$ 减少 $\varepsilon$，则损失准确增加 $\varepsilon/(1+q)$。若保持两模为 r，只把 v 转角 $\theta$，则主损失为 $qr\theta^2/[2(1+q)^2]$：幅差一阶，切向误差二阶。这个区别解释了近极小数据的表示资格为何不同于普通根坐标精度。

同样取仿射根关系 $\eta=Gp+Cv$，令 $G=1,C=-2$。Q 取 $\eta=v=r$，根为 $p=3r$；D 改为 $\eta=r-2\varepsilon,v=r+\varepsilon$，根仍是 $3r$，但自身gap增加 $\varepsilon$。因此 $\Gamma_D>\Gamma_Q$ 绝不推出 $p_D\ne p_Q$；本书实际两包也保留这一区分。

在已付正半径、唯一接触图上，还可直接微分两条等模约束。接触有 $\eta/R=-(C/q)v/R$，而 $d\eta=G\,dp+C\,dv$，故 $(1+q)dR=\operatorname{Re}(\overline{\eta/R}\,G\,dp)$。它把两圆的加权径向变化与先前最小半径法向流连接起来：接近接触时，共同径向变化先被极小半径吸收，剩下的不等模部分产生上述线性gap。这里不新增法向流数值或绝对根坐标，只解释本次比较的结构。

原源/显示/输入/算术四账、同 pT 具名157/158舍入资格与未付门见 chapter_15_euler_second_root_secant_and_dephased_kernel (source record: `chapter_15_euler_second_root_secant_and_dephased_kernel`; not bundled)；全链 reader-only D3 pass1，不作整体review或书级升格。后继可从当前准确幅差与方向差预算继续考察同根平衡数据的表示门；不默认重跑节点/矩，不扩大原产品或更换参数。
