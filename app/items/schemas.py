from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    price: int
    description: str


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemCreate):
    pass


class ItemUpdatePartial(ItemCreate):
    name: str | None = None
    price: int | None = None
    description: str | None = None


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
