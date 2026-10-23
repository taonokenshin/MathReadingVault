# Fibers, reciprocal counting, and actual geometric conditions

## Public reader preface

**Learning question and project role.** Reader-created extensions and counterexamples; omit the textbook source example in lines 8-14 when preparing a short showcase. A foundation-stage combinatorics reader extension. Elementary subsets and quantity vectors motivate deeper questions, but later book gates remain closed and the extensions are not counted as unread source coverage.

**Preparation.** Quantity vectors, finite-box inclusion–exclusion, lattice-point counting, polynomial weights, half-open decompositions, and the effect of forgetting labels on fiber sizes.

**Historical scope and status.** Recorded as a selected review, with only named reworked branches reviewed. New coordinate-class, moment, residue, and arithmetic-face auxiliary arguments remain reader closed-pass1/D3 pending. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Fibers, reciprocal counting, and actual geometric conditions. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The full finite-box/facet arguments and earlier source examples are outside this short excerpt. General unimodality, real-rootedness, spectral questions, and unreviewed branches are not closed; no Stage 1 completion or later-book permission is inferred.

**Source and editorial treatment.** Case ID: `BRUALDI-N2`. Historical source date: recorded in the source metadata. Original project record: `chapter02-section2.5-count-box-synthesis.md`. Original-note SHA256: `be8f9eeccb7e8e2ed16940328fac2c9337af74c08c3aad887840eda50f1db654`. The short historical excerpts use source lines 3–6, 103–158; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–6

- status: `selected-review-completed`; 只有本轮重做且比较过的分支选择性 `closed-reviewed`。
- run: 2026-10-05-0106 (source record: `2026-10-05-0106`; not bundled)。
- source: Brualdi Theorem 2.5.1，PDF p.42 y620–1385；下界例与有限库存模型，PDF p.44 y0–810。先遮旧解重构再窄核；不打开 p.44 y810 以下新来源。
- scope: 数量向量的基本双射/真实纤维，有限箱有效容斥与加权/余数反射，代表性整基底与实际面的平移逆向。没有章节 architecture、后阶段来源或 gate completion。

### Source lines 103–158

## 动态追加：同一个平移如何约束多项式矩

初始代表步骤已可靠闭合，时间仍充足，故只追加一个连接本页两个机制的新问题：单位面距平移对加权坐标矩有什么含义？这不是旧结果 reviewed，而是本轮新辅助 `closed-pass1`。

先取平移点 $q\in sP$，记 $a=q/s$。对次数 $p$ 的齐次多项式 $f$，令 $F_f(t)$ 是闭整数点上 $f(x-ta)$ 的和。权在坐标与尺度中是总次数 $p$ 的多项式；有效容斥及二项式基底同样给次数至多 $d+p$ 的计数多项式。这里的中心 $a$ 是平移决定的点，未假定它等于实数重心。

内部点写成 $x=q+y$、$y\in(t-s)P$ 时，$x-ta=y-(t-s)a$，所以内部中心矩是 $F_f(t-s)$。对坐标与尺度同时反射，$f(-x+ta)=(-1)^pf(x-ta)$，加权互反遂给 $F_f(-t)=(-1)^{d+p}F_f(t-s)$。这在整数正尺度成立，因两边为多项式，便成为恒等式。改写为 $F_f(-t-s)=(-1)^{d+p}F_f(t)$；以 $u=t+s/2$ 为新参数后，$F_f(u-s/2)$ 只有与 $d+p$ 同奇偶的幂。这约束多项式，不声称每个尺度的组合分布关于 $a$ 对称。

单位线段例 $d=1,s=2,a=1/2$：一次中心矩恒零，但二次中心矩是 $t(t+1)(t+2)/12$。改用 $u=t+1$ 后变成 $(u^3-u)/12$，与 $d+p=3$ 的奇性相符。两条独立检查分别是配对 $j\leftrightarrow t-j$、普通平方和减去中心项。

