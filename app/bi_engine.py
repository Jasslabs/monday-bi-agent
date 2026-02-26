from typing import List, Dict
from datetime import datetime


def pipeline_by_sector(data: List[Dict], sector: str | None):
    now = datetime.utcnow()
    current_quarter = (now.month - 1) // 3 + 1

    filtered = [
        d for d in data
        if (not sector or (d["sector"] and sector.lower() in d["sector"].lower()))
        and d["close_date"]
        and ((d["close_date"].month - 1) // 3 + 1) == current_quarter
    ]

    total = sum(d["amount"] for d in filtered)

def total_revenue(data):
    return sum(d["amount"] for d in data)

    return {
        "count": len(filtered),
        "total_value": total,
    }