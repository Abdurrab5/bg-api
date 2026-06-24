from fastapi import FastAPI
from routes.bg_remove import router
from pathlib import Path
import shutil
import os

BASE_DIR = Path(__file__).resolve().parent
MODEL_SRC = BASE_DIR / "models" / "u2net.onnx"
MODEL_DST = Path("/home/user/.u2net/u2net.onnx")

os.makedirs(MODEL_DST.parent, exist_ok=True)

if not MODEL_DST.exists():
    shutil.copy(MODEL_SRC, MODEL_DST)
    
app = FastAPI(
    title="BG Remove API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "BG API running"} 