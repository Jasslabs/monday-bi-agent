from typing import Dict, Any, List
from datetime import datetime


def normalize_currency(value: str | None) -> float:
    if not value:
        return 0.0
    value = value.replace("$", "").replace(",", "").strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


def normalize_date(value: str | None):
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def clean_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cleaned = []

    for item in items:
        columns = {
        col["column"]["title"]: col["text"]
        for col in item["column_values"]
        if col.get("column") and col.get("text") is not None
    }

        cleaned.append({
            "name": item["name"],
            "sector": columns.get("Sector"),
            "amount": normalize_currency(columns.get("Amount")),
            "close_date": normalize_date(columns.get("Close Date")),
            "status": columns.get("Status"),
        })

    return cleaned