# Pairwise correlation is not a block-negative-association proof

## Public reader preface

**Learning question and project role.** Reader-generated boundaries, after the source elementary subset example; preserve granular review versus pass-1 labels. A foundation-stage combinatorics reader extension. Elementary subsets and quantity vectors motivate deeper questions, but later book gates remain closed and the extensions are not counted as unread source coverage.

**Preparation.** Weighted fixed-size subsets, indicator covariance, increasing functions on coordinate blocks, conditional probability, and elementary generating polynomials.

**Historical scope and status.** The source note has granular historical grades: selected coupling/negative-association and counterexample subranges were reviewed, while several later extensions remain pass1/D3 pending. The excerpt retains that preface. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Pairwise correlation is not a block-negative-association proof. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The old basic layer constructions are reused. Pairwise negative correlation does not by itself prove a block statement; negative association does not by itself prove real-rootedness. The source elementary example is omitted from this short release.

**Source and editorial treatment.** Case ID: `BRUALDI-N1`. Historical source date: recorded in the source metadata. Original project record: `chapter02-section2.3-weighted-layers-negative-association.md`. Original-note SHA256: `582f4491242c5846e512a06e63c098555d59652659b36791bae43962a3575a98`. The short historical excerpts use source lines 3–5, 65–100, 133–148; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–5

来源只到 printed p27 / PDF p37 的 Pascal 具体说明；source-exposed reconstruction closed-reviewed，保留解释列表与旧尾句暴露。下面是具名读者问题链，独立证明与有限 guard 分开；不是原书后继定理或编号习题的完成。

选择性第二遍见本轮综合 (source record: `chapter02-section2.3-complement-layers-parity-synthesis.md`; not bundled)：Catalan LC、全覆盖边正的相邻层耦合、整块NA/实际支撑等号、LC滤子四量词/孔与几何严格性、旧三抽样规则、协方差分解、NA与实际宽度Newton失效已reviewed。坐标残余cover、MGF及未重做的附属链保持pass1/D3 pending；新条件两点、Hall/极限/二子式/秩单调性/倒数删除只算reader pass1。

### Source lines 65–100

## 两坐标公式与失败边界

两活跃坐标权 $u,v$，其余为 $R$。写 $a=e_k(R)$、$b=e_{k-1}(R)$、$c=e_{k-2}(R)$、$Z=a+(u+v)b+uvc$。则 $\operatorname{Cov}(X_i,X_j)=uv(ac-b^2)/Z^2$。$0<k<s$ 时严格负；确定层或零权坐标时为 $0$。

权 $(1,2,4)$、$k=2$ 的三对概率为 $1/7,2/7,4/7$。前两坐标包含概率 $3/7,5/7$，协方差 $-8/49$。

去掉乘积结构而保留固定大小可失败：四元素两子集，$\{1,2\},\{3,4\}$ 各 $3/8$，其余四对各 $1/16$；两前坐标边际各 $1/2$，协方差 $1/8>0$。任意混合正确的固定大小层也可失败：二坐标空集/全集各 $3/8$，两单点各 $1/8$，仍得 $1/8$。

全部子集直接按乘积权分布是独立 Bernoulli 坐标，不交块协方差为 $0$。失败的是任意层混合。

## 总数 filter：准确的保持条件

给 $a_0,\ldots,a_n\ge0$，不全为零，定义 $\nu(S)\propto a_{|S|}w(S)$。这里 $a_j$ 是每配置的 rank coefficient（总数系数），不是总数概率；总数概率还带 $e_j(w)$，等权时带 $\binom nj$。

读者命题：以下四项等价。(1) 正支撑是整数区间，且 $a_j^2\ge a_{j-1}a_{j+1}$；(2) 某一组严格正权下，每个正概率坐标指定条件后的分布都负关联；(3) 每组严格正权下原分布都负关联；(4) 每组严格正权下所有正概率坐标指定条件后都负关联。坐标指定条件仅指某些坐标必须选入、另一些必须不选，不包括任意事件。

充分性仍按 $J=|S\cap A|$ 分解。给定 $J=j$，$A$ 与整个补块 $D$ 独立，$A$ 服从 $\mu_j^A$；补块大小 $R$ 的条件概率为 $q_j(r)\propto a_{j+r}e_r(D)$。对 $r>s$，无孔对数凹性给 $a_{j+r+1}a_{j+s}\le a_{j+r}a_{j+s+1}$。若左边正，中间指标全处于正区间，可用递减比值；左边为零则直接成立。因此用交叉乘积处理零项，不除以零系数。

正规化后仍有 $q_{j+1}(r)q_j(s)\le q_{j+1}(s)q_j(r)$。对任意递增大小函数 $H$，两分布均值之差可按 $r>s$ 配对求和，每项为 $(H(r)-H(s))$ 乘这个非正差。故补块大小随 $j$ 按随机序下降。补块递增函数的固定层均值随大小递增，遂其条件均值 $G(j)$ 递减；$F(j)$ 递增。条件独立和前述协方差恒等式完成一般负关联。

坐标指定条件中，设必须选入的数量为 $p$，删除已定坐标后，系数成为截段 $a_{p+r}$。区间支撑和对数凹性保留，故所有正概率条件下都成立。这同时证明 (1) 推出 (4)。

