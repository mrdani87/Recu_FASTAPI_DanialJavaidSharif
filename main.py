from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from services.usuari_service import afegir_usuari

app = FastAPI()

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
   db = Session(engine)
   try:
       yield db
   finally:
       db.close()

@app.post("/usuaris")
def crear_usuari(usuari: Usuari, db: Session = Depends(get_db)):
    return afegir_usuari(db, usuari)