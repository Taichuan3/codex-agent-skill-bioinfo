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

- Main claim and `claim_id`
- Whether the figure belongs in main text, supplement, or PPT-only inspection; keep main text limited to figures that directly carry the result narrative.
- Panels and panel roles
- Input tables and source data
- Generating script path and rerun command/path so future title/size/style changes are easy
- Filtering state
- Statistics, n, denominator, random seed, database/reference version when relevant
- Color/shape encodings
- Caveats and reviewer risks
- What the panel can support, what it cannot support, and whether claim wording needs downgrade
- Required exports

## 绘图规则

- 图表服务证据链，不做装饰性复杂化。
- Reader-facing report / seminar report 图像应先满足读者可读性：结果呈现优先，内部审查信息后置。
- 每个 panel 都要能追踪到 source data，但 **provenance / script / source-data tables 默认放在内部 notes 或 supplementary records，不放进 reader-facing report 正文**。
- 坐标轴、图例、单位、样本数和统计说明必须清楚。
- 默认导出 PNG + SVG；投稿或最终图再加 PDF/TIFF。
- 同一 figure 或同一读者版最终图继续微调时，默认覆盖同名最终输出并同步 QC/source manifest；只有用户明确要求保留草图、对比版本、历史版本或不同尺寸方案时，才另存带版本号/尺寸标记的新文件。
- SVG/PDF 文字尽量保持可编辑。
- 对 UMAP、Manhattan、heatmap、image tile 等高密度层，优先使用 hybrid export：数据层 rasterized，坐标轴、文字、线和注释保留 vector；避免百万点全矢量 PDF/SVG。
- 导出前记录目标物理尺寸、字体、DPI 只作用于 raster layer；不要用 JPEG 保存含文字/线条的科学图。
- 不用图形暗示超出证据的机制或因果关系；claim-boundary / caveat / “不能写成…” 等内部审查语言应保存在作者 notes，不要作为图内文字或正文图表说明呈现给读者。
- 字体大小要统一且可读：论文多 panel 图通常 6.5-8 pt，PPT 展示图通常 12-18 pt；报告/PPT 读者版应优先放大坐标轴、tick labels 和 legend，避免压缩到需要放大才能阅读。
- 优先使用低饱和、可区分、色盲友好的 CNS/Nature 风格配色；避免整张图被高饱和颜色淹没。
- 直接标签优先于复杂图例；图例不得遮挡数据。
- 读者版图像应尽量去掉冗余 in-plot titles/subtitles（由报告小标题和 caption 承担主题），减少不必要文字，把空间留给数据本身。
- 饼图通常不适合承载复杂 source composition；优先改为 ordered bar chart、dot plot 或 heatmap。对于多轴 atlas / metadata composition，优先用 small-multiple ordered bar charts 分别展示关键轴，而不是把所有信息压进一个饼图。关键轴必须服务当前 Results 叙事：如果后续结果按 histone/TF/target、organ-module、cancer/proxy 三层展开，就用这三层组织 atlas overview；不要因为 `modality`、`biosample_object_type` 等字段方便就做成与正文叙事不一致的通用 metadata 图。替换时同步更新正文、caption 和 alt text，避免保留旧分类或 “pie chart” 等旧描述。
- 当读者需要同时理解“metadata atlas 组成”和“输入序列/区域设计”时，优先设计 composite figure：一个 panel 展示与下游结果结构对齐的 atlas/source composition，另一个 panel 展示 genomic input window 和 analysis-region schematic。若真实 genomic scale 下 flank/body 太小而不可读，可同时给出 true-position overview 和 not-to-scale expanded design，并在图中明确标注 not to scale。Expanded design 内部仍应保留关键比例：例如 flanks 固定为 10 kb 时，body 宽度应按实际 body 长度缩放，而不是把 body/flank 三段画成等宽。
- 对已插入报告的图，优先保持输出文件名稳定，除非用户明确同意改路径；这样可减少 Markdown 路径维护成本。
- When reader-facing report source also looks clean, or同名图片可能被 Markdown/PDF 预览缓存，则不要只覆盖原分析图；应把最终版 PNG/SVG 同步到报告专用目录（如 `figures/project_report/`）并更新 Markdown 图片链接为干净文件名，避免 `figure_09O`、`figure_09S`、`*_pie.png` 等内部编号/过时图型名继续出现在报告源码中。
- 当用户要求“参考某张已有图的画法”时，不要只吸收视觉风格后重写新脚本；必须先在本地搜索该图的原始绘图脚本、source data 和输出路径，优先在已有脚本基础上按新需求修改。只有找不到原脚本、原脚本与新数据分辨率/输入完全不匹配、或复用风险更高时，才新建脚本，并在交付中说明理由。详见 `references/reference-figure-script-reuse-and-visual-qa.md`。
- When report figures are regenerated, promoted from supplement to main text, or otherwise repositioned, update the report Markdown in the same pass: replace/insert the corresponding image link, remove duplicate supplementary display if the figure moved into the main narrative, renumber affected supplementary figures, and verify no duplicate or missing image links remain.
- 整合优化一份报告/论文中的多张图时，先从正文 Markdown 枚举实际插入的图片清单，再按“报告使用图”而不是“脚本会生成的全部图”确定修改范围；重跑批量脚本后恢复未进入报告的自动刷新图，避免无关 diff。
- 读者版图内不要保留内部编号式标题或 panel/source 编号（如 `Figure 09O`、`09S`、`Result 2 Figure 1`）；报告小标题、caption 和 alt text 承担叙事，图内只保留必要坐标轴、图例和单位。
- Dotplot/heatmap 的图例和 colorbar 是高风险重叠区域：优先把 dot-size / outline legend 放到右侧独立空白区，给 colorbar 和 legend 分配不同 x 位置；不要把多列 dot-size legend 放在底部挤压旋转 x-axis labels 和脚注。

