from fastapi import APIRouter

router = APIRouter()


@router.post("/simulation")
def simulate() -> dict:
    return {"status": "not_implemented"}
