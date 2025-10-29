# crud.py
from sqlalchemy.orm import Session
import models, schemas
from typing import List, Optional
from sqlalchemy import func

def create_bug(db: Session, bug_in: schemas.BugCreate) -> models.Bug:
    bug = models.Bug(
        titulo=bug_in.titulo,
        descricao=bug_in.descricao,
        projeto=bug_in.projeto,
        prioridade=bug_in.prioridade,
        status=bug_in.status,
        responsavel=bug_in.responsavel,
    )
    db.add(bug)
    db.commit()
    db.refresh(bug)
    return bug

def get_bug(db: Session, bug_id: int) -> Optional[models.Bug]:
    return db.query(models.Bug).filter(models.Bug.id == bug_id).first()

def list_bugs(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = None,
    prioridade: Optional[str] = None,
    projeto: Optional[str] = None,
    responsavel: Optional[str] = None,
    q: Optional[str] = None,
) -> List[models.Bug]:
    query = db.query(models.Bug)
    if status:
        query = query.filter(models.Bug.status == status)
    if prioridade:
        query = query.filter(models.Bug.prioridade == prioridade)
    if projeto:
        query = query.filter(models.Bug.projeto.ilike(f"%{projeto}%"))
    if responsavel:
        query = query.filter(models.Bug.responsavel.ilike(f"%{responsavel}%"))
    if q:
        qterm = f"%{q}%"
        query = query.filter(
            (models.Bug.titulo.ilike(qterm)) | (models.Bug.descricao.ilike(qterm))
        )
    return query.order_by(models.Bug.id.desc()).offset(skip).limit(limit).all()

def update_bug(db: Session, bug: models.Bug, bug_in: schemas.BugUpdate) -> models.Bug:
    for field, value in bug_in.dict(exclude_unset=True).items():
        setattr(bug, field, value)
    db.add(bug)
    db.commit()
    db.refresh(bug)
    return bug

def delete_bug(db: Session, bug: models.Bug) -> None:
    db.delete(bug)
    db.commit()

def count_by_status(db: Session):
    return db.query(models.Bug.status, func.count(models.Bug.id)).group_by(models.Bug.status).all()
