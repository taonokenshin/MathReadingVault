# Why Perron needs finite truncation before interchange

## Public reader preface

**Learning question and project role.** A failure-boundary case study; retain the later corrected source-page qualification and maintenance-gate preface. A selective analysis/analytic-number-theory support lane. Its durable records connect convergence, integral interchange, character sums, products, and generating functions across two books. The historical queue is maintenance-gated; this release does not reopen it.

**Preparation.** Absolute convergence of Dirichlet series, compact-uniform convergence, contour integration, and the hypotheses of dominated convergence and Fubini/Tonelli.

**Historical scope and status.** The 10 July historical supersession note records the Perron finite-truncation/full-line-Fubini boundary as closed. Its old proposed next task is obsolete; Mathematical Analysis remains named-support only. These are the historical project’s labels, retained as provenance rather than a new mathematical audit or a claim of novel mathematics.

**What this excerpt demonstrates.** Why Perron needs finite truncation before interchange. Read the displayed argument or counterexample as a test of the particular inference described in the source. A successful local calculation does not remove the note’s other hypotheses or enlarge its scope.

**Retained dependencies and limitations.** The finite-contour argument and the later kernel-tail estimate are separate obligations. The excerpt demonstrates the obstruction to a naive whole-line interchange, not a standalone proof of every Perron variant. Source page locators in the full record were later extended through the actual proof ending.

**Source and editorial treatment.** Case ID: `APOSTOL-N2`. Historical source date: 2026-07-01. Original project record: `2026-07-01-perron-mellin-dominated-fubini-boundary.md`. Original-note SHA256: `46a13d4f349237b081bdf64d93a173d6c48f59cd1a65453fc218295470ee1565`. The short historical excerpts use source lines 7–32; gaps between them are deliberate omissions. Source textbooks, scanned pages, private source files, and unlisted dependent records are not bundled. Original mathematical notation is preserved; archive links are converted to provenance references. No proof is re-verified, no source error is newly confirmed, and no proof-status label is upgraded.

**Language.** The learning preface is English. The excerpts retain the source record’s original Chinese mathematical exposition with English terminology and LaTeX. They are not presented as an English translation. Read them selectively according to your own study goals. [Return to the other-lanes index](INDEX.md).

## Historical mathematical excerpts

### Source lines 7–32

## 直觉图像

Perron 公式看起来像“把 Dirichlet 级数塞进积分，再把求和和积分交换”。但真正安全的路线不是一次性在整条竖线上做 Fubini。

安全路线是：

1. 先把竖线积分截断到有限区间 $[-T,T]$。
2. 在这个有限 contour 上，用 $F(s+z)$ 的绝对一致收敛逐项积分。
3. 对每个 $n$ 使用 Mellin 阶跃核 Lemma 4。
4. 最后用 Lemma 4 的有限 $T$ 误差估计和 Dirichlet 级数的绝对收敛尾和令 $T\to\infty$。

危险路线是：直接写

$$
\int_{-\infty}^{\infty}
\sum_{n=1}^{\infty}
\frac{f(n)}{n^{s+c+it}}\frac{x^{c+it}}{c+it}\,dt
=
\sum_{n=1}^{\infty}
\int_{-\infty}^{\infty}
\frac{f(n)}{n^{s+c+it}}\frac{x^{c+it}}{c+it}\,dt.
$$

这一步通常没有 Tonelli/Fubini 支撑，因为控制量含有 $1/|c+it|$，它在整条实线上不可积。

## 对应文本位置
