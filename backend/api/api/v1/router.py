from fastapi import APIRouter

from backend.api.api.v1.routes import (
    buildings,
    chat,
    geocode,
    health,
    reports,
    simulation,
)

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(geocode.router, tags=["geocode"])
api_router.include_router(buildings.router, tags=["buildings"])
api_router.include_router(simulation.router, tags=["simulation"])
api_router.include_router(reports.router, tags=["reports"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
