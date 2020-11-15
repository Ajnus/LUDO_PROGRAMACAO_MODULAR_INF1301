from db import base
from db.dominioTabelas import Session, atualizarBD, Peao, Jogador
from src.Tabuleiro import removerPeaoDoJogador

def definirPrimeiroJogador(resultadoRolagemDado):
    id = maior = 0
    numeroSorteado = 1
    primeiroJogador = -1
    empate = []

    for jogador in resultadoRolagemDado:
        if jogador[numeroSorteado] > maior:
            maior = jogador[numeroSorteado]
            primeiroJogador = jogador[id]
            empate = []

        elif jogador[numeroSorteado] == maior:
            maior = jogador[numeroSorteado]
            if primeiroJogador not in empate:
                empate.append(primeiroJogador)
            empate.append(jogador[id])

    if len(empate) != 0:
        return empate
    return primeiroJogador

# Remove o jogador
def removerJogador(idJogador):
    session = Session()
    try:
        jogadorCodigo = session.query(Jogador).filter_by(codigo=idJogador).one()
        session.delete(jogadorCodigo)
        atualizarBD()
        return 1
    except:
        peaoCodigo = 0
        return 0

# define o vencedor
def defineVencedor():
    idVencedor = -1
    nomeVencedor = ''
    i = 0
    j = 0
    session = Session()
    try:
        peaoPosicao = session.query(Peao.posicao).all()
        idPeao = session.query(Peao.codigo).all()
        jogadorId = session.query(Jogador.codigo).all()
        jogadorNome = session.query(Jogador.nome).all()
    except:
        peaoPosicao = -1
        idPeao = -1
        jogadorId = -1

    for posicao in peaoPosicao:
        if posicao[0] >= 57:
            removerPeaoDoJogador(idPeao[i][0])
            atualizarBD()
        i+=1

    try:
        corJogador = session.query(Jogador.corpeao).all()
        corPeao = session.query(Peao.cor).all()
    except:
        corJogador = 0
        corPeao = 0

    for jogadorCor in corJogador:
        if jogadorCor not in corPeao:
            idVencedor = jogadorId[j][0]
            nomeVencedor = jogadorNome[j][0]
            atualizarBD()
            return idVencedor, nomeVencedor
        j+=1
    return (-1, -1)

# verifica vencedor
def verificarVencedor(idJogador):
    vencedor = defineVencedor()
    if idJogador == vencedor[0]:
        print(vencedor[1])
        #removerJogador(idJogador)
        return 1
    return 0
