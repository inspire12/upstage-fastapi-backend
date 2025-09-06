import uvicorn
from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute

from app.api.routes import users
from app.core.settings import settings
from app.core.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

api_router = APIRouter()

api_router.include_router(users.router)


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # 직접 이 파일을 실행할 때만 서버 실행
    uvicorn.run("app.main:app", host="127.0.0.1", port=8002, reload=True)