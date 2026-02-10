from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.dash_app import create_dash_app


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="企业级地理数据智能平台后端",
        version=settings.version,
    )
    app.include_router(api_router, prefix="/api")

    dash_app = create_dash_app()
    app.mount("/dash", WSGIMiddleware(dash_app.server))

    return app


app = create_app()
