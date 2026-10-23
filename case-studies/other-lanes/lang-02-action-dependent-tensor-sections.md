# Equal-length tensor kernels and action-dependent sections

## Public reader preface

**Learning question and project role.** Reader examples and failure boundaries; avoid implying a general classification or a new source theorem. A local reader-generated module problem beside Lang Chapter XVII §7. Explicit relations and coefficient constraints are used to test the limits of structural slogans about tensor kernels and endomorphism rings.

**Preparation.** Rank-one torsion-free modules, fractional ideals, endomorphism rings, tensor right exactness, and the distinction between one-sided module splittings.

**Historical scope and status.** Recorded as an independent first-pass reader proof with only the already-read Lang page as source support. Original theorem and hard-packet grades remain unchanged. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Equal-length tensor kernels and action-dependent sections. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The actual relation module, named examples, and the chosen action determine each section statement. Equal length, Frobenius structure, or a perfect pairing is not silently substituted for a module isomorphism or a splitting theorem.

**Source and editorial treatment.** Case ID: `LANG-N2`. Historical source date: 2026-10-05. Original project record: `2026-10-05-xvii7-nonmonomial-ideal-tensor.md`. Original-note SHA256: `456d981a3a51455f9eca868dad86e84502a6caa77e976f97e0c66a1b2757c8c4`. The short historical excerpts use source lines 3–5, 85–142; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–5

状态：独立第一遍 reader proof；来源支持仅 Lang printed660 / PDF669。原书 Theorem7.1 的 closed-reviewed 等级及全部既有 hard packets 保持原样。本笔记不是新编号定理的来源闭合，也不是集中 synthesis。各计算先独立完成、保存 scratch，后核对该单页。旧详细证明全程遮住。

直觉：把分式理想写成“一个单位生成元加一个非单项式生成元”，不能再按指数是否出现来判断成员资格；同一元素中不同次数的系数会互相约束。真正的张量核来自实际关系模。两个因子上的端环作用虽然交换，也可能给同一核不同的作用与不同的分裂结论。

### Source lines 85–142

## 5. 真正的失败边界：$(4,7)$ 反例

取 $A=k[t^4,t^7]$、$f=t+t^2$。$J$ 的一次与二次、五次与六次系数分别相等，三次系数为零；其余至少七次项自由。因此 $D=k+kt^4+t^7S$。令 $p=t^{11}-t^{12}$、$r=t^{14}$，有 $Q=(p,r)A=kp+kr+k(t^{15}-t^{16})+t^{18}S$。

这里 $Q$ 的 $D$-逆为 $t^{-11}[k(t^4+t^5+t^6)+t^7S]$。更精确地，$Q(D:Q)=kt^4+t^7S=\mathfrak m_D$：用 $p t^{-11}(t^4+t^5+t^6)=t^4-t^7$，再由 $t^7(1-t)S+t^{10}S=t^7S$ 得到等号。不能生成 $1$，所以 $Q$ 不可逆。前两个正例的有限证书模板到这里停止。

$I=QJ=kt^{11}+kt^{12}+kt^{14}+kt^{15}+kt^{16}+t^{18}S=(A:D)$，所有特征相同。草稿一度只取 $fp$、$fr$，误以为特征 $2$ 缺失一个像向量；加入 $f(pt^4)=t^{16}-t^{18}$ 后，$t^{16}$ 与 $t^{15}$ 均出现，疑似特征分支消失。这项修正来自实际生成元检查。

$N=k(t^{14}-2t^{15}+2t^{16})+t^{18}S$。$P$ 的低次基为 $p^2,t^{25}-t^{26},t^{26}-2t^{27},t^{28}$，尾部为 $t^{29}S$；故 $K$ 长度 $8$，$A/I$ 长度 $4$，$D/I$ 长度 $8$。取 $w=[t^{14}-2t^{15}+2t^{16}]$，再加 $[t^{18}],[t^{19}],[t^{20}],[t^{21}],[t^{23}],[t^{24}],[t^{27}]$，得到八个基向量。关系为 $[t^{22}]=2[t^{23}]-[t^{24}]$、$[t^{25}]=[t^{26}]=2[t^{27}]$、$[t^{28}]=0$，特征 $2$ 也独立。

