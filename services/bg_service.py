from rembg import remove, new_session
from fastapi.concurrency import run_in_threadpool
import traceback

session = new_session("u2netp")

async def remove_bg(file):
    try:
        input_image = await file.read()

        output = await run_in_threadpool(
            remove,
            input_image,
            session=session
        )

        return output

    except Exception:
        traceback.print_exc()
        raise