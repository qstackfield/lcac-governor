import requests

class LCAC:
    def __init__(self, base_url="https://api.atomlabs.app", license_key=None):
        self.base_url = base_url.rstrip("/")
        self.license_key = license_key

    def _headers(self):
        h = {"Content-Type": "application/json"}
        if self.license_key:
            h["X-License-Key"] = self.license_key
        return h

    def evaluate(self, prompt, output):
        payload = {"prompt": prompt, "output": output}
        r = requests.post(self.base_url + "/evaluate", json=payload, headers=self._headers())
        return r.json()

    def info(self):
        return requests.get(self.base_url + "/info").json()

    def metrics(self):
        return requests.get(self.base_url + "/metrics").json()

    def overview(self):
        return requests.get(self.base_url + "/overview").json()

    def license_status(self, key=None):
        if key is None:
            key = self.license_key
        return requests.get(self.base_url + "/license/verify", params={"key": key}).json()
