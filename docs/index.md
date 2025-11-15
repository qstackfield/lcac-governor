# LCAC Governor – Cognitive Integrity Framework

LCAC Governor is a cognitive-integrity layer designed to sit in front of any LLM, agent pipeline, or autonomous reasoning system.  
It does not replace your models – it governs them.

LCAC continuously evaluates outputs for:

- Trust degradation  
- Drift variance  
- Cognitive instability  
- Reasoning anomalies  
- Multi-agent interference  
- Prompt-injection behavior  
- Long-context decay  
- Hallucination risk  

It delivers:

- Real-time trust scoring (0.0 → 1.0)  
- Variance and drift detection  
- Metrics and telemetry dashboard  
- License and quota management  
- Stripe-backed billing (Free → Starter → Pro → Enterprise)  
- Evaluation engine + Python SDK  
- Unified `/overview` cognitive snapshot  
- Full SaaS-ready console UI  

---

## Deployment Endpoints

Production API base:

- `https://api.atomlabs.app`

Key endpoints:

- `GET /info` – system health, uptime, prices  
- `GET /overview` – trust, variance, verdict, insight  
- `GET /metrics` – telemetry stream (trust / variance / stability)  
- `POST /evaluate` – core trust evaluation  
- `GET /license/verify?key=XYZ` – license introspection  

Console dashboard:

- `https://console.atomlabs.app/console`

---

## Why LCAC Exists

Modern LLM systems fail silently:

- They drift under long context.  
- They collapse under adversarial prompts.  
- They hallucinate when grounding drops.  
- They become unstable under multi-agent orchestration.  

LCAC addresses this by:

- Scoring trust continuously.  
- Detecting variance and drift.  
- Surfacing a clear verdict (“stable / watch / unstable”).  
- Providing insight and recommendations before failure cascades.  

LCAC is a governor – a control layer that wraps your models with cognitive telemetry and guardrails.

---

## High-Level Architecture

Conceptual flow:

- Client / LLM → LCAC API  
- LCAC API → Trust Engine / Drift Analyzer / Ledger  
- Engine → `/overview` snapshot  
- Snapshot → Console dashboard and SDK

Key components:

1. **API Layer**  
   FastAPI-based HTTP surface. Exposes `/evaluate`, `/overview`, `/metrics`, `/info`, `/license/verify`.

2. **Trust & Drift Engine**  
   Computes trust, variance, verdict, and severity; updates insight and recommendations.

3. **Ledger Layer**  
   Hash-chained records for each evaluation, stored in Redis. Every new entry is linked to the previous hash.

4. **Licensing & Billing Layer**  
   Trial issuance, quotas, usage tracking, and Stripe-backed token packs and subscriptions.

5. **Console Layer**  
   Web UI at `console.atomlabs.app/console` for operators, with live charts, insight, and upgrade controls.

---

## API: Core Endpoints

### `POST /evaluate`

Evaluate a prompt + output pair.

**Request**

```json
{
  "prompt": "Explain cognitive drift.",
  "output": "Cognitive drift is when a model's reasoning shifts unpredictably..."
}
