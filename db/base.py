from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
#                                                username:senha@host:port/database
db_engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/INF1301')
Base = declarative_base()
Base.metadata.bind = db_engine

peoesCoresDisponiveis = ['Amarelo', 'Azul', 'Verde', 'Vermelho']
