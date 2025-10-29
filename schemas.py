# schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import enum

class PriorityEnum(str, enum.Enum):
    baixa = "Baixa"
    media = "Média"
    alta = "Alta"
    critica = "Crítica"

class StatusEnum(str, enum.Enum):
    aberto = "Aberto"
    andamento = "Em andamento"
    resolvido = "Resolvido"
    fechado = "Fechado"

class BugBase(BaseModel):
    titulo: str = Field(..., max_length=200)
    descricao: Optional[str] = None
    projeto: Optional[str] = None
    prioridade: Optional[PriorityEnum] = PriorityEnum.media
    status: Optional[StatusEnum] = StatusEnum.aberto
    responsavel: Optional[str] = None

class BugCreate(BugBase):
    pass

class BugUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=200)
    descricao: Optional[str] = None
    projeto: Optional[str] = None
    prioridade: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None
    responsavel: Optional[str] = None

class BugOut(BugBase):
    id: int
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        orm_mode = True
