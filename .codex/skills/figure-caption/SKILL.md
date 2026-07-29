---
name: figure-caption
description: 用于生物信息学论文图表规划、figure title、panel title、legend、caption、figure-to-claim 审查和图注中的 source data/caveat 表达。
---

# Figure Caption

## 核心问题

如何让每个 figure title、panel title 和 caption 准确说明图中数据，同时不把解释性结论塞进图注？

## 使用场景

当用户要求设计图、重排 panel、写图题、写 caption、检查图注是否支持论文 claim 或准备投稿图注时使用本 skill。

## Figure Contract

写图注前先明确：

- Figure 的主 claim
- 每个 panel 的角色
- 输入数据、样本范围和过滤状态
- 统计方法、n、重复或背景集合
- source data 路径或需要生成的 source data
- caveat 和 reviewer risk

## 写作规则

- 图题概括图的结论或信息功能，不堆方法细节。
- Panel title 要短，优先说明 panel 的证据角色。
- Caption 必须能让读者理解数据来源、比较对象、统计和限制。
- Caption 说明“图中显示什么”：panel、坐标轴、编码、n/denominator、统计、数据来源。
- Caption 使用 reader-facing provenance：写 `Source Data`、`Supplementary Table/Figure` 或正式纳入标准，不写本地路径、repository 目录、脚本/表格文件名、内部布尔字段、run ID、raw command options 或作者批注。软件命令、完整参数和阈值放入 Methods；机器专属路径只保留在 manifest 或项目记录。
- 结果解释说明“这意味着什么”：生物学结论、claim 强度、机制解释和下一步验证应放在正文 Results/Discussion，而不是塞进 caption。
- 不在 caption 中写超出图表证据的机制结论。
- 对 exploratory 图明确使用 candidate、putative、consistent with、suggests 等限定。
- 交付前对 caption 做 lab-internal language scan，重点检查路径分隔符、常见数据/脚本扩展名、`source_data`/`scripts`、内部状态字段、pipeline labels 和未解释 candidate IDs；科学上必须保留的 candidate ID 应在首次出现时定义。

## 输出格式

根据任务输出：

- Figure title
- Panel order and panel titles
- Full caption
- Source data checklist
- Caveat / reviewer-risk notes
