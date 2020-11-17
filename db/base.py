from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
#                                                username:senha@host:port/database
db_engine = create_engine('postgresql+psycopg2://postgres:hamster@localhost:5432/qualquer4')
Base = declarative_base()
Base.metadata.bind = db_engine

peoesCoresDisponiveis = ['Amarelo', 'Azul', 'Verde', 'Vermelho']
