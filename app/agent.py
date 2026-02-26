import os
from dotenv import load_dotenv
from .bi_engine import total_revenue, pipeline_by_sector
from .data_cleaner import clean_items
from typing import List
from .monday_client import MondayClient
from .data_cleaner import clean_items
from .bi_engine import pipeline_by_sector
from .models import ToolTrace

load_dotenv()




class BIAgent:

    def __init__(self):
        self.client = MondayClient()
        self.deals_board_id = os.getenv("DEALS_BOARD_ID")

    def answer(self, user_query: str):

        tool_traces = []

        query = f"""
        {{
        boards(ids: {int(self.deals_board_id)}) {{
            items_page(limit: 500) {{
            items {{
                name
                column_values {{
                text
                type
                column {{
                    title
                }}
                }}
            }}
            }}
        }}
        }}
        """

        response = self.client.query(query)

        # ✅ THIS MUST BE INDENTED INSIDE answer()
        if "errors" in response:
            return f"Monday API Error: {response['errors']}", []

        boards = response.get("data", {}).get("boards", [])
        if not boards:
            return "No boards found.", []

        items = boards[0].get("items_page", {}).get("items", [])
        cleaned = clean_items(items)

        tool_traces.append(
            ToolTrace(
                tool_name="monday_api_query",
                arguments={"board_id": self.deals_board_id},
                response_summary=f"Fetched {len(items)} items"
            )
        )

        query_lower = user_query.lower()

        if "revenue" in query_lower:
            total = total_revenue(cleaned)
            return f"Our total revenue is ${total:,.2f}.", tool_traces

        if "pipeline" in query_lower:
            result = pipeline_by_sector(cleaned, None)
            return (
                f"We have {result['count']} deals worth "
                f"${result['total_value']:,.2f} in pipeline.",
                tool_traces
            )

        return "I need clarification on your question.", tool_traces