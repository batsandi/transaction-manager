from fastapi import APIRouter
from app.api.v1.endpoints import login, transactions


api_router = APIRouter()

# Include the login and transaction routers.
api_router.include_router(login.router, tags=["Authentication"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])

@api_router.get("/")
def api_root_health_check():
    """
    Health check for the v1 API. Confirms the API is running.
    """
    return {"health": "API v1 is Alive and Kickin!"}
