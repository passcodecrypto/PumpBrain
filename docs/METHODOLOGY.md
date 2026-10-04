# PumpBrain methodology

Registry version 0.3.0 · last verified 2026-10-04T16:45:00Z

## Principles
- Discovery, convergence and the Truth Engine run on fixed, versioned rules. AI is optional interpretation only.
- No look-ahead: outcomes are measured only after each observation window (5/15/30/60 min) closes.
- Unknown means unknown. Unverified fields are `null` or labelled `unknown`; nothing is assumed.
- Simulated or test data (Lab, scan, callout tests) never feeds production decisions.
- Callout data is attention, not conviction. It shows UNAVAILABLE until an authorized source is connected.

## Experiment 011 (Live Brain): three separate states
| State | Meaning | Current |
|---|---|---|
| Configured policy | Operator-approved risk limits, append-only versions | CONTROLLED_LIVE_TEST-v1 |
| Successful simulation | Unsigned transactions simulated on mainnet; no signature, no broadcast | BUY→SELL chained round trip PASSED |
| Active live trading | Signed, broadcast orders | **OFF: HALTED / LIVE EXECUTION LOCKED** |

A passed simulation is not permission to execute. "1 SOL → 100 SOL in 30 days" is an aspirational target, not an expected or guaranteed return.

## Qualification pipeline (011)
Quote → unsigned build → inspection (fee payer, signers, program allowlist, mint) → policy limits → simulation with effect checks → separate execution gate (kill switch, limits, cooldowns, idempotency) → STOP.
For the round trip, the BUY and SELL are simulated in order through provider bundle simulation, so the SELL runs on the BUY's resulting state. If that capability isn't available, the result is CHAINED SIMULATION UNAVAILABLE and the blocker stays.

## Secrets
Only variable names are published: `SOLANA_RPC_URL`, `LIVE_BRAIN_WALLET_KEY`, `LIVE_BRAIN_STOP_PASSPHRASE`. Values are never committed.
