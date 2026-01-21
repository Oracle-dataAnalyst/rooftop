from fastapi import APIRouter

router = APIRouter()


@router.get("/geocode")
def geocode() -> dict:
    return {"status": "not_implemented"}
