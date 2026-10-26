# 中文优先写作模块

正文写作采用独立入口，不强制每次串联全部步骤。

| 交付物 | Skill ID | 边界 |
|---|---|---|
| 中文修改、证据/框架到正文 | chinese-scientific-polishing | 中文主入口，含结构和自然表达；保留历史ID |
| 中文润色（Hashimoto风格） | hashimoto-scientific-writing | 可选、独立的本机风格扩展，只有明确点名才使用；本portable包不分发 |
| 英文翻译 | scientific-english-translation | 明确要求翻译时使用；中文确认本身不启动英文 |
| 英文润色 | scientific-english-polishing | 已有英文的结构/表达及科研约束去套话 |

Nature写作机制及Humanizer编辑启发已独立改编到相关正文模块，不安装上游路由、更新器或整套工作流。Hashimoto不默认混入其他模块。跨设备安装本包只获得其中三个portable入口；Hashimoto需另有获授权的独立本机副本，缺失时说明，不假称已具备。

保真优先于风格。用事实充分的小节、缺证框架、冲突数字、阴性观察、成熟段落和打乱中文测试；静态eval与隔离短文测试不是完整论文出版质量的证明。后续作者盲测先中文、确认后再明确要求英文。

三个 portable 模块共用 [编辑保真契约](../.codex/skills/scientific-english-polishing/references/editing-fidelity-contract.md)：起草新主张不越过证据，修改已有主张不静默加强或削弱；疑似过强单列作者核对项。普通润色/翻译默认 light（段内），明确重组采用 structural；保留假设驱动、枚举主次、作者声音、引用绑定与目的/效果区别。英文拼写按用户/期刊参数，否则沿用输入。

比较验收使用 [锚点评分表规范](../.codex/skills/scientific-english-polishing/references/writing-evaluation-rubric.md)。先冻结实际输入和任务范围，再独立评价；区分输入损坏、输出错误和合理改写。已见材料仅作回归，不作盲测。此轮机制为本地反馈的独立总结，没有引入新的外部代码或论文语料；既有来源与许可不变。
