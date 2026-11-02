# SENTRY-13 (prototype)

SENTRY-13 is an early prototype of a multiplicative integrity calculation for funding pipelines. It combines the scores of several pipeline stages ("nodes") into one number, so that a failure at any single stage cannot be offset by good scores elsewhere.

**Status: prototype and research code. It has not been validated on real data, and it is not a production system.** Scores from this code are screening aids for human review. They are not findings of wrongdoing and not legal or audit conclusions.

## What this repository contains today

- `core/engine.py`: the multiplicative engine (`MuseEngine`). It multiplies node scores between 0 and 1. Scores outside 0 to 1 raise an error. If any node score is exactly 0, the result is 0. Optional per-node weights are applied as exponents. The result is rounded to six decimals. An empty input returns 0.
- `core/algorithms.py`: one function, `evaluate_hardware_root_trust`, which maps a signature flag and a key status to a node value (0, 0.5 or 1). It is a stub: it does not read any hardware token.
- `schemas/postgres_supabase.sql`: a draft database schema with two tables (`pipeline_nodes`, `compliance_transactions`).
- `tests/test_engine.py`: four unit tests for the engine.
- `docs/`: short design notes. They describe intended behaviour, including a high-risk threshold and an automatic "circuit breaker", that is not implemented in the code.

## The calculation

    Effective_Integrity = score_1^w_1 x score_2^w_2 x ... x score_n^w_n

Each score is between 0 and 1, and each weight w defaults to 1. With all weights at 1, scores of 1.0, 0.9, 0.85 and 1.0 give 0.765.

Properties and limits:

- Non-compensatory: a node at 0 makes the whole result 0, and low scores pull the product down quickly.
- The result is sensitive to how many nodes there are. More nodes give a lower product even when each is high.
- What each node score means, how it is measured, and what the weights should be are not defined or validated here.

## What it does not do yet

Data ingestion, forecasting or prediction, real cryptographic or hardware-token verification, automatic isolation of transactions, a user interface, and any evaluation against real cases. Any of these appearing in other materials describes plans, not this code.

## Run the tests

    python -m unittest discover -s tests

Requires Python 3.11 or later and no other packages.

## Security

Do not commit secrets, keys or personal data to this repository. To report a security concern, email audit@sumalinoginstitute.com.

## License

Apache License 2.0. See `LICENSE`.

## Contributing

See `CONTRIBUTING.md`. Contributions require a Signed-off-by line (Developer Certificate of Origin).

Copyright 2026 The Sumalinog Institute.