## Report figure placement and captioning lessons

- When readers need both raw model output and attribution layers, preserve the distinction in figure ordering: show raw/default output-type profiles first, then custom atlas/source-attribution panels. Do not let a custom atlas figure substitute for the raw signal overview when the raw overview is the clearest first-pass evidence.
- Be precise about averaging logic in raw output-type overview figures: if a panel shows an output-type-level profile summarized across many returned tracks, describe it as an averaged/summary display that can dilute local, source-specific signals. Do **not** write that the output-type overview avoids averaging; instead use that dilution as the rationale for moving to 15-region summaries and atlas source-attribution layers.
- When a report figure is promoted from supplement to main text or replaced by a better figure, update the Markdown immediately: insert the new link/caption at the correct result point, remove duplicate display from supplement, and move any still-useful screened figure to supplement rather than dropping it.
- For manuscript-style report sections, keep figure captions explanatory rather than interpretive: describe panels, axes, color/size encodings, data universe, n/denominators, and normalization; keep result claims and caveats in the prose around the figure.
- In report subsections with several displayed figures, assign local figure labels consistently (e.g. `图 2.3a`, `图 2.3b`), wrap captions in the same small-caption style used by the document when applicable, and ensure the surrounding prose cites each figure in parentheses at the claim it supports. Do not leave promoted/inserted main-text figures as bare image links.
- For Discussion figures that explain model-performance gaps (e.g. training-track coverage, tissue/context mismatch, reference/sequence gaps), prioritize exact counts over qualitative labels. Good panels include: output type × relevant organ-module track counts; target-specific direct-context versus proxy-context counts with denominators; and external-validation magnitude contrasts that explain why a context is secondary despite training-track coverage. Keep these figures compact and reader-facing, with source-data TSVs indexed in the report.

## QA Checklist

- 图中每个元素是否有解释。
- Caption 是否为论文式图注：正式图题 + panel-specific A/B/... 说明；说明数据来源、统计范围/分母、数字含义和关键设计参数；避免口语化“左侧/右侧/右下”描述。
- 若不同 panel 的统计 universe 不同（例如 histone/TF panel 仅统计 CHIP_HISTONE/CHIP_TF tracks，而 organ/cancer panel 基于全部 tracks），caption 是否显式写出各自 denominator。
- source data 是否能重建主要 panel。
- 色彩和线型是否能区分组别，灰度下是否仍可读。
- 导出文件是否包含正确字体、尺寸和分辨率。
- 文字、点、线、图例、panel label 是否互相遮挡；profile 图中的 rug/tick/CTSS marker 是否遮挡 x-axis labels、baseline 或 region labels，必要时应下移到独立 rug lane 并固定 y-axis range 以便比较。
- PNG 与 SVG 是否都生成，且视觉内容一致。
- PPT 场景下放大/缩小后是否仍可读。
- Omics 图是否说明 gene/sample/cell/variant universe、filtering denominator、normalization、random seed、database version 和 source-data path；UMAP/network/pathway 图不得暗示未经验证的因果机制。
- 高密度图是否采用合适的 raster/vector 分层，文字是否仍可编辑，导出尺寸是否与目标版面一致。

## 输出格式

输出 figure contract、生成或修改的文件路径、source data 路径、生成脚本/重跑入口、运行命令、QA note 和 caveat。若覆盖了同名最终输出，明确说明“已覆盖最终输出”；若保留多个版本，说明保留原因。若用户在整理报告/论文/PPT，明确标注哪些图进入正文主叙事、哪些图只作为 supplement/PPT inspection；正文中不要堆放只能作为过程检查的图。

## 按需读取

- 需要设计主图逻辑、panel 角色或主图/补图区分时，读取 `references/figure-contract.md`。
- 需要从论文 claim 反推主图/补图、建立 `CLAIM_TABLE.md` / `FIGURE_PLAN.md` / reviewer attack matrix，或检查每个 panel 是否有 source-data/script/statistics/limitation 时，读取 `references/claim-to-figure-system.md`。
- 需要交付前视觉检查、遮挡检查、字体/配色/导出检查时，读取 `references/visual-qa.md`。
- 需要把内部项目图整理成读者版报告图、替换饼图、去除冗余标题或保留报告路径稳定时，读取 `references/reader-facing-report-figure-optimization.md`。
- 需要重排结果报告中的主图/补图、区分 raw model output 与自定义 atlas/source-attribution 层、或把图注改成论文式说明时，读取 `references/result-report-figure-workflow.md`。
- 需要处理 RNA-seq/single-cell、variant、pathway/network 或 database-derived figures 的图形证据边界和 source-data QA 时，读取 `references/omics-figure-qa.md`。
- 需要把包含本地图片链接的 Markdown 研究报告导出为 PDF，并验证 PDF 页数、图片嵌入和 macOS QuickLook 预览时，读取 `references/markdown-report-pdf-export.md`。