用 $x=t^4,y=t^7$ 检验可得 $K$ 的 top 和 socle 各三维。$A/I$ 的基为 $1,x,x^2,y$，socle 由 $x^2,y$ 张成，所以 $K$ 不是 $(A/I)^2$；甚至 top 的维数 $3$ 与 $2$ 已不相等。可逆性与自由核公式不能从前两个算例推广。

可以给出更强的具体分类。记 $C=A/I=k[x,y]/(x^3,xy,y^2)$，并把七个纯次数核类依次记为 $a,b,c,d,e,f,g$，次数为 $18,19,20,21,23,24,27$。令 $h=xw=a-2b+2c$、$j=yw=d-2e+2f$。$Cw$ 的基为 $w,h,f,j$，因 $xh=f$、$yh=xj=yj=0$，它同构于 $C$。

再令 $b'=b-2c+2h$、$c'=c-h$。四个向量 $b',c',e,g$ 在 $K/Cw$ 中独立，且 $xb'=e$、$xe=g$、$yc'=g$，其余必要作用为零。因此它们组成的补模同构于 $\operatorname{Hom}_k(C,k)$：分别对应 $x^2,y,x,1$ 的对偶向量。于是 $K\simeq C\oplus\operatorname{Hom}_k(C,k)$。在这里 $C$ 的 socle 二维，不能把 $k$-dual 当成 $C$；前两个正例中 $C$ 的 Frobenius 性与 $K\simeq C^2$ 相容，但尚未把这写成对全部二生成元理想的一般定理。

在 $A$ 和 $D$ 的零点局部，$J,Q$ 都需两个最小生成元，$I$ 需三个，$K$ 也需三个。$T$ 在 $A$ 及两个 $D$-作用下的 top 都是四维：张量取相应因子的 top 后，另一因子再模掉残余极大理想即可。若 $T\to I$ 分裂，top 应有 $3+3=6$ 维。因此这里连 $A$-截面也不存在，两个 $D$-截面同样不存在。这个反例适用于每个特征。

### 一个相邻失败例使核变成循环模：$(4,9)$

追加 $A=k[t^4,t^9]$、$f=t+t^2$，只检验相同机制。系数约束给出 $J=k+kf+kt^4+kt^4f+t^8S$、$D=k+kt^4+t^8S$。令 $p=t^{17}-t^{18}$，则 $Q=(t^{16},p)A=kt^{16}+kp+kt^{20}+kt^4p+t^{24}S$。检验两个生成元可得 $(D:Q)=t^{-8}S$，故 $Q(D:Q)=t^8S$，仍不可逆，而且这次 trace 严格小于 $\mathfrak m_D$。

$I=(t^{16},t^{17},t^{18})A$，其低次为 $16,17,18,20,21,22$，尾部为 $t^{24}S$。$fp=t^{18}-t^{20}$ 保证这些次数在所有特征都出现。$N$ 的两个低次向量为 $n=t^{16}-2t^{17}+2t^{18}$、$t^4n$，尾部为 $t^{24}S$。$P$ 的低次向量为 $t^{32},t^{33}-t^{34},t^{34}-2t^{35},t^{36},t^{37}-t^{38},t^{38}-2t^{39}$，尾部为 $t^{40}S$。因此 $K$ 长度 $12$，$C=A/I$ 长度 $6$，$D/I$ 长度 $12$。

