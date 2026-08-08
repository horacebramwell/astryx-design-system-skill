# Migration and Browser Support Reference

## Migration philosophy

Astryx recommends incremental migration around product shells and workflows rather than a global style replacement.

Preserve:

- routing;
- domain/business logic;
- data fetching;
- state models;
- tests;
- product behavior unless explicitly redesigned.

## Recommended migration order

1. Install/configure Astryx and initialize agent docs.
2. Mount `Theme` at the application root.
3. Establish CSS cascade-layer order.
4. Render a foundation smoke-test surface.
5. Move the persistent frame/navigation.
6. Replace shared interactive primitives.
7. Replace global workflows such as command/search/settings/create/destructive confirmation surfaces.
8. Remove obsolete legacy styles route by route.
9. Verify each route before moving to the next.

## Cascade-layer safety

Layered CSS changes normal specificity intuition:

- unlayered styles outrank named layers;
- a later named layer can outrank an earlier one regardless of selector specificity.

This makes old resets dangerous.

Audit every pre-existing global/reset stylesheet. Explicitly assign resets/preflight to low layers rather than leaving them unlayered.

With webpack/Next.js, remember that import processing/hoisting can alter effective layer order. If necessary, keep the canonical layer declaration in a dedicated CSS file imported first, as Astryx's migration docs recommend.

## Browser support tiers (research snapshot 2026-08-08)

Astryx documents three levels:

- **Tier 1 — full fidelity:** modern baseline with CSS anchor positioning.
- **Tier 2 — functional:** components remain usable, but anchored layered surfaces may not position relative to triggers.
- **Tier 3 — best effort:** no-crash goal; theming/positioning may degrade.

The exact representative browser versions are time-sensitive. Query current Astryx browser-support docs when browser requirements are a release criterion.

## Platform features that matter

Astryx's browser guide highlights:

- CSS anchor positioning;
- Popover API;
- CSS `light-dark()`.

Layered components are the main source of the Tier 1/Tier 2 positioning gap.

Examples documented upstream include tooltips, hover cards, popovers, context menus, selectors/multiselectors, tokenizer suggestion menus, and anchored carousel controls.

## Compatibility strategy

For an app supporting older but still functional browsers:

- feature-detect instead of UA sniffing;
- decide whether to polyfill anchor positioning;
- provide a JS positioning fallback when warranted; or
- explicitly accept degraded positioning if product requirements allow it.

Do not add a polyfill reflexively without checking the app's actual audience and bundle/runtime constraints.

## Verification for migrated surfaces

For each route/surface verify:

- light and dark mode;
- keyboard navigation;
- focus-visible states;
- responsive behavior;
- loading, empty, and error states;
- selection/disabled/destructive states;
- dialog/popover dismissal;
- compatibility with the declared browser tier.
