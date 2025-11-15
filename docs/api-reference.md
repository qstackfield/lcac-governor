LCAC API Reference

Atom Labs · 2025

This page describes the LCAC API and all public endpoints.

Base URL:

https://api.atomlabs.app

All endpoints return JSON and require HTTPS.


Authentication

If you do not send a license key, LCAC issues a trial key on your first /evaluate call.

To use a license key:

X-License-Key: YOUR_KEY_HERE



Endpoints

1. POST /evaluate

Run a full LCAC evaluation on a prompt/output pair.

Request example:

{
  "prompt": "Explain quantum gravity to a child.",
  "output": "It is like magic glue in space."
}

Response example:

{
  "license": "trial_129ab3ac",
  "trace_id": "d511ede8-39cd-4694-8f48-32a65d36a91f",
  "trust": 0.612,
  "variance": 0.004,
  "verdict": "unstable",
  "recommendation": "Cognitive drift detected.",
  "severity": { "level": 3, "label": "critical" },
  "insight": "LCAC observed reasoning state 'UNSTABLE'."
}



2. GET /overview

Returns the current LCAC stability state.

Example:

{
  "trust": 0.598,
  "variance": 0.002,
  "verdict": "unstable",
  "mode": "HOLD",
  "persona": "default",
  "insight": "Monitoring cognitive drift.",
  "ledger_count": 59
}



3. GET /metrics

Returns incremental metrics for dashboards.

Example:

{
  "ts": "2025-11-14T05:01:12Z",
  "trust_score": 0.607,
  "variance": 0.001,
  "stability": 0.999,
  "ledger_count": 22,
  "summary": "UNSTABLE - trust=0.607 var=0.001"
}



4. GET /info

Returns system/runtime metadata.

Example:

{
  "product": "LCAC Cognitive Integrity Framework",
  "version": "1.0.0",
  "platform": "Linux",
  "mode": "HOLD",
  "trust_score": 0.607,
  "uptime_sec": 12402.4,
  "cpu": 12.4,
  "memory": 22.7,
  "prices": {
    "starter": "price_xxx",
    "pro": "price_yyy",
    "enterprise": "price_zzz"
  }
}



5. GET /license/verify

Validate a license key.

Example:

GET /license/verify?key=trial_abc123

Response:

{
  "ok": true,
  "license": {
    "tier": "trial",
    "quota": 1000,
    "used": 22,
    "status": "active"
  }
}



6. POST /stripe/checkout

Create a Stripe Checkout session.

Starter = one-time payment
Pro = subscription
Enterprise = contact-only

Request:

{
  "tier": "starter",
  "email": "user@example.com"
}

Response:

{
  "url": "https://checkout.stripe.com/c/session/abc123"
}



7. POST /stripe/webhook

Stripe webhook endpoint used internally for:
	•	license creation
	•	quota management
	•	subscription updates

Not used directly by end-users.


Error Formats

Generic error:

{ "error": "message" }

Quota exceeded:

{ "detail": "Quota exceeded. Purchase tokens to continue." }

Invalid license:

{ "detail": "Invalid or expired license key" }



Rate Limits

Trial: 1000 evaluations per 7 days
Starter: 5000 evaluations
Pro: 25000 per month
Enterprise: negotiated


Recommended Headers

Content-Type: application/json
X-License-Key: YOUR_KEY
Accept: application/json



Summary

Use:
	•	/evaluate for scoring
	•	/overview and /metrics for dashboards
	•	/info for system health
	•	/license/verify for key validation
	•	/stripe/checkout for upgrades

This document is intentionally minimal and stable for long-term public use.
