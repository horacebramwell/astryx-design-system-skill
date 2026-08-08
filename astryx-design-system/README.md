# Astryx Design System Agent Skill

A reusable skill for coding agents that build, migrate, style, theme, debug, review, or extend applications using Meta's **Astryx** design system.

The skill is intentionally **CLI-driven**. Astryx is currently beta, and its own documentation recommends the CLI as the shared source of truth for people and agents. Rather than freezing 160+ component APIs into a static prompt, this skill teaches an agent to inspect the project, read Astryx's capability manifest, run `doctor`, search the live catalog, inspect template skeletons, query exact component docs, and then implement against the installed version.

## Package contents

```text
astryx-design-system/
├── SKILL.md
├── README.md
├── references/
│   ├── cli-workflow.md
│   ├── setup-styling.md
│   ├── layout-themes.md
│   ├── migration-browser.md
│   ├── integrations-api.md
│   └── research-sources.md
├── checklists/
│   ├── implementation-checklist.md
│   └── review-checklist.md
└── scripts/
    └── validate_skill.py
```

## Install

### Codex

Copy the folder to:

```text
~/.codex/skills/astryx-design-system/
```

### Claude Code

Copy the folder to:

```text
~/.claude/skills/astryx-design-system/
```

The directory name should remain `astryx-design-system` and the entry file should remain `SKILL.md`.

## Typical triggers

- "Build this page with Astryx."
- "Migrate this shadcn/Tailwind screen to Astryx."
- "Create a custom Astryx theme."
- "Why are my Astryx components unstyled?"
- "Use Astryx templates to build this dashboard."
- "Swizzle this Astryx component safely."
- "Audit this Astryx UI for production readiness."
- "Create an Astryx integration package."

## Design decisions baked into the skill

- **Runtime discovery over memorization.** `astryx manifest --json`, `search`, `component`, `template`, `docs`, and `doctor` are first-class workflow steps.
- **Frame first.** App shell and region budgets come before content.
- **No card soup.** Dense records become rows/tables; cards are for self-contained widgets.
- **Semantic styling.** Use Astryx tokens and supported styling surfaces instead of hardcoded values.
- **Theme-first customization.** Swizzle only after supported theme/style extension points are exhausted.
- **SSR-aware theming.** Built themes are preferred for production SSR.
- **Browser contracts.** Layered surfaces are reviewed against Astryx's support tiers.
- **Stable automation.** Scripts and agents branch on JSON response types/error codes rather than prose.

## Validate this skill package

```bash
python3 scripts/validate_skill.py
```

The validator checks required files, YAML-like frontmatter fields, matching skill name, relative reference links, and the established under-500-line `SKILL.md` quality constraint.

## Research basis

Prepared from Astryx's public documentation, official `facebook/astryx` repository documentation, CLI documentation, theming/styling/layout/migration/browser-support guides, and CLI integration authoring guide. Research snapshot: **2026-08-08**.

See `references/research-sources.md` for the source map and beta/version-drift notes.
