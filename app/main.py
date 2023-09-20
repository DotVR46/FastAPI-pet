import uvicorn
from fastapi import FastAPI

from app.users.views import router as users_router

app = FastAPI()


app.include_router(users_router, prefix="/users", tags=["Users"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")