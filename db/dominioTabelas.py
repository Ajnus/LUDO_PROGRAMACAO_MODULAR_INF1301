from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, and_, func
from sqlalchemy.orm import relationship
from db.base import Base, db_engine
from sqlalchemy.orm import sessionmaker, scoped_session

Base.metadata.create_all(db_engine)
Session = scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))

class Jogador(Base):
    __tablename__ = 'jogador'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String)
    corpeao = Column(String)

class Peao(Base):
    __tablename__ = 'peao'

    codigo = Column(Integer, primary_key=True)
    cor = Column(String)
    posicao = Column(Integer)

class Tabuleiro(Base):
    __tablename__ = 'tabuleiro'

    casa = Column(Integer, primary_key=True)
    status = Column(BOOLEAN, default=False) #false para vazia e true quando ocupada.


def atualizarBD():
    session = Session()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

