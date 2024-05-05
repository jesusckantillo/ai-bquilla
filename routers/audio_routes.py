from utils import __annotations__
from typing import Optional
from fastapi import APIRouter, File
from fastapi.exceptions import HTTPException 
#Models import


router = APIRouter()


@router.post("/check-pronuntation")
def check_pronuntiation(audio_file: Optional[bytes] = File(description="Audio file to send")):
    if not audio_file:
        raise HTTPException(status_code=400, detail="Se requiere un archivo de audio")
    return {"message": "Archivo de audio recibido correctamente", "audio_size": len(audio_file)}
