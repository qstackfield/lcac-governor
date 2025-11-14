# Architecture

LCAC Governor is built from four layers:

1. API Layer
   FastAPI service at https://api.atomlabs.app
   Handles evaluation, trust scoring, drift, metrics, license logic, quota usage,
   Stripe checkout, and Stripe webhooks.

2. Memory & Ledger Layer
   Redis storage
   Keys:
   lcac:trust:score
   lcac:trust:variance
   lcac:ledger:last_hash
   lcac:trace:index
   lcac:license:*

3. Console Layer
   The HTML+JS UI at https://console.atomlabs.app/console
   Pulls from /overview, /metrics, /license/verify, and /stripe/checkout

4. Stripe Layer
   Live mode subscription and one-time token packs.
   Webhook issues license keys and updates quotas.

Data Flow:
Your app → POST /evaluate → LCAC trust engine → Redis ledger → Console/SDK
