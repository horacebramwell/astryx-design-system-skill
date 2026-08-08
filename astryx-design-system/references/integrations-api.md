# Integrations and Programmatic API Reference

## CLI programmatic API

Astryx exposes the same operations behind its CLI through `@astryxdesign/cli/api`.

The public CLI documentation shows imports for operations including component, docs, discover, template, hook, search, and `AstryxError`.

Principles:

- use the installed package's exported types;
- branch on stable error codes;
- narrow returned envelopes by their `type` discriminator;
- prefer the generated CLI manifest to discover current commands/options;
- avoid coupling to removed convenience union types.

## Subprocess JSON consumption

When spawning the CLI:

- use `--json`;
- parse the structural envelope;
- detect error envelopes with the package's JSON helpers when available;
- reconstruct only the union of response types your tool actually consumes.

## Project config

Astryx reads optional `astryx.config.{ts,mjs,js}` beside `package.json`.

The current docs describe fields for integration package names, issue reporting, post-codemod hooks, and some experimental surfaces. The schema is strict, so unknown fields should be treated as errors rather than ignored configuration.

Always inspect the live config docs/types before writing uncommon fields.

## Integration packages

The official extension model uses:

- consumer-side `astryx.config.{ts,mjs,js}`;
- package-side `astryx.integration.{ts,mjs,js}`.

An integration can contribute:

- documented components;
- page/block templates;
- upgrade codemods.

### Documented components

The public authoring guide associates a component source file with a same-stem `.doc.{ts,mjs,js}` metadata file so the CLI can expose documentation.

Do not guess the metadata object shape. Query `astryx docs cli-integrations` in the target version and use the package's authoring types.

### Templates

Integration templates use adjacent `.template.{ts,mjs,js}` metadata. The source must be included in package exports so the consumer CLI can materialize it.

Extension-sensitive module resolution details can change; follow the current authoring guide and verify the exported template path can actually be imported by a consumer.

### Codemods

Package integrations can contribute upgrade codemods through the integration manifest. Do not reuse internal core-release staging conventions for a third-party integration unless the public integration guide explicitly instructs it.

## Discovery

Once an integration package is installed and registered, its contributions should participate in the same Astryx CLI discovery surfaces as core contributions.

This is important for agent usability: an extension should teach the CLI about its components/templates rather than requiring a separate undocumented prompt convention.
