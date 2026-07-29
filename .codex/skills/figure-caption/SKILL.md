---
name: figure-caption
description: 用于依据图、panel 说明和分析信息起草、重构或审查生物信息学论文的 figure title、panel titles、legend/caption 及 figure-to-claim 契约，确保样本、编码、统计、n、source data 和 caveat 完整。仅润色既有中文或英文图注分别用 chinese-scientific-polishing 或 scientific-english-polishing，中文图注转英文用 scientific-english-translation；实际绘图与视觉排版用 publication-plotting。
---

# Figure Caption

## 核心问题

如何让每个 figure title、panel title 和 caption 准确说明图中数据，同时不把解释性结论塞进图注？

## 路由与边界

- 主要交付物是完整 title/panel/legend/caption 或其内容完整性审查时用本 Skill，不论最终语言是中文还是英文。
- 只改现成图注的中文语言用 `chinese-scientific-polishing`，只改现成英文语言用 `scientific-english-polishing`，中文转英文用 `scientific-english-translation`。
- 实际绘图、panel 布局、字体、颜色和导出用 `publication-plotting`；全稿图文一致性用 `manuscript-consistency-audit`；逐 panel source-data 可追溯性审计用 `source-data-audit`。
- 不从图像外观猜测未提供的样本、统计、过滤、机制或显著性；缺失项标记为待补。

## Figure contract

起草前锁定主 claim、每个 panel 的证据角色、比较对象、样本范围、过滤、坐标/颜色/符号、n 或 denominator、重复、统计检验、多重校正、source data 和 caveat。无法核验的信息使用明确占位符，不自行补全。

## 工作流程

1. 读取用户提供的图、panel 顺序、分析说明和目标期刊要求；不默认扫描整个项目。
2. 建立 panel-to-claim map，区分图中直接显示的 evidence 与正文 interpretation。
3. 写简短 figure title；按实际 panel 顺序描述对象、比较、编码和必要方法。
4. 补齐 n、重复、统计、显著性标记、缩写、过滤和 source-data 指针；缺失项进入 checklist。
5. 检查图、caption、正文 claim 的术语与强度一致性；探索性结果保留限定词。

## 写作契约

- Caption 说明图中显示什么以及如何读取，不承载超出图证据的机制或因果结论。
- 图题可以概括信息功能，但不得把 exploratory pattern 写成已证明机制。
- Caption 不暴露本机路径、仓库目录、脚本/原始表格文件名、内部 flag/run ID、原始命令或未解决批注；精确 provenance 保存在 source-data inventory、manifest 或项目记录，并在 caption 中仅保留稳定的读者指针。
- 不把 `n` 混同为 biological replicates、technical replicates、cells、variants 或 observations；明确统计单位。
- 统计信息只报告已提供或可验证内容；不得从星号反推检验或阈值。

## 输出格式

- `Figure title`
- `Panel map` 与 `Full caption`
- `Missing information / source-data checklist`：仅列确实缺失的内容
- `Caveat / reviewer-risk notes`：仅在 claim 超界或图文不一致时给出
