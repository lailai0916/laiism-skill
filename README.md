<div align="center">
  <h1>laiism.skill</h1>
  <p><strong>English</strong> · <a href="README.zh-Hans.md">简体中文</a></p>
  <p>
    <img src="https://img.shields.io/github/actions/workflow/status/lailai0916/laiism-skill/ci.yml?branch=main&style=flat-square" alt="CI" />
    <img src="https://img.shields.io/github/last-commit/lailai0916/laiism-skill?style=flat-square" alt="Last commit" />
    <img src="https://img.shields.io/github/languages/top/lailai0916/laiism-skill?style=flat-square" alt="Top language" />
    <img src="https://img.shields.io/github/repo-size/lailai0916/laiism-skill?style=flat-square" alt="Repository size" />
    <img src="https://img.shields.io/badge/code_style-prettier-ff69b4?style=flat-square" alt="Code style: Prettier" />
    <img src="https://img.shields.io/github/license/lailai0916/laiism-skill?style=flat-square" alt="Code license: MIT" />
    <img src="https://img.shields.io/badge/docs-CC_BY_4.0-green?style=flat-square" alt="Documentation license: CC BY 4.0" />
  </p>
</div>

## Project Introduction

An Agent Skill for documenting, examining, and developing laiism with traceable sources.

The project is `laiism.skill`; the philosophy is `laiism`. Both names remain lowercase. The Skill
keeps philosophical material separate from personality simulation, writing rules, and code style.

## Project Features

📚 **Traceable Sources** — Each position retains its source and confirmation evidence.

🧭 **Separate States** — Personal confirmation and doctrinal ratification are recorded independently.

🔍 **Critical Examination** — Explain arguments, examine counterexamples, and draft proposed revisions.

🧩 **Standalone Use** — No personal model, website, or external workflow is required.

## Getting Started

Install the Skill once in the shared skills directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/lailai0916/laiism-skill ~/.agents/skills/laiism-skill
```

Ask the Agent to use `laiism-skill`. It reads [SKILL.md](SKILL.md), then the relevant records in
[positions.json](positions.json), including their sources and confirmation states. For example:
"Explain the recorded view on AI and skill value, then propose a counterexample."

If a checkout already exists, link it into the shared directory instead of making another copy.
Runtime adapters reference the shared root. Run `git pull --ff-only` in the installation directory
to update. See the [maintenance method](references/method.md) before changing position content or status.

## Project Structure

```bash
laiism-skill/
├── references/                     # Interpretation and maintenance method
├── scripts/                        # Repository and evidence-state checks
├── tests/                          # Regression tests and behavior scenarios
├── package.json                    # Text formatting commands and dependencies
├── positions.json                  # Canonical positions, evidence, and states
├── pyproject.toml                  # Python formatting and lint configuration
├── repository.json                 # Project identity and publication state
├── requirements-dev.txt            # Pinned Python development dependencies
└── SKILL.md                        # Skill entry point
```

## Validation

Maintenance checks use Python 3.10+ and Node.js 22. Run from the repository root:

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

Prettier formats supported text files; Ruff formats and checks Python. Local validation checks data,
identity, links, and evidence fields, not the truth of a position or whether approval occurred.
Review [behavior scenarios](tests/scenarios.md) when changing interpretation.

CI also uses a fixed revision of [lailai-template](https://github.com/lailai0916/lailai-template/blob/main/SETUP.md)
for repository and README checks. Run its checker against this checkout with
`--root /path/to/laiism-skill --display-name laiism.skill`; add `--github` to verify live metadata.

## License

This project's code is licensed under [MIT License](https://github.com/lailai0916/tools/blob/main/LICENSE).

Skill text and position material are licensed under [CC BY 4.0](LICENSE-docs).
