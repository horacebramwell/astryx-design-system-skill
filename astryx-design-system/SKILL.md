---
name: astryx-design-system
description: Use when building, migrating, styling, theming, debugging, auditing, or extending React interfaces with Meta's Astryx design system. Covers Astryx CLI-driven discovery, components, templates, hooks, themes, tokens, layout conventions, Tailwind/StyleX interop, swizzling, browser support, migrations, diagnostics, JSON/programmatic APIs, and integration packages. Always query the installed Astryx CLI before relying on remembered component APIs because Astryx is currently beta and its CLI is designed to be the source of truth for agents.
---

# Purpose

Build production-quality interfaces with Astryx while staying aligned with the exact version installed in the project.

Astryx is intentionally agent-ready: its CLI exposes the same component docs, templates, hooks, tokens, guidance, and capability metadata used by humans. Treat the live CLI as authoritative for component names, props, variants, imports, theming targets, templates, hooks, and migration behavior.

# When To Use

Use this skill when the task involves any of the following:

- Adding Astryx to a React project.
- Building a page, dashboard, settings surface, data tool, form, navigation shell, dialog, table, list, or other UI with Astryx.
- Converting an existing Tailwind, shadcn, Radix, or custom React UI to Astryx.
- Styling Astryx components with StyleX, Tailwind, CSS, CSS Modules, or another styling system.
- Creating or extending an Astryx theme, custom variant, icon registry, typography scale, motion scale, or component override.
- Debugging missing styles, CSS cascade problems, theme flashes, version mismatches, or unsupported component props.
- Swizzling/ejecting a component for source ownership.
- Auditing accessibility, keyboard behavior, responsive layout, dark mode, browser compatibility, or design-system consistency.
- Consuming Astryx from scripts through `--json` or `@astryxdesign/cli/api`.
- Authoring an Astryx integration package containing components, templates, or upgrade codemods.

Do not activate merely because the project uses React. Activate when Astryx is present, requested, being evaluated for an existing Astryx codebase, or clearly implicated by package names such as `@astryxdesign/*`.

# Inputs Required

Before changing code, determine from the repository when available:

