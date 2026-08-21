from database import Base, engine
from sqlalchemy.orm import Session
from models import Usuario, Usuario_Preferencia, Alimento
from dependencies import create_session


#Base.metadata.create_all(bind=engine)

def create_user(session: Session):
    usuario = session.query(Usuario).filter_by(email='pedroluna@gmail.com').first()

    if usuario:
        print("Usuario com email já existente, tente outro email.")

    else:
        novo_usuario = Usuario(nome="Pedro Luna", email="pedroluna@gmail.com", senha="1234", idade=21)

        session.add(novo_usuario)
        session.commit()

        session.refresh(novo_usuario)

        print(f"Usuário {novo_usuario.id} criado com sucesso!")

    total_usuarios = session.query(Usuario).all()
    print(f"Usuários no banco: {total_usuarios}")


if __name__ == "__main__":
    create_user(next(create_session()))





