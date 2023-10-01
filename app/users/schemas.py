from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr
from typing import Annotated


class CreateUser(BaseModel):
    id: int
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
