from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductBase(BaseModel):
    codigo: str
    codigoS: str
    detalle: str
    um: str
    pventa: float
    vreferencial: float
    igv: float
    isc: float
    ivap: float
    rc: float
    percepcion: float
    perfil: str
    usuario: str
    estado: str
    valuacion: str
    tipafeigv: str
    ctributo: str
    moneda: str
    anexo: str
    serie: str
    icbper: str
    codigoproveedor: str
    categoria: str
    etiqueta: str
    stock: str
    idfacturalo: str
    bnormalizado: str
    umC65: str
    parancelaria: str
    gtin: str
    fstock: date
    imagen: Optional[str] = None  # Base64 opcional

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    codigo: Optional[str] = None
    codigoS: Optional[str] = None
    detalle: Optional[str] = None
    um: Optional[str] = None
    pventa: Optional[float] = None
    vreferencial: Optional[float] = None
    igv: Optional[float] = None
    isc: Optional[float] = None
    ivap: Optional[float] = None
    rc: Optional[float] = None
    percepcion: Optional[float] = None
    perfil: Optional[str] = None
    usuario: Optional[str] = None
    estado: Optional[str] = None
    valuacion: Optional[str] = None
    tipafeigv: Optional[str] = None
    ctributo: Optional[str] = None
    moneda: Optional[str] = None
    anexo: Optional[str] = None
    serie: Optional[str] = None
    icbper: Optional[str] = None
    codigoproveedor: Optional[str] = None
    categoria: Optional[str] = None
    etiqueta: Optional[str] = None
    stock: Optional[str] = None
    idfacturalo: Optional[str] = None
    bnormalizado: Optional[str] = None
    umC65: Optional[str] = None
    parancelaria: Optional[str] = None
    gtin: Optional[str] = None
    fstock: Optional[date] = None
    imagen: Optional[str] = None

class ProductOut(ProductBase):
    id: int
    class Config:
        from_attributes = True