非对称例 $c=(2,2,4),r=3$ 中 $d=2,s=1,a=(1,1,1)$。$L(t)=(7t^2+7t+2)/2$；第一坐标的中心一阶矩不是零。自由前两坐标从 $[0,2t]^2$ 中剔除 $x_1+x_2>3t$ 的角：整方形的中心和为零，被剔除角经 $y_i=2t-x_i$ 变成总量至多 $t-1$ 的弱二坐标组合。其第一中心和为 $\sum_{v=0}^{t-1}(tv-v(v+1)/2+t)$，等价于 $t(t+1)(2t+1)/6$。故 $F_{x_1}(t)=-t(t+1)(2t+1)/6$，第二坐标相同，第三坐标是其反向两倍；以 $u=t+1/2$ 表示，第一式为 $-(u^3-u/4)/3$，确为奇多项式。

直接点数也核查该式：$t=1$ 时 $L=8$、第一坐标和为 $7$，中心和 $-1$；$t=2$ 时第一坐标五个可能值的纤维为 $5,5,5,4,3$，加权和 $39$，中心和 $39-2\cdot22=-5$。面距平移/回文成立，却没有“每个坐标关于 $tq/s$ 组合对称”的结论；中心矩能识别这个差别。一般高矩、根性质或谱不在本次新辅助中宣称。

同一五边形还可算两项二阶中心和。记 $v=t(t+1)$，第一坐标平方和为 $v(13v+4)/12$，前两坐标的交叉和为 $-v(5v+2)/24$。证明仍只剔除三角角区：角区点数 $v/2$，第一坐标和 $t(t-1)(t+1)/6$，平方和 $t^2(t^2-1)/12$，交叉和 $\binom{t+1}{4}$；展开 $(t-y_i)^2$ 与 $(t-y_1)(t-y_2)$ 后减去完整方形。平方中心和在 $t=1,2$ 为 $5,41$，交叉中心和为 $-1,-8$，与逐纤维手算一致。因为中心均值不为零，实际协方差还需减去均值乘积；不把未归一化中心和叫作 covariance。

相应多项式系列也有精确反射。把 $F_f(t)$ 的生成式写为 $K_f(z)/(1-z)^{d+p+1}$，多项式负参数的逐基底反射给 $K_f(z)=z^{d+p+1-s}K_f(z^{-1})$。这里是带可能前导零的反射，不把分子最高次误当作反射中心。非对称例的一次中心分子是 $-z-z^2$，反射次数 $3$；二次平方分子是 $5z+16z^2+5z^3$，交叉分子是 $-z-3z^2-z^3$，反射次数均为 $4$。负系数来自有符号权，不与普通计数 $H$ 的非负性混淆。这些是当前同一箱模型的新矩接口，不关闭一般加权谱或一般根问题。

作为系数自测，普通 $L(t)$ 的前两系数为 $\alpha,\beta$ 时，反射给 $\beta=ds\alpha/2$。原始一次矩 $M_i(t)$ 的前两系数为 $\alpha_i,\beta_i$ 时，中心反射给 $\beta_i=(d+1)s\alpha_i/2-q_i\alpha/2$。非对称例中 $\alpha=\beta=7/2$，$\alpha_1=19/6,\beta_1=3$，恰好匹配。自由二维区域的实数面积为 $7/2$，第一坐标积分是完整方形的 $4$ 减去角三角形的 $5/6$，因此归一化实数重心坐标为 $19/21$，而 $q_1/s=1$。真实重心、平移点与组合分布中心仍是不同概念。

最后一个精确非齐次类检查：线段的相反类 $(2,2)\bmod3$ 在 $t=3a+1$ 时写 $x_1=3u+2,x_2=3v+2$、$u+v=a-1$。权 $g=1-x_1+x_2^2$ 的分支和为 $3a^3$；未反射权 $f=1+x_1+x_2^2$ 的和为 $3a^3+3a^2+a$。在 $t=-2$ 即 $a=-1$ 处分别是 $-3,-1$；乘维数符号后只有前者给目标内部权 $3$。这是直接等差与平方和计算，不能靠“换一个记号”省去奇次项的反射。

## 同一半开室的余数分子：只做代表性配对

接续动态新矩问题，用已经亲自重做的整基底室核查余数配对。某室基底系数条件为 $\lambda_j\ge\varepsilon_j$，$\varepsilon_j$ 取 $0$ 或 $1$。唯一写成 $\lambda_j=\varepsilon_j+\mu_j+mn_j$，其中 $0\le\mu_j<m$、$n_j\ge0$；空间余数为 $\sum_j(\varepsilon_j+\mu_j)v_j$，尺度为 $\sum_j(\varepsilon_j+\mu_j)+m\sum_jn_j$。把有限代表按余数 $B$ 汇总成 $H_B(z)$，就得闭系列 $H_B(z)/(1-z^m)^k$。

