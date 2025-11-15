LCAC Python SDK

The LCAC Python SDK provides a simple client interface for evaluating prompts, retrieving trust telemetry, and interacting with the LCAC Governor API.

It is designed for developers integrating LCAC into applications, agents, pipelines, SaaS products, or research workflows.

⸻

1. Installation

From PyPI (public release)

pip install lcac-sdk

Developer mode (local source)

From inside your repository:

pip install -e ./sdk/python


⸻

2. Basic Usage

from lcac import LCAC

client = LCAC(
    base_url="https://api.atomlabs.app",
    license_key="trial_abc123"        # optional; LCAC issues trials automatically
)

result = client.evaluate(
    prompt="Explain cognitive drift.",
    output="Cognitive drift is when a model's reasoning shifts unpredictably."
)

print(result)


⸻

3. Class Structure

LCAC Client

lcac/
 ├── __init__.py
 └── client.py

Constructor

LCAC(base_url="https://api.atomlabs.app", license_key=None)

Arguments:

Parameter	Description
base_url	LCAC API base URL (default production endpoint)
license_key	Optional license key. If omitted, LCAC will issue trials automatically.


⸻

4. Available Methods

4.1 evaluate(prompt, output)

Runs an integrity evaluation.

r = client.evaluate(prompt="...", output="...")

Returns:

{
  "license": "trial_xxx",
  "trace_id": "uuid",
  "trust": 0.61,
  "variance": 0.002,
  "verdict": "unstable",
  "reason": "...",
  "severity": {"level": 3, "label": "critical"},
  "insight": "LCAC observed reasoning state ...",
  "hash_self": "sha256..."
}


⸻

4.2 overview()

Unified cognitive snapshot.

client.overview()

Example:

{
  "trust": 0.598,
  "variance": 0.001,
  "verdict": "unstable",
  "mode": "HOLD",
  "persona": "default",
  "ledger_count": 59
}


⸻

4.3 metrics()

Time-series telemetry for the Trust Trend chart.

client.metrics()

Example:

{
  "ts": "2025-11-14T02:22:41Z",
  "trust_score": 0.608,
  "variance": 0.001,
  "stability": 0.999,
  "ledger_count": 41
}


⸻

4.4 info()

System metadata.

client.info()

Example:

{
  "product": "LCAC Cognitive Integrity Framework",
  "version": "1.0.0-Insight",
  "platform": "Linux",
  "mode": "HOLD",
  "trust_score": "0.608",
  "uptime_sec": 48291.5,
  "cpu": 22.4,
  "memory": 70.1
}


⸻

4.5 license_status(key=None)

Validate a license.

client.license_status()

Example:

{
  "ok": true,
  "license": {
    "tier": "starter",
    "quota": "5000",
    "used": "19",
    "status": "active"
  }
}


⸻

5. Full Example Script

from lcac import LCAC

client = LCAC(license_key=None)

print("\n=== INFO ===")
print(client.info())

print("\n=== METRICS ===")
print(client.metrics())

print("\n=== EVALUATE ===")
print(client.evaluate(
    prompt="Explain cognitive drift.",
    output="Cognitive drift is when a model's reasoning shifts unpredictably..."
))


⸻

6. Error Handling

All SDK calls return raw JSON from the LCAC API.

Common error patterns:

Code	Meaning
400	Invalid request
401	Invalid license key
402	Quota exceeded
500	Internal error

Example handling:

resp = client.evaluate("p", "o")
if "error" in resp:
    print("Evaluation failed:", resp["error"])


⸻

7. Best Practices
	•	Always store your license key in environment variables, not code
	•	For batch evaluations, keep requests under 1 req/sec to avoid tunnel throttling
	•	Use /overview for dashboards and monitoring
	•	Use /metrics for visualization or agent supervision loops

⸻

8. Versioning

Version format:

MAJOR.MINOR.PATCH

Your current SDK version: 1.0.0

Updates will appear here:
https://pypi.org/project/lcac-sdk/

⸻

9. Support

For integration help, licensing, or enterprise deployment:

lcac@atomlabs.app


⸻
