# CLI Workflow Reference

## Principle

Astryx's CLI is the operational documentation surface for both humans and agents. The project's installed CLI should be preferred because it reflects the package version actually in use.

## Safe runner selection

1. Inspect `package.json` and lockfiles.
2. If `@astryxdesign/cli` is already installed, invoke the local binary through the project's package manager.
3. If it is not installed and a one-off call is appropriate, use the **scoped** package: `npx @astryxdesign/cli ...`.
4. Do not use bare `npx astryx` before the CLI package is installed; npm can resolve an unrelated package.

## Discovery sequence

```bash
astryx manifest --json
astryx doctor --json
astryx search "table filters" --json
astryx template --list
astryx template <Name> --skeleton
astryx component <Name>
astryx component <Name> --props
astryx docs <topic> --dense
```

Use the manifest rather than hardcoding the command list. It is generated from the CLI's command metadata and includes arguments, options, JSON support, response types, and examples.

## Key command families documented upstream

At the research snapshot, Astryx documents commands for:

- `init`
- `component`
- `search`
- `docs`
- `template`
- `hook`
- `swizzle`
- `upgrade`
- `theme build`
- `discover`
- `doctor`
- `manifest`

The skill intentionally does not freeze the complete flag set. Read `manifest --json` in the project before using less-common options.

## Global output modes

Astryx documents:

- `--json` — typed machine-readable envelopes.
- `--dense` / language `dense` — token-efficient documentation for AI use.
- `--detail` — controls list/detail verbosity.
- localized output options.

## JSON rules

A successful response has a `type` discriminator and `data`. Errors include a stable machine-readable `code`.

Automation rules:

- branch on `type`, not output layout;
- branch on error `code`, not prose `error` text;
- use suggestions returned by the CLI for misspelled/unknown entities;
- do not assume central union types that upstream has removed; import the specific response types you consume.

## Programmatic API

The CLI exposes the same behavior as type-safe imports from `@astryxdesign/cli/api`, including functions such as component/docs/template/hook/search/discover and `AstryxError`.

Prefer direct API imports when:

- the caller is TypeScript/JavaScript;
- the CLI is already a dependency;
- process spawning adds no value.

Prefer `--json` subprocess calls when:

- language/process isolation matters;
- a shell/CI tool consumes Astryx;
- you want command-level parity without importing package internals.

## `doctor`

`astryx doctor` is read-only. Upstream documents checks for:

- Node version;
- core package installation;
- core/CLI version alignment;
- theme packages/wiring;
- `astryx.config` validity;
- generated AI agent docs;
- peer dependencies;
- package manager detection.

It exits nonzero on failures, so it can be used as a CI gate.

## Agent rule

When a component, hook, template, docs topic, CLI option, or response shape is uncertain, stop guessing and query the CLI.
