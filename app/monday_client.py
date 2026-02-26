import os
import requests
from typing import Dict, Any

MONDAY_API_URL = "https://api.monday.com/v2"


class MondayClient:
    def __init__(self):
        self.api_key = os.getenv("MONDAY_API_KEY")
        if not self.api_key:
            raise ValueError("MONDAY_API_KEY not set")

    def query(self, query: str) -> Dict[str, Any]:
        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json",
        }

        response = requests.post(
            MONDAY_API_URL,
            json={"query": query},
            headers=headers,
            timeout=30,
        )

        if response.status_code != 200:
            raise RuntimeError(f"Monday API error: {response.text}")

        return response.json()