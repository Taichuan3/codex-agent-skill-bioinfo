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
