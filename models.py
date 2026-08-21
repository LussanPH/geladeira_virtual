from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import List



class Usuario(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    idade: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String(30), nullable=False)
    preferencias: Mapped[List['Usuario_Preferencia']] = relationship(back_populates='usuario')
    alimentos_armazenados: Mapped[List['Alimento']] = relationship(back_populates='usuario')

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome={self.nome}, idade={self.idade}, email={self.email}, senha={self.senha})>"


class Usuario_Preferencia(Base):
    __tablename__ = "Usuario_Preferencias"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    restricoes: Mapped[str] = mapped_column(String(100), nullable=False)
    preferidos: Mapped[int] = mapped_column(String(100), nullable=False)
    rejeitados: Mapped[str] = mapped_column(String(100), nullable=False)
    fk_id_usuario: Mapped[int] = mapped_column(ForeignKey(Usuario.id), nullable=False)
    usuario: Mapped['Usuario'] = relationship(back_populates='preferencias')

    
    def __repr__(self):
        return f"<Usuario(id={self.id}, nome={self.nome}, idade={self.idade}, email={self.email}, senha={self.senha})>"


class Alimento(Base):
    __tablename__ = "Alimentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    categoria: Mapped[str] = mapped_column(String(15), unique=True)
    quantidade: Mapped[int] = mapped_column(nullable=False)
    fk_id_usuario: Mapped[int] = mapped_column(ForeignKey(Usuario.id), nullable=False)
    usuario: Mapped['Usuario'] = relationship(back_populates="alimentos_armazenados")