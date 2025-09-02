from sqlalchemy import Column, Integer, String, Float
from database import base

class Filme(base):
    __tablename__ = 'filmes'

    id_filme = Column(Integer, primary_key=True,index=True,autoincrement=True)
    titulo  = Column(String(255), index=True)
    genero = Column(String(100), index=True)
    ano = Column(Integer)
    nota_imdb = Column(Float)
    