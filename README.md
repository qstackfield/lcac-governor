# LCAC Governor - Cognitive Integrity Framework

LCAC Governor is a cognitive integrity layer that sits in front of your LLMs and tools.  
It does not replace your modele. It governs them.

It provides:
• Trust scoring (0–1)
• Drift and variance detection
• Real-time monitoring via the console
• License and quota management (free → starter → pro → enterprise)
• Clean HTTP API
• Python SDK

The production API is running at:
https://api.atomlabs.app

The console dashboard is located at:
https://console.atomlabs.app/console

---

WHY LCAC EXISTS
LCAC exists because modern LLM systems can silently drift or behave unpredictably under:
• prompt injection
• multi-agent feedback loops
• long-context degradation
• tool misuse
• hallucination under low grounding

LCAC provides visibility by running your prompts and outputs through a trust-governor.

---

QUICKSTART (SDK)
The Python SDK lives in the sdk/python directory.
Install it with pip -e and import LCAC from lcac.client.

Examples are provided in the examples folder.

---

API ENDPOINTS
The engine exposes these HTTP endpoints:
• POST /evaluate
• GET /metrics
• GET /overview
• GET /info
• GET /license/verify

Full details are provided in docs/api-reference.md.

---

STATUS
Core LCAC engine: live  
Console: live  
Stripe billing: live  
Python SDK: included  
Landing page: included  
Future: JS/Go SDKs

---

LICENSE
MIT License. See LICENSE file.
