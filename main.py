from fastapi import FastAPI
from routes.bg_remove import router
from pathlib import Path
import shutil
import urllib.request
import os

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"
MODEL_SRC = MODELS_DIR / "u2net.onnx"
MODEL_DST = Path.home() / ".u2net" / "u2net.onnx"

MODEL_URL = "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx"

MODELS_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DST.parent.mkdir(parents=True, exist_ok=True)

try:
    if not MODEL_SRC.exists():
        print("Downloading u2net.onnx...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_SRC)
        print(f"Downloaded: {MODEL_SRC}")

    if not MODEL_DST.exists():
        print("Copying model to rembg directory...")
        shutil.copy2(MODEL_SRC, MODEL_DST)
        print(f"Copied to: {MODEL_DST}")

except Exception as e:
    print(f"Model setup failed: {e}")
    raise

app = FastAPI(
    title="BG Remove API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "BG API running"}