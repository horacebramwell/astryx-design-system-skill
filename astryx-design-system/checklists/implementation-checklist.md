# Astryx Implementation Checklist

## Discovery

- [ ] Inspected `package.json`, lockfile, root providers, global CSS, and target surface.
- [ ] Confirmed React and `@astryxdesign/*` package versions.
- [ ] Selected the correct local CLI runner.
- [ ] Read `astryx manifest --json` for current capabilities when needed.
- [ ] Ran `astryx doctor --json` before setup-sensitive work.

## Planning

- [ ] Searched Astryx before inventing a custom primitive.
- [ ] Inspected matching page/block templates.
- [ ] Read `--skeleton` for page-scale work.
- [ ] Chosen application frame before content composition.
- [ ] Written the responsive contract.
- [ ] Chosen rows/tables vs cards based on information type.

## Component work

- [ ] Queried docs/props for every uncertain component.
- [ ] Verified exact import paths.
- [ ] Verified accessible labels and keyboard behavior.
- [ ] Avoided undocumented props and variants.
- [ ] Used Astryx behavior primitives before custom reimplementation.

## Styling/theming

- [ ] Used semantic tokens instead of hardcoded design values.
- [ ] Used `stylex.create()` values for `xstyle`.
- [ ] Used `className` for external styling classes.
- [ ] Avoided deprecated bare state/prop selectors.
- [ ] Avoided private `--_` CSS vars and unnecessary `!important`.
- [ ] Audited cascade layers when Tailwind/legacy CSS is present.
- [ ] Used built theme artifacts for production SSR when applicable.

## Swizzle

- [ ] Confirmed supported styling/theming cannot meet the requirement.
- [ ] Documented why source ownership is needed.
- [ ] Verified a working StyleX compiler path.
- [ ] Verified Next.js SWC compatibility when relevant.

## Compatibility

- [ ] Declared supported browser tier for layered surfaces.
- [ ] Feature-detected required modern platform capabilities where needed.
- [ ] Chosen fallback/polyfill/degraded behavior explicitly.

## Verification

- [ ] Formatter passes.
- [ ] Type checker passes.
- [ ] Tests pass.
- [ ] Production build passes.
- [ ] Light/dark checked where supported.
- [ ] Keyboard/focus checked.
- [ ] Loading/empty/error states checked.
- [ ] Responsive contract checked.
- [ ] `astryx doctor` re-run after setup/config/theme changes.
