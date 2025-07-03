from sqlalchemy import Column, Integer, String, Float, Date, Text
from app.v1.model.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String)
    codigoS = Column(String)
    detalle = Column(String)
    um = Column(String)
    pventa = Column(Float)
    vreferencial = Column(Float)
    igv = Column(Float)
    isc = Column(Float)
    ivap = Column(Float)
    rc = Column(Float)
    percepcion = Column(Float)
    perfil = Column(String)
    usuario = Column(String)
    estado = Column(String)
    valuacion = Column(String)
    tipafeigv = Column(String)
    ctributo = Column(String)
    moneda = Column(String)
    anexo = Column(String)
    serie = Column(String)
    imagen = Column(Text, nullable=True)  # Imagen en base64
    icbper = Column(String)
    codigoproveedor = Column(String)
    categoria = Column(String)
    etiqueta = Column(String)
    stock = Column(String)
    idfacturalo = Column(String)
    bnormalizado = Column(String)
    umC65 = Column(String)
    parancelaria = Column(String)
    gtin = Column(String)
    fstock = Column(Date)