现在 $C=k[x,y]/(x^4,y^2,x^2y)$，其中 $x=t^4,y=t^9$，socle 由 $x^3,xy$ 张成。$Cn$ 的六个基向量是 $n,xn,x^2n,x^3n,yn,xyn$。后四个分别为 $[t^{24}-2t^{25}+2t^{26}]$、$[t^{28}-2t^{29}+2t^{30}]$、$[t^{25}-2t^{26}+2t^{27}]$、$[t^{29}-2t^{30}+2t^{31}]$。

补模可以直接取 $[t^{27}],[t^{31}],[t^{35}],[t^{39}],[t^{26}-2t^{27}],[t^{30}-2t^{31}]$。前四项组成 $x$ 链，后两项组成另一条长二的 $x$ 链；$y$ 把后两项分别送到 $[t^{35}],[t^{39}]$，其他必要作用为零。这正是 $C^*$ 对偶基的作用表。各向量在 $K/Cn$ 中独立，因此又有 $K\simeq C\oplus C^*$，作为 $A$-模 top 三维，socle 三维。

但这次两个 $D$-作用都把核变成循环模！模掉 $\mathfrak m_AK$，top 可用 $n,[t^{27}],[t^{26}-2t^{27}]$ 表示。第二作用的 $t^{10}n$、$t^{11}n$ 分别给出后两个 top 类。第一作用的 $t^{10}$ 为乘 $-(t^8+t^{10})$，$t^{11}$ 为乘 $t^9-t^{11}$，同样给出两个类的相反数。于是两种作用下均由 $n$ 生成 $K$；$I$ 杀死 $K$ 且长度相同，故分别有 $K\simeq D/I$。

这一同构仍不使评价正合列分裂。作为 $A$-模，$T$ 的 top 四维，$I$ 与 $K$ 的 top 各三维，分裂将给六维。任一 $D$-线性截面也必是 $A$-线性截面，所以两个 $D$-截面均不存在。特征 $2$ 时两个作用甚至在核上也不相等：$t^{10}$ 的作用差为 $-t^8-2t^{10}$，此时仍由非零的 $t^8n=x^2n$ 检出。主算例的特征 $2$ 相等现象不能推广。

两种核作用可精确由 $D/I$ 的 involution 联系：它固定 $t^4,t^9$，把 $t^{10}$ 送到 $-t^8-t^{10}$，把 $t^{11}$ 送到 $t^9-t^{11}$。第二作用忠实，第一作用的这些公式因而给出保留全部关系的代数映射；在四个生成元上再作用一次即为恒等，所以是 involution。特征 $2$ 时它仍非平凡，因为 $t^8,t^9$ 在 $D/I$ 中非零。同构类型、同一向量上的作用和正合列分裂是三项独立问题。

### 为什么此处必须区分 $C$ 与 $C^*$

对当前有限维局部交换代数 $C$，$C^*$ 的 top 是 $\operatorname{Soc}(C)$ 的对偶，socle 是 $(C/\mathfrak m_C)^*$。因此两个失败例中 $C\oplus C^*$ 的 top 与 socle 都为 $1+2=3$。这来自有限维对偶的湮灭子关系，不是把 $A$-dual 与 $k$-dual 混同。

前两个正例的 $C$ 确为 Frobenius 代数：在 dual numbers 中取最高 $x$ 系数，在长度五的例中取 $x^3$ 系数。后一配对把 $1$ 与 $x^3$、$x$ 与 $x^2$ 配成两对，$y$ 与自身的值为 $-1$，所以任意特征都非退化。两个失败例的 socle 二维，每个线性泛函都杀死某个非零 socle 向量；该向量也与所有乘积配成零，因此不能得到 $C\simeq C^*$。

这与 regular trace 又不同：当前局部 Artin 代数的乘法算子迹是 $\dim_k(C)$ 乘常数项，幂零极大理想上的迹均为零。因此即使 $C$ 是 Frobenius，regular-trace 配对仍退化；当特征整除该维数时甚至全零。用具体最高系数泛函来判断非退化，而不把 regular trace 当作同一证书。

