# Setup and Styling Reference

## Baseline setup

Astryx requires React 19+ according to the current public getting-started guide.

Typical package set:

```bash
npm install @astryxdesign/core @astryxdesign/theme-neutral @astryxdesign/cli
```

Use the repository's package manager rather than rewriting package-manager conventions.

## Global CSS

Core published-package consumption uses precompiled styles. A basic setup imports:

```css
@import '@astryxdesign/core/reset.css';
@import '@astryxdesign/core/astryx.css';
@import '@astryxdesign/theme-neutral/theme.css';
```

Do not rearrange global CSS casually: Astryx uses cascade layers and existing resets/utilities can override it irrespective of ordinary specificity expectations.

## Theme provider

Wrap the app in `Theme`. For production SSR with a published theme, upstream recommends the theme's `/built` import paired with its CSS so component overrides exist at first paint.

For framework-specific link behavior, inspect the current core README/component docs before assuming a provider API.

## Styling priority

1. component props/variants;
2. theme tokens;
3. `xstyle` or `className` with semantic tokens;
4. supported external selectors;
5. theme component overrides/custom variants;
6. swizzled source.

## `xstyle`

- Every component documents `xstyle` support through StyleX-created styles.
- Values should come from `stylex.create()`.
- Do not pass arbitrary inline style objects to `xstyle`.
- Hover behavior in StyleX should be wrapped in `@media (hover: hover)`.

## `className` and external CSS

Use `className` for Tailwind, CSS Modules, Sass, plain CSS, Emotion/styled-components output, or other class-based styling.

When selecting Astryx internals externally, prefer stable `.astryx-*` classes plus reflected data attributes such as `data-variant` / `data-size`.

Do not write new rules against legacy bare state/prop classes such as `.primary`, `.sm`, or `.checked`.

## Tokens

Use semantic design tokens for:

- color;
- spacing;
- size;
- radius;
- shadows;
- motion duration/easing;
- typography;
- data visualization palettes.

Prefer token variables/typed token exports instead of hardcoded design values so custom themes and dark mode propagate.

## Tailwind

Astryx documents a Tailwind v4 bridge that maps system tokens to utilities. The important invariant is not the exact utility list but the layer contract:

- declare layer order before imports;
- layer Tailwind preflight/base intentionally;
- load Astryx reset/base/theme in their expected position;
- allow consumer utilities to win where intentionally desired.

If buttons/inputs suddenly lose padding or defaults, audit layer order before adding overrides.

## Swizzled/authored StyleX source

Published Astryx components ship precompiled; no StyleX compiler is required just to consume them.

A StyleX compiler **is** required if the app:

- authors its own StyleX source; or
- swizzles Astryx component source.

A missing compiler can produce an especially deceptive failure: code compiles while the swizzled component renders unstyled.

For Next.js App Router, follow the current Astryx example/documentation for an SWC-compatible StyleX transform. Do not introduce a Babel configuration that disables SWC merely to compile StyleX if that breaks `next/font` or other SWC-dependent behavior.

## Things to avoid

- hardcoded design colors and spacing where tokens exist;
- wrapper `<div>` elements used only to add spacing that the component can accept directly;
- `!important` as a first response to cascade problems;
- private CSS custom properties prefixed `--_`;
- unlayered legacy resets above Astryx;
- guessing theme selectors instead of checking `astryx component <Name>`.
