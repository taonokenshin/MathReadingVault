# Specialization and colon ideals need not commute

## Public reader preface

**Learning question and project role.** Reader-created parameter family; retain both module actions and the characteristic qualification. A local reader-generated module problem beside Lang Chapter XVII §7. Explicit relations and coefficient constraints are used to test the limits of structural slogans about tensor kernels and endomorphism rings.

**Preparation.** Fractional ideals, colon ideals, tensor products from presentations, module actions, specialization, and elementary finite-length module calculations.

**Historical scope and status.** Recorded as a new independent first-pass reader proof, including the stated characteristic branches. It is not a review or an upgrade of an original numbered theorem, exercise, or hard packet. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Specialization and colon ideals need not commute. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** Earlier coefficient/colon computations and both module actions are prerequisites. An abstract fiber and a colon ideal recomputed in the special fiber are deliberately distinguished. The explicit family is not a general classification.

**Source and editorial treatment.** Case ID: `LANG-N1`. Historical source date: 2026-10-05. Original project record: `2026-10-05-xvii7-five-nine-tensor-specialization.md`. Original-note SHA256: `519340f2d90a515aa821cfe634fe72473a3ac435ba2df9a780ed838bf502987a`. The short historical excerpts use source lines 3–5, 55–101; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 3–5

状态：新的独立第一遍 reader proof；不是集中 review，也不提升原书编号定理、习题或 hard packet 的等级。旧详细证明遮住，先保存独立系数与关系模推导，再看唯一允许的 printed660 / PDF669。以下 $k$ 是任意域，包括特征 $2$；除明确的 involution 分支外，结论无特征例外。

直觉：一个分式理想虽只有两个生成元，它的张量核仍由真实关系模决定。核与余核同长、商环有完美乘法配对、双对偶恢复原理想，都不能直接推出自由性或截面。参数族还须区分“先算再专化”与“专化后重新求 colon”；两者可能得到不同的模和作用。

### Source lines 55–101

## 5. 同一算例的参数族：专化不能交换 colon

改用 $R=k[\lambda]$、$B=R[t^5,t^9]$、$S_R=R[t]$，$f_\lambda=t+\lambda t^2$、$\mathcal J=B+f_\lambda B$。每个非零纤维经 $t\mapsto\lambda t$ 都同构于前述算例；以下先在整个 $R$ 上重新求解。

通用 colon 为 $\mathcal Q=(B:\mathcal J)=(t^{18},t^{24}-\lambda t^{25},t^{35})_B$。低次数条件仍有六个基方向，并含所有 $32$ 以上次数。第三生成元在 $R$ 上不能删；关系 $\lambda^2t^{35}=x^3t^{18}-(y+\lambda x^2)(t^{24}-\lambda t^{25})$ 只在可逆化 $\lambda$ 后消去它。专化像为 $\bar Q=(t^{18},t^{24},t^{35})$，真实零纤维却是 $Q_0=(A:A+tA)=(t^9,t^{35})$。商 $Q_0/\bar Q$ 的基是 $t^9,t^{14},t^{19}$，同构于 $t^9A/(x^3,y)$。

把 $\mathcal W=\mathcal J/B$ 与 trace 商 $C$ 区分。$\mathcal W$ 是 $R$-自由模，秩 $10$；三个缺口块 $11/12,16/17,21/22$ 的列分别是 $(\lambda,0)$、$(1,\lambda)$，余核都是 $R/(\lambda^2)$。因此 $S_R/\mathcal J\simeq R^6\oplus(R/(\lambda^2))^3$。抽象纤维 $\mathcal W/\lambda\mathcal W=A/\bar Q$ 长 $10$，嵌入式 $J_0/A=A/Q_0$ 只长 $7$。

