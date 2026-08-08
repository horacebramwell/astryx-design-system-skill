# Astryx Design System Skill

A production-grade agent skill for building, styling, migrating, and reviewing applications with the [Astryx](https://astryx.atmeta.com/) design system and CLI.

The skill is designed to stay useful as Astryx evolves: instead of hard-coding a static component catalog, it teaches coding agents to discover the installed Astryx version, query the Astryx CLI for current capabilities and component documentation, use templates and diagnostics, and verify implementation quality.

## Skill

The reusable skill lives in [`astryx-design-system/`](./astryx-design-system/).

Key coverage includes:

- Astryx CLI discovery and diagnostics
- component, hook, template, and documentation lookup
- frame-first layout and composition guidance
- styling, StyleX, Tailwind, tokens, and theming
- migration workflows and CSS cascade-layer pitfalls
- browser support and anchored-surface fallbacks
- swizzling and source customization safeguards
- third-party Astryx integrations
- implementation and review checklists

## Source

Astryx documentation: https://astryx.atmeta.com/

Astryx repository: https://github.com/facebook/astryx
