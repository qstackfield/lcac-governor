## LCAC Governor - Cognitive Integrity Framework ##

LCAC Governor is a cognitive integrity layer designed to sit in front of any LLM, agent pipeline, or autonomous reasoning system.
It does not replace your models - it governs them.

LCAC continuously evaluates outputs for
	•	Trust degradation
	•	Drift variance
	•	Cognitive instability
	•	Reasoning anomalies
	•	Multi-agent interference
	•	Prompt-injection behavior
	•	Long-context decay
	•	Hallucination risk

It delivers:
	•	Real-time trust scoring (0.0 → 1.0)
	•	Variance and drift detection
	•	Metrics and telemetry dashboard
	•	License and quota management
	•	Stripe-backed billing (Free → Starter → Pro → Enterprise)
	•	Evaluation engine + Python SDK
	•	Unified /overview cognitive snapshot
	•	Full SaaS-ready console UI

⸻

Deployment Endpoints

Production API base

https://api.atomlabs.app

Key endpoints
	•	GET /info - system health, uptime, prices
	•	GET /overview - trust, variance, verdict, insight
	•	GET /metrics - telemetry stream (trust / variance / stability)
	•	POST /evaluate - core trust evaluation
	•	GET /license/verify?key=XYZ - license introspection

Console dashboard

https://console.atomlabs.app/console

⸻

Why LCAC Exists

Modern LLM systems fail silently:
	•	They drift under long context.
	•	They collapse under adversarial prompts.
	•	They hallucinate when grounding drops.
	•	They become unstable under multi-agent orchestration.

LCAC addresses this by:
	•	Scoring trust continuously.
	•	Detecting variance and drift.
	•	Surfacing a clear verdict (“stable / watch / unstable”).
	•	Providing insight and recommendations before failure cascades.

LCAC is a governor - a control layer that wraps your models with cognitive telemetry and guardrails.

⸻

High-Level Architecture

Conceptual flow:
	•	Client / LLM → LCAC API
	•	LCAC API → Trust Engine / Drift Analyzer / Ledger
	•	Engine → /overview snapshot
	•	Snapshot → Console dashboard and SDK

Key components:
	1.	API Layer
FastAPI-based HTTP surface. Exposes /evaluate, /overview, /metrics, /info, /license/verify.
	2.	Trust & Drift Engine
Computes trust, variance, verdict, and severity; updates insight and recommendations.
	3.	Ledger Layer
Hash-chained records for each evaluation, stored in Redis. Every new entry is linked to the previous hash.
	4.	Licensing & Billing Layer
Trial issuance, quotas, usage tracking, and Stripe-backed token packs and subscriptions.
	5.	Console Layer
Web UI at console.atomlabs.app/console for operators, with live charts, insight, and upgrade controls.

⸻

API: Core Endpoints

POST /evaluate

Evaluate a prompt + output pair.

Request

{
  "prompt": "Explain cognitive drift.",
  "output": "Cognitive drift is when a model's reasoning shifts unpredictably..."
}

Response

{
  "license": "trial_0cc29bee9bc3d1d3",
  "trace_id": "7f60d991-f16b-487d-b151-c8051db07186",
  "trust": 0.6085,
  "variance": 0.001,
  "verdict": "unstable",
  "ts": "2025-11-14T22:47:07.658192",
  "prompt": "Explain cognitive drift.",
  "output": "Cognitive drift is when a model's reasoning shifts unpredictably...",
  "reason": "Trust score derived from base=0.609, variance=0.001, verdict=unstable.",
  "hash_self": "2acbda91f2d83df46b614825fce4d27fdcfc1be3de7042416d6501d8b5e5b88b",
  "severity": { "level": 3, "label": "critical" },
  "recommendation": "Cognitive drift detected. Reduce context overlap and consider prompt rebalancing or retraining.",
  "explanation": "Verdict 'unstable' based on trust=0.609 and variance.",
  "insight": "LCAC observed reasoning state 'UNSTABLE' at 2025-11-14T22:47:07.659432 - Cognitive drift detected. Reduce context overlap and consider prompt rebalancing or retraining."
}


⸻

GET /overview

Unified cognitive snapshot for the console and SDK.

Example:

{
  "ts": "2025-11-14T22:47:07.639798",
  "persona": "default",
  "mode": "HOLD",
  "trust": 0.598,
  "variance": 0.002,
  "verdict": "unstable",
  "recommendation": "Monitoring cognitive drift.",
  "insight": "Monitoring cognitive drift.",
  "ledger_count": 59,
  "summary": "UNSTABLE • trust=0.608 var=0.0 (Trust score derived from base=0.608, variance=0.0, verdict=unstable.)"
}


⸻

GET /metrics

Returns time-series metrics for the trust trend chart:

{
  "ts": "2025-11-14T22:47:07.639798",
  "trust_score": 0.609,
  "variance": 0.001,
  "stability": 0.999,
  "ledger_count": 20,
  "summary": "UNSTABLE • trust=0.608 var=0.0 (Trust score derived from base=0.608, variance=0.0, verdict=unstable.)"
}


