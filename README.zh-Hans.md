<div align="center">
  <h1>laiism.skill</h1>
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

项目名为 `laiism.skill`，思想体系名为 `laiism`，两者始终小写。思想材料与人格模拟、写作规范、代码风格分开维护。

## 项目特性

📚 **来源可溯** — 每项立场保留来源与确认依据。

🧭 **状态分离** — 个人立场确认与正式教义确立独立记录。

🔍 **论证检验** — 解释论证、检验反例，并起草修订建议。

🧩 **独立使用** — 不依赖个人模型、个人网站或外部工作流。

## 快速开始

在共享 skills 目录中安装一份：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/lailai0916/laiism-skill ~/.agents/skills/laiism-skill
```

让 Agent 使用 `laiism-skill`。它先读 [SKILL.md](SKILL.md)，再读取 [positions.json](positions.json) 中相关条目的正文、来源与确认状态。例如：「解释已记录的 AI 与技能价值立场，再提出一个反例。」

若已有工作副本，将其链接到共享目录，不再复制。Runtime 兼容入口引用共享根目录。在安装目录内运行 `git pull --ff-only` 更新；修改思想正文或状态前，先读 [维护方法](references/method.md)。

## 项目结构

```bash
laiism-skill/
├── references/                     # 思想解释与维护方法
├── scripts/                        # 仓库与证据状态校验
├── tests/                          # 回归测试与行为场景
├── package.json                    # 文本格式化命令与依赖
├── positions.json                  # 思想正文、依据与状态的唯一来源
├── pyproject.toml                  # Python 格式与静态检查配置
├── repository.json                 # 项目身份与发布状态
├── requirements-dev.txt            # 固定版本的 Python 开发依赖
└── SKILL.md                        # Skill 入口
```

## 校验

维护检查使用 Python 3.10+ 和 Node.js 22。在仓库根目录运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
npm ci --ignore-scripts
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
python3 -m ruff check .
python3 -m ruff format --check .
npm run format:check
```

Prettier 负责支持的文本格式，Ruff 负责 Python 格式与静态检查。本地校验检查数据、身份、链接和证据字段，不判断观点真伪或批准是否真实发生。改变解释方式时，另行核对 [行为场景](tests/scenarios.md)。

CI 另行引用固定版本的 [lailai-template](https://github.com/lailai0916/lailai-template/blob/main/SETUP.md) 校验仓库与 README。运行模板检查器时，以 `--root /path/to/laiism-skill --display-name laiism.skill` 指向本仓库，添加 `--github` 可核对线上元数据。

## 许可协议

本项目代码采用 [MIT 许可协议](https://github.com/lailai0916/tools/blob/main/LICENSE)。

Skill 文本与思想材料采用 [CC BY 4.0](LICENSE-docs)。
