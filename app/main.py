from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.api.v1.router import api_router
from app.db.database import init_db
from app.core.exceptions import register_exception_handlers


def create_application() -> FastAPI:
    app = FastAPI(
        title=Settings.APP_NAME,
        version=Settings.APP_VERSION,
        debug=Settings.DEBUG,
        openapi_url=f"{Settings.API_V1_PREFIX}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=Settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        api_router,
        prefix=Settings.API_V1_PREFIX
    )

    app.mount(
        "/uploads",
        StaticFiles(directory=Settings.UPLOAD_DIR),
        name="uploads"
    )

    register_exception_handlers(app)

    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    print("Student Programming Platform started!")
    await init_db()


@app.on_event("shutdown")
async def shutdown_event():
    print("Platform suspended...")







