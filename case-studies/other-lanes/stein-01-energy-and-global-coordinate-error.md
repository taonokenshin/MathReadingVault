# Energy rigidity does not give global coordinate closeness

## Public reader preface

**Learning question and project role.** Reader-generated counterexample family; link the reused energy identity as an external dependency within the project. A reader extension of the Complex Analysis lane. It uses established local mechanisms to test when a proposed global interpretation is justified, while keeping the Fourier book and earlier proof grades separate.

**Preparation.** Univalent functions, normalized conformal maps, Green functions, Dirichlet energy, and compact versus whole-domain convergence.

**Historical scope and status.** Recorded as reader first proof / peer-audited. It is a project-authored extension, not a newly numbered source theorem or a whole-chapter reviewed claim. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Energy rigidity does not give global coordinate closeness. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The earlier sharp-covering energy identity and the same normalized family are reused. A missing dependency is identified by its original record basename. The excerpt does not assert general boundary regularity or convert near-extremality into uniform global coordinate convergence.

**Source and editorial treatment.** Case ID: `STEIN-N1`. Historical source date: 2026-10-13. Original project record: `2026-10-13-energy-rigidity-and-global-coordinate-failure.md`. Original-note SHA256: `1eab8fad97d2798b3a8ed18747f05d8f2ef0fcf5baf5dc6a1b808cf9fff1f650`. The short historical excerpts use source lines 33–100; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 33–100

## 全盘函数误差：sharp上界其实一直是2

对每个固定 $t\in(0,1)$，归一化单射自映射类都有

$$
\sup_g\sup_{z\in D}|g(z)-z|=2.
$$

上界是圆盘内三角不等式，单个内点严格小于2；下面有单个合法 $g$ 的sup恰为2。因此即使 $t\uparrow1$，也没有趋零的全盘函数误差界。已有radial-slit的平方根反例只给一个特定族的下界，未曾证明全类全盘 $O(\sqrt{1-t})$；本稿明确阻止误用。

令 $\tau=-\log t$、$\omega=\pi/\tau$、$\kappa=(1-i\omega)/(1+i\omega)$，故 $|\kappa|=1$、$\kappa\ne-1$。定义 $p(z)=(\kappa+z)/(\kappa-z)+i\omega$。圆盘中 $\operatorname{Re}p=(1-|z|^2)/|\kappa-z|^2>0$，且 $p(0)=1+i\omega$。取直接ODE

$$
\partial_sY_s(z)=-Y_s(z)p(Y_s(z)),\qquad Y_0(z)=z.
$$

模平方导数为 $-2|Y_s|^2\operatorname{Re}p(Y_s)\le0$，故每个源紧盘的轨道始终留在该盘，普通Picard可全时续接。解析初值依赖给全纯；若两个初值在某时同像，倒向比较两条已经存在的轨道并用唯一性，给初值相同。因此 $Y_s$ 是单射圆盘自映射，不要求全圆盘存在倒向flow。

零点线性化给 $Y_s'(0)=e^{-(1+i\omega)s}$。定义 $g(z)=e^{i\omega\tau}Y_\tau(z)=-Y_\tau(z)$，便有 $g(0)=0$、$g'(0)=e^{-\tau}=t>0$。

现在真正核边界分支。因为 $p(-1)=0$，$Y_s(-1)=-1$ 是ODE的一条常数轨道。向量场在 $-1$ 的邻域全纯，极点 $\kappa$ 与它隔开；有限时间区间用Gronwall选择足够小初值邻域，使所有轨道留在这个邻域。Picard故给 $Y_\tau$ 在 $-1$ 附近的全纯延拓。于是 $g(-1)=1$，沿盘内 $z=-r\to-1$，$|g(z)-z|\to2$。

使用的是这条显式局部延拓，未把单位圆点当作原定义域，也未宣称所有boundary点有连续值。复导数在该点还可精算：$p'(-1)=(1+\omega^2)/2$，向量场导数同值，故

$$
g'(-1)=-\exp\left(\frac{\tau+\pi^2/\tau}{2}\right).
$$

对 $t\uparrow1$，这一局部边界导数增长极快；紧集Cauchy仍给每个固定内盘导数趋1，二者并不矛盾。这是可检查的端点风险，不是“所有单射族的导数都发散”。

