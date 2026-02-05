from fastapi import APIRouter

from app.api.routes import auth, data, projects

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(data.router, prefix="/data", tags=["data"])
