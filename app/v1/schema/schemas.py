from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    usuario: str
    password: str

class UserCreate(UserBase):
    #password: str
    pass

class UserOut(UserBase):
    id: UUID    # Debe ser tipo UUID ya que es el tipo de dato con el que se creo en la BD y que viene desde el Modelo

    class Config:
        from_attributes = True