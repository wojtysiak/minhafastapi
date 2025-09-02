from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List,Optional
from database import sessionlocal, engine, base


import models,schemas
from database import sessionlocal,engine

base.metadata.create_all(bind=engine)


app = FastAPI(title='Api de catalogo de filmes')

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return{'mensagem ':'bem vindo api filmes :~)'}


@app.post("/filmes",response_model=schemas.Filme)
def criar_filme(filme:schemas.FilmeCreate,db:Session=Depends(get_db)):
    novo_filme = models.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme