# Approximation versus an exact Heegner certificate

## Public reader preface

**Learning question and project role.** Prefer an editorial case study of exact recognition, termination, inverse substitution, and withdrawn reader error; do not reproduce the cited deep theorem as an independent proof. An arithmetic certification and hypothesis-tracking example from Cohen Volume I, Chapter 8. The larger first pass remains unfinished, and Volume II remains gated.

**Preparation.** Binary quadratic forms, CM/Heegner constructions, rational reconstruction, elliptic heights, and the difference between a numerical estimate and an exact certificate.

**Historical scope and status.** The source note records reader/collaborative closed-pass1 for local algorithm repair, termination, rational recognition, and torsion clearing. Gross–Zagier and other deep inputs retain cited or conditional status. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Approximation versus an exact Heegner certificate. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The quoted height theorem, level-CM input, local height tables, BSD-derived estimates, and general twist nonvanishing are not independently proved here. An earlier conductor misreading is explicitly withdrawn. The example distinguishes conditional discovery from an eventual exact witness.

**Source and editorial treatment.** Case ID: `COHEN-N1`. Historical source date: 2026-10-15. Original project record: `2026-10-15-ch8-heegner-algorithm-certification.md`. Original-note SHA256: `d7915443c03a9cda5e906092726daf88b17e9b9583bd1d80b55c1f7327a454e0`. The short historical excerpts use source lines 3–5, 15–35; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–5

来源：Cohen I §§8.6.3–5、Thm8.6.9、Conj10、Alg11/Subalg12–13及改进，printed590–598/PDF615–623页图；615、619另240dpi核对。状态：GZ/扩展常数和局部高度表为cited/conditional；最小A算法修复、列表终止、有理识别、扭点清除为reader/collaborative closed-pass1。源实用精度与BSD估计不能冒充通用误差定理。来源作用约定与明确变量代换均已核，下面的方向反例为本地source-caveat，非官方errata。

直觉：CM互反律给出目标点确实有理，指数收敛级数给近似，最后还要一道有界分母识别把近似变回精确点。计算速度主要由CM点虚部控制；保持层结构的最小A问题是一个带互素约束的二维最短向量问题。

### Source lines 15–35

**列表算法的正确性和终止。** 固定可容许$\beta$，依次取$B=\beta+2Nk$，令$R=(B^2-D)/(4N)>0$。枚举$R$的正约数$d$，得到$(Nd,B,R/d)$；约化形式作为普通理想类的canonical键去重。2026-10-15-ch8-heegner-forms-and-trace (source record: `2026-10-15-ch8-heegner-forms-and-trace`; not bundled)已证明每个普通类有固定$\beta$的代表；Γ0中的整数平移可把其$B$变得足够大且非负。因此上面的$B$扫描最终会命中每类，达到可靠类数$h(D)$时终止。有限等待不是终止证明，真正依据是已补齐的存在性及有限类数。

**最小A的决定性公式。** 令$\tau=(-B+i\sqrt{|D|})/(2A)$，$N\mid A$。对$\gamma=(a,b;Nc,d)$有$\operatorname{Im}(\gamma\tau)=\operatorname{Im}\tau/|Nc\tau+d|^2$。设$u=-NB/(2A)$、$v^2=N^2|D|/(4A^2)$，则待最小化的正量是$m(c,d)=(cu+d)^2+c^2v^2$，约束$\gcd(Nc,d)=1$。$c=0,d=1$给初始界1；负$c$可同时反号，故只扫$c>0$。

当已有界$m_0$时，只有$c^2v^2<m_0$可能改善，故循环有限。固定$c$，应找距$-cu$最近且与$Nc$互素的整数$d$；普通最近整数不互素时不能直接跳过$c$。左右各向外搜索到首个可容许整数，再比较距离即可；因模$Nc$的一个完整剩余块总有单位，该步骤终止。全程可平方比较有理数，避免浮点L导致漏掉边界。

