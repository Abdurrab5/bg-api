from fastapi import FastAPI
from routes import bg_remove

app = FastAPI(
    title="BG Remove API",
    version="1.0",
    
)

app.include_router(bg_remove.router)

@app.get("/")
def root():
    return {"status": "BG API running"}