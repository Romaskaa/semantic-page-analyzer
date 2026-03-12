from fastapi import APIRouter
from services.knowledge_base import load_knowledge_base
from services.rag_generator import generate_content_rag

router = APIRouter()

@router.post("/generate-content")
def create_content(topic: str):
    knowledge = load_knowledge_base()
    content = generate_content_rag(topic, knowledge)
    return {"content": content}