抽象 $\bar J=\mathcal J/\lambda\mathcal J$ 到真实 $J_0=A+tA$ 的核长 $3$，生成元为 $[f_\lambda t^9-t^{10}]=[\lambda t^{11}]$，其两个 $x$ 倍数是 $[\lambda t^{16}]$、$[\lambda t^{21}]$，annihilator 为 $(x^3,y)$。该扩张不分裂：$\bar J$ 的 top 为 $2$，而核与 $J_0$ 的 top 之和为 $3$。抽象纤维含真实 torsion，不能直接当作嵌入式分式理想。

通用端环为 $\mathcal D=B+B\lambda^2(t^{11}-\lambda t^{12})+B\lambda^2t^{16}+B\lambda^2t^{17}+Bt^{26}$。其中第二、第三缺口块各强制两系数可被 $\lambda^2$ 整除；第一块结合 $df_\lambda$ 同样强制 $11$ 的系数可被 $\lambda^2$ 整除，特征 $2$ 也成立。故 $S_R/\mathcal D\simeq R^9\oplus(R/(\lambda^2))^5$。

真实 $D_0=A+At^{26}$；抽象 $\bar D=\mathcal D/\lambda\mathcal D=D_0\ltimes E$。$E$ 是平方零理想，$E\simeq A/(x^3,y)\oplus A/(x^2,y)$。两个生成元是 $e=[\lambda^2(t^{11}-\lambda t^{12})]$、$h=[\lambda^2t^{17}]$；其 $x$ 链分别长 $3$、$2$，$y,t^{26}$ 杀掉 $E$。未缩放的 $D_0$ 提供环截面；这与刚才 $\bar J$ 的不分裂形成对照。

## 6. 通用核是平坦的，结构仍会跳变

$\mathcal I=\mathcal Q\mathcal J=(t^{18},t^{19}+\lambda t^{20},t^{25})$。它是 $\lambda$-饱和的，$B/\mathcal I$ 对 $R$ 自由，秩 $7$。专化像 $I_b=(t^{18},t^{19},t^{25})$；真实 $I_0=(t^9,t^{10})$。$I_0/I_b$ 长 $5$，分别是次数 $9,14$ 的链与次数 $10,15,20$ 的链，不能把 $I_b$ 替换为 $I_0$。

同样的真实关系证明给出 $\mathcal K=\mathcal N/\mathcal Q^2$。$\mathcal N$ 的低基为 $n_\lambda=t^{23}-2\lambda t^{24}+2\lambda^2t^{25}$、$p_\lambda=t^{27}-\lambda^2t^{29}+\lambda^3t^{30}$、$xn_\lambda$，并含全部 $32$ 以上次数。乘积理想 $\mathcal Q^2$ 的四个生成元为 $t^{36}$、$t^{42}-\lambda t^{43}$、$t^{48}-2\lambda t^{49}+\lambda^2t^{50}$、$t^{53}$。它含 $50,51,53,54$，再由第二生成元的 $x^2$ 倍数取得 $52$；乘 $x$ 即覆盖全部 $50$ 以上次数。

在低次数商中，关系都是单位首项：$t^{42}=\lambda t^{43}$、$t^{47}=\lambda t^{48}=2\lambda^2t^{49}$，以及 $36,41,45,46$ 为零。因此 $\mathcal K$ 对 $R$ 自由，秩 $14$，基可取 $n_\lambda,p_\lambda,xn_\lambda$ 加前述十一尾部次数。$\mathcal I$ 也对 $R$ 平坦，故 $0\to\mathcal K\to\mathcal Q\otimes_B\mathcal J\to\mathcal I\to0$ 在零点仍正合，通用张量本身对 $R$ 平坦。

抽象核 $\bar K$ 长 $14$；其 $x$ 链为 $23\to28\to33\to38\to43\to0$，$27\to32\to37\to0$，$34\to39\to44\to49\to0$，$35\to40\to0$。$y$ 送 $23$ 到 $32$，$28$ 到 $37$，$34$ 到 $43$，$35$ 到 $44$，$40$ 到 $49$，其余链项到零。因此 $\mu_A(\bar K)=4$，top 基为 $23,27,34,35$。

