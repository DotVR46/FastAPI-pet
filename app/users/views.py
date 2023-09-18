from typing import Annotated

from fastapi import APIRouter, Path, Depends

from app.users.schemas import CreateUser

users_router = APIRouter()

users = [
    {"id": 1, "username": "user1", "email": "user1@gmail.com"},
    {"id": 2, "username": "user2", "email": "user2@gmail.com"},
    {"id": 3, "username": "user3", "email": "user3@gmail.com"},
]


@users_router.get("/")
async def get_users_list():
    return {"users": users}


@users_router.get("/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"message": "User not found."}


@users_router.post("/create")
async def create_user(user: CreateUser):
    users.append(dict(user))
    return {"message": "User created", "user": user}
