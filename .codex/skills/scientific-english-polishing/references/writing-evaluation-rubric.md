# 写作回归与盲评

仅在测试、比较版本或验收时加载，不是日常写作的强制输出。

## 冻结材料

生成前冻结实际输入、任务范围/编辑层级、预期锚点及输入哈希。原始论文只作诊断参考，不把劣译/乱稿缺失的信息作为必须恢复项。已看过的材料标为 regression；另取独立未见材料作 held-out，不能以原五组回测宣称泛化。

锚点逐项记录：`id, input_span, dimension, expected_relation, output_span, verdict, origin, rationale`。维度包括事实/数字，主张（因果、确定、新颖、范围），结构/枚举/优先级，引用绑定，术语，以及叙事/作者声音。不要用与原文词面相似度评分。

判定：`preserved / weakened / strengthened / lost / added_error / equivalent / uncertain / not_applicable`。归因：`input_error / output_error / recoverable_unrepaired / acceptable_rewrite / unresolved`。同一事实改了位置不等于事实遗漏；原文不是不可质疑的金标准。存在争议时给证据跨度和 uncertain，不硬扣分。

## 独立执行

- 生成者只读候选 Skill、任务和输入，不看预期答案/评分结论。
- 独立评审读取冻结锚点表、实际输入、任务范围、匿名 A/B 输出；需要诊断时另给原文，明确其不是生成输入。不给 Skill 规则或生成者自评分。
- v1/v2 使用同一张表；先冻结各评审意见再综合。不能真正隔离时报告降级，不称盲评。
- 报告逐维度计数、分母及不确定项；无适用项记 NA。数字/因果/引用绑定新增错误、未经许可跨段重排，以及丢失实质主张或枚举项为发布阻断。自然度与作者声音单列，不能被流畅度平均分掩盖。

## 必须覆盖的对照

1. 既有 new/reveal/causal 等主张没有矛盾时不降级；空泛重复可删。
2. 仅相关却称完全证明因果：保留可追溯原句、独立标疑及替代建议，不静默削弱或无条件照发。
3. light 不跨段；structural 可成组移论点/证据/限制/引用。
4. 假设驱动、反常动机、四项枚举与主次保留。
5. 引用跟随支持的子句；不得凭空加 therefore；源文已有 another 不误判。
6. 领域术语混用单列；目的 to reduce 不改成效果 reduced；US/UK 服从参数。

JSON 用例通过解析只证明规格可读；必须另记模型实际执行的输出、评分和限制。少量合成样例通过不等于真实稿件的出版水平已验证。