- package manager and lockfile;
- React version;
- installed `@astryxdesign/*` packages and versions;
- current global CSS/reset/theme setup;
- whether `Theme` is mounted at the app root;
- whether Tailwind or StyleX is already configured;
- existing `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or Astryx-generated agent docs;
- target route/surface and its surrounding application shell;
- supported-browser requirements if layered surfaces are involved.

Do not ask the user for information that can be inspected from the repository.

# Core Rule: Discover, Do Not Guess

Astryx is beta. Never invent a component, prop, import path, template name, hook, theme target, or CLI flag from memory.

Before substantial Astryx work:

1. Confirm the CLI is installed or deliberately use the scoped one-off package.
2. Read the CLI capability manifest.
3. Run diagnostics.
4. Query only the docs/components/templates needed for the task.

Recommended local flow after confirming `@astryxdesign/cli` is a project dependency:

```bash
# adapt the runner to the repository's package manager
npm exec -- astryx manifest --json
npm exec -- astryx doctor --json
```

For a one-off invocation when the CLI is not installed locally, use the scoped package explicitly:

```bash
npx @astryxdesign/cli manifest --json
```

Never run bare `npx astryx` before `@astryxdesign/cli` is installed. npm may resolve an unrelated package named `astryx`.

If a command or flag is uncertain, inspect `astryx manifest --json`; do not scrape remembered help text.

# Workflow

## 1. Inspect the Existing Project

Read relevant repository files first. Preserve routing, state, data fetching, business logic, tests, and existing application architecture unless the task specifically requires changes.

Look for:

- `package.json` and package-manager metadata;
- root layout/providers;
- global CSS and CSS layer declarations;
- theme source/build artifacts;
- shared UI primitives;
- route-level shells and navigation;
- existing Astryx config and integration packages.

For migrations, treat Astryx adoption as a product-shell and workflow migration, not a blind class-name replacement.

## 2. Establish the Correct CLI Surface

Prefer the project's local Astryx CLI so documentation matches installed core packages.

Run:

```bash
astryx manifest --json
astryx doctor --json
```

The manifest is the machine-readable source for current commands, arguments, options, JSON support, and response types. `doctor` is read-only and should be used as an early health check and again before completion when setup changed.

If `doctor` reports a core/CLI version mismatch, resolve version alignment before relying on generated docs or applying codemods.

## 3. Search Before Choosing Components

When the needed primitive is not already obvious from inspected code, search across components, hooks, docs, and templates:

```bash
astryx search "<need>" --json
```

Optionally restrict by domain only after the broad search has identified the likely surface.

Never substitute a generic `<div>`, custom control, or third-party primitive until searching confirms Astryx lacks the needed capability or the task explicitly requires custom behavior.

If an Astryx capability is genuinely missing, report the gap rather than inventing an API.

## 4. Start Full Surfaces From Templates

For page-scale or workflow-scale UI:

```bash
astryx template --list
astryx template <TemplateName> --skeleton
```

Study the skeleton before copying or adapting the full template. The skeleton communicates spatial structure and is usually a better planning artifact than raw source.

Use block templates for reusable interaction patterns and page templates for larger layouts. Adapt content and product requirements without discarding the layout principles encoded by the template.

## 5. Query Every Component You Will Depend On

Before implementing or modifying an Astryx component whose API is not already proven by local code, retrieve its current docs:

```bash
astryx component <Name>
astryx component <Name> --props
```

Use component docs to confirm:

- exact import path;
- props and types;
- variants and states;
- examples and composition patterns;
- accessibility guidance;
- theming targets and public CSS variables;
- related templates or hooks.

For automation, prefer `--json`. For model context where machine parsing is unnecessary, `--dense` is token-efficient.

## 6. Build Frame First

Choose the application frame before filling it with content.

Default layout reasoning:

- `AppShell` for applications with persistent top/side navigation.
- `Layout` + `LayoutPanel` + `LayoutContent` for multi-pane tools, explorers, consoles, and master-detail workflows.
- Plain content columns for documents, marketing pages, and simple forms.

Write a responsive contract before implementation: identify which regions remain fixed, collapse, overlay, wrap, or disappear at meaningful breakpoints.

For master-detail workflows, favor a fixed/resizable inspector panel rather than unnecessary route changes when the surrounding product pattern supports it.

## 7. Choose Containers by Information Type

Avoid generic AI-dashboard composition.

- Dense, scannable, sortable, selectable records belong in `Table` or list/item rows.
- Self-contained widgets, KPI tiles, chart panels, gallery entries, and isolated settings groups may use cards.
- Do not wrap every list item in a `Card`.
- Do not nest cards as page structure.
- Reserve `Badge` for counts and enumerated states rather than decorative metadata.
- Use the Astryx component docs to choose status/metadata primitives.

## 8. Style Through the Supported Escalation Path

Use the least invasive customization level that satisfies the requirement:

1. component API and variants;
2. theme tokens;
3. `xstyle`/`className` using semantic tokens;
4. supported external CSS selectors;
5. component theme overrides/custom variants;
6. swizzle only when source ownership is truly required.

Rules:

- `xstyle` accepts styles produced by `stylex.create()`, not arbitrary inline objects or class strings.
- Use `className` for Tailwind, CSS Modules, plain CSS, and styling-library classes.
- Prefer semantic Astryx tokens over hardcoded colors, spacing, radius, motion, or typography.
- When writing StyleX hover styles, guard them with `@media (hover: hover)`.
- Prefer stable `.astryx-*` component classes plus reflected `data-*` attributes for external CSS selectors.
- Do not author new CSS against legacy bare prop/state classes such as `.primary`, `.sm`, or `.checked`.
- Do not use private Astryx CSS custom properties prefixed `--_`.
- Avoid `!important`; diagnose cascade/specificity instead.

## 9. Preserve CSS Cascade Layer Safety

Astryx styles are cascade-layered. Existing resets and Tailwind can silently override components if imported into the wrong layer or left unlayered.

When Tailwind or legacy global CSS is present:

- declare layer order explicitly before imports;
- place legacy resets in the lowest reset layer;
- ensure Astryx base/theme layers are ordered intentionally;
- ensure Tailwind preflight is layered rather than silently overriding Astryx;
- inspect webpack/Next.js import-hoisting behavior when layer order appears correct in source but wrong in output.

If Astryx components unexpectedly lose padding, borders, or control styling, audit cascade layers before rewriting component CSS.

See `references/setup-styling.md`.

## 10. Theme Correctly

For ordinary theming, prefer `Theme` + an Astryx theme package or `defineTheme` rather than ad hoc component wrappers.

For custom themes:

- override only what differs from defaults;
- use scale inputs for typography, color, radius, and motion where appropriate;
- use semantic component override keys such as `base` and `prop:value`;
- inspect `astryx component <Name>` before writing component theme targets;
- build custom themes with `astryx theme build` when production/SSR fidelity matters.

Production SSR apps should use pre-built theme artifacts (or the published `/built` theme import plus `theme.css`) so component overrides are present on first paint.

Runtime-injected themes are convenient for development and client-only apps but can flash component overrides during SSR hydration.

## 11. Swizzle Only as a Last Resort

`astryx swizzle <Component>` transfers component source ownership into the application. Use it only when supported component APIs, theming, and styling escape hatches cannot meet the requirement.

Before swizzling:

- read the component docs and source surface;
- document why theme/style overrides are insufficient;
- verify the project has a StyleX compiler path for authored/swizzled source;
- understand that future upstream fixes no longer arrive automatically for the owned copy.

Critical Next.js App Router rule: do not add the canonical StyleX Babel plugin merely to compile swizzled Astryx source if doing so disables SWC and breaks SWC-dependent features such as `next/font`. Follow the current Astryx docs/example for the supported SWC-based path.

## 12. Handle Browser Support Deliberately

Astryx relies on modern platform features including the Popover API, CSS anchor positioning, and `light-dark()`.

If the surface uses layered/anchored UI such as tooltips, popovers, context menus, selectors, tokenizers, or anchored carousel controls:

- determine the application's supported-browser tier;
- feature-detect capabilities rather than user-agent sniffing;
- decide explicitly whether to polyfill/fallback or accept degraded positioning for older supported browsers.

Do not claim full fidelity on a browser tier the project has not chosen to support.

See `references/migration-browser.md`.

## 13. Migrate Incrementally

For existing apps:

1. install/configure Astryx and agent docs;
2. mount `Theme` at the root;
3. fix CSS layer order;
4. smoke-test foundations;
5. migrate the persistent frame/navigation;
6. replace shared interactive primitives;
7. replace global workflows and dialogs;
8. remove obsolete legacy styling route by route;
9. verify light/dark, keyboard, responsive, loading, empty, and error states before moving on.

Keep existing product logic intact unless the user requested a redesign of behavior.

## 14. Use Stable Machine Interfaces for Automation

When consuming Astryx programmatically:

- prefer `--json` envelopes or `@astryxdesign/cli/api`;
- narrow results using the response `type` discriminator;
- branch on stable error `code` values, never human-readable error strings;
- inspect the live manifest for supported response types rather than hardcoding stale assumptions.

Use direct API imports when building a TypeScript tool already depending on the CLI package; use subprocess JSON only when process isolation is appropriate.

## 15. Author Integrations Through the Official Extension Model

When creating reusable Astryx packages, use `astryx.config.{ts,mjs,js}` on the consumer side and `astryx.integration.{ts,mjs,js}` on the integration-package side.

Integration packages may contribute documented components, templates, and codemods. Follow the live `astryx docs cli-integrations` guide for exact metadata and export requirements because authoring contracts can change during beta.

Do not invent custom discovery conventions that bypass Astryx's integration mechanism.

# Verification

Before declaring Astryx work complete:

1. Re-run `astryx doctor` if setup, packages, config, themes, or agent docs changed.
2. Run the repository's formatter, type checker, tests, and build.
3. Confirm no guessed Astryx props/imports remain; verify questionable ones with the CLI.
4. Verify responsive behavior against the written contract.
5. Verify both light and dark modes when the product supports both.
6. Keyboard-test interactive flows and focus order.
7. Check loading, empty, error, selected, disabled, hover, focus-visible, and destructive states as applicable.
8. If layered surfaces are used, verify the browser-support contract.
9. If a custom theme is used in SSR, verify built theme CSS is loaded on first paint.
10. If swizzled StyleX source exists, verify its compiler actually emits styles in production build output.

Use `checklists/implementation-checklist.md` and `checklists/review-checklist.md` for deeper passes.

# Output Format

When reporting completed work, include:

- what Astryx CLI/docs were consulted;
- components/templates/hooks chosen and why;
- theme/styling approach;
- layout/responsive decisions;
- verification performed;
- any browser-support, migration, or swizzle tradeoffs that remain.

Keep implementation notes tied to actual project evidence. Do not imply that a component or prop exists unless verified in the project version or live CLI output.

# Quality Bar

A strong Astryx implementation:

- looks like a deliberate product, not a generic card-heavy AI mockup;
- uses Astryx behavior/accessibility primitives before custom reimplementation;
- follows frame-first layout and explicit responsive contracts;
- uses semantic tokens and supported customization paths;
- avoids undocumented props and brittle selectors;
- is fully navigable by keyboard;
- works in the product's declared browser tier;
- passes project type/build/test checks;
- remains maintainable as Astryx evolves.

# Common Failure Modes

- Guessing a component API instead of querying `astryx component`.
- Running bare `npx astryx` before the Astryx CLI is installed.
- Building a whole page from scratch without inspecting templates.
- Replacing product structure with stacked cards.
- Hardcoding colors/spacing instead of using Astryx tokens.
- Passing plain objects to `xstyle` instead of StyleX-created styles.
- Styling deprecated bare state classes.
- Letting Tailwind preflight or a legacy reset override Astryx layers.
- Using runtime theme injection in SSR production and accepting a hydration flash unintentionally.
- Swizzling before trying supported theme/style extension points.
- Swizzling without a working StyleX compiler.
- Adding a Babel-based StyleX path to a Next.js App Router project and breaking SWC features.
- Assuming a popover-positioning experience is identical across browser tiers.
- Branching automation on human-readable CLI error text.
- Hardcoding a current Astryx version into the skill.

# Supporting References

Read the smallest relevant reference for the task:

- `references/cli-workflow.md` — CLI discovery, JSON API, manifest, doctor, automation.
- `references/setup-styling.md` — installation, CSS imports, Tailwind, StyleX, tokens, selector rules, swizzling.
- `references/layout-themes.md` — frame-first design, cards vs rows, responsive contracts, themes and SSR.
- `references/migration-browser.md` — migration order, cascade-layer safety, browser support tiers.
- `references/integrations-api.md` — programmatic API and Astryx integration authoring.
- `references/research-sources.md` — upstream source map and research notes.
