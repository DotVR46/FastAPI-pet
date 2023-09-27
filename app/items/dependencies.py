from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.models import db_helper, Item
from app.items import crud


async def get_item_by_id(
    item_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Item:
    item = await crud.get_item(session=session, item_id=item_id)
    if item:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item ID = {item_id} not found!",
    )
