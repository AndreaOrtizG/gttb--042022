from fastapi import FastAPI

from app.api.api import api_router
from app.core.config_fastapi import Settings
from app.infra.postgres.config import generate_schema, init_db

settings = Settings()


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    init_db(app)
    await generate_schema()
