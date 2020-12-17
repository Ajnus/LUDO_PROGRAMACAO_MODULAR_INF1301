from db.dominioTabelas import *

# Define todas as casas passáveis
def definirStatusCasa(posicao):
    if posicao < 57: #casas passáveis
        return 0
    if posicao == 57: # casa final
        return 1
    else:
        return 2

# Remove o peão do jogador
def removerPeaoDoJogador(idPeao):
    session = Session()
    try:
        session.query(Peao).filter_by(codigo = idPeao).one()
        session.query(Peao).filter_by(codigo = idPeao).update({'nojogo': False})
        atualizarBD()
        return 0
    except:
        return 1

# Move o peão para base
def moverParaBase(idPeao):
    session = Session()
    try:
        peao = session.query(Peao).filter(Peao.codigo==idPeao).one()
        session.query(Peao).filter(Peao.codigo==idPeao).update({'posicao':0})
        atualizarBD()
        return 0
    except:
        return 1

def criarCasasTabuleiro():
    session = Session()
    for casa in range(1, 93):
        tabuleiro = Tabuleiro(casa=casa)
        session.add(tabuleiro)
        atualizarBD()


def armazenaStatusCasaTabState(casa, statusCasa, tabState):
    try:
        session = Session()
        statusState = Tabuleiro(casa=casa, statuscasa=statusCasa, tabstate=tabState)
        session.add(statusState)
        atualizarBD()
        return 0
    except:
        return 1


def alteraStatusCasa(idCasa):
    try:
        session = Session()
        statusCasaAtual = session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).one()
        if statusCasaAtual.statuscasa == False:
            session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).update({'statuscasa': True})
        else:
            session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).update({'statuscasa': False})
        atualizarBD()
        return 0
    except:
        return 1


def verificarStatusCasa(idCasa):
    try:
        session = Session()
        casa = session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).one()
        return casa.statuscasa
    except:
        return 1


# Mover Peão
def moverPeao(idPeao, valorDado):
    session = Session()
    try:
        posPeao = session.query(Peao).filter_by(codigo=idPeao).one()
        posPeao.posicao += valorDado
        atualizarBD()
        return 0
    except:
        posPeao = -1
        return 1


# Sair da Base
def sairBase(idPeao):
    session = Session()
    try:
        posPeao = session.query(Peao).filter_by(codigo=idPeao).one()
        posPeao.posicao = 1
        atualizarBD()
        return 0
    except:
        posPeao = -1
        return 1

