from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app.users.views import router as users_router
from app.items.views import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(items_router, prefix="/items", tags=["Items"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
