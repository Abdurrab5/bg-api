import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_WAIT_POLICY"] = "PASSIVE"
os.environ["OMP_DYNAMIC"] = "FALSE"
from fastapi import FastAPI
from routes.bg_remove import router

app = FastAPI(
    title="BG Remove API",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "BG API running"}