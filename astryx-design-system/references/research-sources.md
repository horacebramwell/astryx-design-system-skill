# Research Sources

Research snapshot: **2026-08-08**

Astryx is currently beta. This skill separates durable workflow principles from version-sensitive API details and instructs agents to query the installed CLI at runtime.

## Primary sources

- Astryx homepage: https://astryx.atmeta.com/
- Getting Started: https://astryx.atmeta.com/docs/getting-started
- CLI: https://astryx.atmeta.com/docs/cli
- Styling Components: https://astryx.atmeta.com/docs/styling
- Theme System: https://astryx.atmeta.com/docs/theme
- Tokens: https://astryx.atmeta.com/docs/tokens
- Layout: https://astryx.atmeta.com/docs/layout
- Migration Guide: https://astryx.atmeta.com/docs/migration
- Browser Support: https://astryx.atmeta.com/docs/browser-support
- CLI Integrations: https://astryx.atmeta.com/docs/cli-integrations
- Official repository: https://github.com/facebook/astryx
- Core package README: https://github.com/facebook/astryx/blob/main/packages/core/README.md
- Astryx architecture blog: https://astryx.atmeta.com/blog/how-astryx-works
- Astryx CLI/template-quality blog: https://astryx.atmeta.com/blog/astryx-cli-build-command

## Important source findings encoded in the skill

1. **The CLI is designed as agent-facing documentation.** It exposes components, hooks, templates, docs, tokens, diagnostics, and a capability manifest.
2. **Runtime discovery matters.** The CLI manifest is generated from actual command metadata so agents do not need to scrape help output.
3. **JSON is first-class.** Commands support typed envelopes and stable error codes intended for machine consumption.
4. **`doctor` is read-only.** It is suitable for local diagnostics and CI gating.
5. **Full surfaces should start from templates.** Astryx's own AI-quality work emphasizes giving agents strong examples and template skeletons.
6. **Layout is frame-first.** The official guidance explicitly warns against content-first card stacks and generic "card soup."
7. **Customization is graduated.** Component API → tokens/theme → styling → theme overrides/custom variants → swizzle.
8. **Published components are precompiled.** A StyleX compiler is only necessary when the app authors StyleX source or swizzles component source.
9. **Next.js + StyleX has a sharp edge.** A naive Babel path can disable SWC and break SWC-dependent Next features; follow the current Astryx example.
10. **Production SSR should use built themes.** Runtime-injected component overrides can flash during hydration.
11. **Cascade layers are a migration hazard.** Unlayered or badly ordered legacy resets/preflight can silently defeat Astryx styles.
12. **Browser tiers are explicit.** Anchor positioning is the main full-fidelity gap for layered surfaces in the documented Tier 1/Tier 2 split.
13. **Integrations are native.** Third-party packages can register components/templates/codemods into the same CLI discovery system.

## Version-drift note

At the research date, different Astryx public pages/examples contained different version numbers because some snippets demonstrate older states while the main CLI page labels a newer release. The skill therefore avoids pinning a library version and requires installed-version discovery before implementation.

## What is intentionally not frozen into this skill

- the complete 160+ component catalog;
- every component prop and variant;
- every template/hook name;
- exact current CLI version;
- exact current browser version matrix;
- undocumented MCP tool names/configuration;
- unstable experimental config fields.

Those should be resolved from the installed CLI or current upstream documentation when needed.
