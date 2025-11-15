LCAC Deployment & Hosting Guide

This document explains how to deploy LCAC Governor in production:
API, console, billing, Redis, and Cloudflare Tunnel.

The instructions match your current production architecture exactly.


1. Deployment Architecture

LCAC runs as three core components:

/opt/lcac
  ├── lcac_api.py          (FastAPI governor)
  ├── lcac_console.html    (SaaS dashboard)
  ├── lcac_landing.html    (public homepage)
  ├── lcac_stripe_checkout.py
  ├── lcac_stripe_hooks.py
Redis (DB 15)
Cloudflare Tunnel  → api.atomlabs.app / console.atomlabs.app

Your current API host:

https://api.atomlabs.app

Your console:

https://console.atomlabs.app/console

Your landing page:

https://console.atomlabs.app/

Everything runs through one FastAPI app + one Redis + one Tunnel.


2. System Requirements

Server
	•	2 vCPU
	•	4 GB RAM
	•	Ubuntu 22.04+
	•	Python 3.10+
	•	Redis 6+
	•	Cloudflare Tunnel

Your production environment exceeds these requirements.

Network
	•	Only Cloudflare Tunnel exposes the API
	•	Redis remains localhost-only
	•	No inbound ports required


3. Environment Variables

The LCAC API uses the following environment variables:

REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_PASS=""
REDIS_DB=15

STRIPE_SECRET_KEY=sk_live_xxx
STRIPE_PUBLIC_KEY=pk_live_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx

LCAC_API_HOST=0.0.0.0
LCAC_API_PORT=8079

Your system already uses these correctly.


4. Redis Configuration

You are currently using Redis for:
	•	license storage
	•	quota tracking
	•	trust score
	•	insight fields
	•	ledger entries
	•	hash-chain entries

Default configuration is correct:

bind 127.0.0.1
protected-mode yes
maxmemory-policy allkeys-lru



5. Systemd Service

File: /etc/systemd/system/lcac-api.service

Example:

[Unit]
Description=LCAC Governor API
After=network.target

[Service]
User=root
WorkingDirectory=/opt/lcac/core/api
ExecStart=/usr/bin/python3 /opt/lcac/core/api/lcac_api.py
Restart=always
EnvironmentFile=/opt/lcac/secrets/stripe.env
EnvironmentFile=/opt/lcac/secrets/redis.env

[Install]
WantedBy=multi-user.target

Your system already includes:
	•	10-envdir.conf
	•	90-exec.conf
	•	91-path.conf
	•	96-cors.conf
	•	97-cors-fix.conf

All correct.

Restart commands:

sudo systemctl daemon-reexec
sudo systemctl restart lcac-api



6. Cloudflare Tunnel

Your Cloudflare config is correct.

/etc/cloudflared/config.yml:

tunnel: e00fc3eb-ce73-4e11-8b5e-178c0a34ebae
credentials-file: /root/.cloudflared/e00fc3eb-ce73-4e11-8b5e-178c0a34ebae.json

ingress:
  - hostname: api.atomlabs.app
    service: http://127.0.0.1:8079
  - hostname: console.atomlabs.app
    service: http://127.0.0.1:8079
  - hostname: stripe.atomlabs.app
    service: http://127.0.0.1:8079
  - service: http_status:404

originRequest:
  cache-level: bypass
  no-chunked-encoding: true

Restart:

sudo systemctl restart cloudflared



7. Stripe Billing Deployment

LCAC uses two files:

lcac_stripe_checkout.py
lcac_stripe_hooks.py

Checkout handler (client → Stripe)

Creates sessions for:
	•	Starter (one-time)
	•	Pro (monthly subscription)
	•	Enterprise (yearly subscription)

Webhook (Stripe → LCAC)

Writes to Redis:

lcac:license:<email>

Fields include:

tier
quota
used
status
stripe_customer
expires
created
updated

Your webhook endpoint:

https://api.atomlabs.app/stripe/webhook

Webhook secret is already set in your environment file.


8. SSL & Security

All API traffic → Cloudflare Tunnel
All Redis traffic → localhost only
All license keys processed server-side
CORS restricted to:

"https://api.atomlabs.app"
"https://console.atomlabs.app"
"https://stripe.atomlabs.app"

You are fully compliant with:
	•	No direct public ports
	•	No direct Redis exposure
	•	TLS termination via Cloudflare
	•	Correct CORS
	•	Single origin policy


9. Backup & Restore Strategy

You should back up:

/opt/lcac
/opt/lcac/core/api
/opt/lcac/secrets
/opt/lcac/core/etc/lcac_billing.yml
/opt/lcac/core/api/lcac_console.html
/root/.cloudflared

And optionally Redis snapshot:

/var/lib/redis/dump.rdb



10. Scaling Strategy

To scale horizontally:
	1.	Clone the API node
	2.	Point all LCAC replicas at the same Redis
	3.	Run multiple Cloudflare connectors
	4.	Set health rules in Cloudflare Zero Trust

Because LCAC is:
	•	stateless API
	•	stateful Redis backend
	•	shared billing engine

Scaling is trivial.


11. High-Availability Deployment Pattern

Recommended pattern:

Node A: LCAC API + Redis
Node B: LCAC API (stateless clone)
Node C: LCAC API (stateless clone)

Cloudflare Tunnel: 3 connectors → same hostname

Redis remains on one node unless you want clustering (not needed yet).


12. Monitoring

Use:

GET /info
GET /overview
GET /metrics

Best fields for dashboards:
	•	trust_score
	•	variance
	•	stability
	•	ledger_count
	•	last_license
	•	uptime_sec
	•	cpu / memory

Grafana integration:

curl -s https://api.atomlabs.app/metrics | jq .



13. Logs

Systemd logs:

journalctl -u lcac-api -n 200 --no-pager

Tunnel logs:

cat /var/log/cloudflared.log

Stripe logs:
	•	visible via Stripe dashboard
	•	or log manually under /opt/lcac/logs (your system supports this)


14. Disaster Recovery

Restore process:

1. Recreate server
2. Install Redis + Python
3. Restore /opt/lcac
4. Restore /root/.cloudflared
5. Restore Redis snapshot (optional)
6. Start lcac-api and cloudflared

Recovery time: under 10 minutes.



15. Support

For enterprise licensing or strategic partnership:

lcac@atomlabs.app
