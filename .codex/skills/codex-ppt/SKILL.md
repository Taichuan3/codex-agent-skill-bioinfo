---
name: codex-ppt
description: 将论文、报告或提纲制作为视觉统一的整页图片式PPT，含样张确认、逐页生成、讲稿和组装；适用于接受页面不可逐对象编辑的演示。需要可编辑文字/图表、原图无损嵌入或修改现有PPT对象时用pptx-generator；不负责科研绘图或正文润色。
---

# 图片式科研演示

## 核心问题

如何把已确认的内容和视觉风格制作成图片式演示，同时保留来源、生成状态与作者确认？

## 范围与边界

- 只负责图片式幻灯片；文字、曲线和形状不是独立可编辑对象。需要原图无损嵌入或逐对象编辑时交给 `pptx-generator`，不默默换后端。
- 内置图像工具优先；仅在不可用、缺少必需能力或用户明确指定时使用 API/CLI。确认后端、模型和数据发送范围后才调用外部 API，不凭历史默认模型名发请求。
- 原始科学图是严格输入，不是重绘参考；生成图片不能证明数值/标注保真。逐项比对数据、坐标轴、标签和图例，不能确认时报告阻塞并建议无损嵌入路线。
- 不改研究结论、数字和证据强度；不自动配置凭据、安装依赖或上传私人素材。安装 Skill 本身不等于依赖已安装。
- 下列文档的 OS 命令以 `docs/portable-runtime.md` 为准；项目目录约定优先，不把最终图或PPT只留在临时目录。

## 流程

1. 阅读输入，确认受众、页数与可编辑性；按 `docs/workflow-gates-and-progress.md` 和 `docs/outline-style-and-sample.md` 先出提纲及逐页素材映射。用户已明确批准的决定不重复询问；否则保留提纲、风格、后端和样张确认门。
2. 按 `docs/backend-selection.md` 选择后端；先生成一页代表样张，获准后才批量生成。记录 sample_generation_method，不推断内置工具未暴露的模型参数。
3. 按 `docs/user-supplied-assets.md` 读取/检查每个源图；本地图先用 view_image 查看，再通过当前工具实际支持的图像引用方式传入；跨会话不假设图片上下文自动继承。
4. 按 `docs/slide-generation-and-subagents.md` 准备自包含 job。样张获准且运行时支持子 Agent 时，每页一个 worker；主 Agent 独占共享状态、最终目录、QA与组装。使用 `prompts/slide-worker.md`，每个 worker 返回真实后端、图片路径和检查结论。不可调用所选后端时停止该页，不用本地绘图代替。
5. 逐页视觉检查；每个非样张结果必须用记录脚本入账。全部 expected slide 已 recorded/accepted 才按 `docs/project-assembly-and-reporting.md` 编写讲稿并组装，不能以文件存在代替视觉或科学验收。
6. 先交PPT及关键限制，再给原图、讲稿和来源入口。按 `project-state-maintenance` 更新本次受影响索引；失败保留可恢复状态，不宣称完成。仅查看已有PPT不新建管理文件。

## 资源按需路由

- 运行前/换机：`docs/portable-runtime.md`、`requirements.txt`；`scripts/codex_ppt_runtime.py` 只在获准后建立隔离依赖或配置API；同步时不带 `.env`、环境和缓存。
- API fallback：`docs/cli-api-fallback.md`、`scripts/image_gen.py`；仅配置失败或用户要求设置时读 `docs/image-model-configuration.md`。`scripts/image_providers/` 是该CLI的内部实现，不独立调用。
- job准备：`scripts/prepare_slide_prompts.py`；状态查询：`scripts/slide_job_status.py`；派发：`scripts/record_slide_dispatch.py`；结果：`scripts/record_slide_result.py`；阻塞：`scripts/record_slide_blocker.py`。`scripts/slide_run_state.py` 是共享状态库，不手改状态JSON。
- 组装：`scripts/assemble_ppt.py`；仅明确需要色键去背景时用 `scripts/remove_chroma_key.py`，它不用于重新绘制科学图或绕过既定图片生成路线。
- 维护/换机验证：`scripts/test_portable_workflow.py` 离线测试CLI、状态、后端不匹配和PPT组装；合成测试图不代表真实生成质量或科研保真通过。
- 保存可复用风格：`docs/style-library.md`，只保存去隐私的视觉规则到本机自定义风格目录，不修改不可变安装快照。
- 选择风格时，按内容只读一份：`references/清爽专业风.md`、`references/科研答辩风.md`、`references/教学课件风.md`、`references/数据仪表盘风.md`、`references/创意杂志风.md`、`references/电子墨水杂志风.md`、`references/复古扁平插画风.md`、`references/手绘技术解释风.md`、`references/手绘白板风.md`、`references/温暖手工风.md`、`references/麦肯锡风格.md`、`references/党政红风格.md`。自定义同名风格按用户约定优先，不批量读取全部样式。

## 交付契约

交付正式PPT、outline、speech（需要讲稿时）、origin_image和job状态的精确路径；说明图片式可编辑性限制、页数、后端及未通过项。来源图与生成图分开保存，追踪逐页输入；不把视觉漂亮等同科学正确。不因缺少单页素材、依赖或授权而伪造完整稿；先交已完成部分并定位阻塞页。

## 来源

基于 ningzimu/codex-ppt-skill 的 MIT 版本；本包保留脚本与按需文档，压缩入口、补跨平台运行及科研保真边界。精确版本和改动见包级来源记录，原版权声明见 `LICENSE`。
