from pydantic import BaseModel
from typing import Optional
# Esquema completo Taea (Modelo Pydantic)
class Producto(BaseModel):
    id_prod: Optional[int]
    nombre: str
    provedor: str
    
    class Config:
        orm_mode = True 