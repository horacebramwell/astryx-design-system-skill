# Layout and Theme Reference

## Frame-first layout

Astryx's public layout guidance explicitly recommends deciding the application frame before writing content.

Choose among:

- `AppShell` for top/side navigation applications;
- `Layout` + `LayoutPanel` + `LayoutContent` for multi-pane tools;
- plain content columns for documents, marketing, and simpler forms.

Budget regions before filling them. Upstream examples use concrete widths for side navigation, rails, inspector panels, and facet/filter regions. Treat those as guidance rather than universal constants.

## Responsive contract

Write down the behavior before implementation:

- what remains visible;
- what collapses;
- what becomes a drawer;
- what overlays the content;
- what wraps;
- what is removed at narrow widths.

For master-detail applications, Astryx guidance favors an inspector panel that can overlay content at narrower widths instead of crushing the central workspace.

## Cards vs rows

The strongest design warning in Astryx layout documentation is against "card soup."

Use:

- `Table` for columnar/scannable datasets;
- list/item rows for single-line records;
- cards for self-contained widgets, chart panels, galleries, or isolated settings groups;
- empty-state components inside the region they describe.

Avoid:

- one card per record in dense data;
- full-width stacks of cards as page structure;
- nested cards;
- decorative badges for generic metadata.

## Templates

Use `astryx template --list` to find an archetype and `--skeleton` to understand its spatial model before pulling full source.

Templates are examples for composition quality, not immutable layouts. Preserve their structural lessons while adapting the product.

## Theme model

Astryx themes can control:

- semantic tokens;
- typography scale/families;
- color generation;
- radii;
- motion;
- component overrides;
- icons/fonts;
- custom component prop variants.

Use `defineTheme` for custom themes and inspect the live theme docs/TypeScript types before relying on a remembered shape.

## Theme inheritance

Astryx supports extending a base theme. Upstream documents different merge behavior by field (tokens, components, icons, fonts, and scale inputs). When exact merge semantics matter, query `astryx docs theme` for the installed version.

## Component overrides

Prefer semantic keys rather than raw selectors. Typical concepts include:

- `base` for all instances;
- `prop:value` keys for variant/state axes;
- public CSS variables only when no standard CSS property maps to the customization.

Check `astryx component <Name>` for supported theming targets and public variables.

## Custom variants

Themes can extend component prop values. Build the theme so Astryx can emit type augmentations. Do not add arbitrary values to component props without the corresponding theme support.

## Runtime vs built themes

Runtime/source themes are convenient for development and client-only rendering.

For production SSR, prefer built theme artifacts so component overrides arrive in static CSS instead of appearing only after hydration.

Published themes expose a `/built` path that pairs with `theme.css`; custom themes can be compiled with `astryx theme build`.

## Light/dark mode

Astryx uses light/dark token tuples and `Theme` mode values. Treat theme mode as application state when users can switch it.

Test both modes, including semantic status colors, disabled states, borders, overlays, charts, and third-party surfaces that read resolved token values in JavaScript.
