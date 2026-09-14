<div align="center">
  <h1>laiism</h1>
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

## Introduction

An Agent Skill for documenting, examining, and developing laiism with traceable sources.

This project separates philosophical material from personality simulation and everyday style rules.
It supports explanation, critique, conditional application, and drafts without inventing beliefs or
turning historical personal positions into doctrine. The name `laiism` is always lowercase.

## Features

- 📚 **Traceable material** — Each position carries its source and confirmation status.
- 🧭 **Separate states** — Personal confirmation and doctrinal ratification remain independent.
- 🔍 **Open examination** — Arguments, assumptions, counterexamples, and unresolved tensions stay visible.
- 🧩 **Standalone use** — No personal model, website, or external workflow is required.

## Getting Started

Install once in the shared skills directory. Git refuses to overwrite an existing installation:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/lailai0916/laiism-skill ~/.agents/skills/laiism-skill
```

Read [SKILL.md](SKILL.md), then the relevant records in [positions.json](positions.json).
For example: “Use laiism-skill to examine the recorded view on AI and skill value; distinguish
the existing position from your own proposed extensions.”

If you already maintain a checkout elsewhere, link it into the shared skills directory instead of
cloning a second copy. A runtime that needs an adapter should reference the shared root, not receive
a separate copy of each Skill. Update an installation with `git pull --ff-only` inside its directory.

## Project Structure

```bash
laiism-skill/
├── references/                     # Interpretation and maintenance method
├── scripts/                        # Repository and evidence-state checks
├── tests/                          # Regression tests and behavior scenarios
├── positions.json                  # Canonical positions, evidence, and states
├── repository.json                 # Project identity and publication state
└── SKILL.md                        # Skill entry point
```

## Validation

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
npm ci --ignore-scripts
npm run format:check
```

Checks validate structure, naming, links, and required evidence fields. They cannot establish that
a statement is true or that approval actually occurred. Review [behavior scenarios](tests/scenarios.md)
separately when changing interpretation.

## Sources

Imported material preserves its original attribution and historical confirmation status. Each record
links to an immutable source version; model summaries are not presented as verbatim user quotations.
Migration itself does not ratify doctrine. See the [maintenance method](references/method.md).

[repository.json](repository.json) records the canonical GitHub identity, description, and topics.
Keep these values aligned with the repository's About settings when changing project metadata.

## License

This project's code is licensed under [MIT License](https://github.com/lailai0916/tools/blob/main/LICENSE).

Skill text and position material retain [CC BY 4.0](LICENSE-docs), including attribution to the sources
listed in each imported record. Code scaffolding is adapted from
[lailai-template](https://github.com/lailai0916/lailai-template).
