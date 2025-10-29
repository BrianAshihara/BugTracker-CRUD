# routes/bugs.py
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
import schemas, crud, models
from database import SessionLocal
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/bugs", tags=["bugs"])

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BugOut, status_code=201)
def create_bug(bug_in: schemas.BugCreate, db: Session = Depends(get_db)):
    return crud.create_bug(db, bug_in)

@router.get("/", response_model=List[schemas.BugOut])
def read_bugs(
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = Query(None),
    prioridade: Optional[str] = Query(None),
    projeto: Optional[str] = Query(None),
    responsavel: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    return crud.list_bugs(db, skip, limit, status, prioridade, projeto, responsavel, q)

@router.get("/counts")
def get_counts(db: Session = Depends(get_db)):
    counts = crud.count_by_status(db)
    return JSONResponse(content={status.value: count for status, count in counts})

@router.get("/{bug_id}", response_model=schemas.BugOut)
def read_bug(bug_id: int, db: Session = Depends(get_db)):
    bug = crud.get_bug(db, bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return bug

@router.put("/{bug_id}", response_model=schemas.BugOut)
def update_bug(bug_id: int, bug_in: schemas.BugUpdate, db: Session = Depends(get_db)):
    bug = crud.get_bug(db, bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return crud.update_bug(db, bug, bug_in)

@router.delete("/{bug_id}", status_code=204)
def delete_bug(bug_id: int, db: Session = Depends(get_db)):
    bug = crud.get_bug(db, bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    crud.delete_bug(db, bug)
    return