必要性有两个不同证书。若局部对数凹性在 $j$ 失败，强制 $j-1$ 个坐标选入、$n-j-1$ 个不选，余下两个正权为 $u,v$。写 $Z=a_{j-1}+(u+v)a_j+uv a_{j+1}$，其协方差为 $uv(a_{j-1}a_{j+1}-a_j^2)/Z^2>0$，所以条件负关联失败。

长零洞不能只用局部不等式排除。取两个相邻正支撑指标 $\ell<u$，若 $u-\ell\ge2$，强制 $\ell$ 个选入、$n-u$ 个不选，余下 $u-\ell$ 个只能全空或全满，两者概率均正；任意两个剩余坐标的协方差为 $p(1-p)>0$。这些反例对任意残余正权有效，故 (2) 已推出 (1)。

最后，若 (3) 成立，任一正概率坐标指定条件可由正权极限取得：必须选入者乘 $T$，必须不选者乘 $T^{-1}$。最大 $T$ 次幂的配置恰好满足指定条件，$T\to\infty$ 时收敛于条件分布。有限空间的负关联不等式连续；严格正协方差也会在足够大有限 $T$ 时保留。因此 (3) 推出 (4)，四项等价。$n=0,1$ 的局部不等式为空，结论仍成立。

## 单组权的 NA 不能代替全部条件化

$n=3,w_i=1,a=(0,2,1,1)$，正规化为 $10$。单点均值 $1/2$，两点同选概率 $1/5$，三点同选概率 $1/10$。单点与另一单点协方差 $-1/20$；单点与余下 AND 的协方差为 $0$，与余下 OR 的协方差为 $-1/10$。

三坐标中不交非空块至少一块是单坐标；两个变量上的递增函数扣常数后可表示为单坐标、AND、OR 的非负线性组合。具体写 $u=f(10)-f(00)$、$v=f(01)-f(00)$、$d=f(11)-f(10)-f(01)+f(00)$。$d\ge0$ 时用系数 $u,v,d$ 乘单点、单点、AND；$d<0$ 时用 $u+d,v+d,-d$ 乘单点、单点、OR，单调性保证系数非负。因此上述三个检查证明此固定权原分布 NA。但 $a_2^2<a_1a_3$；条件 $X_1=1$ 后剩余两坐标质量为 $2,1,1,1$，协方差 $1/25>0$。

把第一坐标权改成 $t$，另两权为 $1$，正规化 $Z=5+5t$；后两坐标协方差为 $(t^2-2t-4)/Z^2$。所以 $t>1+\sqrt5$ 时已严格正；$t=4$ 给 $4/625>0$。外部权反例是有限具体值，不只是抽象极限。

### Source lines 133–148

## 负关联不等于计数多项式全实根

四元素等权、总数只准 $1,2,3$，系数 $a=(0,1,1,1,0)$ 无孔且对数凹，所以所有坐标指定条件下保留负关联。但计数多项式为 $P(z)=4z+6z^2+4z^3$；去零根后的二次因子 $4+6z+4z^2$ 判别式 $-28<0$。

其支持宽度为 $2$，对应 Newton 条件应为 $6^2\ge4\cdot4\cdot4$，实际 $36<64$；按原多项式实际次数 $3$ 也要求 $36\ge48$，同样失败。以环境大小 $4$ 归一化时，系数除以 $\binom4r$ 恰是无孔对数凹的 $a$，中间只要求 $36\ge36$。三种常数来源须分开；不能从负关联把以前实际次数根证书的结论迁移过来。

## 非负同向积与计数尾界

不交块上的非负递增函数，其乘积仍递增；全部递减时也同样，且两递减函数的协方差由同时取负仍非正。因此可迭代得到 $\mathbb E\prod h_i\le\prod\mathbb Eh_i$。非负性不能省，否则积的单调方向不保留。

对块计数 $Y=\sum_{i\in A}X_i$，令 $p_i=\mathbb EX_i$、$\mu=\sum p_i$。对任意有限实 $t$，正因子 $e^{tX_i}$ 同向，所以 $\mathbb Ee^{tY}\le\prod_i(1-p_i+p_ie^t)\le\exp(\mu(e^t-1))$。负 $t$ 时迭代原来的正递减因子，不把多个因子分别取负。

上尾取 $t=\log(1+\delta)$，指数界为 $-\mu((1+\delta)\log(1+\delta)-\delta)$，$\delta\ge0$。下尾事件 $Y\le(1-\delta)\mu$ 对负 $t$ 蕴含指数随机变量大于相应阈值；取 $t=\log(1-\delta)$，指数界为 $-\mu(\delta+(1-\delta)\log(1-\delta))$，$0\le\delta<1$。

$\delta=1$ 的下尾由 $t\to-\infty$ 得 $P(Y=0)\le e^{-\mu}$，保留乘积则有更精确 $\prod(1-p_i)$。$\mu=0$ 时 $Y=0$；固定层的实际范围是 $\max(0,k-|E\setminus A|)\le Y\le\min(k,|A|)$，范围外事件直接为零。这个尾界只用依赖不等式，不宣称实际坐标独立。
