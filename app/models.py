from pydantic import BaseModel
from typing import List, Dict, Any


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ToolTrace(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]
    response_summary: str


class ChatResponse(BaseModel):
    answer: str
    tool_traces: List[ToolTrace]