反向室把严格坐标互补，再令 $\mu'_j=m-1-\mu_j$，于是新代表系数是 $m-(\varepsilon_j+\mu_j)$；尺度补到 $km$，空间余数变成 $-B$。因此内部 numerator 为 $z^{km}H_{-B}(z^{-1})$。若实际面距平移成立，内部余数系列又是 $z^s$ 乘类 $B-Q$ 的闭系列，故 $H_B(z)=z^{km-s}H_{-B-Q}(z^{-1})$。这只重做代表性配对接口；一般阈值、密度与真实最小周期仍不在 reviewed 范围。

类自配对的指标条件是 $2B\equiv-Q\pmod m$。即使如此，分子可能有前导零：若首项在 $z^a$，末项在 $z^b$，它们满足 $a+b=km-s$；去掉 $z^a$ 后才是通常意义、次数 $b-a$ 的回文。两个不同类的分子也可能偶然相同，不等于指标自配对。

单位线段在 $m=3$ 时更直观：闭基底代表就是两坐标余数，$H_{(b_1,b_2)}=z^{b_1+b_2}$；$s=2,Q=(1,1)$，类配对为 $(b_1,b_2)\mapsto(2-b_1,2-b_2)$，指数补到 $4$。唯一自配对类 $(1,1)$ 的分子是 $z^2$；类 $(0,2)$ 与 $(2,0)$ 虽有相同分子，却是相互配对。该自配对类在尺度 $t=3a+2$ 的点满足 $x_1=3u+1,x_2=3v+1,u+v=a$；二次中心和为 $3a(a+1)(a+2)/4=(t-2)(t+1)(t+4)/36$，与尺度反射 $t\mapsto-t-2$ 的奇号一致。

两室正方形 $c=(2,1,1),r=2,m=3$ 给更实质的共享边界检查。右室三个顶点为 $(2,0,0),(1,1,0),(1,0,1)$，全部坐标闭；左室为 $(0,1,1),(1,0,1),(1,1,0)$，第一基底坐标开。对 $B=(b_1,b_2,b_3)$，右室代表为 $\mu_1=b_2,\mu_2=b_3$、$\mu_0\equiv2(b_1-b_2-b_3)\pmod3$。左室代表为 $\mu_0\equiv2(b_2+b_3-b_1-2)$、$\mu_1\equiv b_3-1-\mu_0$、$\mu_2\equiv b_2-1-\mu_0$；全部取 $0,1,2$ 代表。对应两个指数分别是 $\sum\mu$ 与 $1+\sum\mu$。这把真实开放端点的 $1$ 留在了同余式中。

这里 $s=2,Q=(2,1,1)$，指数配对中心为 $km-s=7$。类 $000$ 的分子是 $1+z^3$，其配对类 $122$ 是 $z^4+z^7$；自配对类 $211$ 是 $z^2+z^5$。此外 $012$ 与 $021$ 同有 $z^3+z^6$，但分别配对 $110$ 与 $101$，后两者均有 $z+z^4$。这些具体手算保留“相同数值”和“真实指标配对”的区别。全 $27$ 类的有限枚举只检验这个两室例，不作为所有模数或所有箱切片的新分类。

未加权余数质量还有一个简短算术解释。累计坐标增广格到空间坐标的变换行列式为 $r$；每个增广室基底行列式为 $\pm1$，故其空间顶点矩阵的行列式绝对值为 $r$。它生成的格恰为总和可被 $r$ 整除的空间整数格：包含关系显然，两边指数同为 $r$。模 $m$ 后，“空间类 $B$ 加尺度类 $\tau$”可达当且仅当 $r\tau\equiv\sum_i B_i$；增广整基底使每个这种二元数据恰有一个代表。

记 $g=\gcd(r,m)$、$T$ 为室数。可达空间类当且仅当 $g\mid\sum_iB_i$，每类有 $g$ 个允许的尺度类，每个室在每个允许尺度类中恰贡献一个代表。所以 $H_B(1)=gT$，但单个尺度分支的首项系数只是 $T/(m^d d!)$，不能再乘一次 $g$。这个结论仅关于未加权分子质量，不移植到有符号中心矩分子。

