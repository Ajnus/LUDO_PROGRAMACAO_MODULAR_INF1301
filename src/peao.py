from db import base
from src.excecoes import InputError
from db.dominioTabelas import Session, atualizarBD, Peao

def criarPeoes():
    excecao = InputError()
    cores = base.peoesCoresDisponiveis
    posicao = 0
    for cor in cores:
        for i in range(4):
            codigo = excecao.gerarCodigoPeao()
            armazenaPeao(codigo, cor, posicao)

def armazenaPeao(codigo, corPeao, posicao):
    try:
        session = Session()
        peao = Peao(codigo=codigo, cor=corPeao, posicao=posicao)
        session.add(peao)
        atualizarBD()
        return 0
    except:
        return 1

def coresDisponiveis():
    cores = base.peoesCoresDisponiveis
    return cores

def removeCor(cor):
    cores = base.peoesCoresDisponiveis
    cores.remove(cor)
    base.peoesCoresDisponiveis = cores
