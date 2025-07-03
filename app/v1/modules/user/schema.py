from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    city: str
    username: str
    hashed_password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    city: Optional[str] = None
    username: Optional[str] = None
    hashed_password: Optional[str] = None

class UserOut(UserBase):
    id: UUID

    class Config:
        from_attributes = True