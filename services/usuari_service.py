from sqlmodel import Session
from models.usuari import Usuari

def afegir_usuari(db: Session, usuari: Usuari):
    db.add(usuari)
    db.commit()
    db.refresh(usuari)
    return usuari