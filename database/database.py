# Importar librerías para la configuración de la base de datos
from sqlalchemy import Column, DateTime, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Importar librerías para cargar variables de entorno
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)
FASTAPI_DB_HOST = os.getenv('FASTAPI_DB_HOST')
FASTAPI_DB_USER = os.getenv('FASTAPI_DB_USER')
FASTAPI_DB_PASSWORD = os.getenv('FASTAPI_DB_PASSWORD')
FASTAPI_DB_NAME = os.getenv('FASTAPI_DB_NAME')
FASTAPI_DB_PORT = os.getenv('FASTAPI_DB_PORT')
FASTAPI_DB_SERVER = os.getenv('FASTAPI_DB_SERVER')

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = f"{FASTAPI_DB_HOST}+pymysql://{FASTAPI_DB_USER}:{FASTAPI_DB_PASSWORD}@{FASTAPI_DB_SERVER}:{FASTAPI_DB_PORT}/{FASTAPI_DB_NAME}"
print(SQLALCHEMY_DATABASE_URL)

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Crear una sesión de base de datos mariadb
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

"""
Este archivo contiene la configuración de la base de datos para el proyecto FastAPI Finance Corporation.
Se utiliza SQLAlchemy para crear el motor de la base de datos y declarative_base para definir la base de datos.
También se utiliza sessionmaker para crear una sesión de base de datos y se carga la configuración de la base de datos desde un archivo .env.
"""


def timestamp():
    return Column(DateTime, server_default=func.now(), onupdate=func.now())
