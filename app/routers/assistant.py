from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import get_rag_response

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/assistant")
def chat(request: ChatRequest):

    answer = get_rag_response(request.question)

    return {"response": answer}
