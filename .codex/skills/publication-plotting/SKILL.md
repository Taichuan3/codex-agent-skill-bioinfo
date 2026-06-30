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

- Main claim
- Panels and panel roles
- Input tables and source data
- Filtering state
- Statistics and n
- Color/shape encodings
- Caveats and reviewer risks
- Required exports

## 绘图规则

- 图表服务证据链，不做装饰性复杂化。
- 每个 panel 都要能追踪到 source data。
- 坐标轴、图例、单位、样本数和统计说明必须清楚。
- 默认导出 PNG + SVG；投稿或最终图再加 PDF/TIFF。
- SVG/PDF 文字尽量保持可编辑。
- 不用图形暗示超出证据的机制或因果关系。
- 字体大小要统一且可读：论文多 panel 图通常 6.5-8 pt，PPT 展示图通常 12-18 pt；不要让坐标轴、图例、panel label 小到无法阅读。
- 优先使用低饱和、可区分、色盲友好的 CNS/Nature 风格配色；避免整张图被高饱和颜色淹没。
- 直接标签优先于复杂图例；图例不得遮挡数据。

## QA Checklist

- 图中每个元素是否有解释。
- caption 是否说明数据来源和过滤状态。
- source data 是否能重建主要 panel。
- 色彩和线型是否能区分组别，灰度下是否仍可读。
- 导出文件是否包含正确字体、尺寸和分辨率。
- 文字、点、线、图例、panel label 是否互相遮挡。
- PNG 与 SVG 是否都生成，且视觉内容一致。
- PPT 场景下放大/缩小后是否仍可读。

## 输出格式

输出 figure contract、生成或修改的文件路径、source data 路径、运行命令、QA note 和 caveat。

## 按需读取

- 需要设计主图逻辑、panel 角色或主图/补图区分时，读取 `references/figure-contract.md`。
- 需要交付前视觉检查、遮挡检查、字体/配色/导出检查时，读取 `references/visual-qa.md`。
