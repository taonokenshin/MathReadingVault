# Boundary inputs can map to an interior output

## Public reader preface

**Learning question and project role.** Explain the genuine real-rank mechanism and scope; do not promote the older numerical witness to a current global certificate. A Chapter XV reader extension on rigorous approximation with correlated admissible data. It is useful as a methodological case study in error geometry; it is not a claim of a new textbook theorem or generally available numerical accuracy.

**Preparation.** Real derivatives of a complex-valued map, two phase variables, the inverse function mechanism, and quantitative control on an already licensed analytic domain.

**Historical scope and status.** The 7 October source records reader-only-chain-closed-pass1. Its later selected review covers only the real-rank inner-disk mechanism and global normal-contraction interface; the older numerical witness is expressly excluded from that review. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Boundary inputs can map to an interior output. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The exact correlated observations, existing derivative bounds, and old root/domain licenses remain required. Boundary points in the input product are not automatically output support points. The excerpt does not certify an unbundled high-precision numerical witness or update the current root enclosure.

**Source and editorial treatment.** Case ID: `DIEUDONNE-N2`. Historical source date: 2026-10-07. Original project record: `chapter_15_euler_second_boundary_torus_interior.md`. Original-note SHA256: `f1c96c4fa0946250ee1c3b6f827427ca4ec693b385edef1b7879bbe9a8eed8fd`. The short historical excerpts use source lines 14–49, 99–101; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 14–49

直觉：一个圆周只有一个实切向；两项观测分别在圆周上，就有两个实相位。若这两个切向在输出平面不平行，输出能在附近向任意方向移动，所以输入的双边界点反而可以给像内点。这里两向几乎平行，必须保持准确相关性；浮点作图或把小角当0都会丢掉结论。

沿用准确 $\eta_R=-\zeta v_R$、$|\zeta|=1$、$|\eta_R|=|v_R|=\rho$。记观测 a 中心为 $a_c$。两实相位的真实映射为 $f(\theta_1,\theta_2)=P(a_c+\eta_Re^{i\theta_1},\delta_0+v_Re^{i\theta_2})$。输入误差模恒为 rho；任何实相位仍在原两个圆的边界。$f(0)=p_*$ 是唯一真实根，不是显示中心或仿射预测。

既有逐对存在性、内 p 半平面导数和局部隐函数拼接，使这个相位映射在实相位球上光滑。即使原观测是闭圆周点，真实 Gauss 根仍简单，局部全纯分支存在；实相位路径本身始终保留原物理输入资格。

## 一项准确小虚部决定实秩

令 $A=1/(\delta_R\mathcal H_p)$、$C=h_R+\delta_R\mathcal H_\delta$，所有根导数在同一 $p_*$ 计算。两列分别是 $iA\eta_R$ 与 $-iACv_R$。按相位1、相位2和标准实输出 x、y 的顺序，准确实雅可比行列式为 $|A|^2\rho^2\operatorname{Im}(\bar\zeta C)$，符号不能另加负号。

记 $q_H=|H|$、$r_d=\rho/|\delta_0|$。原相位公式给 $h_R/\zeta=(q_H+r_ds_R)/(1-r_ds_R)$，因此

$$
\operatorname{Im}(\bar\zeta h_R)=\frac{(1+q_H)r_d\operatorname{Im}s_R}{|1-r_ds_R|^2}.
$$

旧有向标量包络给这一数约 $-9.5695932588643\times10^{-15}$。即使用旧 $|\mathcal H_\delta|<397$，$|\delta_R\mathcal H_\delta|<5.622\times10^{-38}$ 也不能抵消它；新实际导数只让此账更紧。整个行列式严格负，约 $-5.638\times10^{-30}$。于是实二维隐函数定理直接证明 $p_*$ 是真实产品像的内点。

这不是一般超几何根分类，也不是把任意输入边界都宣布为内点。当前条件依赖具体 $\operatorname{Im}s_R\ne0$。若该虚部为0且其他项也消失，两列可平行，必须重新处理；本证明不跨这个退化支。

## 用已有解析域给一个明确内圆

