LCAC Python SDK

Lightweight client for the LCAC Governor API

⸻

Installation

From PyPI

pip install lcac-sdk

From source (local development)

pip install -e ./sdk/python


⸻

Importing the Client

from lcac import LCAC

client = LCAC(
    base_url="https://api.atomlabs.app",
    license_key="your_license_key"  # optional
)

If no license key is provided, LCAC will automatically issue a trial key on first evaluate.

⸻

Methods

1. evaluate(prompt, output)

Runs a full cognitive integrity analysis.

result = client.evaluate(
    prompt="Explain gravity.",
    output="Gravity is the force that makes apples fall."
)

print(result["verdict"])
print(result["trust"])


⸻

2. overview()

Gets unified trust/drift snapshot.

state = client.overview()
print(state)


⸻

3. metrics()

Retrieves incremental trust telemetry.

metrics = client.metrics()
print(metrics)


⸻

4. info()

Gets system health + uptime.

info = client.info()
print(info)


⸻

5. license_status(key=None)

Validates a license or returns current key metadata.

client.license_status()          # uses your key
client.license_status("key123")  # check another


⸻

Example Script

from lcac import LCAC

gov = LCAC(license_key=None)  # auto-trial mode

info = gov.info()
print("INFO:", info)

metrics = gov.metrics()
print("METRICS:", metrics)

evaluation = gov.evaluate(
    prompt="Explain cognitive drift.",
    output="Cognitive drift is when a model shifts unpredictably."
)
print("EVALUATE:", evaluation)


⸻

Error Handling

All LCAC errors follow a clean JSON pattern:

{ "error": "message" }

Quota exceeded:

{ "detail": "Quota exceeded. Purchase tokens to continue." }

Invalid license:

{ "detail": "Invalid or expired license key" }


⸻

Notes
	•	SDK uses only requests (light footprint).
	•	Works with Python 3.8+.
	•	Designed for server or notebook environments.
	•	Automatically sends license headers when provided.

⸻

