from fastapi import APIRouter, UploadFile
from services.knowledge_base import save_file

router = APIRouter()

@router.post("/upload")

def upload(file: UploadFile):

    path = save_file(file)

    return {"path":path}