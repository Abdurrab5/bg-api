from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import Response
from services.bg_service import remove_background

router = APIRouter()

@router.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        if not image_bytes:
            raise HTTPException(status_code=400, detail="Empty file")

        output = remove_background(image_bytes)

        return Response(content=output, media_type="image/png")

    except Exception as e:
        print("FATAL ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))