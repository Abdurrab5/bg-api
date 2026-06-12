from rembg import remove, new_session

session = new_session()

def remove_background(image_bytes: bytes) -> bytes:
    return remove(image_bytes, session=session)