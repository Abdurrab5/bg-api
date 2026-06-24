from rembg import remove, new_session
from fastapi.concurrency import run_in_threadpool

# Load model once when app starts
session = new_session("u2netp")

async def remove_bg(file):
    input_image = await file.read()

    output_image = await run_in_threadpool(
        remove,
        input_image,
        session=session
    )

    return output_image