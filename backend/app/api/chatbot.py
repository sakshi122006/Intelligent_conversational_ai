from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.rag import answer_query

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    language: str = 'en'
    voice: bool = False

@router.post('/query')
async def chat_query(req: ChatRequest):
    """Pass the user message through the RAG pipeline and return response + explanation."""
    resp = await answer_query(req.message, language=req.language)
    return resp
