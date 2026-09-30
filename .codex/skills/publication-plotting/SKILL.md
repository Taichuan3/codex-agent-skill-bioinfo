---
name: publication-plotting
description: 实际生成、重绘或组合科研图，交付 figure contract、可重跑脚本、source data、PNG/SVG 与视觉检查。撰写图注→figure-caption；仅语言润色→对应中英文polishing Skill；仅来源审计→source-data-audit；仅claim审查→claim-evidence-audit；无图分析→bioinfo-analysis-code。
---
# Publication Plotting
## 核心问题
如何交付可追踪、可重建且可读的论文/PPT图？
## 边界
拥有视觉编码、panel组合、导出、报告嵌入与 visual QA；pathway/network 方法解释归 pathway-network-analysis。用户确认 figure contract、panel hierarchy、main/supplement 和最终图形逻辑；技术通过不等于作者接受，不升级机制/因果证据。
## 流程与交付
1. 读项目边界/相关 Directory Card，确认读者、版面、稳定 module/asset ID、canonical 路径、候选/当前状态、脚本/source data、覆盖权限；图号只是映射，不迁移历史。
2. contract 固定主信息、panel角色、universe、n/denominator、过滤/统计、reference/database版本、编码、尺寸、格式、caveat。各panel universe分别声明。
3. 原始数据只读，优先复用兼容脚本，否则写可重跑脚本；先核 schema/数量/分母/统计，再绘图，source data进项目约定路径。
4. 跨panel一致、色盲友好；默认 PNG+SVG（文字线条尽量 vector），按需PDF/TIFF。重新打开最终插入尺寸导出，核字体、轴、图例、colorbar、误差、panel、rug/interval、裁切与PNG/SVG渲染一致性；XML/schema通过不能替代视觉检查，缺少检查时QA仍为 incomplete，不得宣称完成。
5. 已嵌入报告则同步链接/caption/alt/编号/placement；不裁剪隐藏证据universe。交 contract、图/source/script、命令、QA、caveat和版本；delta交 project-state-maintenance，验证根→稳定模块（成熟论文可Result）入口，不仅日期包。

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