$C_b=A/I_b=k[x,y]/(y^2,x^2y,x^5)$ 长 $7$、type 为 $2$。所以 $\bar K$ 不能同构于 $C_b\oplus C_b^*$，后者 top 为 $3$。虽然 $C_bn\subset\bar K$ 仍长 $7$，它也不分裂：$xp=yn$ 会要求投影后的 $p$ 满足 $xa=y$，而 $y\notin xC_b$。这给出本笔记最明确的一般化失败边界。

还可量化非零纤维的补模怎样失效。令 $C_\lambda=B/\mathcal I$，$\zeta_\lambda=-\lambda t^{32}+\lambda^2t^{33}-\lambda^4t^{35}$，$V_\lambda=Bp_\lambda+B\zeta_\lambda$。其 $R$-基为 $p_\lambda,xp_\lambda,x^2p_\lambda,x^3p_\lambda,x^4p_\lambda,yp_\lambda,\zeta_\lambda$；稳定性来自 $x\zeta_\lambda=-\lambda x^2p_\lambda-yp_\lambda$、$y\zeta_\lambda=\lambda^2x^3p_\lambda$。这是补格，不宣称它在整数参数环上等于 $C_\lambda$ 的对偶。$C_\lambda n_\lambda\oplus V_\lambda$ 嵌入 $\mathcal K$；尾部 $32\ldots35$ 与 $37\ldots40$ 两块各留下 $\lambda^2,\lambda^4$，$43,44$ 与 $49$ 两块各留下一个 $\lambda^2$。因此格余核为 $(R/(\lambda^2))^4\oplus(R/(\lambda^4))^2$，行列式为 $\pm\lambda^{16}$，零点像只有秩 $8$。消去带系数 $3\lambda$ 的项只用单位行操作，特征 $3$ 也无例外。非零纤维的直和分解确实须反转 $\lambda$；不能直接延伸到零点。

这四个 Smith 块有直接证书。令 $r_\lambda=yn_\lambda$、$s_\lambda=x^2n_\lambda$；第一个残余是 $xp_\lambda-r_\lambda-2\lambda s_\lambda=\lambda^2t^{34}-3\lambda^3t^{35}$，另一个是 $\zeta_\lambda+\lambda r_\lambda+\lambda^2s_\lambda=\lambda^4t^{35}$。第二块同样留下 $\lambda^2t^{39}-3\lambda^3t^{40}$ 与 $-\lambda^4t^{40}$。第三块是 $x^3p_\lambda-\lambda x^4n_\lambda=\lambda^2t^{44}$；第四块直接是 $x^4p_\lambda=\lambda^2t^{49}$。所有主张都由这些有限关系和尾部消去给出。

抽象专化乘法序列仍没有 $A$-截面：$\mu_A(\bar Q)=3$、$\mu_A(\bar J)=2$，所以张量 top 为 $6$；$\bar K$ 与 $I_b$ 的 top 之和为 $4+3=7$。两种 $\bar D$ 截面随之都不存在。

还须保留抽象端环的作用。FIRST 在 $\bar K$ 上杀掉 $E$；SECOND 却让 $e$ 作用为 $-y$，$xe$ 为 $-xy$，$h$ 为 $x^3$，$xh$ 为 $x^4$。令 $z_0=t^{26}$，FIRST 送 $n$ 到 $t^{49}$，SECOND 送到 $-t^{49}$。这些公式来自通用核乘子 $e'-f_\lambda b$：对通用 $e$ 为 $-y-\lambda x^2-e$，对 $d_{16}=\lambda^2t^{16}$ 为 $-xy-d_{16}$，对 $h$ 为 $x^3-h$，对 $z_0$ 为 $-z_0-\lambda y^3$。注意 $d_{16}=xe+\lambda h$，故通用 $xe$ 的公式还含 $-\lambda x^3$；只有零纤维才省掉该项。SECOND 不能先把 $\bar D$ 缩成嵌入式 $D_0$。

