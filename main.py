from typing import Union

from fastapi import FastAPI

# Archivos locales ---------------

# Database

from database.database import Base, engine

# Importar todos los modelos
from models import users, devolution, equipment, materials, roles

# -----------------------------


# Body --------------------------------------

# Corriendo el motor DB --------------
from sqlalchemy.exc import SQLAlchemyError

try:
    print("Creando tablas en la base de datos...")
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")
    print(Base.metadata.tables.keys())  # 🔎 Esto mostrará las tablas detectadas

except SQLAlchemyError as e:
    print(f"Error al crear tablas: {e}")
# -----------------------------------

app = FastAPI()

app.title = 'Almacen telecable'
app.version = '1.0.1'


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
