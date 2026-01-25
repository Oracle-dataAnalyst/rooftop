from fastapi import APIRouter

router = APIRouter()


@router.get("/reports")
def list_reports() -> dict:
    return {"status": "not_implemented"}
