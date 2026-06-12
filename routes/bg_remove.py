from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import Response
from services.bg_service import remove_background

router = APIRouter()

@router.post("/remove-bg")
async def remove_bg(request: Request):
    try:
        image_bytes = await request.body()

        if not image_bytes:
            raise HTTPException(status_code=400, detail="No image provided")

        print("IMAGE SIZE:", len(image_bytes))

        output = remove_background(image_bytes)

        return Response(content=output, media_type="image/png")

    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))