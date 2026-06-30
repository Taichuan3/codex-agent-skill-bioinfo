# All External Skill / Agent Repository Structure Audit

> Date: 2026-06-30. Branch: `Hermes-review`. Scope: all previously collected external skill/agent repositories, shallow-cloned under `/Users/yajiehu/.hermes/tmp/external-skill-sources/`. This is an audit artifact, not runtime installation.

## 0. User-directed change in strategy

- Previous approach: P0/P1/P2 staged audit.
- Updated approach: first inspect every collected repository, then do 2–3 cross-review passes because overlapping skills may solve each other's gaps.
- Merge principle: keep the user's GitHub repo as source of truth; absorb modules/ideas, not whole large repositories; default runtime skills remain only the mature subset.

## 1. Current local baselines

- Source candidate repo: `/Users/yajiehu/.hermes/tmp/codex-agent-skill-bioinfo`
- Candidate skills in source repo: 29 after second-pass split/refactor (`scientific-database-grounding`, `protein-structure-docking`, `drug-discovery-admet-screening` included)
- Hermes default runtime bioinfo skills: 10

### 1.1 Candidate source skills
- `bioinfo-analysis-code` — 用于生物信息学分析脚本、表格整理、轻量统计、Jupyter/CLI 工作流、运行命令、环境记录、可重复性说明、代码整理和发表前代码可读性优化。
- `chinese-scientific-polishing` — 用于中文科研文本润色、结构优化和可读性提升，包括摘要、引言、结果、讨论、图注、项目说明和审稿回复草稿。只做中文层面的润色，不做英文翻译；必须保护证据边界，并根据文稿部分控制数据密度和叙事功能。
- `citation-verifier` — 用于核验科研文本中的引用、DOI、PMID、BibTeX、参考文献条目和 claim-to-citation 是否匹配，防止引用幻觉、错误文献、错配 citation 或 unsupported citation。适用于论文写作、投稿前检查、文献表整理和审稿回复。
- `claim-evidence-audit` — 用于审查论文文本、结果解释、图注、审稿回复或投稿前材料中的生物信息学 claim 是否被 figure/table/source data/citation/caveat 充分支持，并给出证据等级、风险和安全降级写法。不用于普通代码执行、绘图实现、文件整理或环境安装。
- `drug-discovery-admet-screening` — 用于药物靶点探索、virtual screening、ADMET/QSAR、drug repurposing、target validation 和小分子筛选策略的候选工作流设计、数据库 grounding、工具选择、结果优先级排序和证据边界控制。
- `environment-and-tool-adoption` — 用于在生物信息学任务中安装缺失的 Python/R/命令行包，评估并采用 GitHub 工具、论文代码、官方 protocol 或成熟软件，避免重复造轮子，同时记录版本、来源、license、环境和适配改动。
- `evidence-gap-finder` — 用于从已有结果、论文草稿、figure plan、claim-evidence map 或审稿风险中找出缺失证据、过弱 claim、未闭合 caveat 和最小补分析集合。适用于准备加强论文证据链或决定下一步补什么分析。
- `figure-caption` — 用于生物信息学论文图表规划、figure title、panel title、legend、caption、figure-to-claim 审查和图注中的 source data/caveat 表达。
- `literature-search-workflow` — 用于生物信息学或计算生物学项目的系统文献检索、关键词设计、数据库选择、纳入排除标准、证据表和知识缺口整理。适用于项目启动、补证据、查找方法依据或为论文背景寻找文献；不用于阅读单篇指定论文。
- `manuscript-consistency-audit` — 用于检查科研稿件内部一致性，包括摘要、正文、结果标题、图注、方法、补充表、source data 和引用中的数字、术语、样本集合、过滤标准、figure/table 编号和 claim 表述是否冲突。
- `paper-reader` — 用于阅读用户指定的科研论文、PDF、全文 markdown 或网页论文，并输出中文结构化阅读笔记、关键证据、figure grounding、可借鉴方法和局限。不用于开放式文献检索；需要查找新文献时使用 literature-search-workflow。
- `project-environment-bootstrap` — 用于新生信项目启动、切换机器或工作目录、运行分析前环境不明、缺少 PROJECT_ENVIRONMENT.md、conda/Jupyter/VS Code/GitHub 同步配置检查和本地环境记录初始化。不用于日常编码、绘图、分析、写作、翻译或已确认环境下的小任务。
- `project-guide-maintainer` — 用于创建、更新或压缩生物信息学项目的轻量 PROJECT_GUIDE.md 项目指导文件。适用于需要把 research-project-planner 和 research-question-brief 的输出整合成可长期读取的研究背景、核心问题、主线、路线、当前进度、结果框架和论文草稿骨架；也适用于用户要求“维护项目指导文件”“更新研究主线”“把当前进展
- `protein-structure-docking` — 用于蛋白结构与 docking 任务的输入定义锁定、结构来源选择、protein-ligand 或 protein-protein docking 工具选择、运行计划、结果 QC 和证据边界控制。
- `publication-plotting` — 用于生物信息学 manuscript-ready figures、PPT 可读图、论文主图/补图的 figure contract、source data、panel hierarchy、Python/R 绘图、PNG/SVG 导出、字体配色统一、遮挡检查和 visual QA。不用于一般数据分析或单纯 claim 审查。
- `research-data-organization` — 用于组织生物信息学项目的数据、表格、结果、图和常用文件路径，解决结果分散、最新文件不清、重要表格难找、投稿数据难汇总的问题。适用于建立目录结构、整理 latest/priority 文件、设计 manifest、迁移常用结果到一级目录或索引表。
- `research-decision-review` — 用于在已经理解用户需求和必要背景后，对生物信息学研究中的高影响决策进行建设性反对和取舍评估，包括分析方案、论文结构、外部工具采用、证据解释、是否继续/转向/停止、是否重写已有方法。适用于用户问“这样做合理吗”“要不要采用这个工具/方法”“是否值得继续”“我是不是过度解释了”“要不要自己重写代码”，或当前方案明显存在证据、复现、成本或审稿风险的场景；不用于普通
- `research-project-planner` — 用于生物信息学或计算生物学项目启动前，将模糊研究方向转成可执行研究路线：澄清 central question、knowledge gap、hypothesis、evidence package、figure skeleton、技术路线、风险和 stop/pivot criteria。不用于已明确的代码执行、单篇论文阅读或单纯文本润色。
- `research-question-brief` — 用于把用户口头、零散或多轮讨论中的研究想法压缩成简短 research question brief，保留 one-line idea、working question、why it matters、evidence needed、constraints 和 next decision。不用于完整技术路线设计、文献检索或项目执行。
- `reviewer-response-builder` — 用于处理真实审稿意见、返修信、editor decision 或合作者批注，将评论拆解为 response table、行动计划、补分析优先级、正文修改点和礼貌但有边界的回复草稿。不用于模拟潜在审稿人风险；模拟风险使用 reviewer-simulation。
- `reviewer-simulation` — 用于模拟生物信息学论文审稿人，识别证据链、统计、复现、图表、方法、机制解释和期刊叙事风险，并生成 response strategy 或补分析优先级。
- `scientific-database-grounding` — 用于生物信息学研究中需要查询或核验科学数据库时，围绕基因、变异、调控元件、表达、蛋白结构、化合物、药物靶点和文献记录建立可追踪的 database grounding。
- `scientific-english-polishing` — 用于已有英文科研文本的润色、压缩、段落重构、标题/摘要/图注/response letter 英文打磨和学术语气检查；必须保护证据边界，不能升级科学 claim。中文到英文翻译使用 `scientific-english-translation`。
- `scientific-english-translation` — 用于将中文科研文本翻译为英文，或把中文草稿转成证据边界安全的英文科研表达，适用于摘要、引言、结果、讨论、方法、图注、回复信和标题。不负责中文润色，也不应为了更像高水平期刊而升级 claim。
- `skill-quality-audit` — 用于审查本地 Codex/Agent skill 的质量、触发描述、结构完整性、上下文占用、references 拆分、安全风险、科研诚信边界和可维护性。适用于用户要求“检查这个 skill”“优化 skill”“这个 skill 是否太长/会误触发”“按 Anthropic/AIPOCH 思路审计 skill”等场景。
- `source-data-audit` — 用于构建或审查生物信息学论文 source-data inventory、numbers-to-lock、figure/table-to-source traceability、Data/Code Availability、FAIR-like metadata、repository/accession plan 和关键文字证据来源。
- `submission-readiness-audit` — 用于生物信息学论文投稿前或大版本收尾前的综合预检，检查主文、图表、方法、source data、代码、数据可用性、引用、补充材料和审稿风险是否达到可投稿状态。不用于普通任务交付前轻量自检。
- `task-self-check` — 用于任何生物信息学研究任务交付前的轻量自检，检查证据是否支撑 claim、文件是否可追踪、代码是否可复现、图表是否可读、文字是否越界，以及是否需要记录建议更新项。适用于用户要求“检查一下”“自检”“交付前 QA”“看看有没有问题”，或任务完成前需要统一质量门控的场景。
- `validation-strategy-planner` — 用于为探索性生物信息学结果、候选机制、模型结论、富集结果或审稿风险设计验证策略，区分计算验证、外部数据验证、统计敏感性分析、实验验证和降级写法。

