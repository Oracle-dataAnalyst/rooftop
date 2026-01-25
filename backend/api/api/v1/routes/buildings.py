from fastapi import APIRouter

router = APIRouter()


@router.get("/buildings")
def list_buildings() -> dict:
    return {"status": "not_implemented"}
