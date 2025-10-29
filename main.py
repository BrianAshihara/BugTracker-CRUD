# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import engine, Base, SessionLocal
import models
from routes import bugs
from sqlalchemy.orm import Session
import crud, schemas
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="BugTrack - CRUD focused bug tracker")

# create tables
Base.metadata.create_all(bind=engine)



# Rota principal redireciona para a página do app
@app.get("/", response_class=FileResponse)
async def root():
    return Path("index/index.html")

# Mantém arquivos estáticos funcionando (CSS, JS, imagens, etc.)
app.mount("/static", StaticFiles(directory="index"), name="static")


# include API router
app.include_router(bugs.router)

# optional seed data if empty
def seed_if_empty():
    db: Session = SessionLocal()
    try:
        count = db.query(models.Bug).count()
        if count == 0:
            sample = [
                schemas.BugCreate(
                    titulo="Erro ao salvar configuração",
                    descricao="Ao salvar as configurações, ocorre timeout.",
                    projeto="Painel Admin",
                    prioridade=schemas.PriorityEnum.alta,
                    status=schemas.StatusEnum.aberto,
                    responsavel="Mariana"
                ),
                schemas.BugCreate(
                    titulo="Layout quebrado no mobile",
                    descricao="Menu sobrepondo conteúdo em iPhone SE.",
                    projeto="Site Institucional",
                    prioridade=schemas.PriorityEnum.media,
                    status=schemas.StatusEnum.andamento,
                    responsavel="Pedro"
                ),
            ]
            for s in sample:
                crud.create_bug(db, s)
    finally:
        db.close()

seed_if_empty()
