# Repository instructions

This repository owns `laiism.skill`: philosophical positions, their evidence, status, arguments,
and proposed development. The philosophy is `laiism`; the repository and installation identifier
remain `laiism-skill`. All three names are lowercase, including headings and sentence starts.
Read `SKILL.md` and `references/method.md` before changing content.

- `positions.json` is the only source of position content and status. Do not mirror it in docs.
- Keep personal confirmation separate from doctrinal ratification. Never fabricate either.
- Preserve source attribution and distinguish model summaries from direct user statements.
- Do not copy personality profiles, writing rules, code conventions, or unrelated workflows here.
- Use runtime-neutral instructions. `CLAUDE.md` is only an import of this file.
- Shared installation belongs under `~/.agents/skills/`; do not create per-runtime skill copies.
- `repository.json` records canonical project identity and publication state. Keep its description,
  homepage, and topics aligned with GitHub About. Publication does not ratify any doctrine.
- Keep both READMEs aligned, including their shared installation commands and real repository badges.
  Publishing changes remains a separate authorized action; only report CI results actually observed.
- Repository standards and generic validation come from
  [lailai-template](https://github.com/lailai0916/lailai-template/blob/main/SETUP.md).
  The local checker validates position evidence, the lowercase brand, links, and publication state.
  Keep generic README, tree, and metadata rules in the template; CI uses a fixed template revision.

## Validation

Use Python 3.10+ and Node.js 22. Install development dependencies in a virtual environment:

```bash
python3 -m pip install -r requirements-dev.txt
npm ci --ignore-scripts
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
python3 -m ruff check .
python3 -m ruff format --check .
npm run format:check
```

Prettier owns supported text formats; Ruff owns Python formatting and static checks.
Use `npm run format` and `python3 -m ruff format .` to apply their formatting.

Run the behavioral scenarios in `tests/scenarios.md` when changing interpretation or routing.
Automated checks do not establish the truth of a doctrine or verify consent.
