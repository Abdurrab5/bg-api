from rembg import remove, new_session

def remove_background(image_bytes: bytes) -> bytes:
    session = new_session()
    return remove(image_bytes, session=session)