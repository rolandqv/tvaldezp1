from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import List
from app.v1.utils.db import get_db, get_current_user
from .schema import ProductCreate, ProductUpdate, ProductOut
from .crud import create_product, get_all_products, get_product_by_id, update_product, delete_product

router = APIRouter()

@router.post("/", response_model=ProductOut, summary="Crear Producto", dependencies=[Depends(get_current_user)])
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/", response_model=List[ProductOut], summary="Listar Productos", dependencies=[Depends(get_current_user)])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.get("/{product_id}", response_model=ProductOut, summary="Obtener Producto", dependencies=[Depends(get_current_user)])
def get(product_id: int = Path(...), db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/{product_id}", response_model=ProductOut, summary="Actualizar Producto", dependencies=[Depends(get_current_user)])
def update(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product_update)

@router.delete("/{product_id}", summary="Eliminar Producto", dependencies=[Depends(get_current_user)])
def delete(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)