LCAC Governor — System Architecture Overview
Atom Labs · 2025


1. Purpose

LCAC Governor is a cognitive-integrity layer designed to sit in front of any LLM, agent, or reasoning system, providing:
	•	Trust scoring
	•	Drift / variance detection
	•	Ledger-based traceability
	•	Persona-consistent reasoning analysis
	•	Live monitoring
	•	Governance modes (HOLD / ELEVATE / LOCKDOWN)

LCAC does not replace a model.
It governs how it behaves.


2. High-Level Architecture (Text Diagram)

[Client / Application / Agent]
            │
            ▼
     ┌────────────────┐
     │ LCAC API Layer │  /info /overview /evaluate /metrics
     └────────────────┘
            │
            ▼
     ┌────────────────┐
     │ Trust Engine   │  trust score (0–1)
     └────────────────┘
            │
            ▼
     ┌─────────────────────────┐
     │ Variance & Drift Logic │ variance / drift signal
     └─────────────────────────┘
            │
            ▼
     ┌────────────────────────┐
     │ Hash-Chained Ledger   │ immutable evaluation store
     └────────────────────────┘
            │
            ▼
     ┌────────────────────────┐
     │ Unified Overview API   │ /overview snapshot
     └────────────────────────┘
            │
            ▼
     ┌────────────────────────┐
     │ Console Dashboard UI   │ SaaS front-end
     └────────────────────────┘



3. Component Breakdown

3.1 API Layer (lcac_api.py)

Central entrypoint providing:
	•	/evaluate
	•	/overview
	•	/metrics
	•	/info
	•	/license/verify
	•	/stripe/*

Features:
	•	JSON requests only
	•	Optional license headers
	•	Zero-model dependency
	•	Stateless evaluation
	•	Consistent response schema


3.2 Trust Engine

The trust engine computes:
	•	Base trust (lcac:trust:score)
	•	Adjusted trust (base − variance/2)
	•	Verdict thresholds:
	•	stable ≥ 0.85
	•	watch ≥ 0.65
	•	unstable < 0.65

Inputs:
	•	Prompt
	•	Output
	•	Historical trust values
	•	Variance signals

Outputs:
	•	trust
	•	variance
	•	verdict
	•	severity
	•	insight
	•	recommendation


3.3 Variance & Drift Analyzer

Evaluates:
	•	Short-term deviation
	•	Long-term trend instability
	•	Variance delta
	•	Drift vectors (directional trust change)

All drift logic is model-agnostic.


3.4 Ledger & Trace Chain

Each evaluation generates:
	•	trace_id
	•	Serialized JSON of evaluation
	•	hash_self = SHA256(previous_hash + new_payload)

Ledger keys:

lcac:ledger:last_hash
lcac:trace:<trace_id>
lcac:trace:index   (list)

Provides:
	•	Tamper resistance
	•	Sequential continuity
	•	Deterministic auditing


3.5 Unified /overview Endpoint

Aggregates:
	•	Trust
	•	Variance
	•	Verdict
	•	Recommendation
	•	Insight
	•	Persona
	•	Governance mode
	•	Ledger depth
	•	Summary string

Used by:
	•	Console dashboard
	•	SDK convenience methods
	•	Health monitoring


4. License & Billing Layer

License object is stored as:

lcac:license:<email>

Fields:

tier
quota
used
status
created
expires (for trial)
stripe_customer

Evaluation increments:

used += 1

Quota exhaustion triggers HTTP 402.

Stripe webhook updates:
	•	License creation
	•	Quota grants
	•	Subscription cancellation
	•	Payment failures


5. Console Architecture

The dashboard is pure static HTML + JS:

Files:
	•	lcac_console.html
	•	lcac_console_fix.py
	•	lcac_console_alias.py

Features:
	•	Heartbeat status
	•	Trust trend graph
	•	Verdict highlighting
	•	Live metrics polling
	•	License usage display
	•	Stripe tier buttons
	•	Local trial auto-assignment

All data is fetched from:
	•	/info
	•	/metrics
	•	/overview
	•	/evaluate

No backend rendering is required.


6. Dependencies & Runtime

Server-side:
	•	Python 3.10+
	•	FastAPI
	•	Redis
	•	Stripe Python SDK
	•	uvicorn

Client-side (Console):
	•	Pure JS
	•	Chart.js for graphs

Storage:
	•	Redis DB 15 (configurable)


7. Governance Modes
	•	HOLD
Normal evaluation.
	•	ELEVATE
More strict variance analysis.
	•	LOCKDOWN
Extreme drift or injection detected
(future extended behaviors apply here).

Modes are written to:

lcac:governance:mode



8. Security Considerations
	•	All API traffic forced through TLS (Cloudflare Tunnel)
	•	CORS locked to:
	•	console.atomlabs.app
	•	api.atomlabs.app
	•	stripe.atomlabs.app
	•	Redis stored behind private network
	•	License keys protected by:
	•	No plaintext exposure
	•	Hash chaining
	•	Status flags
	•	Expiry logic


9. Scaling Paths

Future extensions:
	•	Multi-LLM adapters
	•	Agent-tree supervision
	•	Fine-grained drift classifiers
	•	Cross-agent coherence governance
	•	Enterprise audit dashboards
	•	Multi-tenant license separation
	•	SDKs for JS/Go/Rust


10. Summary

LCAC Governor is a modular, production-grade system designed for:
	•	LLM stability monitoring
	•	Drift and reasoning integrity tracking
	•	SaaS billing integration
	•	Multi-agent safety enhancement
	•	Enterprise governance visibility

It is purpose-built to sit between:

Your model  →  LCAC Governor  →  Your application

Providing continuous trust oversight.

