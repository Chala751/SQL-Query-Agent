from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.api_core.exceptions import ResourceExhausted
from agent.graph import app as agent_app

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_sql_agent(payload: QueryRequest):
    question = payload.question
    try:
        final = agent_app.invoke({"question": question})
        return {"answer": final["final_answer"]}
    except ResourceExhausted:
        raise HTTPException(
            status_code=429,
            detail="Gemini API quota exceeded, try again later"
        )
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))
