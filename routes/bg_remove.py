from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from services.bg_service import remove_bg
import io

router = APIRouter()

@router.post("/bg-remove")
async def bg_remove(file: UploadFile = File(...)):
    print("REQUEST RECEIVED")

    output_image = await remove_bg(file)

    print("REMOVE_BG RETURNED")

    return StreamingResponse(
        io.BytesIO(output_image),
        media_type="image/png"
    )