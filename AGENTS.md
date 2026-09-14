# Repository instructions

This repository owns the standalone `laiism-skill`: philosophical positions, their evidence,
status, arguments, and proposed development. Always spell `laiism` in lowercase, including
headings and sentence starts. Read `SKILL.md` and `references/method.md` before changing content.

- `positions.json` is the only source of position content and status. Do not mirror it in docs.
- Keep personal confirmation separate from doctrinal ratification. Never fabricate either.
- Preserve source attribution and distinguish model summaries from direct user statements.
- Do not copy personality profiles, writing rules, code conventions, or unrelated workflows here.
- Use runtime-neutral instructions. `CLAUDE.md` is only an import of this file.
- Shared installation belongs under `~/.agents/skills/`; do not create per-runtime skill copies.
- `repository.json` records canonical project identity and publication state. Keep its description
  and topics aligned with the GitHub About settings. Publication does not ratify any doctrine.
- Keep both READMEs aligned, including their shared installation commands and real repository badges.
  Publishing changes remains a separate authorized action; only report CI results actually observed.

## Validation

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
npm ci --ignore-scripts
npm run format:check
```

Run the behavioral scenarios in `tests/scenarios.md` when changing interpretation or routing.
Automated checks do not establish the truth of a doctrine or verify consent.
