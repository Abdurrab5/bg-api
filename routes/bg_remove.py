# routes/bg_remove.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
from services.bg_service import remove_background

router = APIRouter()

@router.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()

    output_image = remove_background(input_image)

    return Response(
        content=output_image,
        media_type="image/png"
    )