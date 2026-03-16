from sqlalchemy import Column, Integer, String
from database import Base



class Producto(Base):
    __tablename__ = "productos"
    id_prod = Column(Integer, primary_key = True, index = True )
    nombre = Column(String(50))
    provedor = Column(String(50))

class Provedor(Base):
    __tablename__ = "provedor"
    Id_prov = Column(Integer, primary_key = True, index = True)
    nombre = Column(String(50))
    email = Column(String(50))