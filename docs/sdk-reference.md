LCAC Python SDK Reference
Atom Labs · 2025

⸻

1. Overview

The LCAC Python SDK provides a simple interface for interacting with:
	•	/evaluate
	•	/overview
	•	/metrics
	•	/info
	•	/license/verify

It wraps LCAC’s cognitive-governor API in a clean Python class.

Package name:

lcac-sdk

Class import:

from lcac import LCAC


⸻

2. Installation

Install from PyPI

pip install lcac-sdk

Developer mode (local)

pip install -e ./sdk/python


⸻

3. SDK Class

class LCAC:
    def __init__(self, base_url="https://api.atomlabs.app", license_key=None):
        ...

Arguments:

Parameter	Description
base_url	API root (default: LCAC production endpoint)
license_key	Optional license or trial key


⸻

4. Authentication

Authentication is automatic.

If you pass license_key, every request includes:

X-License-Key: <key>

If you don’t, LCAC automatically issues trial keys on first /evaluate.

⸻

5. Methods

5.1 evaluate(prompt, output)

Runs trust + drift + verdict analysis on a prompt/output pair.

result = governor.evaluate("Explain gravity", "It is magic pushing you down.")

Returns:

{
  "license": "trial_123...",
  "trust": 0.61,
  "variance": 0.003,
  "verdict": "unstable",
  "severity": {"level": 3, "label": "critical"},
  "insight": "Cognitive drift detected...",
  "reason": "Trust score derived from base=0.61, variance=0.003"
}


⸻

5.2 overview()

Unified cognitive state from the LCAC governor.

state = governor.overview()

Returns trust, variance, verdict, mode, persona, summary, ledger count.

⸻

5.3 metrics()

Telemetry snapshot of trust score and drift over time.

metrics = governor.metrics()

Example:

{
  "ts": "2025-11-14T22:47",
  "trust_score": 0.608,
  "variance": 0.002,
  "stability": 0.999
}


⸻

5.4 info()

General system health:
	•	mode
	•	trust score
	•	uptime
	•	CPU/memory
	•	Stripe pricing ids

info = governor.info()


⸻

5.5 license_status(key=None)

Checks current license quota + status.

If no key is passed, uses the SDK’s license key.

governor.license_status()


⸻

6. Full Example

from lcac import LCAC

governor = LCAC(license_key="trial_abc123")

prompt  = "Explain quantum entanglement."
output  = "It's when particles talk to each other telepathically."

res = governor.evaluate(prompt, output)

print("Verdict:", res["verdict"])
print("Trust:", res["trust"])
print("Insight:", res["insight"])


⸻

7. Error Handling

All methods return structured JSON.

Example:

{"error": "Invalid or expired license key"}

Recommended wrapper:

try:
    res = governor.evaluate(p, o)
except Exception as e:
    log("LCAC error:", e)


⸻

8. License Behavior
	•	Free trials auto-generated
	•	Quota decrements on each evaluation
	•	Stripe purchases auto-update Redis license records
	•	Deterministic email-based license key in production mode

⸻

9. Best Practices
	•	Always log LCAC verdict + insight
	•	Block or escalate on severity ≥ 3
	•	Use /overview for dashboards
	•	Use /metrics for time-series drift monitoring
	•	Use /info for uptime + health checks

⸻

10. Summary

The Python SDK offers:
	•	one-line evaluation
	•	trust + variance scoring
	•	reasoning insight engine
	•	quota + license verification
	•	complete telemetry access

LCAC gives any developer a governor layer for LLMs and agent systems.

⸻
