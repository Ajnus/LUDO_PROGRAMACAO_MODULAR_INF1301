from db.dominioTabelas import Session, atualizarBD, Partida, Jogador
from src.excecoes import InputError

def criaPartida():
    excecao = InputError()
    codigo = excecao.gerarCodigoPartida()
    return codigo


def armazenaPartida(codigo, nomevencedor=None, codigovencedor=None):
    try:
        session = Session()
        i = 0
        listaNomeJogadores = session.query(Jogador).filter(Jogador.numpartida == codigo).all()
        participante = ''
        while i < 4:
            if i < 3:
                participante += listaNomeJogadores[i].nome + ','
                i += 1
            else:
                participante += listaNomeJogadores[i].nome
                i += 1
        partida = Partida(codigo=codigo, nomevencedor=nomevencedor, codigovencedor=codigovencedor, participantes=participante)
        session.add(partida)
        atualizarBD()
        return 0
    except:
        return 1
