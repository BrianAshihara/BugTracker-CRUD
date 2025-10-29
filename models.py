# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import Enum as SQLAEnum
from datetime import datetime
from database import Base
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

class Bug(Base):
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descricao = Column(Text, nullable=True)
    projeto = Column(String(100), nullable=True)
    prioridade = Column(SQLAEnum(PriorityEnum), default=PriorityEnum.media)
    status = Column(SQLAEnum(StatusEnum), default=StatusEnum.aberto)
    responsavel = Column(String(100), nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
