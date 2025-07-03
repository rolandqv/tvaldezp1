from fastapi import FastAPI
from app.v1.utils.db import engine
from app.v1.model.base import Base
from app.v1.modules.user.router import router as user_router
from app.v1.modules.product.router import router as product_router

app = FastAPI()

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(product_router, prefix="/api/v1/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API escalable de FastAPI"}




