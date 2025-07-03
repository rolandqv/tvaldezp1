from sqlalchemy.orm import Session
from fastapi import HTTPException
from .model import User
from .schema import UserCreate, UserUpdate
from app.v1.utils.db import get_password_hash
from uuid import UUID
from fastapi import Path


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.hashed_password)
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        city=user.city,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

# NUEVO: Obtener usuario por ID
def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()

# NUEVO: Actualizar usuario
def update_user(db: Session, user_id, user_update: UserUpdate):
    user_db = get_user_by_id(db, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Solo actualizamos los campos que no son None
    if user_update.first_name is not None:
        user_db.first_name = user_update.first_name
    if user_update.last_name is not None:
        user_db.last_name = user_update.last_name
    if user_update.city is not None:
        user_db.city = user_update.city
    if user_update.username is not None:
        user_db.username = user_update.username
    if user_update.hashed_password is not None:
        user_db.hashed_password = get_password_hash(user_update.hashed_password)

    db.commit()
    db.refresh(user_db)
    return user_db

# NUEVO: Eliminar usuario
def delete_user(db: Session, user_id):
    user_db = get_user_by_id(db, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user_db)
    db.commit()
    return {"ok": True, "message": "Usuario eliminado"}