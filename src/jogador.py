from src.excecoes import InputError
from src.mensagem import *
from db import base

class Jogador:
    def __init__(self):
        pass

    def cadastraJogador(self, coresDisponiveis):
        indiceCor = 0
        repete = True
        excecao = InputError()

        #captura nome válido do usuário
        while repete:
            nome = input(SOLICITA_NOME).strip()
            if excecao.validaNome(nome) == 0:
                repete = False

        print("%s, escolha o seu peão:"%nome)

        #exibe cores dispiveis
        for cor in coresDisponiveis:
            print('%d para escolher o peão %s.' % (indiceCor + 1, cor))
            indiceCor += 1

        #captura escolha válida do usuario para a cor do peão
        while True:
            escolha = input('Digite a sua escolha: ')
            status = excecao.validaNumeroInteiro(escolha)
            if status == 0:
                escolha = int(escolha)
                status = excecao.validaIntervalo(escolha, 1, len(coresDisponiveis))
                if status == 0:
                    cor = coresDisponiveis[escolha-1]
                    print("Jogador cadastrado com sucesso!\n")
                    return cor, nome

    def armazenaJogador(self, id, nome, cor_peao):
        base.jogadoresCadastrados[id] = nome, cor_peao