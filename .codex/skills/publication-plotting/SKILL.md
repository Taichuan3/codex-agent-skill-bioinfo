---
name: publication-plotting
description: 用于生物信息学 manuscript-ready figures、PPT 可读图、论文主图/补图的 figure contract、source data、panel hierarchy、Python/R 绘图、PNG/SVG 导出、字体配色统一、遮挡检查和 visual QA。不用于一般数据分析或单纯 claim 审查。
---

# Publication Plotting

## 核心问题

如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？

## 使用场景

当用户要求生成论文图、修改图、审查图、定义 panel、导出 PNG/SVG、整理 source data 或做 visual QA 时使用本 skill。参考 Nature-skill 的 figure contract 思路，但按本地项目需求默认输出 PNG + SVG，最终投稿再补 PDF/TIFF。

## 不适合触发

- 只需要清洗数据、统计分析或生成中间表格时，使用 `bioinfo-analysis-code`。
- 只需要判断图是否支持科学结论时，联动或优先使用 `claim-evidence-audit`。
- 只需要写 caption 文本且不涉及图形生成时，可使用 `figure-caption` 或写作 skill。


## Figure Contract

绘图前先定义：

- Main claim / `claim_id`, panel roles and intended audience.
- Main text、supplement 或 inspection/PPT placement。
- Input tables、source data、filtering state、statistics、n/denominator、random seed 和 database/reference version。
- Generating script、rerun command、color/shape encodings 和 required exports。
- 每个 panel 能支持什么、不能支持什么，以及 caveat/reviewer risk。

Figure contract、panel hierarchy、main/supplement placement 和 analysis/figure logic 由用户决定。Agent 提供备选 contract、实现、测试、provenance、sensitivity 和 visual QA，不把技术默认当成最终图逻辑。

## 绘图规则

- 图表服务证据链，不做装饰性复杂化。
- 每个 panel 都要追踪到 source data、生成脚本、统计、过滤状态和 caveat；reader-facing 正文只保留读图所需信息，详细 provenance 放 source-data index、Methods、supplement 或作者 notes。
- 坐标轴、图例、单位、样本数、denominator 和统计说明必须清楚；不同 panel 的统计 universe 不同时分别声明。
- 默认导出 PNG + SVG；投稿或最终图再加 PDF/TIFF。
- 同一 figure 或同一读者版最终图继续微调时，默认覆盖同名最终输出并同步 QC/source manifest；只有用户明确要求保留草图、对比版本、历史版本或不同尺寸方案时，才另存带版本号/尺寸标记的新文件。
- SVG/PDF 文字尽量保持可编辑；高密度数据层可 rasterize，坐标轴、文字、线和注释保留 vector。记录最终物理尺寸、字体和 raster DPI，不用 JPEG 保存含文字/线条的科学图。
- 使用可区分、色盲友好且不过饱和的配色；同一条件跨 panel 保持一致，必要时用形状或线型提供冗余编码。
- 不用图形暗示未经验证的机制或因果关系；内部 claim-boundary notes 不作为图内文字。
- 读者版优先简洁、插入尺寸可读和直接标签；复杂 composition 通常优先 ordered bar、dot plot、heatmap 或 small multiples，而不是饼图。
- 参考已有图时先定位原脚本、source data 和输出；能安全复用就修改原生成逻辑。详见 `references/reference-figure-script-reuse-and-visual-qa.md`。
- 已嵌入报告的图在裁剪、替换、移动或重命名时，同步 caption、alt text、编号、主/补图位置和链接，并验证无重复或缺失。

## QA Checklist

- Source data 能否重建主要 panel；script、statistics、denominator、version 和 caveat 是否可追踪。
- Caption 是否解释 panels、axes、encodings、data universe、n/denominator、normalization 和关键参数，而把结果解释留给正文。
- 文字、点、线、误差、图例、colorbar、rug/interval lane 和 panel label 是否遮挡或裁切。
- PNG/SVG 是否都存在、重新打开后视觉一致、插入目标版面后仍可读。
- 报告链接、caption、alt text 和主/补图位置是否与最终输出一致且无重复。
- Omics、interval 和 model-vs-external profile 是否使用对应 reference 的额外 evidence-boundary 检查。

## 输出格式

输出用户确认的 figure contract、生成或修改的文件、source data、脚本/重跑入口、运行命令、QA note、caveat 和 main/supplement placement。若覆盖同名最终输出或保留多个版本，明确说明状态和原因。

## 按需读取

- 需要设计主图逻辑、panel 角色或主图/补图区分时，读取 `references/figure-contract.md`。
- 需要从论文 claim 反推主图/补图、建立 `CLAIM_TABLE.md` / `FIGURE_PLAN.md` / reviewer attack matrix，或检查每个 panel 是否有 source-data/script/statistics/limitation 时，读取 `references/claim-to-figure-system.md`。
- 需要交付前视觉检查、裁剪、遮挡、字体/配色、导出或链接同步时，读取 `references/visual-qa.md`。
- 需要把内部图整合进 reader-facing report、同步 caption/alt text/link 或调整 main/supplement placement 时，读取 `references/reader-facing-report-figure-optimization.md`。
- 需要比较模型预测、官方 processed target 与项目 observed signal 的多分辨率 profile 时，读取 `references/model-vs-external-profile-figures.md`。
- 需要处理 RNA-seq/single-cell、variant、pathway/network、database-derived 或 interval-hit figures 的图形证据边界和 source-data QA 时，读取 `references/omics-figure-qa.md`。
- 需要把包含本地图片链接的 Markdown 研究报告导出为 PDF，并验证 PDF 页数、图片嵌入和 macOS QuickLook 预览时，读取 `references/markdown-report-pdf-export.md`。
