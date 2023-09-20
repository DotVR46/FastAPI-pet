from typing import Annotated

from fastapi import APIRouter, Path, Depends

from app.users import crud
from app.users.schemas import CreateUser

router = APIRouter()


@router.post("/create")
async def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