最后，通用 $\mathcal D/\mathcal I$ 对 $R$ 自由，秩 $14$；其抽象零纤维的 socle 是 $kx^4+kxy+kxz_0+kx^2e+kxh$，type 为 $5$。非零纤维的 $D/I$ type 为 $1$，而下一段重新计算的真实 $D_0/I_0$ 也 type 为 $1$。平坦与长度不变都不能省略这个区别。

这个退化可以精确量化。取 $t^{31}$ 系数作为泛函，$\mathcal D/\mathcal I$ 的乘法配对有两组单位互补项：$0/31$、$5/26$；其余五组为 $9/22,10/21,14/17,15/16,20/11$，都带系数 $\lambda^2$。后七个方向依次采用 $t^{31},t^{26},\lambda^2t^{22},\lambda^2t^{21},\lambda^2t^{17},\lambda^2t^{16},e$，所以 Gram 行列式为 $-\lambda^{20}$，配对映射的余核为 $(R/(\lambda^2))^{10}$。零点的 radical 恰是 $\bar D/I_b\to D_0/I_0$ 的核；诱导到真实四维商后的配对仍完美。这是系数型 Frobenius 配对。正次数理想幂零，普通乘法的 regular trace 却只有常数系数的 $14$ 倍，其配对秩至多 $1$；特征 $2,7$ 时为零。两种 trace 不可混用。

## 7. 重新计算真实零纤维：出现单侧截面

这里 $J_0=A+tA$，$Q_0=t^9D_0$，$I_0=(y,x^2)$。$C_0=A/I_0=k[x]/(x^2)$；$D_0/I_0=k[x,z_0]/(x^2,z_0^2)$ 长 $4$。重新计算 $N_0=Q_0\cap t^{-1}Q_0$，其低基是 $18,23,27,28$，并含全部 $32$ 以上次数；$Q_0^2=(t^{18},t^{44})$。真实核 $K_0$ 的基为 $t^{34},t^{35},t^{39},t^{40}$，$x$ 给出两条长 $2$ 的链，$y,z_0$ 都作用为零。故 $K_{0,A}\simeq C_0^2$，两个 $D_0$ 作用在核上相同，但 $K_0\not\simeq D_0/I_0$。

因为 $I_0=t^9J_0$，映射 $s_0(i)=t^9\otimes(i/t^9)$ 是真正的 $A$-截面，而且对 SECOND 即 $J$ 因子的 $D_0$ 作用线性。FIRST 截面仍失败。归一化为 $D_0\otimes_AJ_0\to J_0$ 后，$z_0s_0(1)-s_0(z_0)=z_0\otimes1-t^{25}\otimes t$，对应真实核参数 $-t^{34}\ne0$。任意 $A$-线性修正 $h:J_0\to K_0$ 都有 $z_0h=0$、$h(z_0)=t^{25}h(t)=0$，无法消除此缺陷。核上两作用相同，不能推出整个序列有共同截面。

自然比较映射也能完整求出。$\bar Q\subset Q_0$、$\bar Q^2\subset Q_0^2$，所以 $\bar K\to K_0$ 保持同一个关系参数；次数 $34,35,39,40$ 给出满射。其核 $W$ 长 $10$，$x$ 链分别长 $5,3,2$，生成元为 $n,p,t^{44}$；$y$ 只送 $n$ 到 $t^{32}$、$xn$ 到 $t^{37}$。因此 $\mu_A(W)=3$，比较序列不能分裂：$3+2>\mu_A(\bar K)=4$。它对两种作用都等变，$E$ 的 SECOND 像落入 $W$，所以也没有任一种 $\bar D$ 截面。

把两条乘法短正合列放在一起，左端比较满射，右端是 $I_b\subset I_0$。蛇引理给出 $0\to W\to\bar T\to T_0\to I_0/I_b\to0$：自然张量比较的核长 $10$，余核长 $5$。这个具体映射解释了专化失败，超过单纯的维数比较。$\bar\tau$ 保持配对 radical，降到真实 $D_0/I_0$ 后送 $x$ 到 $x$、$z_0$ 到 $-z_0$；它在 $K_0$ 上看不出差别，因为 $z_0K_0=0$。
