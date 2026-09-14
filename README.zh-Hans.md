<div align="center">
  <h1>laiism</h1>
  <p><a href="README.md">English</a> · <strong>简体中文</strong></p>
  <p>
    <img src="https://img.shields.io/github/actions/workflow/status/lailai0916/laiism-skill/ci.yml?branch=main&style=flat-square" alt="持续集成" />
    <img src="https://img.shields.io/github/last-commit/lailai0916/laiism-skill?style=flat-square" alt="最后提交" />
    <img src="https://img.shields.io/github/languages/top/lailai0916/laiism-skill?style=flat-square" alt="主要语言" />
    <img src="https://img.shields.io/github/repo-size/lailai0916/laiism-skill?style=flat-square" alt="仓库大小" />
    <img src="https://img.shields.io/badge/code_style-prettier-ff69b4?style=flat-square" alt="代码格式：Prettier" />
    <img src="https://img.shields.io/github/license/lailai0916/laiism-skill?style=flat-square" alt="代码许可：MIT" />
    <img src="https://img.shields.io/badge/docs-CC_BY_4.0-green?style=flat-square" alt="文档许可：CC BY 4.0" />
  </p>
</div>

## 项目简介

用于整理、讨论与发展 laiism 的 Agent Skill，每项思想材料均保留可追溯来源。

本项目将思想材料与人格模拟、日常风格规范分开维护。它支持解释、批评、条件性应用与拟稿，不编造信仰，也不把历史个人立场自动提升为教义。名称 `laiism` 始终小写。

## 特性

- 📚 **材料可追溯** — 每项立场保留来源与确认状态。
- 🧭 **状态分离** — 个人立场确认与正式教义确立独立记录。
- 🔍 **允许检验** — 明确论证、前提、反例与尚未解决的张力。
- 🧩 **独立使用** — 不依赖个人模型、个人网站或外部工作流。

## 快速开始

在共享 skills 目录中安装一份。Git 不会覆盖已有安装：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/lailai0916/laiism-skill ~/.agents/skills/laiism-skill
```

先读 [SKILL.md](SKILL.md)，再读取 [positions.json](positions.json) 的相关条目。例如：「使用 laiism-skill 分析已记录的 AI 与技能价值立场，区分已有材料和你提出的新建议。」

若其他位置已有工作副本，将其链接到共享 skills 目录，不重复克隆。需要适配的 runtime 引用共享根目录，不为每个 Skill 再建一份副本。在安装目录内运行 `git pull --ff-only` 更新。

## 项目结构

```bash
laiism-skill/
├── references/                     # 思想解释与维护方法
├── scripts/                        # 仓库与证据状态校验
├── tests/                          # 回归测试与行为场景
├── positions.json                  # 思想正文、依据与状态的唯一来源
├── repository.json                 # 项目身份与发布状态
└── SKILL.md                        # Skill 入口
```

## 验证

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
npm ci --ignore-scripts
npm run format:check
```

脚本检查结构、命名、链接与必要的证据字段，不能证明观点为真，也不能证明批准实际发生。改变解释方式时，另行核对 [行为场景](tests/scenarios.md)。

## 来源

迁入材料保留原始归属与历史确认状态，每项条目链接到不可变的来源版本。模型摘要不冒充本人逐字引文；迁移本身不确立教义。详见 [维护方法](references/method.md)。

[repository.json](repository.json) 记录权威 GitHub 身份、描述与 topics。变更项目元数据时，同步仓库的 About 设置。

## 许可协议

本项目代码采用 [MIT 许可协议](https://github.com/lailai0916/tools/blob/main/LICENSE)。

Skill 文本与思想材料沿用 [CC BY 4.0](LICENSE-docs)，包括迁入条目中所列来源的归属信息。代码骨架改编自 [lailai-template](https://github.com/lailai0916/lailai-template)。