扩展Euclid补$ad-bNc=1$后，**必须输出逆代换**$f(dx-by,-Ncx+ay)$。其根正是$\gamma\tau$，首系数$A'=Ad^2-BNcd+CN^2c^2=Am(c,d)$。源PDF619 Step3字面输出$f(ax+by,Ncx+dy)$，其根却是$\gamma^{-1}\tau$，与前面最小化的目标不符；同页proof明确用了$\gamma\tau$，不能仅改抽象作用记号消除此变量代换冲突。

精确反例取$N=37,f=(3404,165,2)$，$D=-7$。$(c,d)=(1,1)$给$m=1/92$，可补$a=1,b=0$。因任意$Am=f(d,-Nc)$都是被37整除的正整数，$Am\ge37$，此候选达到下界，确为全局最优。正确逆代换给$(37,17,2)$；原字面正代换给$(12247,313,2)$，首系数反而增大。证书`../checks/2026-10-15-heegner-form-guard.py`验证此恒等式和57组小判别式/层/定向的列表与最小化，有限测试只辅助一般证明。

**近似不是有理点，精确回代才是。** 已有严格$H(P)$上界和高度差界便得$h_x(P)\le B$；因此既约分母$q_x\le e^B$。不同分母不超过$Q$的有理数相距至少$1/Q^2$，所以小于$1/(2Q^2)$的严格误差允许唯一有界分母识别。最小整Weierstrass模型另给$q_x=d^2$、$y$分母为$d^3$，但“分母是平方”只能加强过滤，不能替代识别误差界。候选$x$必须精确回代，判纵坐标判别式是否为有理平方，并检验非挠；某个连分数部分商很大不是单独的证明。

从$z\bmod\Lambda_E$传到$x=\wp(z)$时还须控制远离格点的距离和导数；固定“再加10位”是源实用建议，不是跨所有模型/判别式的误差定理。可用自适应区间先排除极点，再收紧到上述分母识别门。找到精确非挠点后，其有效性不再依赖用于发现它的BSD估计。

**分点与扭点。** 若已可靠知道整数$m=k/s$、$s=\sqrt{|\Sha|}$，令$e$为有理挠群指数，$\ell=\gcd(e,m^\infty)$、$m'=m\ell$。则$[\ell]P=[m'](sG)+[\ell]T$，而$[\ell]T$的阶与$m'$互素，所以存在有理挠点$T'$使$[m']T'=[\ell]T$。枚举$[m']$在复环面上的$m'^2$个逆像，必含$sG+T'$。Mazur给挠指数各素指数至多3，故$\ell=\gcd(e,m^3)$。这解释源分点步骤，而不是默认$P/m$已经有理。

若$m=u/v$约分是有理数，不能直接用“$0\le u,v<m'$”一类整数循环。可改用$\ell=\gcd(e,u^\infty)$，枚举$[u\ell]R=[v\ell]P$的逆像；同一素数逐项论证给$R=sG+T'$。但从任意浮点$m$恢复其精确分子分母仍需额外界。保守回退是直接识别迹点$P$，它可能更大，却不需要BSD分点系数。

**Cremona–Silverman分母识别。** 源局部高度表及$H(P)=2\log d+H_\infty(P)+\sum H_p(P)$作为引用，必须使用相同最小模型/高度约定。有限坏位的每个$H_p$只取一个有限列表中的值；未知$p\mid d$情形加入0。给定$x$的实区间、$H(P)$的严格区间与阿基米德高度算法，逐个列表组合便得到$d$的指数区间。收紧到每区间至多一个正整数，再由$n\approx d^2x$恢复分子、精确回代。这把分母平方结构真正用于识别；局部表的正确性未在本轮独立重证。

Atkin–Lehner改进只在exact divisors上作用，可能改变$\beta$并引入可算挠点平移；保定向和坐标平移不可略。CM trace加速复用此前Cornacchia/Jacobi可靠方法；非最大order不等PID的旧护栏继续保留。运行时间/“没有某种LLL识别法”等书内历史评论不升级为当前研究结论。
