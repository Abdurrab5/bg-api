import subprocess
from fastapi import APIRouter

router = APIRouter()

@router.get("/packages")
def packages():
    result = subprocess.run(
        ["pip", "list"],
        capture_output=True,
        text=True
    )

    return {"packages": result.stdout}