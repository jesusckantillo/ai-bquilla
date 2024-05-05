import sys
import os
import time
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))
import asyncio
from utils import __annotations__
from typing import Optional
from fastapi import File, APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.exceptions import HTTPException 
from pydantic import BaseModel
from pathlib import Path
from services.ai_services.gemini_controller import  gemini_model
from services.audio_services.eleven_labs import sound_generator
from models.text.text_model import TextModel


router = APIRouter()

class TextCard(BaseModel):
    text1: str = ""
    text2: list[str] = []


@router.post("/get-mdx", response_class=FileResponse)
def generate_mdx(pdf_file: Optional[bytes] = File(description="File to send")):
    if not pdf_file:
        raise HTTPException(status_code=400, detail="Se requiere un archivo PDF")    
    mdx_file: 2
    return FileResponse(mdx_file, filename="generated.mdx")


@router.post("/get-audio/")
async def get_audio(word: str):
    try:
        file_path = sound_generator(word)
        
        
        max_wait_time = 5  
        wait_interval = 0.1  
        waited_time = 0
        while not os.path.exists(file_path) and waited_time < max_wait_time:
            time.sleep(wait_interval)
            waited_time += wait_interval
    
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Archivo no encontrado")
        return FileResponse(file_path, media_type="audio/mpeg")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/text-card/")
def get_text_card(context: TextModel):
    word = context.word
    return gemini_model.generate_text_card(word)