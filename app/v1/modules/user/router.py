from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.v1.utils.db import get_db, authenticate_user, create_access_token, get_current_user
from .schema import UserCreate, UserOut, UserUpdate
from .crud import create_user, get_all_users, update_user, delete_user, get_user_by_id
from app.v1.schema.token import Token
from uuid import UUID
from fastapi import Path

router = APIRouter()

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrectos")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=UserOut, summary="Crear Usuario")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=List[UserOut], summary="Listar Usuarios", dependencies=[Depends(get_current_user)])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserOut, summary="Obtenter un Usuario",dependencies=[Depends(get_current_user)])
def get_user(user_id: UUID = Path(...), db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# NUEVO: actualizar usuario
@router.put("/{user_id}", response_model=UserOut, summary="Actualizar Usuario", dependencies=[Depends(get_current_user)])
def update_user_route(user_id: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

# NUEVO: eliminar usuario
@router.delete("/{user_id}", summary="Eliminar Usuario", dependencies=[Depends(get_current_user)])
def delete_user_route(user_id: str, db: Session = Depends(get_db)):
    return delete_user(db, user_id)