质量相同不使有限计数相同。单位线段模 $2$ 的 $H_{00}=1,H_{11}=z^2$ 都有质量 $1$，但尺度 $2$ 的计数为 $2,1$。两室正方形模 $2$ 只允许总和为偶数的四类；$H_{000}=1+z+z^2+z^3$、$H_{011}=z+z^2+z^3+z^4$，各质量 $4$。它们的自由两坐标计数分别为 $(\lfloor t/2\rfloor+1)^2$ 与 $\lceil t/2\rceil^2$；前两者并不有限均匀。另两类 $101,110$ 同有 $z+2z^2+z^3$，相互配对却没有指标自配对。所有允许尺度分支的首项仍为 $t^2/4$。这是新逐坐标质量辅助；旧标量余数最短阈值/周期分类保持原状态。

## 同一实际面判据的算术消元与源例压力

下面只是把已重做的实际面条件消去 $q$，属于新辅助 pass1，不新增来源定理。限定 $k\ge3$，令 $m_0=\min(r,C-r)$、$M_0=\max(r,C-r)$。容量至少 $M_0$ 的坐标至多一个，否则加上其他正容量会使总容量超过自身。

若没有这种坐标，先用补集令 $r\le C/2$。每个下界都实际成面，故全部 $q_i=1$，从总量得 $sr=k$。同时双面指标恰是 $c_i<r$，要求 $sc_i=2$；只成下界的坐标没有新条件。反向这些等式直接满足全部实际面的单位高度。补回另一半总量，统一条件为 $sm_0=k$，并对所有 $c_i<m_0$ 要求 $sc_i=2$；$r\ge C/2$ 时用 $q_i=sc_i-1$。中间等量情形的两种表达一致，因为正容量与这些条件迫使每坐标双面。

若有唯一大坐标 $e$，其余容量和至多 $m_0$；由于至少还有两项正容量，其余每项都严格小于 $m_0$，所以全部双面，要求 $sc_j=2$。整数 $s$ 只可能为 $1$ 或 $2$，对应其余容量全为 $2$ 或全为 $1$。大坐标由 $q_e=sr-(k-1)$ 确定；原不等式保证它严格在容量之间。自由其余坐标实际就是一个完整箱子，故这是不同边长能否共享同一单位内点尺度的问题。

源容量 $(2,1,3)$、总量 $3$ 正好是这种大盒情形。前两坐标独立在 $\{0,1,2\}$ 与 $\{0,1\}$ 中选择，第三坐标是 $3-x_1-x_2$；故六个数量向量既可由容斥 $10-1-3=6$，也可由矩形 $3\cdot2=6$ 得到。同步计数 $L(t)=(2t+1)(t+1)$，分子 $H=1+3z$ 不回文：前两实际双面分别要求 $2s=2$ 与 $s=2$，不能共享 $s$。这不妨碍均匀数量法则中前两坐标独立；独立与面距平移仍是不同性质。源六项列表历史 source-exposed 状态保留，本轮不另作其 source reviewed promotion。

该六态最适合核查纤维。按源顺序 $210,201,111,102,012,003$，词纤维是 $(3,3,6,3,3,1)$，总数 $19$；标签库存子集纤维是 $(1,3,6,6,3,1)$，总数 $20$；数量法则则六态各 $1/6$。这些不是三种计算同一均匀样本。均匀数量下 $\operatorname{Cov}(X_1,X_2)=0$；均匀词下是 $-24/361$；均匀标签子集下是 $-1/10$。

进一步直接枚举三步前向路径，检验“只在尚未耗尽的类型中公平选下一类”的失败。十九个词的概率按路径当前可选类型数相乘，汇总六态为 $(21,14,38,12,19,4)/108$；例如 $210$ 的三条路径概率是 $1/18,1/18,1/12$，并不恒定。前两次数的协方差为 $-5/81$。若改成在未耗尽类型中按当前次数加 $1$ 强化，六态为 $(5,3,4,2,4,2)/20$，也不等于条件化无界 urn 得到的均匀数量法则，协方差为 $-3/200$。正确处理有限库存需未来完成数或全局拒绝条件化；局部删掉违规选项不保留旧 urn 的纤维抵消。这里只闭合指定三步例的纸面路径，不关闭一般抽样链谱。
