# PumpBrain

Versioned experiment specifications for PumpBrain, covering experiments 001–011.

The canonical specification is [`experiments/registry.json`](experiments/registry.json), currently registry v0.1.0 / schema v1.0.0. This repository contains documentation and registry validation. The Lovable application source is not synced here. Registry checks do not prove deployment, trading readiness, provider connectivity or runtime behavior.

## Experiments

| ID | Name | Intended purpose | Implementation |
|---|---|---|---|
| 001 | Convergence Chamber | Study independent signal convergence and persistence. | Unknown |
| 002 | Narrative Garden | Study forming narratives. | Unknown |
| 003 | Signal DNA | Study recurring signal structures. | Unknown |
| 004 | Brain vs Random | Compare structured signals with randomized persistence. | Unknown |
| 005 | Shadow Brain | Record frozen hypothetical decisions. | Unknown |
| 006 | Paper Brain | Evaluate decisions using simulated SOL. | Unknown |
| 007 | Strategy Arena | Compare frozen strategies. | Unknown |
| 008 | Memory Chamber | Study historical pattern recognition. | Unknown |
| 009 | Signal Decay | Measure signal duration. | Unknown |
| 010 | The Hive | Study collective activity. | Unknown |
| 011 | Live Brain | Execute policy-constrained autonomous Solana trades. | Unknown |

Names and purposes were recovered from prior project specifications; they are not deployment evidence. Exact routes, activation state and experiment test results remain unknown. Callouts belong within the existing experiments; there is no Experiment 012. Their last documented provider state was unavailable, and a current connection has not been verified.

## Validate changes

Use Python 3.12 and an isolated environment:

```sh
python -m venv .venv
.venv/bin/python -m pip install jsonschema==4.25.1
.venv/bin/python scripts/validate_registry.py
```

The GitHub Actions workflow validates pushes to `main`, pull requests and manual runs. It checks the JSON Schema, required fields, allowed status values, the exact experiment ID sequence, evidence references and proposed route IDs. It does not test the application or scan every possible secret format.

## Update the registry

Keep IDs stable and retain evidence sources. Bump `registry_version` when content changes; bump `schema_version` and update the schema when structure changes. Record commit or run evidence before changing unknown implementation, activation or test states. Keep recommendations separate from verified behavior. Update this table when names, purposes or implementation status change.

## Credentials and Live Brain

[`.env.example`](.env.example) documents only the variable names recovered from prior specifications, with empty values. Exact app bindings remain unverified. Store real values server-side outside Git. `.gitignore` excludes common credential files; it does not remove secrets already tracked and cannot guarantee that every secret filename is covered.

Adding these files does not activate Live Brain. Before activation, verify the registry's dry-run criteria, numeric risk limits, signing isolation, legitimate required data sources and authenticated emergency stop. Simulated signals must never enter live execution.

## Next source-of-truth step

Sync the actual Lovable project source into this repository, then map implemented routes and services to the registry and record test results. Until then, implementation status stays unknown.
