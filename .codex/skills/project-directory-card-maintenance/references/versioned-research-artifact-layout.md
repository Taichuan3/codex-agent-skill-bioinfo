# Versioned research artifact navigation

Use this reference when versioned data, reports and figures are difficult to navigate. It defines a classification and card pattern, not permission to move files.

## Classify before writing cards

Identify these portable artifact roles:

- curated stable inputs and external reference material;
- immutable raw snapshots;
- reusable processed data consumed by current code;
- interim or cache-like outputs;
- current strategy/method documents and superseded versions;
- run reports grouped by analysis family;
- report-used figures and their source data;
- external reviews or prompts;
- deprecated or provenance-only artifacts.

Do not infer `current`, `canonical` or `deprecated` from a version-like filename alone. Verify against manifests, registries, producer/consumer code and user-confirmed project state.

## Navigation pattern

For each durable family, a short Directory Card should state:

1. purpose and scope;
2. current/candidate/deprecated artifacts;
3. what to read first;
4. producing script or command;
5. exact manifest/registry pointer;
6. replacement relationships and known path caveats.

Use a machine-readable artifact manifest for exact path, family, timestamp, status and size metadata. The card should summarize and link, not reproduce the entire inventory.

## Consumer verification

- Discover artifacts recursively when report families span historical and current subdirectories.
- Compare card entries with actual producer and consumer paths.
- If paths changed in an already authorized migration, verify current scripts and latest-artifact discovery use the new locations.
- Preserve historical reports as immutable snapshots unless the user explicitly authorizes rewriting them.

## Migration handoff

If classification suggests renaming or moving artifacts, stop at a proposed navigation map. Hand off to `research-data-organization`, which must create a migration map covering source, target, reason, consumers, compatibility action and verification. No physical move occurs without explicit user authorization.
