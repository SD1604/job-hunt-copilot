# Architecture Notes

This doc tracks *why* decisions were made, not just what was built —
updated at the end of each subpart.

## Subpart 0 — Raw API call

**What**: a single call to Gemini's `interactions.create()`, no framework.

**Why this exists before any framework code**: LangChain/LangGraph
abstractions (chains, agents, graph nodes) are all wrappers around this
exact call. Understanding the raw shape — system instruction vs. input,
the response object's structure — makes every later abstraction
explainable instead of magic.

**Key files**:
- `backend/app/config.py` — env/config, single source of truth
- `backend/app/clients/gemini_client.py` — single client instance
- `backend/scripts/subpart0_basic_call.py` — the actual call
