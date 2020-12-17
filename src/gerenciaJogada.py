from db import base
from db.dominioTabelas import Session, atualizarBD, Peao, Jogador
from src.tabuleiro import removerPeaoDoJogador
from src.parteGrafica import valorDado
from src.dado import rolarDado

#ordena os jogadores
def ordemJogador(resultadoRolagemDados):
    resultadoRolagemDados.sort(reverse=True)
    ordem = []
    for maior in resultadoRolagemDados:
        ordem.append(maior[1])
    return ordem


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
        if posicao[0] > 72:
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
        return 0
    return 1

#chama próximo jogador
def chamarProximoJogador(idJogador, ordem):
    for i in range(len(ordem)):
        if ordem[i] == idJogador:
            if i == len(ordem) - 1:
                return ordem[0]
            else:
                return ordem[i + 1]
    return -1


def Sorteio(numPartida):
    session = Session()
    jogadores = session.query(Jogador).filter(Jogador.numpartida == numPartida).all()
    listaJogadoresNumero = []
    for i,jogador in enumerate(jogadores):
        dado = rolarDado()
        listaJogadoresNumero.append((dado,jogador.codigo))
    return listaJogadoresNumero