### 1.2 Default runtime bioinfo skills
- `bioinfo-analysis-code` — 用于生物信息学分析脚本、表格整理、轻量统计、Jupyter/CLI 工作流、运行命令、环境记录、可重复性说明、代码整理和发表前代码可读性优化。
- `chinese-scientific-polishing` — 用于中文科研报告、论文草稿、结果段、摘要、引言、讨论、Methods 和图注的可读性润色；强调读者能读懂、证据链清楚、术语一致，而不是堆砌论文腔或过度安全声明。
- `claim-evidence-audit` — 用于审查论文文本、结果解释、图注、审稿回复或投稿前材料中的生物信息学 claim 是否被 figure/table/source data/citation/caveat 充分支持，并给出证据等级、风险和安全降级写法。不用于普通代码执行、绘图实现、文件整理或环境安装。
- `literature-search-workflow` — 用于生物信息学或计算生物学项目的系统文献检索、关键词设计、数据库选择、纳入排除标准、证据表和知识缺口整理。适用于项目启动、补证据、查找方法依据或为论文背景寻找文献；不用于阅读单篇指定论文。
- `paper-reader` — 用于阅读用户指定的科研论文、PDF、全文 markdown 或网页论文，并输出中文结构化阅读笔记、关键证据、figure grounding、可借鉴方法和局限。不用于开放式文献检索；需要查找新文献时使用 literature-search-workflow。
- `publication-plotting` — 用于生物信息学 manuscript-ready figures、PPT 可读图、论文主图/补图的 figure contract、source data、panel hierarchy、Python/R 绘图、PNG/SVG 导出、字体配色统一、遮挡检查和 visual QA。不用于一般数据分析或单纯 claim 审查。
- `research-project-planner` — 用于生物信息学或计算生物学项目启动前，将模糊研究方向转成可执行研究路线：澄清 central question、knowledge gap、hypothesis、evidence package、figure skeleton、技术路线、风险和 stop/pivot criteria。不用于已明确的代码执行、单篇论文阅读或单纯文本润色。
- `research-question-brief` — 用于把用户口头、零散或多轮讨论中的研究想法压缩成简短 research question brief，保留 one-line idea、working question、why it matters、evidence needed、constraints 和 next decision。不用于完整技术路线设计、文献检索或项目执行。
- `scientific-english-polishing` — 用于已有英文科研文本的润色、压缩、段落重构、标题/摘要/图注/response letter 英文打磨和学术语气检查；必须保护证据边界，不能升级科学 claim。中文到英文翻译使用 `scientific-english-translation`。
- `scientific-english-translation` — 用于将中文科研文本翻译为英文，或把中文草稿转成证据边界安全的英文科研表达，适用于摘要、引言、结果、讨论、方法、图注、回复信和标题。不负责中文润色，也不应为了更像高水平期刊而升级 claim。

## 2. External repository inventory

| Repo | Commit | License | SKILL.md | Agent YAML | Python files | Main role |
|---|---:|---|---:|---:|---:|---|
| `ClawBio_ClawBio` | `fbb0910` | MIT | 92 | 29 | 499 | local-first 生信执行与 benchmark |
| `GPTomics_bioSkills` | `c8d4039` | MIT | 553 | 0 | 399 | 超大生信覆盖词典/缺口发现 |
| `K-Dense-AI_scientific-agent-skills` | `0807ddb` | MIT | 149 | 9 | 298 | 跨学科科学 skill 地图 |
| `NVIDIA-BioNeMo_bionemo-agent-toolkit` | `54fc67c` | Apache-2.0 | 65 | 0 | 41 | protein/docking/generative biology agent toolkit |
| `NVIDIA_skills` | `2dceed6` | Apache-2.0 | 238 | 481 | 341 | NVIDIA 官方 AI/GPU workflow |
| `VoltAgent_awesome-agent-skills` | `934b1e8` | MIT | 0 | 0 | 0 | 索引目录/生态雷达 |
| `Yuan1z0825_nature-skills` | `af29cdd` | Apache-2.0 | 14 | 15 | 63 | 科研写作/审稿/图表 router 参考 |
| `adaptyvbio_protein-design-skills` | `59dd633` | MIT | 24 | 0 | 0 | protein/binder design 专项 |
| `addyosmani_agent-skills` | `aba7c4e` | MIT | 24 | 1 | 0 | 工程质量与生产实践 |
| `affaan-m_ECC` | `81af407` | MIT | 887 | 55 | 62 | 大而全 agent/skill/memory/security 参考 |
| `agentskills_agentskills` | `5d4c1fd` | Apache-2.0 | 0 | 0 | 11 | Agent Skills spec/标准参考 |
| `anthropics_skills` | `3541475` | unknown | 18 | 0 | 72 | 官方 skill 规范参考 |
| `google-deepmind_science-skills` | `33557e0` | Apache-2.0 | 37 | 0 | 63 | 科学数据库 grounding |
| `google_skills` | `dae4b19` | Apache-2.0 | 67 | 22 | 28 | Google 官方 skill 结构参考 |
| `huggingface_skills` | `35e8c35` | Apache-2.0 | 20 | 7 | 41 | HF Hub/model/dataset workflow |
| `learningmatter-mit_AtomisticSkills` | `ca695e1` | MIT | 127 | 55 | 349 | 原子/化学/材料计算 workflow |
| `mattpocock_skills` | `43ea088` | MIT | 36 | 1 | 0 | 工程重构/TypeScript/质量实践 |
| `muratcankoylan_Agent-Skills-for-Context-Engineering` | `175cee7` | MIT | 21 | 5 | 49 | 上下文工程与多 agent 参考 |
| `obra_superpowers` | `896224c` | MIT | 14 | 3 | 1 | agentic workflow / planning 方法论 |
| `openai_skills` | `49f948f` | unknown | 44 | 57 | 42 | Codex skill 结构参考 |

Full machine-readable inventory: `docs/external-skill-audits/all_external_repos_inventory.csv`.

## 3. First-pass thematic hits across all repositories

