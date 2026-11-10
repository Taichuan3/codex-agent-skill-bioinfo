# 写作与PPT跨设备同步

本包43个Skill包含四个写作模块，以及两种独立PPT入口：

| 需求 | 入口 | 运行依赖 |
|---|---|---|
| 中文修改/成稿 | chinese-scientific-polishing | Codex |
| 明确指定Hashimoto中文润色 | hashimoto-scientific-writing | Codex |
| 中译英 | scientific-english-translation | Codex |
| 英文润色 | scientific-english-polishing | Codex |
| 统一图片式幻灯片 | codex-ppt | 可用图像后端；组装用Python库 |
| 可编辑图文/模板修改/读取PPTX | pptx-generator | 可用演示后端，或Node.js/PptxGenJS；文本读取可用markitdown |

安装本仓库不安装软件依赖、字体、插件或API凭据。写作模块可直接使用；
PPT模块只在任务实际需要时检查并配置所选后端。图片式PPT不承诺逐元素可编辑，
图像生成不等于科学原图保真。科学图必须保留来源和原始数值，不能为美化重画数据。

## Windows更新

在仓库根目录使用Python 3.11+：

```powershell
git switch main
git pull --ff-only
py -3.11 scripts/validate_package.py
py -3.11 scripts/install_codex_bioinfo.py
py -3.11 scripts/install_codex_bioinfo.py --apply
```

切换/更新前先保留本机Git修改，不用reset或强制覆盖。新机器先clone再验证安装。
若旧版同名Skill另在用户的 `.codex/skills` 目录，可先运行
`py -3.11 scripts/install_codex_bioinfo.py --retire-packaged-codex-skills`
查看范围，确认后再加 `--apply`。此选项把包内重名旧扩展移入安装备份，
不删除其他扩展。备份中的 `legacy-codex-skills` 可用于恢复原文件；
恢复后不要同时保留重复的发现入口。

重启Codex后检查四个写作名和两个PPT名。运行依赖随各Skill的portable-runtime说明，
不从Mac复制虚拟环境到Windows。安装复制模式测试不等于Windows原生端到端测试，
具体字体、渲染软件、图像服务和凭据仍需在目标机按需确认。
