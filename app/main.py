from fastapi import FastAPI
from .models import ChatRequest, ChatResponse
from .agent import BIAgent

app = FastAPI()
agent = BIAgent()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer, traces = agent.answer(request.message)
    return ChatResponse(answer=answer, tool_traces=traces)