from fastapi import APIRouter

router = APIRouter()

@router.post('/query')
async def query_chatbot(payload: dict):
    # Placeholder: route to LangChain/RAG/LLM
    return {"response": "This is a placeholder response from the AI chatbot."}
