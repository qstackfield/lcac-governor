# LCAC Governor  
Cognitive Integrity Framework for LLMs

LCAC Governor is a lightweight trust-layer that evaluates any model’s output for:
- drift  
- variance  
- reasoning instability  
- prompt-injection indicators  
- hallucination risk  
- multi-agent interference  

The framework provides:
- `/evaluate` cognitive scoring  
- `/overview` unified trust snapshot  
- `/metrics` telemetry  
- `/info` system metadata  
- License + quota engine  
- Python SDK  
- SaaS dashboard  

---

## Quick Links

- **API Base:** https://api.atomlabs.app  
- **Console:** https://console.atomlabs.app/console  
- **GitHub:** https://github.com/qstackfield/lcac-governor  
- **PyPI SDK:** https://pypi.org/project/lcac-sdk  

---

## Evaluate Example

```bash
curl -X POST https://api.atomlabs.app/evaluate \
  -H "Content-Type: application/json" \
  -d '{
        "prompt": "Explain cognitive drift.",
        "output": "Cognitive drift is the instability of reasoning..."
      }'
```

---

## Python SDK Example

```python
from lcac import LCAC

gov = LCAC()
result = gov.evaluate("test prompt", "test output")
print(result)
```

---

## Components

- **Trust Engine**  
- **Variance Analyzer**  
- **Governance Layer**  
- **Hash-Chained Ledger**  
- **License + Quota Manager**  
- **Stripe Billing Integration**  
- **SaaS Console UI**

---

## Documentation Pages

- [API Reference](api-reference.md)  
- [Architecture](architecture.md)  
- [Governance Model](governance-model.md)  
- [SDK Usage](sdk-usage.md)  
