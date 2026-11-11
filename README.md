# Commercial Claims & Policy Compliance Agent

> An enterprise-grade, agentic RAG and compliance validation platform designed
> for commercial card services. It aims to automate
> commercial expense audits by orchestrating stateful agent loops, enforcing
> metadata pre-filtering, and executing hybrid semantic and lexical search across
> enterprise policy libraries.

## Project persona and objective

**Target role:** Senior Forward Deployed Engineer (FDE) / Senior AI Platform Engineer  
**Business domain:** FinTech / Commercial Card Services & Expense Governance

Commercial cardholders submit complex expense claims. Traditional rule engines
can struggle with unstructured receipts and policy nuances, while unconstrained
LLMs can produce unsupported conclusions. The intended solution is an agent
platform connecting event-driven ingestion, enterprise microservices, and
retrieval-augmented policy workflows to support auditable claim reviews.

## System architecture

The planned platform follows a four-layer architectural pattern. Detailed layer
definitions and workflows have not yet been provided.

## Planned technical capabilities

The following are design goals, not features currently active in this scaffold:

1. **Hybrid retrieval (dense + BM25):** Combine semantic vector search with
   lexical BM25 search, then merge rankings with Reciprocal Rank Fusion (RRF).
   Semantic retrieval can match related concepts (for example, "lodging" and
   "hotel"), while lexical retrieval can find exact section codes and amounts.
2. **Metadata pre-filtering:** Apply the company or tenant scope and policy
   validity constraints in the data store before scoring results. Filters must
   be mandatory and validated at the retrieval boundary; a prompt-level
   instruction is not an isolation control.
3. **Structured audit decisions:** Validate model output against a Pydantic
   decision schema before returning it to downstream services. Structured
   output validation improves shape and type safety; it does not by itself
   guarantee that a decision is supported by policy evidence.
4. **Stateful agent workflow:** Use a LangGraph workflow to separate retrieval,
   evaluation, and review routing. Keep side effects and any database mutations
   behind explicitly authorized, validated service operations.

## Repository layout

```text
app/
├── config.py                  # Environment settings
├── models/
│   └── schemas.py             # API request and response schemas
├── retrieval/
│   └── hybrid_store.py        # Retrieval interface; Qdrant + BM25 not connected
├── agents/
│   ├── state.py               # Typed workflow state
│   └── graph.py               # Fail-closed placeholder; LangGraph not connected
└── main.py                    # FastAPI endpoints
tests/
├── test_api.py                # Endpoint behavior and request validation
├── test_retrieval.py          # Ensures company tier is mandatory in retrieval
└── test_agent.py              # Ensures unimplemented workflow fails closed
```

### How the pieces fit together

`main.py` is the HTTP entry point. It validates input with `models/schemas.py`.
When implemented, it will pass claim data into `agents/graph.py`; the graph will
request policy evidence through `retrieval/hybrid_store.py` and return a
validated audit decision. `agents/state.py` defines the data carried between
workflow steps.

Today, `hybrid_store.py` only defines the tier-scoped retrieval contract, and
`graph.py` intentionally raises an error instead of returning a fabricated
decision. The service does not connect to Qdrant, BM25, LangGraph, Kafka, or an
LLM. Tenant isolation, policy freshness, evidence-grounded decisions, and
cross-service authorization must be implemented and tested before production use.

## Current implementation status

This repository currently provides a FastAPI service scaffold. It validates audit
requests and exposes health and readiness endpoints, but it does not yet evaluate
claims. The audit and readiness endpoints return HTTP 503 until a real policy
retrieval and evaluation workflow is connected. This avoids returning a fabricated
approval or rejection.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for the generated API documentation.

To run tests, install the development dependencies with
`pip install -r requirements-dev.txt`, then run `python -m pytest`.

## Run with Docker

```powershell
docker compose up --build
```

- `GET /healthz` is a liveness check.
- `GET /readyz` reports whether the audit workflow is configured (currently 503).
- `POST /v1/audit/claim` validates the request and currently returns 503 rather
  than a mock audit result.

## Costs and credentials

This scaffold does not call OpenAI or another paid model API and does not require
an API key, so running it does not create model API usage charges. Container
runtime, hosting, or other infrastructure can still incur charges depending on
where it is run. A ChatGPT subscription and API usage are separate products;
check the provider's current billing page for account-specific pricing and usage.

## Before enabling audits

Connect the retrieval and policy-evaluation workflow, configure its credentials
through environment variables or a secrets manager, and add tests using approved
policy fixtures. Do not treat this scaffold's health response as evidence that
the audit capability is ready.