### variant/genetics
- `ClawBio_ClawBio` / `clinical-trial-finder` — `skills/clinical-trial-finder/SKILL.md` — Find clinical trials for a gene, variant, or condition from ClinicalTrials.gov + EUCTR, with FHIR R4 output
- `ClawBio_ClawBio` / `clinical-variant-reporter` — `skills/clinical-variant-reporter/SKILL.md` — Classify germline variants from VCF/BCF files according to the ACMG/AMP 2015 28-criteria evidence framework and
- `ClawBio_ClawBio` / `gwas-lookup` — `skills/gwas-lookup/SKILL.md` — Federated variant lookup across 9 genomic databases — GWAS Catalog, Open Targets, PheWeb (UKB, FinnGen, BBJ),
- `ClawBio_ClawBio` / `rare-high-impact-variants` — `skills/rare-high-impact-variants/SKILL.md` — >-
- `ClawBio_ClawBio` / `variant-annotation` — `skills/variant-annotation/SKILL.md` — Annotate VCF variants with Ensembl VEP REST, ClinVar significance, gnomAD/population frequency context, and prioritized
- `ClawBio_ClawBio` / `vcf-annotator` — `skills/vcf-annotator/SKILL.md` — Annotate VCF variants with Ensembl VEP, ClinVar, and gnomAD. Ranks variants by impact (HIGH/MODERATE/LOW/MODIFIER) and generates a reproducible report.
- `ClawBio_ClawBio` / `wgs-prs` — `skills/wgs-prs/SKILL.md` — End-to-end WGS to polygenic risk score pipeline. Takes paired-end FASTQ files (or a pre-existing VCF) through nf-core/sarek for variant calling, applies VCF QC (normalisation, hard filtering,
- `GPTomics_bioSkills` / `bio-alignment-sorting` — `alignment-files/alignment-sorting/SKILL.md` — Sort alignment files by coordinate or read name using samtools and pysam. Use when preparing BAM files for indexing, variant calling, or paired-end analysis.
- `GPTomics_bioSkills` / `bio-alignment-validation` — `alignment-files/alignment-validation/SKILL.md` — Validate alignment quality with insert size distribution, proper pairing rates, GC bias, strand balance, and other post-alignment metrics. Use when verifying alignment data quality before variant calling or quantificatio
- `GPTomics_bioSkills` / `bio-duplicate-handling` — `alignment-files/duplicate-handling/SKILL.md` — Mark and remove PCR/optical duplicates using samtools fixmate and markdup. Use when preparing alignments for variant calling or when duplicate reads would bias analysis.
- `GPTomics_bioSkills` / `bio-pileup-generation` — `alignment-files/pileup-generation/SKILL.md` — Generate pileup data for variant calling using samtools mpileup and pysam. Use when preparing data for variant calling, analyzing per-position read data, or calculating allele frequencies.
- `GPTomics_bioSkills` / `bio-outlier-splicing-detection` — `alternative-splicing/outlier-splicing-detection/SKILL.md` — Detects aberrant splicing in single rare-disease patients vs a control panel using FRASER 2.0 (Bioconductor; Beta-binomial autoencoder on Intron Jaccard Index, default delta cutoff 0.1, q hyperparameter), OUTRIDER (gene-

### genomics
- `ClawBio_ClawBio` / `archaic-introgression` — `skills/archaic-introgression/SKILL.md` — Detect Neanderthal and Denisovan introgression segments from modern human genomes
- `ClawBio_ClawBio` / `claw-ancestry-pca` — `skills/claw-ancestry-pca/SKILL.md` — Ancestry decomposition PCA against the Simons Genome Diversity Project
- `ClawBio_ClawBio` / `claw-metagenomics` — `skills/claw-metagenomics/SKILL.md` — Shotgun metagenomics profiling — taxonomy, resistome, and functional pathways
- `ClawBio_ClawBio` / `clinpgx` — `skills/clinpgx/SKILL.md` — Query the ClinPGx API for pharmacogenomic gene-drug data, clinical annotations, CPIC guidelines, and FDA drug
- `ClawBio_ClawBio` / `genome-compare` — `skills/genome-compare/SKILL.md` — Compare your genome to George Church (PGP-1) and estimate ancestry composition via IBS and EM admixture
- `ClawBio_ClawBio` / `genome-match` — `skills/genome-match/SKILL.md` — Score genetic compatibility across all male-female pairings in a Genomebook generation
- `ClawBio_ClawBio` / `gi-annotation` — `skills/gi-annotation/SKILL.md` — Predict gene and transcript structure (intervals, exons, strand) from a DNA sequence using the Genomic Intelligence DNA Annotation model, via the hosted /v1/tasks/annotation/predict API. Async-only
- `ClawBio_ClawBio` / `gi-chromatin` — `skills/gi-chromatin/SKILL.md` — Predict chromatin state — histone marks, DNase, TF binding — across 919 tracks (DeepSEA-style) for DNA sequences, via the hosted Genomic Intelligence /v1/tasks/chromatin/predict API.
- `ClawBio_ClawBio` / `gi-enhancer` — `skills/gi-enhancer/SKILL.md` — Predict enhancer activity in DNA sequences using the Genomic Intelligence G0 DeepSTARR model, via the hosted /v1/tasks/enhancer/predict API. Returns per-window activity scores.
- `ClawBio_ClawBio` / `gi-expression` — `skills/gi-expression/SKILL.md` — Predict tissue / cell-type expression (log TPM + TPM) from a 9,198 bp TSS-centered DNA sequence using the Genomic Intelligence G0 Expression model, via the hosted /v1/tasks/expression/predict
- `ClawBio_ClawBio` / `gi-promoter` — `skills/gi-promoter/SKILL.md` — Detect promoter regions in DNA sequences using the Genomic Intelligence G0 transformer (GENA-LM BERT Large), via the hosted /v1/tasks/promoter/predict API. Returns per-window promoter probabilities
- `ClawBio_ClawBio` / `gi-splice` — `skills/gi-splice/SKILL.md` — Detect splice donor and acceptor sites in DNA sequences using the Genomic Intelligence G0 BigBird transformer, via the hosted /v1/tasks/splice/predict API. Returns per-position site probabilities

### alphagenome
- `google-deepmind_science-skills` / `alphagenome-single-variant-analysis` — `skills/alphagenome_single_variant_analysis/SKILL.md` — >

### protein/structure
- `ClawBio_ClawBio` / `analyze-fasta` — `skills/analyze-fasta/SKILL.md` — Analyze a single FASTA file (nucleotide or protein), compute sequence-level metrics (GC, ORFs, MW, pI, GRAVY, secondary-structure fractions) with Biopython, and write a Markdown report plus structured JSON for downstream
- `ClawBio_ClawBio` / `struct-predictor` — `skills/struct-predictor/SKILL.md` — Protein structure prediction with Boltz-2. Accepts YAML inputs (single protein or multi-chain complex), runs
- `GPTomics_bioSkills` / `bio-alignment-pairwise` — `alignment/pairwise-alignment/SKILL.md` — Perform pairwise sequence alignment using Biopython Bio.Align.PairwiseAligner. Use when comparing two sequences, finding optimal alignments, scoring similarity, and identifying local or global matches between DNA, RNA, o
- `GPTomics_bioSkills` / `bio-alignment-structural` — `alignment/structural-alignment/SKILL.md` — Align protein structures using Foldseek 3Di, TM-align, US-align, DALI, or Foldmason for structural MSA. Predict, score, and superpose backbone coordinates when sequence identity is below the twilight zone or remote-homol
- `GPTomics_bioSkills` / `bio-isoform-switching` — `alternative-splicing/isoform-switching/SKILL.md` — Analyzes differential transcript usage (DTU) and isoform switches with functional consequence prediction (NMD via 50nt rule, ORF disruption, protein domain loss/gain, signal peptide changes, IDR alterations, coding-poten
- `GPTomics_bioSkills` / `bio-causal-genomics-mediation-analysis` — `causal-genomics/mediation-analysis/SKILL.md` — Decompose total effects into direct and indirect paths through mediators using mediation, CMAverse 4-way, HIMA/HIMA2 high-dimensional, BAMA, two-step / MVMR mediation, or double-ML medDML. Use when testing whether a mole
- `GPTomics_bioSkills` / `bio-causal-genomics-proteome-mr-drug-target` — `causal-genomics/proteome-mr-drug-target/SKILL.md` — Runs cis-pQTL Mendelian randomization for drug-target validation using UKB-PPP (Olink), deCODE (SomaScan), Fenland, INTERVAL, ARIC, and FinnGen-PPP proteomes plus colocalization triangulation, phenome-wide on-target adve
- `GPTomics_bioSkills` / `bio-ml-docking-rescoring` — `chemoinformatics/ml-docking-rescoring/SKILL.md` — Performs ML-based protein-ligand pose prediction and scoring using DiffDock-L (diffusion-based), Boltz-1 / Boltz-2 (foundation model with affinity), Chai-1, AlphaFold3 ligand, EquiBind, TANKBind, NeuralPLexer, and hybrid
- `GPTomics_bioSkills` / `bio-pose-validation` — `chemoinformatics/pose-validation/SKILL.md` — Validates docked / generated protein-ligand poses using PoseBusters physical-validity tests, strain energy quantification, geometric checks (planarity, vdW overlap, bond/angle distortion), and pose-energy reasonableness.
- `GPTomics_bioSkills` / `bio-protac-degraders` — `chemoinformatics/protac-degraders/SKILL.md` — Designs PROTACs, molecular glues, and bivalent degraders with explicit handling of E3 ligase choice (VHL, CRBN, IAP, MDM2, KEAP1), linker design (length, composition, rigidity), ternary complex prediction (PRosettaC, Dee
- `GPTomics_bioSkills` / `bio-virtual-screening` — `chemoinformatics/virtual-screening/SKILL.md` — Performs structure-based virtual screening using AutoDock Vina, SMINA, GNINA (CNN scoring), and DiffDock-L hybrid workflows with explicit choice rules across rigid vs flexible docking, cross-docking vs self-docking, bind
- `GPTomics_bioSkills` / `bio-clip-seq-clip-peak-calling` — `clip-seq/clip-peak-calling/SKILL.md` — Call protein-RNA binding sites from CLIP-seq BAM with CLIPper, PureCLIP, Skipper, Piranha, omniCLIP, CTK, CLAM, or Paraclu. Use when choosing between coverage-based, HMM-based, beta-binomial window-based, and crosslink-s

### docking/drug
- `ClawBio_ClawBio` / `clinpgx` — `skills/clinpgx/SKILL.md` — Query the ClinPGx API for pharmacogenomic gene-drug data, clinical annotations, CPIC guidelines, and FDA drug
- `ClawBio_ClawBio` / `drug-photo` — `skills/drug-photo/SKILL.md` — Medication photo to personalised PGx dosage card via Claude vision — snap a pill, get genotype-informed guidance
- `ClawBio_ClawBio` / `drug-repurposing-screen` — `skills/drug-repurposing-screen/SKILL.md` — >-
- `ClawBio_ClawBio` / `pharmgx-reporter` — `skills/pharmgx-reporter/SKILL.md` — Pharmacogenomic report from DTC genetic data (23andMe/AncestryDNA) — 12 genes, 31 SNPs, 51 drugs
- `ClawBio_ClawBio` / `target-validation-scorer` — `skills/target-validation-scorer/SKILL.md` — Evidence-grounded target validation scoring with GO/NO-GO decisions for drug discovery campaigns
- `GPTomics_bioSkills` / `bio-causal-genomics-mendelian-randomization` — `causal-genomics/mendelian-randomization/SKILL.md` — Estimate causal effects of an exposure on an outcome from GWAS summary statistics using genetic instruments. Implements IVW (fixed/random), MR-Egger, weighted median/mode, MR-RAPS, CAUSE, GSMR-HEIDI, MR-PRESSO, MVMR, MR-
- `GPTomics_bioSkills` / `bio-causal-genomics-proteome-mr-drug-target` — `causal-genomics/proteome-mr-drug-target/SKILL.md` — Runs cis-pQTL Mendelian randomization for drug-target validation using UKB-PPP (Olink), deCODE (SomaScan), Fenland, INTERVAL, ARIC, and FinnGen-PPP proteomes plus colocalization triangulation, phenome-wide on-target adve
- `GPTomics_bioSkills` / `bio-admet-prediction` — `chemoinformatics/admet-prediction/SKILL.md` — Predicts ADMET properties using ADMETlab 3.0 (119 endpoints with uncertainty), ADMET-AI, DeepChem MolNet, and chemprop D-MPNN with explicit handling of OECD QSAR principles, applicability domain assessment, calibration, 
- `GPTomics_bioSkills` / `bio-conformer-generation` — `chemoinformatics/conformer-generation/SKILL.md` — Generates 3D conformer ensembles using RDKit ETKDGv3 with knowledge-enhanced distance geometry, MMFF94/UFF force-field optimization, CREST + GFN2-xTB semi-empirical refinement, and macrocycle-aware torsion preferences. P
- `GPTomics_bioSkills` / `bio-covalent-design` — `chemoinformatics/covalent-design/SKILL.md` — Designs covalent inhibitors and warheads targeting cysteine (most common, 98% of covalent drugs), lysine, serine, threonine, tyrosine, and aspartate residues, with explicit handling of warhead reactivity (acrylamide, chl
- `GPTomics_bioSkills` / `bio-free-energy-calculations` — `chemoinformatics/free-energy-calculations/SKILL.md` — Performs alchemical free-energy calculations including relative binding free energy (RBFE / FEP+) and absolute binding free energy (ABFE) via OpenFE, FEP+, GROMACS, AMBER pmemd, and OpenMM with explicit lambda window sch
- `GPTomics_bioSkills` / `bio-generative-design` — `chemoinformatics/generative-design/SKILL.md` — Designs novel molecules using REINVENT 4 (de novo, scaffold decoration, linker design, R-group, molecular optimization), MolMIM, Diffusion-based generators (DiGress, DiffSMol), and JT-VAE with explicit handling of multi-

### chemistry
- `GPTomics_bioSkills` / `bio-single-cell-splicing` — `alternative-splicing/single-cell-splicing/SKILL.md` — Analyzes alternative splicing at single-cell resolution. The first decision is library chemistry — 10X 3' is fundamentally limited (RT primes from poly-A, R2 falls in 3' UTR, <0.1 junction read per cell per AS event). Pl
- `GPTomics_bioSkills` / `bio-admet-prediction` — `chemoinformatics/admet-prediction/SKILL.md` — Predicts ADMET properties using ADMETlab 3.0 (119 endpoints with uncertainty), ADMET-AI, DeepChem MolNet, and chemprop D-MPNN with explicit handling of OECD QSAR principles, applicability domain assessment, calibration, 
- `GPTomics_bioSkills` / `bio-conformer-generation` — `chemoinformatics/conformer-generation/SKILL.md` — Generates 3D conformer ensembles using RDKit ETKDGv3 with knowledge-enhanced distance geometry, MMFF94/UFF force-field optimization, CREST + GFN2-xTB semi-empirical refinement, and macrocycle-aware torsion preferences. P
- `GPTomics_bioSkills` / `bio-covalent-design` — `chemoinformatics/covalent-design/SKILL.md` — Designs covalent inhibitors and warheads targeting cysteine (most common, 98% of covalent drugs), lysine, serine, threonine, tyrosine, and aspartate residues, with explicit handling of warhead reactivity (acrylamide, chl
- `GPTomics_bioSkills` / `bio-free-energy-calculations` — `chemoinformatics/free-energy-calculations/SKILL.md` — Performs alchemical free-energy calculations including relative binding free energy (RBFE / FEP+) and absolute binding free energy (ABFE) via OpenFE, FEP+, GROMACS, AMBER pmemd, and OpenMM with explicit lambda window sch
- `GPTomics_bioSkills` / `bio-generative-design` — `chemoinformatics/generative-design/SKILL.md` — Designs novel molecules using REINVENT 4 (de novo, scaffold decoration, linker design, R-group, molecular optimization), MolMIM, Diffusion-based generators (DiGress, DiffSMol), and JT-VAE with explicit handling of multi-
- `GPTomics_bioSkills` / `bio-ml-docking-rescoring` — `chemoinformatics/ml-docking-rescoring/SKILL.md` — Performs ML-based protein-ligand pose prediction and scoring using DiffDock-L (diffusion-based), Boltz-1 / Boltz-2 (foundation model with affinity), Chai-1, AlphaFold3 ligand, EquiBind, TANKBind, NeuralPLexer, and hybrid
- `GPTomics_bioSkills` / `bio-molecular-descriptors` — `chemoinformatics/molecular-descriptors/SKILL.md` — Calculates molecular fingerprints (ECFP/Morgan, FCFP, MACCS, RDKit, AtomPair, TopologicalTorsion, Avalon, MAP4, MHFP6) and physicochemical descriptors (Lipinski, QED, TPSA, Crippen LogP, 3D shape) with explicit choice ta
- `GPTomics_bioSkills` / `bio-molecular-io` — `chemoinformatics/molecular-io/SKILL.md` — Reads, writes, and converts molecular file formats (SMILES, InChI, SDF V2000/V3000, MOL2, PDB, MMTF) using RDKit and Open Babel with rigorous handling of aromaticity perception, stereochemistry, implicit/explicit hydroge
- `GPTomics_bioSkills` / `bio-molecular-standardization` — `chemoinformatics/molecular-standardization/SKILL.md` — Standardizes molecular structures using ChEMBL chembl_structure_pipeline and RDKit rdMolStandardize covering sanitization, salt/solvent stripping, neutralization, tautomer canonicalization, stereochemistry standardizatio
- `GPTomics_bioSkills` / `bio-pharmacophore-modeling` — `chemoinformatics/pharmacophore-modeling/SKILL.md` — Builds and applies 3D pharmacophore models using RDKit Pharm3D, the apo2ph4 receptor-based workflow (Heider et al 2022/2023 J Chem Inf Model 63:147-158), Pharmer / Pharmit (search), and PharmacoForge (diffusion-based gen
- `GPTomics_bioSkills` / `bio-pose-validation` — `chemoinformatics/pose-validation/SKILL.md` — Validates docked / generated protein-ligand poses using PoseBusters physical-validity tests, strain energy quantification, geometric checks (planarity, vdW overlap, bond/angle distortion), and pose-energy reasonableness.

### rnaseq
- `ClawBio_ClawBio` / `celltype-specificity-profiler` — `skills/celltype-specificity-profiler/SKILL.md` — Given a gene and a single-cell atlas, compute how cell-type-specific its expression is — the tau specificity index, Sarle's expression bimodality coefficient, and the cell types that drive the signal; a pure analytic tra
- `ClawBio_ClawBio` / `diff-visualizer` — `skills/diff-visualizer/SKILL.md` — Rich downstream visualisation and reporting for bulk RNA-seq differential expression and scRNA marker/contrast
- `ClawBio_ClawBio` / `nfcore-rnaseq-wrapper` — `skills/nfcore-rnaseq-wrapper/SKILL.md` — Wrapper skill for running nf-core/rnaseq bulk RNA-seq preprocessing from FASTQ or BAM inputs with strict preflight, reproducibility outputs, and downstream handoff to ClawBio bulk RNA-seq DE skills.
- `ClawBio_ClawBio` / `nfcore-scrnaseq-wrapper` — `skills/nfcore-scrnaseq-wrapper/SKILL.md` — Wrapper skill for running nf-core/scrnaseq 4.1.0 upstream single-cell RNA-seq preprocessing from FASTQ with strict preflight, reproducibility outputs, and downstream handoff to ClawBio scRNA
- `ClawBio_ClawBio` / `rare-disease-rnaseq` — `skills/rare-disease-rnaseq/SKILL.md` — Blood RNA-seq expression-outlier detection for rare-disease diagnostics. Cases scored against a control reference panel; outliers ranked and filtered by a haploinsufficient disease-gene panel.
- `ClawBio_ClawBio` / `rnaseq-de` — `skills/rnaseq-de/SKILL.md` — Differential expression analysis for bulk RNA-seq and pseudo-bulk count matrices with QC, PCA, and contrast testing.
- `ClawBio_ClawBio` / `scrna-embedding` — `skills/scrna-embedding/SKILL.md` — Local scVI/scANVI-based single-cell latent embedding and batch-aware integration from raw-count .h5ad or 10x
- `ClawBio_ClawBio` / `scrna-orchestrator` — `skills/scrna-orchestrator/SKILL.md` — Local Scanpy pipeline for single-cell RNA-seq QC, optional doublet detection, clustering, marker discovery, optional
- `GPTomics_bioSkills` / `bio-alignment-pairwise` — `alignment/pairwise-alignment/SKILL.md` — Perform pairwise sequence alignment using Biopython Bio.Align.PairwiseAligner. Use when comparing two sequences, finding optimal alignments, scoring similarity, and identifying local or global matches between DNA, RNA, o
- `GPTomics_bioSkills` / `bio-differential-splicing` — `alternative-splicing/differential-splicing/SKILL.md` — Detects differential alternative splicing between conditions using rMATS-turbo (binomial LRT on junction counts), leafcutter (Dirichlet-multinomial GLM on intron clusters), MAJIQ V3 deltapsi/HET (Bayesian posterior on LS
- `GPTomics_bioSkills` / `bio-isoform-switching` — `alternative-splicing/isoform-switching/SKILL.md` — Analyzes differential transcript usage (DTU) and isoform switches with functional consequence prediction (NMD via 50nt rule, ORF disruption, protein domain loss/gain, signal peptide changes, IDR alterations, coding-poten
- `GPTomics_bioSkills` / `bio-long-read-splicing` — `alternative-splicing/long-read-splicing/SKILL.md` — Analyzes alternative splicing from PacBio Iso-Seq (HiFi, Kinnex/MAS-Iso-seq) and Oxford Nanopore (direct cDNA, direct RNA, R10.4.1+) long-read RNA-seq with full-isoform resolution. Tools include FLAIR (correct/collapse/q

### single-cell
- `ClawBio_ClawBio` / `celltype-specificity-profiler` — `skills/celltype-specificity-profiler/SKILL.md` — Given a gene and a single-cell atlas, compute how cell-type-specific its expression is — the tau specificity index, Sarle's expression bimodality coefficient, and the cell types that drive the signal; a pure analytic tra
- `ClawBio_ClawBio` / `diff-visualizer` — `skills/diff-visualizer/SKILL.md` — Rich downstream visualisation and reporting for bulk RNA-seq differential expression and scRNA marker/contrast
- `ClawBio_ClawBio` / `nfcore-scrnaseq-wrapper` — `skills/nfcore-scrnaseq-wrapper/SKILL.md` — Wrapper skill for running nf-core/scrnaseq 4.1.0 upstream single-cell RNA-seq preprocessing from FASTQ with strict preflight, reproducibility outputs, and downstream handoff to ClawBio scRNA
- `ClawBio_ClawBio` / `scrna-embedding` — `skills/scrna-embedding/SKILL.md` — Local scVI/scANVI-based single-cell latent embedding and batch-aware integration from raw-count .h5ad or 10x
- `ClawBio_ClawBio` / `scrna-orchestrator` — `skills/scrna-orchestrator/SKILL.md` — Local Scanpy pipeline for single-cell RNA-seq QC, optional doublet detection, clustering, marker discovery, optional
- `GPTomics_bioSkills` / `bio-single-cell-splicing` — `alternative-splicing/single-cell-splicing/SKILL.md` — Analyzes alternative splicing at single-cell resolution. The first decision is library chemistry — 10X 3' is fundamentally limited (RT primes from poly-A, R2 falls in 3' UTR, <0.1 junction read per cell per AS event). Pl
- `GPTomics_bioSkills` / `bio-atac-seq-single-cell-atac` — `atac-seq/single-cell-atac/SKILL.md` — Process and analyze single-cell ATAC-seq data with Signac, ArchR, SnapATAC2, or Cell Ranger ATAC. Use when handling 10X scATAC or 10X Multiome (paired RNA+ATAC) data, performing per-cell QC, choosing between ArchR/Signac
- `GPTomics_bioSkills` / `bioskills` — `bioskills-installer/SKILL.md` — Installs 425 bioinformatics skills covering sequence analysis, RNA-seq, single-cell, variant calling, metagenomics, structural biology, and 56 more categories. Use when setting up bioinformatics capabilities or when a bi
- `GPTomics_bioSkills` / `bio-clip-seq-stamp-antibody-free` — `clip-seq/stamp-antibody-free/SKILL.md` — Profiles RNA-binding protein targets without antibody or UV crosslinking using STAMP (APOBEC1-RBP fusion, C-to-U editing), scSTAMP (single-cell), TRIBE/HyperTRIBE (ADAR-RBP, A-to-I editing), DART-seq (APOBEC1-YTH for m6A
- `GPTomics_bioSkills` / `bio-crispr-screens-combinatorial-screens` — `crispr-screens/combinatorial-screens/SKILL.md` — Designs and analyzes combinatorial CRISPR screens covering paired-Cas9 (Big Papi, Najm 2018), enhanced AsCas12a multiplex (enCas12a, DeWeirdt 2021), in4mer 4-guide-array Cas12a (Esmaeili Anvar N et al 2024 Nat Commun 15:
- `GPTomics_bioSkills` / `bio-crispr-screens-perturb-seq-analysis` — `crispr-screens/perturb-seq-analysis/SKILL.md` — Analyzes single-cell pooled CRISPR screens (Perturb-seq, CROP-seq, Perturb-CITE-seq, ECCITE-seq, multiome) where each cell carries an sgRNA and a scRNA-seq / surface-protein / chromatin readout. Covers experimental desig
- `GPTomics_bioSkills` / `bio-data-visualization-dimensionality-reduction-plots` — `data-visualization/dimensionality-reduction-plots/SKILL.md` — Produce and interpret PCA, t-SNE, UMAP, and PHATE plots for high-dimensional omics data with rigor about which method preserves what (variance, local structure, manifold, transitions), hyperparameter sensitivity, and the

### literature
- `ClawBio_ClawBio` / `claw-semantic-sim` — `skills/claw-semantic-sim/SKILL.md` — Semantic Similarity Index for disease research literature using PubMedBERT embeddings
- `ClawBio_ClawBio` / `lit-synthesizer` — `skills/lit-synthesizer/SKILL.md` — Search PubMed and bioRxiv for bioinformatics literature, synthesise results into a structured report, and build
- `ClawBio_ClawBio` / `pubmed-summariser` — `skills/pubmed-summariser/SKILL.md` — Search PubMed for a gene name or disease term and generate a structured research briefing of the top recent English-language
- `GPTomics_bioSkills` / `bio-entrez-fetch` — `database-access/entrez-fetch/SKILL.md` — Retrieve records from NCBI databases using Biopython Bio.Entrez (EFetch, ESummary). Use when downloading sequences, fetching GenBank/GenPept records, getting document summaries, parsing nested XML, navigating GI deprecat
- `GPTomics_bioSkills` / `bio-entrez-link` — `database-access/entrez-link/SKILL.md` — Find cross-database references between NCBI databases using Biopython Bio.Entrez (ELink). Use when navigating gene to protein/structure, sequence to publication, PubMed to GEO, BioProject to SRA runs, or discovering all 
- `GPTomics_bioSkills` / `bio-entrez-search` — `database-access/entrez-search/SKILL.md` — Search NCBI databases using Biopython Bio.Entrez (ESearch, EInfo, EGQuery, ESpell). Use when finding records by keyword, building reproducible field-qualified queries, navigating the Entrez Query Translator, exploiting t
- `K-Dense-AI_scientific-agent-skills` / `bgpt-paper-search` — `skills/bgpt-paper-search/SKILL.md` — Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including methods, results, sample sizes, quality scores, and conc
- `K-Dense-AI_scientific-agent-skills` / `biopython` — `skills/biopython/SKILL.md` — Comprehensive molecular biology toolkit. Use for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogenetics, and programmatic NCBI/PubMed access (Bio.Entrez). Best for batch processing, custom bioinformatics 
- `K-Dense-AI_scientific-agent-skills` / `citation-management` — `skills/citation-management/SKILL.md` — Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be us
- `K-Dense-AI_scientific-agent-skills` / `hypogenic` — `skills/hypogenic/SKILL.md` — Automated LLM-driven hypothesis generation and testing on tabular datasets. Use when you want to systematically explore hypotheses about patterns in empirical data (e.g., deception detection, content analysis). Combines 
- `K-Dense-AI_scientific-agent-skills` / `literature-review` — `skills/literature-review/SKILL.md` — Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Semantic Scholar, etc.). This skill should be used when conducting systematic literature reviews, meta-analy
- `K-Dense-AI_scientific-agent-skills` / `paper-lookup` — `skills/paper-lookup/SKILL.md` — Search 10 academic paper databases via REST APIs for research papers, preprints, and scholarly articles. Covers PubMed, PMC (full text), bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall. Use

### citation
- `K-Dense-AI_scientific-agent-skills` / `citation-management` — `skills/citation-management/SKILL.md` — Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be us
- `K-Dense-AI_scientific-agent-skills` / `hugging-science` — `skills/hugging-science/SKILL.md` — Use when the user is doing AI/ML work in a scientific domain such as biology, chemistry, physics, astronomy, climate, genomics, materials, medicine, ecology, energy, engineering, math, drug discovery, protein design, wea
- `K-Dense-AI_scientific-agent-skills` / `literature-review` — `skills/literature-review/SKILL.md` — Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Semantic Scholar, etc.). This skill should be used when conducting systematic literature reviews, meta-analy
- `K-Dense-AI_scientific-agent-skills` / `networkx` — `skills/networkx/SKILL.md` — Create, analyze, and visualize complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures, computing graph algorithms (shortest paths, centrality, clustering), detecting comm
- `K-Dense-AI_scientific-agent-skills` / `paper-lookup` — `skills/paper-lookup/SKILL.md` — Search 10 academic paper databases via REST APIs for research papers, preprints, and scholarly articles. Covers PubMed, PMC (full text), bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall. Use
- `K-Dense-AI_scientific-agent-skills` / `parallel-web` — `skills/parallel-web/SKILL.md` — All-in-one web toolkit powered by parallel-cli, with a strong emphasis on academic and scientific sources. Use this skill whenever the user needs to search the web, fetch/extract URL content, enrich data with web-sourced
- `K-Dense-AI_scientific-agent-skills` / `pyzotero` — `skills/pyzotero/SKILL.md` — Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3. Use this skill when working 
- `K-Dense-AI_scientific-agent-skills` / `scientific-writing` — `skills/scientific-writing/SKILL.md` — Core skill for the deep research and writing tool. Write scientific manuscripts in full paragraphs (never bullet points). Use two-stage process with (1) section outlines with key points using research-lookup then (2) con
- `K-Dense-AI_scientific-agent-skills` / `treatment-plans` — `skills/treatment-plans/SKILL.md` — Generate concise (3-4 page), focused medical treatment plans in LaTeX/PDF format for all clinical specialties. Supports general medical treatment, rehabilitation therapy, mental health care, chronic disease management, p
- `Yuan1z0825_nature-skills` / `nature-citation` — `skills/nature-citation/SKILL.md` — >-
- `affaan-m_ECC` / `deep-research` — `.agents/skills/deep-research/SKILL.md` — Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence an
- `affaan-m_ECC` / `deep-research` — `.kiro/skills/deep-research/SKILL.md` — Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence an

### writing
- `ClawBio_ClawBio` / `analyze-fasta` — `skills/analyze-fasta/SKILL.md` — Analyze a single FASTA file (nucleotide or protein), compute sequence-level metrics (GC, ORFs, MW, pI, GRAVY, secondary-structure fractions) with Biopython, and write a Markdown report plus structured JSON for downstream
- `ClawBio_ClawBio` / `clawpathy-autoresearch` — `skills/clawpathy-autoresearch/SKILL.md` — Eval-driven skill tuning. Given a task and an LLM-judge rubric, iteratively rewrites a SKILL.md until a downstream executor agent performs well against the judge. Low-code: all evaluation
- `GPTomics_bioSkills` / `bio-alignment-io` — `alignment/alignment-io/SKILL.md` — Read, write, and convert multiple sequence alignment files using Biopython Bio.AlignIO. Supports Clustal, PHYLIP, Stockholm, FASTA, Nexus, and other alignment formats for phylogenetics and conservation analysis. Use when
- `GPTomics_bioSkills` / `bio-molecular-io` — `chemoinformatics/molecular-io/SKILL.md` — Reads, writes, and converts molecular file formats (SMILES, InChI, SDF V2000/V3000, MOL2, PDB, MMTF) using RDKit and Open Babel with rigorous handling of aromaticity perception, stereochemistry, implicit/explicit hydroge
- `GPTomics_bioSkills` / `bio-clinical-databases-polygenic-risk` — `clinical-databases/polygenic-risk/SKILL.md` — Constructs and validates polygenic risk scores using LDpred2-auto, SBayesRC, MegaPRS, PRS-CS, PROSPER, MUSSEL, BridgePRS, JointPRS, PRSmix, or PGS Catalog Calculator with ancestry-aware reference panels (HapMap3, UKB-LD)
- `GPTomics_bioSkills` / `bio-epitranscriptomics-m6anet-analysis` — `epitranscriptomics/m6anet-analysis/SKILL.md` — Detects m6A modifications from Oxford Nanopore direct-RNA-sequencing (ONT DRS) signal data using m6Anet (Hendra 2022 *Nat Methods* 19:1590; multiple-instance-learning neural network over DRACH 5-mer signal). Covers the r
- `GPTomics_bioSkills` / `bio-flow-cytometry-fcs-handling` — `flow-cytometry/fcs-handling/SKILL.md` — Reads, inspects, and writes Flow Cytometry Standard (FCS) files from conventional, spectral, and mass cytometry (CyTOF), and parses FlowJo/Cytobank/Diva workspaces. Covers FCS 2.0/3.0/3.1/3.2 internals ($PnE linear-vs-lo
- `GPTomics_bioSkills` / `bio-genome-assembly-assembly-polishing` — `genome-assembly/assembly-polishing/SKILL.md` — Decides whether and how to polish a draft genome assembly to raise consensus accuracy (QV) with read-type-matched tools - Racon and medaka (ONT consensus), dorado polish, Polypolish and pypolca (Illumina, repeat-aware), 
- `GPTomics_bioSkills` / `bio-genome-assembly-assembly-qc` — `genome-assembly/assembly-qc/SKILL.md` — Evaluates genome assembly quality across the three orthogonal axes - contiguity (QUAST auN/NG50/NGx, not bare N50), completeness (BUSCO/compleasm gene-space plus Merqury k-mer completeness), and correctness (reference-fr
- `GPTomics_bioSkills` / `bio-genome-assembly-long-read-assembly` — `genome-assembly/long-read-assembly/SKILL.md` — Assembles genomes de novo from noisy long reads (Oxford Nanopore R9/R10/Dorado, PacBio CLR) with Flye (repeat graph), Canu (correct-trim-assemble OLC), NextDenovo, Shasta, Raven, wtdbg2, or miniasm, and reconciles bacter
- `GPTomics_bioSkills` / `bio-genome-intervals-bigwig-tracks` — `genome-intervals/bigwig-tracks/SKILL.md` — Reads, queries, and writes bigWig indexed binary signal tracks (coverage, fold-change, conservation, methylation-rate) with pyBigWig (Python) and the UCSC Kent tools (bedGraphToBigWig, bigWigToBedGraph, bigWigInfo, bigWi
- `GPTomics_bioSkills` / `bio-long-read-sequencing-basecalling` — `long-read-sequencing/basecalling/SKILL.md` — Basecalls raw Oxford Nanopore signal (POD5/FAST5) into reads with Dorado, choosing the chemistry-matched model and accuracy tier (fast/hac/sup), requesting modified bases (5mCG_5hmCG, 6mA, m6A) at basecall time, and hand

### review
- `GPTomics_bioSkills` / `bio-chipseq-spike-in-normalization` — `chip-seq/spike-in-normalization/SKILL.md` — Normalizes ChIP-seq data using exogenous spike-in (ChIP-Rx with Drosophila chromatin per Orlando 2014 / Egan 2016; E. coli carryover for CUT&RUN/CUT&Tag). Distinguishes RRPM from Rx-Input scaling, integrates with DiffBin
- `GPTomics_bioSkills` / `bio-clinical-biostatistics-adaptive-designs` — `clinical-biostatistics/adaptive-designs/SKILL.md` — Designs adaptive clinical trials including group-sequential (O'Brien-Fleming, Pocock, Lan-DeMets spending), sample-size re-estimation (blinded Friede-Kieser, unblinded Cui-Hung-Wang, Mehta-Pocock promising zone), seamles
- `GPTomics_bioSkills` / `bio-clinical-databases-polygenic-risk` — `clinical-databases/polygenic-risk/SKILL.md` — Constructs and validates polygenic risk scores using LDpred2-auto, SBayesRC, MegaPRS, PRS-CS, PROSPER, MUSSEL, BridgePRS, JointPRS, PRSmix, or PGS Catalog Calculator with ancestry-aware reference panels (HapMap3, UKB-LD)
- `GPTomics_bioSkills` / `bio-data-visualization-flow-and-transition-plots` — `data-visualization/flow-and-transition-plots/SKILL.md` — Build Sankey, alluvial, river, and CONSORT-style flow diagrams to visualize cohort transitions, cell-state changes, or pipeline filtering using ggalluvial, networkD3, plotly, and consort. Use when showing how entities mo
- `GPTomics_bioSkills` / `bio-uniprot-access` — `database-access/uniprot-access/SKILL.md` — Query UniProt's REST API (post-2022 endpoint at rest.uniprot.org) for protein sequences, annotations, GO terms, cross-references, ID mappings, and proteomes. Use when fetching UniProtKB entries, navigating the JSON schem
- `GPTomics_bioSkills` / `bio-gene-regulatory-networks-perturbation-simulation` — `gene-regulatory-networks/perturbation-simulation/SKILL.md` — Simulate transcription factor perturbation effects on cell state in silico with CellOracle and Dynamo, and predict transcriptional responses to genetic perturbations with GEARS, scGen, and CPA. Covers the direction-not-m
- `GPTomics_bioSkills` / `bio-immunoinformatics-immunogenicity-scoring` — `immunoinformatics/immunogenicity-scoring/SKILL.md` — Rank and prioritize neoantigen/epitope candidates by likely T-cell response using NeoFox feature annotation, PRIME2.0, BigMHC-IM, the Łuksza/Balachandran fitness model (agretopicity + foreignness), and pVACtools tiering.
- `GPTomics_bioSkills` / `bio-longitudinal-monitoring` — `liquid-biopsy/longitudinal-monitoring/SKILL.md` — Tracks ctDNA across serial liquid-biopsy timepoints for molecular residual disease (MRD) and treatment-response monitoring, treating MRD as a binary integrated detection call across the patient's full variant set (with a
- `GPTomics_bioSkills` / `bio-pathway-reactome` — `pathway-analysis/reactome-pathways/SKILL.md` — Tests a gene list or ranked gene vector for over-representation or coordinated shifts in Reactome's curated, peer-reviewed, reaction-level pathways using ReactomePA's enrichPathway (ORA) and gsePathway (GSEA), reading th
- `GPTomics_bioSkills` / `bio-pathway-wikipathways` — `pathway-analysis/wikipathways/SKILL.md` — Tests a gene list (ORA, enrichWP) or a ranked gene vector (GSEA, gseWP) against the WikiPathways community-curated pathway collection with clusterProfiler and rWikiPathways. Covers why a WikiPathways result is a snapshot
- `GPTomics_bioSkills` / `bio-restriction-golden-gate-assembly` — `restriction-analysis/golden-gate-assembly/SKILL.md` — Design and validate Type IIS scarless DNA assembly (Golden Gate, MoClo) using Biopython Bio.Restriction. Screens parts for internal BsaI/BsmBI/BbsI/SapI sites (domestication), previews the fusion overhangs a digest expos
- `GPTomics_bioSkills` / `bio-single-cell-cell-communication` — `single-cell/cell-communication/SKILL.md` — Infers ligand-receptor cell-cell communication from scRNA-seq with a consensus-first workflow (LIANA), plus CellPhoneDB specificity tests, CellChat pathway probabilities, and NicheNet downstream ligand-activity. Use when

### figure
- `ClawBio_ClawBio` / `data-extractor` — `skills/data-extractor/SKILL.md` — Extract numerical data from scientific figure images using Claude vision + OpenCV calibration. Supports 26+ plot
- `ClawBio_ClawBio` / `equity-scorer` — `skills/equity-scorer/SKILL.md` — Compute HEIM diversity and equity metrics from VCF or ancestry data. Generates heterozygosity, FST, PCA plots,
- `GPTomics_bioSkills` / `bio-sashimi-plots` — `alternative-splicing/sashimi-plots/SKILL.md` — Creates sashimi-style plots showing RNA-seq read coverage and splice junction counts using ggsashimi (general-purpose, condition-grouped overlays), rmats2sashimiplot (rMATS-output-aware), MAJIQ-VOILA (LSV posteriors inte
- `GPTomics_bioSkills` / `bio-atac-seq-nucleosome-positioning` — `atac-seq/nucleosome-positioning/SKILL.md` — Map nucleosome center positions, occupancy, and fuzziness from ATAC-seq fragment-size patterns using NucleoATAC, ATACseqQC, DANPOS3, or scprinter. Use when characterizing nucleosome organization at promoters and enhancer
- `GPTomics_bioSkills` / `bio-chipseq-qc` — `chip-seq/chipseq-qc/SKILL.md` — Assesses ChIP-seq quality across antibody specificity, fragmentation, enrichment, replicate concordance, and library complexity. Computes FRiP, NSC/RSC (phantompeakqualtools), library complexity (NRF/PBC1/PBC2), deepTool
- `GPTomics_bioSkills` / `bio-chipseq-visualization` — `chip-seq/chipseq-visualization/SKILL.md` — Visualizes ChIP-seq data using deepTools (computeMatrix, plotHeatmap, plotProfile, bamCoverage, bamCompare), pyGenomeTracks (modern INI-driven track plots), Gviz (R browser-style), EnrichedHeatmap (ComplexHeatmap-based),
- `GPTomics_bioSkills` / `bio-clinical-biostatistics-effect-measures` — `clinical-biostatistics/effect-measures/SKILL.md` — Computes and interprets treatment effect measures (OR, RR, RD, HR, NNT) with calibrated confidence intervals (Wilson, Newcombe, Miettinen-Nurminen, MOVER, profile likelihood, Bender NNT) and reports marginal vs condition
- `GPTomics_bioSkills` / `bio-comparative-genomics-pangenome-analysis` — `comparative-genomics/pangenome-analysis/SKILL.md` — Build and analyze pangenomes for prokaryotes (Panaroo, PPanGGOLiN, PEPPAN, GET_HOMOLOGUES, anvi'o pangenomics) and eukaryotes (Minigraph-Cactus, PGGB, vg pangenome graphs). Implement Tettelin core/accessory/cloud genome 
- `GPTomics_bioSkills` / `bio-comparative-genomics-synteny-analysis` — `comparative-genomics/synteny-analysis/SKILL.md` — Detect syntenic blocks and structural rearrangements between genomes using MCScanX (Wang 2012), JCVI/MCScan (Tang 2008 Python), GENESPACE (Lovell 2022) for orthology-anchored riparian visualization, SyRI for structural v
- `GPTomics_bioSkills` / `bio-copy-number-cnv-visualization` — `copy-number/cnv-visualization/SKILL.md` — Visualize copy number profiles, segments, allele-specific tracks, and cohort patterns from CNVkit, GATK, ASCAT, FACETS, Sequenza, and other callers. Covers genome-wide and per-chromosome log2 scatter plots, B-allele-freq
- `GPTomics_bioSkills` / `bio-copy-number-subclonal-copy-number` — `copy-number/subclonal-copy-number/SKILL.md` — Resolve subclonal copy number, whole-genome doubling, and copy-number tumor evolution from bulk sequencing with Battenberg, TITAN, and MEDICC2. Covers clonal versus subclonal copy-number states, haplotype phasing for sub
- `GPTomics_bioSkills` / `bio-data-visualization-circos-plots` — `data-visualization/circos-plots/SKILL.md` — Build circular genome visualizations using circlize (R), pyCirclize (Python), or Circos (Perl CLI) with ideogram tracks, multi-data tracks (scatter, histogram, heatmap), chord/link arcs for interactions, and explicit cir

### data/provenance
- `ClawBio_ClawBio` / `article-data-fetcher` — `skills/article-data-fetcher/SKILL.md` — >-
- `ClawBio_ClawBio` / `bgpt-mcp` — `skills/bgpt-mcp/SKILL.md` — Search scientific papers via the BGPT MCP server and retrieve structured experimental data — methods, results,
- `ClawBio_ClawBio` / `bigquery-public` — `skills/bigquery-public/SKILL.md` — Run read-only SQL against BigQuery public datasets with local result capture, cost safeguards, and reproducibility
- `ClawBio_ClawBio` / `claw-methylation-cycle` — `skills/claw-methylation-cycle/SKILL.md` — Methylation cycle analysis — enzymatic activity profiles, Net Methylation Capacity, BH4 axis estimates, compound heterozygosity detection from SNP genotype data.
- `ClawBio_ClawBio` / `clinpgx` — `skills/clinpgx/SKILL.md` — Query the ClinPGx API for pharmacogenomic gene-drug data, clinical annotations, CPIC guidelines, and FDA drug
- `ClawBio_ClawBio` / `data-extractor` — `skills/data-extractor/SKILL.md` — Extract numerical data from scientific figure images using Claude vision + OpenCV calibration. Supports 26+ plot
- `ClawBio_ClawBio` / `equity-scorer` — `skills/equity-scorer/SKILL.md` — Compute HEIM diversity and equity metrics from VCF or ancestry data. Generates heterozygosity, FST, PCA plots,
- `ClawBio_ClawBio` / `flow-bio` — `skills/flow-bio/SKILL.md` — Flow.bio API bridge — authenticate, browse pipelines/samples/projects, search, upload data, launch pipeline executions,
- `ClawBio_ClawBio` / `gwas-lookup` — `skills/gwas-lookup/SKILL.md` — Federated variant lookup across 9 genomic databases — GWAS Catalog, Open Targets, PheWeb (UKB, FinnGen, BBJ),
- `ClawBio_ClawBio` / `gwas-prs` — `skills/gwas-prs/SKILL.md` — Calculate polygenic risk scores from DTC genetic data using the PGS Catalog
- `ClawBio_ClawBio` / `hla-typing` — `skills/hla-typing/SKILL.md` — HLA allele typing from WGS/WES VCF data
- `ClawBio_ClawBio` / `labstep` — `skills/labstep/SKILL.md` — Query and display Labstep electronic lab notebook data — experiments, protocols, resources, and inventory — via

### reproducibility
- `ClawBio_ClawBio` / `bigquery-public` — `skills/bigquery-public/SKILL.md` — Run read-only SQL against BigQuery public datasets with local result capture, cost safeguards, and reproducibility
- `ClawBio_ClawBio` / `nfcore-rnaseq-wrapper` — `skills/nfcore-rnaseq-wrapper/SKILL.md` — Wrapper skill for running nf-core/rnaseq bulk RNA-seq preprocessing from FASTQ or BAM inputs with strict preflight, reproducibility outputs, and downstream handoff to ClawBio bulk RNA-seq DE skills.
- `ClawBio_ClawBio` / `nfcore-scrnaseq-wrapper` — `skills/nfcore-scrnaseq-wrapper/SKILL.md` — Wrapper skill for running nf-core/scrnaseq 4.1.0 upstream single-cell RNA-seq preprocessing from FASTQ with strict preflight, reproducibility outputs, and downstream handoff to ClawBio scRNA
- `ClawBio_ClawBio` / `pathway-enricher` — `skills/pathway-enricher/SKILL.md` — Gene-set pathway enrichment analysis using Enrichr — queries KEGG, GO (BP/MF/CC), Reactome, WikiPathways, MSigDB, and Disease Ontology. Produces ranked pathway tables, interactive bubble charts, and a reproducible Markdo
- `ClawBio_ClawBio` / `repro-enforcer` — `skills/repro-enforcer/SKILL.md` — Export any bioinformatics analysis as a reproducible bundle with Conda environment, Singularity container definition,
- `ClawBio_ClawBio` / `rnaseq-de` — `skills/rnaseq-de/SKILL.md` — Differential expression analysis for bulk RNA-seq and pseudo-bulk count matrices with QC, PCA, and contrast testing.
- `ClawBio_ClawBio` / `skill-builder` — `skills/skill-builder/SKILL.md` — Scaffold a new ClawBio skill from a spec file (JSON/YAML) or interactively — generates SKILL.md, Python skeleton, tests, and updates catalog.json
- `ClawBio_ClawBio` / `vcf-annotator` — `skills/vcf-annotator/SKILL.md` — Annotate VCF variants with Ensembl VEP, ClinVar, and gnomAD. Ranks variants by impact (HIGH/MODERATE/LOW/MODIFIER) and generates a reproducible report.
- `GPTomics_bioSkills` / `bio-single-cell-splicing` — `alternative-splicing/single-cell-splicing/SKILL.md` — Analyzes alternative splicing at single-cell resolution. The first decision is library chemistry — 10X 3' is fundamentally limited (RT primes from poly-A, R2 falls in 3' UTR, <0.1 junction read per cell per AS event). Pl
- `GPTomics_bioSkills` / `bio-causal-genomics-colocalization-analysis` — `causal-genomics/colocalization-analysis/SKILL.md` — Test whether two or more traits share a causal variant at a locus using Bayesian colocalization (coloc.abf, coloc.susie, HyPrColoc, moloc, eCAVIAR, SMR/HEIDI, PWCoCo, SharePro). Use when integrating GWAS with eQTL/sQTL/p
- `GPTomics_bioSkills` / `bio-causal-genomics-genomic-sem` — `causal-genomics/genomic-sem/SKILL.md` — Fits structural equation models to GWAS summary statistics using GenomicSEM (Grotzinger 2019), including common-factor models, confirmatory factor models, ESEM, common-factor GWAS with Q_SNP heterogeneity, multivariate W
- `GPTomics_bioSkills` / `bio-causal-genomics-mediation-analysis` — `causal-genomics/mediation-analysis/SKILL.md` — Decompose total effects into direct and indirect paths through mediators using mediation, CMAverse 4-way, HIMA/HIMA2 high-dimensional, BAMA, two-step / MVMR mediation, or double-ML medDML. Use when testing whether a mole

### clinical
- `ClawBio_ClawBio` / `clinical-trial-finder` — `skills/clinical-trial-finder/SKILL.md` — Find clinical trials for a gene, variant, or condition from ClinicalTrials.gov + EUCTR, with FHIR R4 output
- `ClawBio_ClawBio` / `clinical-variant-reporter` — `skills/clinical-variant-reporter/SKILL.md` — Classify germline variants from VCF/BCF files according to the ACMG/AMP 2015 28-criteria evidence framework and
- `ClawBio_ClawBio` / `clinpgx` — `skills/clinpgx/SKILL.md` — Query the ClinPGx API for pharmacogenomic gene-drug data, clinical annotations, CPIC guidelines, and FDA drug
- `ClawBio_ClawBio` / `recombinator` — `skills/recombinator/SKILL.md` — Produce offspring genomes from parent pairs via meiotic recombination, mutation, and clinical evaluation
- `ClawBio_ClawBio` / `variant-annotation` — `skills/variant-annotation/SKILL.md` — Annotate VCF variants with Ensembl VEP REST, ClinVar significance, gnomAD/population frequency context, and prioritized
- `ClawBio_ClawBio` / `vcf-annotator` — `skills/vcf-annotator/SKILL.md` — Annotate VCF variants with Ensembl VEP, ClinVar, and gnomAD. Ranks variants by impact (HIGH/MODERATE/LOW/MODIFIER) and generates a reproducible report.
- `ClawBio_ClawBio` / `wes-clinical-report-en` — `skills/wes-clinical-report-en/SKILL.md` — Generates professional clinical PDF reports in English from WES (Whole Exome Sequencing) data with clinical interpretation
- `ClawBio_ClawBio` / `wes-clinical-report-es` — `skills/wes-clinical-report-es/SKILL.md` — Generates professional clinical PDF reports in Spanish from WES (Whole Exome Sequencing) data with clinical interpretation,
- `GPTomics_bioSkills` / `bio-outlier-splicing-detection` — `alternative-splicing/outlier-splicing-detection/SKILL.md` — Detects aberrant splicing in single rare-disease patients vs a control panel using FRASER 2.0 (Bioconductor; Beta-binomial autoencoder on Intron Jaccard Index, default delta cutoff 0.1, q hyperparameter), OUTRIDER (gene-
- `GPTomics_bioSkills` / `bio-splice-variant-prediction` — `alternative-splicing/splice-variant-prediction/SKILL.md` — Predicts whether a DNA variant alters mRNA splicing using sequence-based deep-learning tools — SpliceAI (10kb context dilated CNN, clinical default), Pangolin (multi-tissue), MMSplice (modular per-region CNN with calibra
- `GPTomics_bioSkills` / `bio-clinical-biostatistics-adaptive-designs` — `clinical-biostatistics/adaptive-designs/SKILL.md` — Designs adaptive clinical trials including group-sequential (O'Brien-Fleming, Pocock, Lan-DeMets spending), sample-size re-estimation (blinded Friede-Kieser, unblinded Cui-Hung-Wang, Mehta-Pocock promising zone), seamles
- `GPTomics_bioSkills` / `bio-clinical-biostatistics-bayesian-trials` — `clinical-biostatistics/bayesian-trials/SKILL.md` — Designs Bayesian clinical trials including Phase I dose-finding (BOIN, CRM, EWOC, mTPI-2), meta-analytic-predictive (MAP) priors with robust mixtures for external data borrowing, EXNEX for basket trials, hierarchical mod

## 4. Cross-review pass design

Pass 1 — coverage map: identify what each external repo is good for, without merging.
Pass 2 — gap/overlap map: compare against the 10 runtime skills and 26 source candidate skills; mark each external module as strengthen-existing / candidate-new / reference-only / reject.
Pass 3 — absorption draft: edit only the GitHub source repo on `Hermes-review`; do not directly overwrite runtime skills until the user has used and accepted them.

## 5. Immediate absorption hypotheses to test in the next pass

| Capability | Likely source repos | Existing target | Expected action |
|---|---|---|---|
| Scientific database grounding for genetics/protein/drug | `science-skills`, `scientific-agent-skills`, `ClawBio`, `BioNeMo` | no exact current runtime skill; partial `bioinfo-analysis-code`, `literature-search-workflow` | create candidate skill `scientific-database-grounding` or `genetic-database-grounding` |
| Local-first reproducible execution | `ClawBio`, `bioSkills`, `agent-skills` | `bioinfo-analysis-code`, `project-environment-bootstrap`, `task-self-check` | strengthen checklists/references, not copy tool wrappers |
| Protein docking / binder design / ADMET expansion | `BioNeMo`, `protein-design-skills`, `AtomisticSkills`, `NVIDIA_skills` | no exact current candidate skill | create candidate docking/protein-design skill only after second-pass review |
| Scientific writing/review/caption QA | `nature-skills`, `superpowers` workflow discipline | existing writing/reviewer/figure skills | merge selected output contracts and QA language |
| Agent workflow / context engineering | `superpowers`, `Agent-Skills-for-Context-Engineering`, `ECC` | `AGENTS.md`, `skill-quality-audit`, collaboration docs | strengthen repo-level collaboration rules, avoid runtime bloat |

## 6. Guardrails

- Do not import large libraries wholesale (`bioSkills`, `ECC`, `scientific-agent-skills`).
- Do not copy dependency-heavy execution wrappers into default runtime until they have real local verification.
- Preserve the user's concise Chinese bioinfo workflow and evidence-boundary language as the primary design.
- Prefer references/templates/checklists over new always-loaded runtime skills when the capability is rare or heavy.
