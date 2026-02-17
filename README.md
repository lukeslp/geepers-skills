# geepers-skills

Portable skill pack for Codex/Claude-style CLI workflows.

## What This Repo Contains

- Core routing helpers: `skills/geepers`, `skills/team`, `skills/swarm`, `skills/quality`, `skills/dream`
- Practical aliases: `skills/publish`, `skills/doublecheck`, `skills/poet`, `skills/readme`, `skills/humanize`
- Workflow aliases: `skills/scout`, `skills/planner`, `skills/builder`, `skills/testing`, `skills/validator`
- Source variants: `skills/dataset-publish`, `skills/geepers-doublecheck`, `skills/geepers-poet`, `skills/geepers-readme`

## Local Source of Truth

These were synced from:
- `~/.codex/skills`

## Install Into Codex

Copy one or more skills into your Codex skills directory:

```bash
cp -a skills/<skill-name> ~/.codex/skills/<skill-name>
```

Then restart Codex.

## Notes

- This repo is intended for sharing and versioning custom skills.
- Keep secrets/tokens out of skill files.
