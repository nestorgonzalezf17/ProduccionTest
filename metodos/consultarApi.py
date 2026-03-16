from sqlalchemy import Column, Integer, String
from database import Base
from fastapi import APIRouter, Query, Depends, status
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from modelos import model_producto
from fastapi import HTTPException
from esquemas import eschemas



router = APIRouter()
@router.get("/")
async def consultar():
    return "Consultar Alumnos del Programa...."

@router.get("/prod_all")
def get_users(db: Session = Depends(get_db)):
    # Ejemplo: obtener todos los usuarios
    producto = db.query(model_producto.Producto).all()
    return producto

@router.get("/prod/{prodId}")
def get_id(prodId : int, db: Session = Depends(get_db)):
    # Ejemplo: obtener un solo usuario
    producto=db.query(model_producto.Producto).filter(model_producto.Producto.id_prod == prodId).first()
    if (producto):
        return producto
    return "Producto no existe.... "

@router.get("/produc/{prodId}")
def get_id(prodId : int, db: Session = Depends(get_db)):
    # Ejemplo: obtener un solo usuario
    producto=db.query(model_producto.Producto).get(prodId)
    if (producto):
        return producto
    else:
        raise HTTPException(status_code=404, detail=f"Tarea con id {prodId} no encontrada")
    

## Ingresar un producto
@router.post("/add", response_model=eschemas.Producto, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: eschemas.Producto, sesion: Session = Depends(get_db)):
    productoAdd = model_producto.Producto(
        id_prod= producto.id_prod,
        nombre= producto.nombre,
        provedor= producto.provedor,
        )
    sesion.add(productoAdd)
    sesion.commit()
    sesion.refresh(productoAdd)
    return productoAdd