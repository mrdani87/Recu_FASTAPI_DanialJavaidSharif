from sqlmodel import SQLModel, Field

class Usuari(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    email: str
    telefon: str
    ciutat: str
    edat: int