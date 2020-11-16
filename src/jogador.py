from src.excecoes import InputError
from src.mensagem import *
from db.dominioTabelas import Session, atualizarBD, Jogador


def cadastraJogador(coresDisponiveis):
    indiceCor = 0
    repete = True
    excecao = InputError()

    # gera codigo do jogador
    codigo = excecao.gerarCodigoJogador()

    # captura nome válido do usuário
    while repete:
        nome = input(SOLICITA_NOME).strip()
        if excecao.validaNome(nome) == 0:
            repete = False

    print("%s, escolha o seu peão:" % nome)

    # exibe cores dispiveis
    for cor in coresDisponiveis:
        print('%d para escolher o peão %s.' % (indiceCor + 1, cor))
        indiceCor += 1

    # captura escolha válida do usuario para a cor do peão
    while True:
        escolha = input('Digite a sua escolha: ')
        status = excecao.validaNumeroInteiro(escolha)
        if status == 0:
            escolha = int(escolha)
            status = excecao.validaIntervalo(escolha, 1, len(coresDisponiveis))
            if status == 0:
                cor = coresDisponiveis[escolha-1]
                return cor, nome, codigo


def armazenaJogador(codigo, nome, corPeao):
    try:
        session = Session()
        jogador = Jogador(codigo=codigo, nome=nome, corpeao=corPeao)
        session.add(jogador)
        atualizarBD()
        return 0
    except:
        return 1