## 6. 参数专化不能替代重新求 colon

在 $(5,8)$ 例中改取 $f_\lambda=t^2+\lambda t^3$。非零参数时 $S/J$、$S/D$ 长度分别为 $6,9$，核长度 $10$；零参数时实际嵌入理想为 $J_0=A+t^2A$，长度变成 $8,12$，核长度变成 $4$。零参数有 $D_0=k[t^5,t^8,t^{22}]$、$Q_0=t^8D_0$、$I_0=t^8J_0$，故 $A/I_0$、$D_0/I_0$ 长度为 $2,4$。第一截面仍成立，第二截面仍被 top 阻止。

令 $B=k[\lambda]$，考虑真正的 $B$-族 $J_B=A_B+f_\lambda A_B$。它作为 $B$-模自由，但 $S_B/J_B$ 有 $\lambda$-挠：$t^{11},t^{19}$ 的商类被 $\lambda$ 杀死。抽象纤维 $J_B\otimes_Bk$ 到实际嵌入 $J_0$ 的映射并非单射，其核由 $\varepsilon_{11}=[\lambda t^{11}]$、$\varepsilon_{19}=[\lambda t^{19}]$ 张成。

$x=t^5$ 杀死两者，$y=t^8$ 把 $\varepsilon_{11}$ 送到 $\varepsilon_{19}$，再送到零。因此这个核是 $A/(x,y^2)$，长度二。这说明“族模在参数上平坦”和“作为归一化子模的商平坦”不同；后者失败，不能把抽象特殊纤维当成无挠分式理想。

直接求 $Q_B=(A_B:J_B)$ 后，专化的像缺少真正 $Q_0$ 中的 $t^8,t^{16}$；这两个缺失类也具有同一 $A/(x,y^2)$ 作用。冒号求解中的 $\lambda q_8=0$、$\lambda q_{16}=0$ 在 $B$ 中迫使系数为零，先把 $\lambda$ 置零后却不再迫使它们消失。这是 colon 与 base change 不交换的具体原因，无须泛称为“连续参数所以结论连续”。

整个参数环上必须保留第三个生成元：$Q_B=(t^{13},t^{24}-\lambda t^{25},t^{30})A_B$。前两项得到 $t^{28},t^{29},t^{31},t^{32}$，第三项补入 $t^{30}$；五个连续次数再乘 $t^5$ 覆盖尾部。不能用 $t^{29}-\lambda t^{30}$ 除以 $\lambda$，故非零纤维的二生成元证明不能原封不动用于总空间。

同样，积分端环为 $D_B=A_B+B\lambda(t^{11}-\lambda t^{12})+B\lambda t^{17}+B\lambda t^{19}+Bt^{22}+Bt^{27}$。这是直接从 $J_B$ 的 $t^{11},t^{19}$ 系数须被 $\lambda$ 整除，再检验乘 $f_\lambda$ 得到的。$Q_B/t^{13}D_B$ 由 $t^{24}-\lambda t^{25},t^{30},t^{32}$ 的类张成，各被 $\lambda$ 杀死，所以为三份 $B/(\lambda)$。作为特殊纤维的 $A$-模，前一项被 $y$ 送到第三项，再送到零；中间项被极大理想杀死。这不把积分 $Q_B$ 判为可逆，也不把每个实际嵌入纤维的 $Q$ 与积分模纤维混同。

抽象纤维的短正合列也不分裂。取 $U,F$ 为 $1,f_\lambda$ 的抽象生成元，特殊纤维中有 $yF-x^2U=\varepsilon_{11}$。真正嵌入的 $J_0$ 中该关系为零。任何提升修正属于 $L$，$yL$ 只张成 $\varepsilon_{19}$，$x^2L=0$，因此无法消去 $\varepsilon_{11}$。这里的挠子模不是可以随意剥离的形式副本。
