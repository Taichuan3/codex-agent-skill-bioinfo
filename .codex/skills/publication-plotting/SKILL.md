---
name: publication-plotting
description: 用于实际生成、重画、排版或整合生物信息学论文/PPT 图，交付 figure contract、panel hierarchy、Python/R 绘图、source data、PNG/SVG、字体配色和 visual QA；只写 caption、只审 source data/claim 或无图形交付的分析不使用本 Skill。
---

# Publication Plotting

## 核心问题

如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？

## 边界与组合

- 负责图形交付：新建/重绘、panel 组合、视觉编码、导出、报告嵌入和 visual QA。
- 只写或润色 caption/legend 且不改图时，用 `figure-caption`。
- 只核查既有 figure 的 source data、producer、统计定义和 repository readiness 时，用 `source-data-audit`；本 Skill 在实际绘图时生成必要 source data，但不替代独立审计。
- 只判断 figure 是否支持 claim 时，用 `claim-evidence-audit`；若审查结果要求重绘，再组合本 Skill。
- 无图形交付的数据清洗、统计或 pipeline 实现用 `bioinfo-analysis-code`；pathway/network 的方法和解释用 `pathway-network-analysis`。

Figure contract、panel hierarchy、main/supplement placement 和最终 figure logic 由用户确认。Agent 提供备选、实现、provenance、敏感性与 QA。

## 工作流程

1. 读取项目边界和相关 Directory Card，确认目标读者、版面、canonical 输出、已有脚本/source data 和是否允许覆盖。
2. 绘图前定义 contract：主信息、panel 角色、数据 universe、n/denominator、过滤与统计、reference/database version、编码、尺寸、导出格式和 caveat。
3. 优先复用兼容的生成脚本；缺少时创建可重跑脚本。不要直接修改原始数据，图形 source data 写入项目约定路径。
4. 先验证 source-data schema、数量、分母和统计定义，再绘图；不同 panel 的 universe 不同则分别声明。
5. 使用清晰、色盲友好且跨 panel 一致的编码。默认导出 PNG + SVG；需要时再加 PDF/TIFF，线条和文字尽量保持 vector。
6. 重新打开导出文件，在最终插入尺寸检查字体、轴、图例、colorbar、误差、panel label、rug/interval lane、裁切和 PNG/SVG 一致性。
7. 图已嵌入报告时，同步链接、caption、alt text、编号和 main/supplement placement；不得让裁剪或隐藏元素改变证据 universe。
8. 交付 figure contract、精确图像/source-data/script 路径、重跑命令、QA、caveat 和版本状态；图形不得暗示未验证的机制或因果。

## 按需资源

- 新图的 contract、panel 角色和 main/supplement 选择：读取 [figure-contract.md](references/figure-contract.md)。
- 从 claim 设计或重组 figure system 时读取 [claim-to-figure-system.md](references/claim-to-figure-system.md)；audit-only 请求转给 `claim-evidence-audit` 或 `source-data-audit`。
- 字体、配色、裁剪、导出、遮挡和链接 QA：读取 [visual-qa.md](references/visual-qa.md)。
- 已嵌入稿件/报告的读者版整合：读取 [reader-facing-report-figure-optimization.md](references/reader-facing-report-figure-optimization.md)。
- 参考既有图形家族并复用原脚本：读取 [reference-figure-script-reuse-and-visual-qa.md](references/reference-figure-script-reuse-and-visual-qa.md)。
- 模型预测、official target 与 observed signal 的 profile 比较：读取 [model-vs-external-profile-figures.md](references/model-vs-external-profile-figures.md)。
- RNA-seq、single-cell、variant、pathway/network 或 interval-hit 图：读取 [omics-figure-qa.md](references/omics-figure-qa.md)。
- 含本地图片的 Markdown 报告导出 PDF：读取 [markdown-report-pdf-export.md](references/markdown-report-pdf-export.md)。

最终回复先给图形结果，再列精确文件、source data、脚本/命令、visual QA、证据边界和剩余风险。
