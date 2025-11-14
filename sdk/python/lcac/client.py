import requests
from typing import Any, Dict, Optional

class LCAC:
    """
    LCAC Governor Python client.

    Default base_url: https://api.atomlabs.app
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.atomlabs.app",
        timeout: float = 10.0,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self._session = session or requests.Session()

    # Internal utilities
    def _headers(self) -> Dict[str, str]:
        h = {"Content-Type": "application/json"}
        if self.api_key:
            h["X-License-Key"] = self.api_key
        return h

    def _get(self, path: str, *, params=None):
        url = f"{self.base_url}{path}"
        r = self._session.get(url, headers=self._headers(), params=params, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def _post(self, path: str, *, json_body):
        url = f"{self.base_url}{path}"
        r = self._session.post(url, headers=self._headers(), json=json_body, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    # Public API
    def evaluate(self, prompt: str, output: str):
        return self._post("/evaluate", json_body={"prompt": prompt, "output": output})

    def evaluate_pairs(self, pairs: Dict[str, str]):
        return {p: self.evaluate(p, o) for p, o in pairs.items()}

    def info(self):
        return self._get("/info")

    def metrics(self):
        return self._get("/metrics")

    def overview(self):
        return self._get("/overview")

    def license_status(self, key=None):
        key = key or self.api_key
        if not key:
            raise ValueError("No license key provided.")
        return self._get("/license/verify", params={"key": key})

    # Cleanup
    def close(self):
        if self._session:
            self._session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
