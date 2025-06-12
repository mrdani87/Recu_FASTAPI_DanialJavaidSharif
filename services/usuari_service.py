from sqlmodel import Session
from models.usuari import Usuari

def afegir_usuari(db: Session, usuari: Usuari):
    db.add(usuari)
    db.commit()
    db.refresh(usuari)
    return usuari

def obtenir_usuari_per_id(db: Session, usuari_id: int):
    return db.get(Usuari, usuari_id)