# 按需运行与跨设备说明

Skill安装只同步指令，不安装Node.js、Python库、PowerPoint或字体。
优先复用当前可用的演示文稿后端；需要PptxGenJS时在任务工作目录内使用
项目级依赖与lockfile，先检查 `node --version` 和 `npm ls pptxgenjs`。
经用户授权安装后执行 `npm install pptxgenjs`，不要用全局npm安装解决
`require('pptxgenjs')` 的模块查找问题。保留package.json和lockfile，
只在任务目录生成文件，不写入不可变Skill安装目录。

文本读取可用已安装的markitdown，命令 `python -m markitdown input.pptx`。
Windows可将Python前缀替换为 `py -3.11` 或实际环境的python.exe。
若缺库，经授权在隔离环境安装 `python -m pip install "markitdown[pptx]"`，
不要要求为了读取PPT安装全套生信环境。

Node命令在macOS与PowerShell均为 `node compile.js`。创建输出目录后
await `pres.writeFile(...)`，并保留实际异常；不以进程启动作为成功证据。
路径使用Node的path模块，包含空格的shell参数加引号。POSIX参考中的
grep检查可换为PowerShell `Select-String -Pattern`；它只查占位符，
不是完整内容或视觉验收。

中文字体不能假定Microsoft YaHei在macOS存在；使用设备实际存在且
用户认可的字体，交接时记录字体名称和替换风险，不随包上传字体文件。
PPTX的ZIP/XML完整性、文本回读和PowerPoint/LibreOffice渲染是不同检查。
无渲染工具时可交候选稿，但说明视觉检查未完成。科学图嵌入采用原图，
避免以图片生成后端重绘数据来填补排版缺口。
