from fastapi import APIRouter
from services.content_generator import generate_content

router = APIRouter()

@router.post("/generate-content")

def create_content(topic:str, knowledge:str):

    content = generate_content(topic, knowledge)

    return {"content":content}