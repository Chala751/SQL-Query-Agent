from fastapi import APIRouter
from agent.graph import app as agent_app

router = APIRouter()

@router.post("/ask")
async def ask_sql_agent(payload: dict):
    question = payload["question"]
    final = agent_app.invoke({"question": question})
    return final["final_answer"]
