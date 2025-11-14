# LCAC API Reference

This document describes the production LCAC API running at:

https://api.atomlabs.app

LCAC is a cognitive governance engine that evaluates model outputs,
assigns trust scores, monitors drift, and enforces token quotas
using Stripe-backed licensing.

------------------------------------------------------------
# Root Endpoints
------------------------------------------------------------

GET /
Basic service heartbeat.

Response:
ok: true
service: "LCAC API"
message: "Landing endpoint active."

------------------------------------------------------------
# Evaluate
------------------------------------------------------------

POST /evaluate
Evaluates a prompt/output pair and returns trust, drift insight,
severity levels, and ledger hash chaining for auditability.

Headers:
X-License-Key: <optional license key>

Body:
prompt: string
output: string

Returns:
license: trial key or existing key
trust: float 0–1
variance: float
verdict: stable | watch | unstable
recommendation: human-readable guidance
explanation: reasoning behind verdict
severity: {level, label}
insight: summary string
hash_self: ledger hash (SHA-256)
trace_id: unique event ID

------------------------------------------------------------
# Metrics
------------------------------------------------------------

GET /metrics
Lightweight endpoint for console charting.

Returns:
ts: timestamp
trust_score: float
variance: float
stability: float or null
ledger_count: int
summary: string or null

------------------------------------------------------------
# Overview
------------------------------------------------------------

GET /overview
Main console data feed.

Returns:
ts
persona
mode
trust
variance
verdict
recommendation
insight
ledger_count
summary

------------------------------------------------------------
# Info
------------------------------------------------------------

GET /info
System-level metadata for console header.

Returns:
product
version
platform
mode
trust_score
last_license
uptime_sec
cpu
memory
prices: {starter, pro, enterprise}

------------------------------------------------------------
# License Verification
------------------------------------------------------------

GET /license/verify?key=<license_key>

Returns:
ok: true/false
license: {tier, quota, used, status, created, expires}

------------------------------------------------------------
# Stripe Checkout
------------------------------------------------------------

POST /stripe/checkout
Creates a live Stripe Checkout Session.

Body:
tier: starter | pro | enterprise
email: billing email

Returns:
url: Stripe session URL

------------------------------------------------------------
# Stripe Webhook
------------------------------------------------------------

POST /stripe/webhook
Receives validated Stripe events.

Events handled:
checkout.session.completed
invoice.payment_failed
customer.subscription.deleted

The webhook issues:
lcac:license:<email_normalized>
with quota, status, stripe_customer_id, timestamps.

------------------------------------------------------------
# Rate Limits
------------------------------------------------------------

Evaluation limited by license quotas.
All other endpoints unrestricted.

------------------------------------------------------------
# Error Handling
------------------------------------------------------------

401 - invalid or expired license
402 - quota exceeded
500 - evaluation engine internal error
