from pydantic import BaseModel


class filmeBase (BaseModel):
    titulo: str
    genero: str
    ano: int
    nota_imdb: float

class FilmeCreate(filmeBase):
    pass

class Filme(filmeBase):
    id_filme:int
    class Config:
        orm_mode = True
