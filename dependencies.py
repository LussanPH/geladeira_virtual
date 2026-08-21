from sqlalchemy.orm import Session, sessionmaker
from database import engine

def create_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()

        yield session

    finally:
        session.close()
