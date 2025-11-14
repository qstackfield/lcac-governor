# LCAC Governor - Cognitive Integrity Framework  
**Atom Labs · 2025**

LCAC Governor is a cognitive integrity layer designed to sit in front of any LLM, agent, toolchain, or reasoning system.  
It does not replace your model. It governs it.

LCAC evaluates outputs for:

- Trust degradation  
- Drift variance  
- Cognitive instability  
- Reasoning anomalies  
- Multi-agent interference  
- Prompt-injection exploitation  
- Long-context decay  
- Hallucination risks  

It delivers:

- Real-time trust scoring (0–1)  
- Variance and drift detection  
- Metrics and telemetry dashboard  
- Keyed license and usage quota system  
- Stripe-backed tiering (Free → Starter → Pro → Enterprise)  
- Evaluation engine + SDK  
- Unified `/overview` cognitive snapshot  
- A complete SaaS-ready console UI  

---

# Production API

**Base URL:**  
`https://api.atomlabs.app`

**Primary endpoints:**

- `GET /info`  
- `GET /overview`  
- `GET /metrics`  
- `POST /evaluate`  
- `GET /license/verify?key=XYZ`  

---

# Why LCAC Exists

Modern LLMs fail silently.

They drift without warning, hallucinate unpredictably, collapse under long context, or behave differently depending on past interactions.  
Multi-agent setups amplify this instability.

LCAC gives operators **visibility before things break**, not after.

LCAC identifies:

- Hidden instability  
- Drift vectors  
- Trust loss patterns  
- Adversarial prompt behavior  
- Injection attempts  
- Tool misuse  
- Reasoning shortcuts  

Enterprises use LCAC as a cognitive safety guardrail.

---

# High-Level Architecture

```
mermaid
flowchart TD
  A[Client / LLM] --> B[LCAC Governor API]
  B --> C[Trust Engine]
  B --> D[Variance Analyzer]
  B --> E[Hash-Chained Ledger]
  C --> F[/overview Endpoint]
  D --> F
  E --> F
  F --> G[Console Dashboard]

```

---

# API Overview

| Method | Endpoint            | Description |
|--------|----------------------|-------------|
| POST   | `/evaluate`         | Cognitive trust evaluation |
| GET    | `/overview`         | Unified trust + variance + verdict snapshot |
| GET    | `/metrics`          | Trust trend metrics |
| GET    | `/info`             | System metadata and health |
| GET    | `/license/verify`   | License validation |

More detail is in:  
`docs/api-reference.md`

---

# Example: Evaluate Prompt/Output

**Request**

```json
{
  "prompt": "Explain quantum gravity to a child.",
  "output": "It is like magic glue in space."
}
```

**Response**

```json
{
  "license": "trial_129ab3ac",
  "trace_id": "d511ede8-39cd-4694-8f48-32a65d36a91f",
  "trust": 0.612,
  "variance": 0.004,
  "verdict": "unstable",
  "reason": "Trust score derived from base=0.61 variance=0.004",
  "recommendation": "Cognitive drift detected. Reduce context overlap.",
  "severity": {
    "level": 3,
    "label": "critical"
  },
  "insight": "LCAC observed reasoning state 'UNSTABLE' at 2025-11-13T04:54Z — cognitive drift detected."
}
```

---

# `/overview` Cognitive Snapshot

Example output:

```json
{
  "trust": 0.598,
  "variance": 0.002,
  "verdict": "unstable",
  "mode": "HOLD",
  "persona": "default",
  "insight": "Monitoring cognitive drift.",
  "ledger_count": 59
}
```

---

# LCAC Console (Dashboard)

Live at:

```
https://console.atomlabs.app/console
```

<p align="center">
  <img src="docs/img/lcac-console.png" width="880"/>
</p>

```

The dashboard includes:

- System heartbeat  
- Trust trend graph  
- Variance overlay  
- Reasoning insight stream  
- Governor mode  
- License + quota indicators  
- Test suite (hallucination / logic / injection / bias)  
- Stripe billing integration  

---

# Licensing & Billing

LCAC includes a built-in licensing and quota system with Stripe checkout and webhook integration.

## Default Tiers

| Tier | Price | Tokens | Billing |
|------|--------|---------|----------|
| Starter | $19 | 5,000 | One-time |
| Pro | $79 | 25,000/month | Subscription |
| Enterprise | $999 | Custom | Subscription |

Example license object:

```json
{
  "email": "user@example.com",
  "tier": "pro",
  "quota": 25000,
  "used": 141,
  "status": "active",
  "stripe_customer": "cus_ABC123"
}
```

---

# Python SDK

Install from PyPI (example once published):

```
pip install lcac-sdk
```

Or from source:

```
pip install -e ./sdk/python
```

### Usage Example

```python
from lcac import LCAC

g = LCAC(license_key="trial_abc123")

result = g.evaluate(
    prompt="Summarize the plot of Dune.",
    output="A boy becomes a space wizard."
)

print(result["verdict"], result["trust"])
```

SDK Methods:

- evaluate()  
- overview()  
- metrics()  
- info()  
- license_status()  

---

# Repository Structure

```
lcac-governor/
│
├── api/
│   ├── lcac_api.py
│   ├── lcac_console.html
│   ├── lcac_console_alias.py
│   ├── lcac_stripe_checkout.py
│   ├── lcac_stripe_hooks.py
│   └── lcac_landing.py
│
├── sdk/
│   └── python/
│       └── lcac/
│           ├── __init__.py
│           ├── client.py
│           └── models.py
│
├── docs/
│   ├── api-reference.md
│   ├── architecture.md
│   ├── governance-model.md
│   └── img/
│       ├── console.png
│       ├── header.png
│       └── sdk.png
│
├── examples/
│   ├── sdk_basic.py
│   ├── eval_batch.py
│   └── risk_analysis.py
│
└── README.md
```

---

# Security Model

### Cognitive Integrity Layer
- Trust scoring  
- Variance analysis  
- Verdict classification  
- Drift detection  
- Persona tracking  

### Execution Governance Layer
- Mode switching (HOLD → ELEVATE → LOCKDOWN)  
- Hash-chained ledger  
- Insight generator  

### Access Control Layer
- License keys  
- Quota enforcement  
- Stripe customer linkage  
- Redis-based usage tracking  

---

# Roadmap

- API v1  
- Console UI  
- Stripe billing  
- Python SDK  
- Landing page  
- JS SDK  
- Go SDK  
- Enterprise LLM adapters  
- Admin dashboard  
- CI test suite  

---

# License

Apache-2.0 (see LICENSE)

---

# Support

For enterprise licensing or partnership inquiries:

```
lcac@atomlabs.app
```
