from rembg import remove, new_session
from fastapi.concurrency import run_in_threadpool

print("LOADING U2NETP MODEL...")

session = new_session("u2netp")

print("MODEL LOADED SUCCESSFULLY")

async def remove_bg(file):
    print("START remove_bg")

    input_image = await file.read()

    print("FILE SIZE:", len(input_image))

    print("CALLING REMBG")

    output_image = await run_in_threadpool(
        remove,
        input_image,
        session=session
    )

    print("REMBG FINISHED")

    return output_image