---
name: publication-plotting
description: 用于生物信息学 manuscript-ready figures、PPT 可读图、论文主图/补图的 figure contract、source data、panel hierarchy、Python/R 绘图、PNG/SVG 导出、字体配色统一、遮挡检查和 visual QA。不用于一般数据分析或单纯 claim 审查。
---

# Publication Plotting

## 核心问题

如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？

## 使用场景

当用户要求生成论文图、修改图、审查图、定义 panel、导出 PNG/SVG、整理 source data 或做 visual QA 时使用本 skill。目标是把“可运行的分析结果”变成“读者能理解、审稿人能追踪、作者能重跑”的图。

## 不适合触发

- 只需要清洗数据、统计分析或生成中间表格：使用 `bioinfo-analysis-code`。
- 只需要判断图是否支持科学结论：优先或联动 `claim-evidence-audit`。
- 只需要写 caption 文本且不涉及图形生成：使用 `figure-caption` 或写作 skill。
- 只需要 source-data / Data Availability 总审计：使用 `source-data-audit`。

## 最小 Figure Contract

绘图前先锁定：

- Main claim：这张图服务哪个结果句子。
- Output target：main text、supplement、PPT/report inspection 或 internal QC。
- Panel map：每个 panel 的角色是 definition、main evidence、validation、robustness、case illustration 还是 limitation。
- Input/source data：输入表、过滤状态、n/denominator、统计方法、source-data 路径。
- Generating path：脚本、参数、重跑命令、输出 PNG/SVG 路径。
- Visual grammar：颜色、形状、线型、排序、normalization 和直接标签策略。
- Caveat/reviewer risk：哪些结论只能写成 exploratory 或需要转到 prose 解释。

复杂主图设计时读取 `references/figure-contract.md`。

## 绘图规则

- 图表服务证据链，不做装饰性复杂化。
- 读者版图像优先呈现结果；provenance、script path、source-data index 和 claim-boundary notes 默认放在 Methods、supplement、source-data index 或作者 notes，不堆在正文图旁。
- Caption 解释如何读图：panel、坐标轴、颜色/大小编码、数据 universe、n/denominator、normalization。结果解释和机制 claim 放在 Results prose。
- 每个 panel 都要能追踪到 source data；如果 source-data 清单很长，生成单独 index，而不是把路径塞进 reader-facing 正文。
- 默认导出 PNG + SVG；最终投稿按期刊再补 PDF/TIFF。SVG/PDF 文字尽量保持可编辑。
- 字体、图例、colorbar、panel labels 必须在最终插入尺寸下可读：论文多 panel 常用 6.5–8 pt，PPT/报告展示常用 12–18 pt。
- 使用低饱和、可区分、色盲友好的配色；直接标签优先于复杂图例；图例不得遮挡数据。
- 不用图形暗示超出证据的机制或因果关系。

## Report / manuscript figure integration

当图已经进入报告、论文或 PPT 时，把“图像文件”和“文档链接”作为一个整体处理：

1. 先从 Markdown/PPT 枚举实际插入的图，不要按脚本会生成的全部输出决定修改范围。
2. 优先复用原生成脚本和输出 prefix；用户要求“像某张图”时先找原脚本，不要凭记忆重写。
3. 对已插入报告的图，尽量保持稳定路径；若需要干净 reader-facing copy，再同步更新 Markdown 链接。
4. 批量脚本重跑后，只保留报告实际使用图的 intended diff，恢复无关自动刷新图。
5. 替换、提升或移动主图时，同步更新 caption、alt text、补图编号和重复显示。

完整报告图整理时读取 `references/report-figure-integration.md`。

## QA Checklist

- 图中每个元素是否有解释。
- Caption 是否说明数据来源、过滤状态、统计范围/分母和关键设计参数。
- Source data 是否能重建主要 panel。
- 色彩和线型是否能区分组别，灰度下是否仍可读。
- 字体、点、线、图例、colorbar、panel label 是否互相遮挡。
- PNG 与 SVG 是否都生成，且视觉内容一致。
- PPT/报告插入尺寸下是否仍可读。
- 文档中的 image link 是否存在，是否有 paired SVG，是否残留旧图型名或内部编号。
- Omics 图是否说明 gene/sample/cell/variant universe、filtering denominator、normalization、random seed、database version 和 source-data path；UMAP/network/pathway 图不得暗示未经验证的因果机制。

交付前视觉检查读取 `references/visual-qa.md`。

## 输出格式

- Figure contract
- 生成/修改的图像路径：PNG、SVG、必要时 PDF/TIFF
- Source data 路径
- 生成脚本、参数和重跑命令
- 文档链接或 caption 是否已同步
- QA note：可读性、遮挡、导出一致性、source-data traceability
- Caveat：哪些 claim 不能由图直接支持

## 按需读取

- 需要设计主图逻辑、panel 角色或主图/补图区分：`references/figure-contract.md`
- 需要交付前视觉检查、遮挡检查、字体/配色/导出检查：`references/visual-qa.md`
- 需要整理 reader-facing report / manuscript 中已经插入的多张图：`references/report-figure-integration.md`
- 需要处理 RNA-seq/single-cell、variant、pathway/network 或 database-derived figures 的图形证据边界和 source-data QA：`references/omics-figure-qa.md`