## 同时移动参数和源点，直接达到直径量级

上面的每个固定 $t$ 先取boundary极限已足以证明sup为2；下面另付一个联合极限，避免把两次极限交换。记 $d=|\kappa+1|=2/\sqrt{1+\omega^2}$、$\eta=d/4$，在 $B(-1,\eta)$ 内有 $|\kappa-z|\ge3d/4$。所以 $|p'(z)|\le32/(9d^2)$；由 $p(-1)=0$，还得 $|p(z)|\le8/(9d)$。向量场 $V=-zp$ 故可取Lipschitz常数 $L=8/d^2$。

取真实盘内点 $z_\tau=-1+\epsilon_\tau$，其中 $\epsilon_\tau=\eta e^{-2L\tau}$。与固定轨道 $-1$ 比较，首次出邻域前Gronwall给 $|Y_s(z_\tau)+1|\le\epsilon_\tau e^{Ls}$；右端在 $0\le s\le\tau$ 小于 $\eta$，故轨道不能首次出邻域。于是

$$
|g(z_\tau)-z_\tau|\ge2-\eta e^{-L\tau}-\epsilon_\tau\longrightarrow2.
$$

这里 $\eta\asymp\tau$、$L\tau\asymp1/\tau$，选择的源点离边界约为 $\tau e^{-C/\tau}$。这只是显式充分尺度，未宣称最佳过渡宽度。它同时证明 $t\uparrow1$ 与源点向boundary移动时确有直径量级位移。

## 同一族的固定内盘切向极限

令 $G_s=e^{i\omega s}Y_s$，则 $G_0(z)=z$、$G_\tau=g$，而旋转坐标消去常数虚部：

$$
\partial_sG_s=-G_sP_s(G_s),\qquad P_s(w)=\frac{\kappa e^{i\omega s}+w}{\kappa e^{i\omega s}-w}.
$$

在固定 $|z|\le r<1$ 上，$|G_s(z)|\le r$，$|P_s|\le(1+r)/(1-r)$，$|P_s'|\le2/(1-r)^2$。先由积分方程得 $G_s-z=O_r(s)$，再代回一次，得 $g(z)=z-\tau z\overline P_\tau(z)+O_r(\tau^2)$；这里横线表示时间平均，不是复共轭。

作变量 $\theta=\omega s$，平均为 $\pi^{-1}\int_0^\pi(\kappa e^{i\theta}+z)/(\kappa e^{i\theta}-z)\,d\theta$。由于 $\kappa=-1+O(\tau)$，固定紧盘上的平均误差为 $O_r(\tau)$。逐项积分在紧盘上一致收敛的几何级数，偶数次项消失，奇数次项系数为 $4i/(\pi n)$，故极限为

$$
p_*(z)=1+\frac{2i}{\pi}\log\frac{1+z}{1-z},\qquad g(z)=z-(1-t)zp_*(z)+O_r((1-t)^2).
$$

log取Cayley右半平面的解析支，零点值为0。其辐角在 $(-\pi/2,\pi/2)$，故 $0<\operatorname{Re}p_*<2$、$p_*(0)=1$。因此这族具有确定而温和的紧集切向；这个事实完全不控制上一节指数窄的boundary层。

还可对二阶项作独立常数检查。写 $G_s=a_1(s)z+a_2(s)z^2+\cdots$，则 $a_1=e^{-s}$，$a_2'=-a_2-2\kappa^{-1}e^{-(2+i\omega)s}$。积分至 $\tau$，使用 $e^{-i\omega\tau}=-1$，得到

$$
c_2(g)=-\frac{2t(1+t)}{1-i\omega},\qquad \frac{|c_2(g)|}{2t(1-t)}=\frac{\coth(\tau/2)}{\sqrt{1+\pi^2/\tau^2}}\longrightarrow\frac2\pi.
$$

该比值严格小于1：平方后只需 $\tau/\sinh(\tau/2)<\pi$，而左边小于2。小参数展开也给 $c_2/(1-t)\to-4i/\pi$，与 $p_*$ 的一次项相符。于是最佳二阶系数界、紧集切向与全盘位移2可以在同一显式单射族中逐项共存。
