from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Item, ItemCreate
from app.core.models import db_helper

router = APIRouter()


@router.get("/", response_model=list[Item])
async def get_items(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_items(session=session)


@router.post("/", response_model=Item)
async def create_item(
    item_in: ItemCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_item(session=session, item_in=item_in)


@router.get("/{item_id}", response_model=Item)
async def get_item(
    item_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    item = await crud.get_item(session=session, item_id=item_id)
    if item:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item ID = {item_id} not found!",
    )