⸻

GET /info

System status and telemetry:
	•	product name
	•	version
	•	uptime
	•	CPU and memory
	•	last license issued
	•	configured Stripe price IDs

Example:

{
  "product": "LCAC Cognitive Integrity Framework",
  "version": "1.0.0-Insight",
  "platform": "Linux",
  "mode": "HOLD",
  "trust_score": "0.607",
  "last_license": "N/A",
  "uptime_sec": 103823.7,
  "cpu": 20.8,
  "memory": 22.4,
  "prices": {
    "starter": "price_1SSQpjHk2p1wdo6EYwYvpUgo",
    "pro": "price_1SSQqdHk2p1wdo6EAupeMC6W",
    "enterprise": "price_1SSQrQHk2p1wdo6ERHrh9olc"
  }
}


⸻

GET /license/verify

License and quota lookup:

{
  "ok": true,
  "license": {
    "email": "user@example.com",
    "tier": "pro",
    "quota": "25000",
    "used": "141",
    "status": "active",
    "stripe_customer": "cus_ABC123"
  }
}


⸻

LCAC Console

The console is available at:

https://console.atomlabs.app/console

It shows:
	•	Trust trend line chart
	•	Variance and stability data
	•	Verdict and mode (HOLD / ELEVATE / LOCKDOWN)
	•	Insight and recommendation summary
	•	License tier and quota usage
	•	Quick evaluate form
	•	Stripe-backed upgrade buttons

![LCAC Console](img/console.png)

Update the path to whatever you actually use in docs/img.

⸻

Licensing and Billing

LCAC ships with a Stripe-backed licensing model.

Default tiers:

Tier	Price	Tokens	Mode
Starter	$19	5,000 evals	one-time
Pro	$79	25,000 evals/mo	subscription
Enterprise	$999	custom	subscription

The Stripe checkout flow:
	1.	Console calls /stripe/checkout with { "tier": "...", "email": "..." }.
	2.	Stripe Checkout handles payment.
	3.	Stripe webhook /stripe/webhook receives checkout.session.completed.
	4.	LCAC creates or updates a license at a deterministic key: lcac:license:<email-transformed>.
	5.	Quota and usage are enforced via Redis.

Example internal license object:

{
  "email": "user@example.com",
  "tier": "starter",
  "quota": 5000,
  "used": 0,
  "status": "active",
  "stripe_customer": "cus_ABC123",
  "updated": "2025-11-14T22:40:00Z"
}


⸻

Python SDK

The LCAC SDK is published as lcac-sdk on PyPI.

Install:

pip install lcac-sdk

Basic usage:

from lcac import LCAC

gov = LCAC(license_key="trial_abc123")

print("=== INFO ===")
print(gov.info())

print("=== METRICS ===")
print(gov.metrics())

print("=== EVALUATE ===")
result = gov.evaluate(
    prompt="Explain cognitive drift.",
    output="Cognitive drift is when a model's reasoning shifts unpredictably..."
)
print(result["verdict"], result["trust"])

SDK methods:
	•	LCAC.evaluate(prompt, output)
	•	LCAC.info()
	•	LCAC.metrics()
	•	LCAC.overview()
	•	LCAC.license_status(key=None)

The SDK automatically:
	•	Sends the license key as X-License-Key header when provided
	•	Targets https://api.atomlabs.app by default

⸻

Repository Structure (Reference)

A typical LCAC Governor repository structure:

lcac-governor/
  api/
    lcac_api.py
    lcac_console.html
    lcac_console_alias.py
    lcac_stripe_checkout.py
    lcac_stripe_hooks.py
    lcac_landing.py
  sdk/
    python/
      lcac/
        __init__.py
        client.py
  docs/
    index.md
    api-reference.md
    architecture.md
    img/
  examples/
    sdk_basic.py
    eval_batch.py
    risk_analysis.py
  README.md


⸻

Security Model (Summary)

LCAC security and governance is divided into three conceptual layers:
	1.	Cognitive Integrity Layer
	•	trust scoring
	•	variance measurement
	•	verdict classification
	•	insight and recommendations
	2.	Execution Governance Layer
	•	HOLD / ELEVATE / LOCKDOWN modes
	•	hash-chained ledger of reasoning events
	•	overview aggregation
	3.	Access Control & Billing Layer
	•	license key validation
	•	quota checks and enforcement
	•	Stripe-backed customer linkage
	•	Redis-backed usage state

⸻

Roadmap

Current:
	•	Live API and console
	•	Stripe-backed billing and licensing
	•	Python SDK (lcac-sdk)
	•	Landing page and documentation

Planned:
	•	JavaScript SDK
	•	Go SDK
	•	Multi-LLM adapter layer
	•	Admin/operator console
	•	CI-based integrity test suite

⸻

Support and Contact

For enterprise, partnership, or integration discussions:

lcac@atomlabs.app

For SDK issues and feature requests, use the GitHub issues page of the lcac-governor repository.
