from fastapi import FastAPI, Depends

from AppDB.metodos import consultarApi

app = FastAPI()
app.include_router(consultarApi.router, prefix="/productos")