全部当前产品真根距 $p_0$ 小于 $4.333\times10^{-7}$。在已有真实内 p 圆中以各点为中心取 $r_p=5\times10^{-8}$；在原相对 delta 圆中取 $r_\delta=5\times10^{-46}$。旧 $|\mathcal H_p|<.03494$、$|\mathcal H_\delta|<397$ 经 Cauchy 分别给 $|\mathcal H_{pp}|<698800$、$|\mathcal H_{p\delta}|<7.94\times10^9$、$|\mathcal H_{\delta\delta}|<7.94\times10^{47}$。这是同域解析预算，无新高阶节点。

从 $B(f(\theta),\delta(\theta))=a(\theta)$ 作两次实方向微分。二阶项分别来自相位自身二阶导数、$B_{pp}p'p'$、两项 $B_{p\delta}p'\delta'$ 和 $B_{\delta\delta}\delta'\delta'$。其中 $B_{pp}=\delta\mathcal H_{pp}$，$B_{p\delta}=\mathcal H_p+\delta\mathcal H_{p\delta}$，$B_{\delta\delta}=2\mathcal H_\delta+\delta\mathcal H_{\delta\delta}$。

旧物理逆一阶界给两相位列模 $<2.974\times10^{-8}$、$<5.984\times10^{-8}$，所以 $\|Df\|<L=6.683\times10^{-8}$。相位二阶自身项是对角项：对两个单位实方向用 $|\xi_1\eta_1|+|\xi_2\eta_2|\le1$，其输出模 $<5.984\times10^{-8}$，不重复付两列之和。

记 $A_m=2.974\times10^{41}$、$d_m=1.415\times10^{-40}$。上述四组项的共同上界是自身项，加 $A_md_m(698800)L^2$，加 $2A_m(.03494+d_m\cdot7.94\times10^9)L\rho$，再加 $A_m(794+d_m\cdot7.94\times10^{47})\rho^2$。精确有理和 $<1.911788542\times10^{-7}$；统一可取 $M=2\times10^{-7}$。

另一方面，行列式模除以两列的 Frobenius 范数给最小奇异值下界；本轮有向预算 $>1.0346\times10^{-22}$，保守取 $\sigma=8\times10^{-23}$。这些是实二维奇异值，不是原 Gauss 对 a 的简单根导数。

在相位实球 $r=2\times10^{-16}$ 上，写 $f(\theta)=p_*+J\theta+R(\theta)$。$|R|\le Mr^2/2$，并且 $\|DR\|\le Mr$。对任意 $|z|\le8\times10^{-39}$，实映射 $T(\theta)=J^{-1}[z-R(\theta)]$ 的 Lipschitz 常数小于 .478，且像半径小于 $1.478\times10^{-16}<r$。Banach 因此给唯一局部相位解，结论是 $B(p_*,8\times10^{-39})$ 包含于双圆周像，从而包含于原产品真实像。

内圆很小，因为这张相位图几乎退化；它是存在与包含结论，不是新计算的每个根坐标。中心是准确函数定义的 $p_*$，旧绝对坐标精度不因此提高到 $10^{-39}$。

### Source lines 99–101

## 2026-10-07第3轮后继付款

上段“支持相位/坐标未求”是14:01当轮的历史边界。现在chapter_15_euler_second_true_support_phase_certificate (source record: `chapter_15_euler_second_true_support_phase_certificate`; not bundled)已在同一产品闭合真实相位/最右坐标；chapter_15_euler_second_true_support_geometry (source record: `chapter_15_euler_second_true_support_geometry`; not bundled)与chapter_15_euler_second_boundary_depth_and_inward_fiber (source record: `chapter_15_euler_second_boundary_depth_and_inward_fiber`; not bundled)付当前凸像、环面fold、改进内圆和准确内向纤维。主status仍reader-only pass1，无旧datum更新或范围扩张。下一fresh START occurrence4集中代表复盘1302/1401/1504；最近边界具体方向/坐标未求，详见2026-10-07-1504 (source record: `2026-10-07-1504`; not bundled)及state。
