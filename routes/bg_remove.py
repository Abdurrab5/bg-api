from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import Response
from services.bg_service import remove_background

router = APIRouter()

@router.post("/remove-bg")
async def remove_bg(request: Request):
    image_bytes = await request.body()

    if not image_bytes:
        raise HTTPException(status_code=400, detail="No image provided")

    output_image = remove_background(image_bytes)

    return Response(
        content=output_image,
        media_type="image/png"
    )