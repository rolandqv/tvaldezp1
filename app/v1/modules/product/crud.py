from sqlalchemy.orm import Session
from fastapi import HTTPException
from .model import Product
from .schema import ProductCreate, ProductUpdate

def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    product_db = get_product_by_id(db, product_id)
    if not product_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for field, value in product_update.dict(exclude_unset=True).items():
        setattr(product_db, field, value)

    db.commit()
    db.refresh(product_db)
    return product_db

def delete_product(db: Session, product_id: int):
    product_db = get_product_by_id(db, product_id)
    if not product_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product_db)
    db.commit()
    return {"ok": True, "message": "Producto eliminado"}