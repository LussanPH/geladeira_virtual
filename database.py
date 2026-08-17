from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+psycopg2://admin:senha1234@localhost:5432/geladeira_db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass