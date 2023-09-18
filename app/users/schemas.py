from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    id: int
    username: str
    email: EmailStr
