from fastapi import FastAPI
from core.settings import settings
import odoo
from api.api import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version
    )

    @app.on_event("startup")
    def set_default_executor() -> None:
        from concurrent.futures import ThreadPoolExecutor
        import asyncio

        loop = asyncio.get_running_loop()
        # Tune this according to your requirements !
        loop.set_default_executor(ThreadPoolExecutor(max_workers=5))


    @app.on_event("startup")
    def initialize_odoo() -> None:
        # Read Odoo config from $ODOO_RC.
        odoo.tools.config.parse_config([])

    @app.get("/")
    def index() -> dict:
        return {
            'app_name': settings.app_name,
            'app_description': settings.app_description,
            'app_version': settings.app_version
        }

    @app.get("/health")
    def health() -> str:
        return "ok"

    app.include_router(api_router, prefix=settings.api_version)

    return app
