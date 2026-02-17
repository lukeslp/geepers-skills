---
name: dream
description: Dual-model second opinion. Use Claude CLI and Gemini CLI in read-only mode to critique a concept or implementation and synthesize recommendations.
aliases:
  - second-opinion
  - redteam-lite
---

# Dream Critique

Use this when you want an independent, two-model critique before implementation or release.

## Fast Intent

`/dream` means: run both Claude CLI and Gemini CLI in read-only mode, compare criticisms, then return a merged recommendation set.

## Inputs

- A concept, design, PR diff, or implementation path
- Optional focus: architecture, UX, performance, security, test strategy

## Read-Only Commands

Claude (read-only planning mode):
```bash
claude -p --permission-mode plan --tools "" "<critique prompt>"
```

Gemini (read-only planning mode):
```bash
gemini -p "<critique prompt>" --approval-mode plan --sandbox
```

## Workflow

1. Use the same prompt for both CLIs.
2. Ask each for:
   - Top risks/regressions
   - Missing tests/validation
   - Better alternatives with tradeoffs
   - Clear next actions
3. Synthesize overlap first (highest confidence).
4. Keep unique recommendations if they are concrete and testable.
5. Produce a final priority list: critical, important, optional.

## Prompt Template

```text
Critique this <concept|implementation> as a senior reviewer.
Focus on: <focus areas>.
Return:
1) Risks/regressions
2) Missing tests/validation
3) Better alternatives + tradeoffs
4) Recommended next steps (ordered)
Context:
<paste summary, files, or diff>
```
