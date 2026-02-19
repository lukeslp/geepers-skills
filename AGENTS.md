# Repository Guidelines

## Project Structure & Module Organization
This repository contains portable, shareable skill definitions.
- `skills/<skill-name>/SKILL.md`: required instruction file per skill.
- Optional `skills/<skill-name>/scripts/`: utility scripts used by that skill.
- `README.md`: install and distribution workflow.

Keep each skill folder independent so it can be copied into `~/.codex/skills` without extra dependencies.

## Build, Test, and Development Commands
This repo is content-first; validation is file- and script-level.

```bash
# Discover all skills
find skills -mindepth 2 -maxdepth 2 -name SKILL.md | sort

# Confirm required frontmatter fields are present
rg -n "^(name|description):" skills/*/SKILL.md

# Compile-check Python script skills
python3 -m compileall skills

# Install one skill locally for runtime verification
cp -a skills/<skill-name> ~/.codex/skills/<skill-name>
```

## Coding Style & Naming Conventions
- Use YAML frontmatter at the top of every `SKILL.md`.
- Required keys: `name`, `description`.
- Skill names and folder names should be lowercase kebab-case.
- Keep instructions concise, explicit, and example-driven.
- Keep scripts small and deterministic; avoid environment-coupled assumptions.

## Testing Guidelines
- Run frontmatter checks for every modified skill.
- Smoke-test modified scripts (for example, run module/help mode if available).
- After install, trigger the skill once in the target CLI to verify routing.

## Commit & Pull Request Guidelines
This repo is new; use Conventional Commits for consistency (`feat:`, `fix:`, `docs:`, `chore:`).
- One logical change per commit.
- PRs should include changed skill paths and test/validation commands run.
- Include prompt examples when behavior or routing instructions change.

## Security & Configuration Tips
- Do not commit secrets, tokens, or local-only config files.
- Keep editor swap files and OS metadata out of version control.
