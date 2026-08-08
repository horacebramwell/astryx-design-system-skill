# Astryx Review Checklist

Use this for code review or production-readiness audits.

## API correctness

- [ ] No guessed Astryx component names, props, variants, hooks, templates, or imports.
- [ ] Uncertain APIs were validated with the installed CLI.
- [ ] Automation branches on JSON `type` / stable error `code` rather than human prose.

## Information architecture

- [ ] Page has a deliberate shell/frame.
- [ ] Region widths/behavior are intentional.
- [ ] Responsive collapse/overlay behavior is explicit.
- [ ] Dense data is rows/tables, not card-per-record.
- [ ] Cards are limited to self-contained widget-like content.
- [ ] Badges are meaningful states/counts, not decoration.

## Accessibility and interaction

- [ ] Interactive controls use Astryx behavior primitives where available.
- [ ] Icon-only controls have accessible names.
- [ ] Keyboard navigation and focus order work.
- [ ] Dialog/popover close and focus-return behavior is correct.
- [ ] Disabled/error/destructive states remain understandable without color alone.

## Styling system

- [ ] Semantic Astryx tokens are used.
- [ ] `xstyle` values come from StyleX when used.
- [ ] External CSS targets stable class/data surfaces.
- [ ] No new legacy bare prop/state selectors.
- [ ] No private Astryx CSS variables.
- [ ] No unnecessary `!important`.
- [ ] CSS reset/preflight layer order is safe.

## Theme and SSR

- [ ] `Theme` is mounted in the correct scope.
- [ ] Custom theme overrides use supported semantic targets.
- [ ] Custom variants are built/type-augmented.
- [ ] Production SSR loads built theme CSS on first paint.
- [ ] Light/dark mode is tested and third-party visualizations use resolved tokens if needed.

## Swizzled code

- [ ] Swizzle was justified.
- [ ] StyleX compilation is present in production build.
- [ ] Next.js SWC/`next/font` behavior remains intact.
- [ ] Team understands the owned source no longer receives upstream fixes automatically.

## Browser/runtime

- [ ] Layered surfaces match the application's declared browser tier.
- [ ] Anchor/popover/theme platform features are feature-detected where fallback behavior exists.
- [ ] No UA sniffing is used for capability detection.

## Maintenance

- [ ] `astryx doctor` passes without unexplained failures.
- [ ] Core/CLI/theme package versions are compatible.
- [ ] Agent docs/config are valid if maintained by the project.
- [ ] No version-sensitive facts were hardcoded where the CLI can discover them.
