from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    price: int
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
