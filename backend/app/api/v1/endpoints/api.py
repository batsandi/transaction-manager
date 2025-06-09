from fastapi import APIRouter
from .endpoints import login 


api_router = APIRouter()

@api_router.get("/")
def api_root_health_check():
    """
    Health check for the v1 API. Confirms the API is running.
    """
    return {"health": "API v1 is Alive and Kickin!"}
