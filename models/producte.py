from sqlmodel import SQLModel, Field

class Producte(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    descripcio: str
    preu: float
    en_stock: bool
    categoria: str
    fabricant: str