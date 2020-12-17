from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, and_, func
from db.base import Base, db_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

Base.metadata.create_all(db_engine)
Session = scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))


class Jogador(Base):
    __tablename__ = 'jogador'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String)
    corpeao = Column(String)
    vencedor = Column(BOOLEAN, default=False)
    numpartida = Column(Integer)

class Peao(Base):
    __tablename__ = 'peao'

    codigo = Column(Integer, primary_key=True)
    cor = Column(String)
    posicao = Column(Integer)
    nojogo = Column(BOOLEAN, default=True)


class Tabuleiro(Base):
    __tablename__ = 'tabuleiro'

    casa = Column(Integer, primary_key=True)
    statuscasa = Column(BOOLEAN, default=False)     # false para vazia e true quando ocupada.
    tabstate = Column(Integer, default=0)           # +1 = + 90º horário

class Partida(Base):
    __tablename__ = 'partida'

    codigo = Column(Integer, primary_key=True)
    nomevencedor = Column(String, default=None)
    codigovencedor = Column(Integer, default=None)
    participantes = Column(String)

def atualizarBD():
    session = Session()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()