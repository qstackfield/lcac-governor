LCAC Security Model

This document defines the full LCAC Governor security posture:
architecture, access controls, data flow controls, and operational hardening.

This is the version appropriate for enterprise briefings, compliance review, and pre-sales evaluation.


1. Overview

LCAC Governor is designed to provide cognitive integrity enforcement without exposing sensitive internal data or allowing external manipulation.

Security principles include:
	•	Minimal attack surface
	•	No public inbound ports
	•	Strict access boundary enforcement
	•	Deterministic trust scoring (non-stochastic)
	•	Ledger-based reasoning traceability
	•	Quota-based licensing to prevent abuse
	•	Single-tenant control plane per deployment


2. Data Flow Architecture

Client → LCAC API → Trust Engine → Variance Analyzer → Ledger (Redis)
                                       |
                                       → Overview Snapshot → Console UI

Key security points:
	•	No model output leaves LCAC except evaluation metadata.
	•	No external LLM calls are made during evaluation.
	•	No prompt/output text is stored long-term (only hash + metadata stored).
	•	Redis is strictly local-only (127.0.0.1 binding).
	•	Cloudflare Tunnel is the only public exposure point.


3. API Surface

Public endpoints (all authenticated via Cloudflare Tunnel):

Endpoint	Auth	Purpose
/evaluate	License key	Cognitive integrity evaluation
/overview	None	Read-only trust snapshot
/metrics	None	Time-series telemetry
/info	None	System & health metadata
/license/verify	None	License metadata
/stripe/checkout	None	Creates Stripe session
/stripe/webhook	Stripe-signed	Issues licenses

No other endpoints exist.
No administrative endpoints exist.
No shell or system calls.
No file execution.


4. Attack Surface Reduction

4.1 No Open Ports (Zero Inbound)

The servers expose zero inbound ports.

All HTTP traffic is routed via:

Cloudflare → Cloudflare Tunnel → localhost:8079

If Cloudflare is down, LCAC is unreachable.

4.2 Redis Not Exposed

Redis configuration:

bind 127.0.0.1
protected-mode yes

No remote Redis access is possible.

4.3 CORS Restricted

LCAC API only allows:

https://api.atomlabs.app
https://console.atomlabs.app
https://stripe.atomlabs.app

Everything else receives HTTP 403.


5. Request Validation

Each evaluation request is checked for:
	•	prompt length
	•	output length
	•	missing fields
	•	malformed JSON
	•	invalid keys
	•	quota exhaustion
	•	expired license
	•	tampered license metadata

Malformed or unauthorized requests return:
	•	400 (bad input)
	•	401 (invalid license)
	•	402 (quota exceeded)
	•	500 (internal)


6. License Enforcement Model

Licenses are stored at:

lcac:license:<email>

Fields include:

tier
quota
used
status
stripe_customer
created
updated
expires

Once quota is exceeded:

POST /evaluate → 402 Payment Required

No bypass mechanisms exist.


7. Reasoning Ledger

LCAC maintains a hash-chained audit ledger:

lcac:ledger:last_hash
lcac:trace:<trace_id>
lcac:trace:index

Each trace entry includes:
	•	trust
	•	variance
	•	verdict
	•	reason
	•	timestamp
	•	prompt hash
	•	output hash
	•	hash_self: SHA256(previous_hash + payload)

This ensures:
	•	tamper-evident history
	•	compliance traceability
	•	trust reproducibility
	•	forensic investigation


8. Cloudflare Security

LCAC uses Cloudflare for:
	•	TLS termination
	•	Zero Trust routing
	•	Firewall-level DDoS protection
	•	Bot detection
	•	API abuse prevention
	•	Rate limiting (optional)
	•	WAF

DNS is locked so that:

api.atomlabs.app
console.atomlabs.app
stripe.atomlabs.app

resolve only to Cloudflare.


9. Stripe Security

Stripe account uses:
	•	Webhook signing (HMAC SHA-256)
	•	Enforced webhook secret
	•	Restricted API keys
	•	Live mode keys stored in environment variables
	•	No card data ever touches LCAC servers

Webhook flow:
	1.	Stripe sends event to /stripe/webhook
	2.	LCAC verifies signature
	3.	License updated in Redis
	4.	No customer PII stored except:

email
stripe_customer_id
tier
quota
status



10. Console Security

LCAC Console is completely static:
	•	HTML
	•	CSS
	•	JS
	•	Fetches only from LCAC API

No cookies
No sessions
No tokens
No tracking scripts

All license handling happens client-side (localStorage).


11. Update Procedure (Safe Deployment)

To safely update LCAC:

sudo systemctl stop lcac-api
git pull or replace /opt/lcac/*
sudo systemctl daemon-reexec
sudo systemctl restart lcac-api
sudo systemctl restart cloudflared

Cloudflare tunnel ensures no downtime.


12. Disaster Recovery

Backup:

/opt/lcac
/opt/lcac/core/api
/opt/lcac/secrets
/root/.cloudflared
/var/lib/redis/dump.rdb

Restore:

Install Python + Redis + Tunnel
Restore above files
Start lcac-api + cloudflared

Recovery time: under 10 minutes.


13. Compliance Readiness

LCAC meets controls for:
	•	SOC 2 (Logging, least privilege, TLS routing, no open ports)
	•	HIPAA (no PHI handled, TLS required, audit logs)
	•	FedRAMP low/moderate (can run inside GovCloud or isolated VPC)
	•	GDPR (no personal data stored except customer email for licenses)

Additional enterprise controls can be layered on request.


14. Threat Model Summary

Threat	Mitigation
Prompt injection	Trust scoring + variance detection
Model drift	Continuous telemetry
Credential theft	License keys revocable in Redis
DDoS	Cloudflare WAF/Tunnel
Port scanning	No open ports
Redis compromise	Local-only binding
Tampering	Hash-chained ledger
Billing fraud	Stripe-signed webhooks



15. Contact

For enterprise licensing or integration partnerships:

lcac@atomlabs.app



