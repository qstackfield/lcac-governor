LCAC Glossary

Terms Used in the LCAC Cognitive Integrity Framework


Cognitive Integrity

A measurement of how stable, grounded, and consistent an LLM’s reasoning is.
Represented through trust score, variance, drift, and verdict.


Trust Score

A normalized value between 0.0 → 1.0 indicating output reliability.
	•	High (≥ 0.85): Expected consistent behavior
	•	Medium (0.65–0.85): Monitor for drift
	•	Low (< 0.65): High risk of reasoning failure


Variance

Statistical volatility measured across evaluations.
Higher variance suggests instability or reasoning spread.


Drift

Directional degradation in reasoning behavior detected over time.

Examples:
	•	Overgeneralization
	•	Loss of grounding
	•	Pattern collapse
	•	Inconsistent chain-of-thought


Verdict

Final classification produced by LCAC:
	•	stable
	•	watch
	•	unstable

Determines recommended actions and console visual indicators.


Insight

Human-readable explanation describing why a verdict was reached.

Example:

"Observed minor drift in reasoning abstraction layer."



Recommendation

Operational guidance tied to verdict and variance trends.

Examples:
	•	“Increase grounding.”
	•	“Reduce context overlap.”
	•	“Restrict execution actions.”


Ledger

A Redis-backed chain of evaluation entries.
Each evaluation includes:
	•	trace_id
	•	trust
	•	variance
	•	verdict
	•	hashed integrity link

Used for audit and tamper detection.


Hash Chain

Deterministic SHA-256 chain linking each evaluation through:

prev_hash + evaluation_payload

Ensures evaluation integrity over time.


Persona

Logical identity or strategy assigned to an evaluation session.
Defaults to "default" unless overridden.


Governor Mode

Runtime control mode:
	•	HOLD
	•	ELEVATE
	•	LOCKDOWN

Controls how outputs downstream can be consumed.


Quota

Token count allowed under a license.
Each /evaluate call consumes 1 quota unit.


License Key

A unique value identifying a user’s entitlement and remaining quota.

Example:

trial_f3ab9281



Webhook

A Stripe event push that LCAC listens for to:
	•	Activate new licenses
	•	Recharge quotas
	•	Disable expired subscriptions

Path:

POST /stripe/webhook



Overview State

Unified summary of system integrity from /overview.
Used by the console and SDK.


SDK

A client library allowing developers to interact with LCAC using:
	•	evaluate
	•	info
	•	metrics
	•	license_status
	•	overview


Console

The LCAC web UI located at:

https://console.atomlabs.app/console

Displays live trust telemetry and evaluation insights.

