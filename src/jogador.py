from src.excecoes import *
from src.mensagem import *
from db import base

class Jogador:
    def __init__(self):
        pass

    def cadastra_jogadores(self, cores_disponiveis):
        indice_cor = 0
        nome = input(SOLICITA_NOME)
        print("%s, escolha o seu peão:"%nome)

        #exibe cores dispiveis
        for cor in cores_disponiveis:
            print('%d para escolher o peão %s.' % (indice_cor + 1, cor))
            indice_cor += 1

        #captura escolha válida do usuario para a cor do peão
        while True:
            try:
                escolha = int(input('Digite a sua escolha: '))

                if 1 > escolha or escolha > len(cores_disponiveis):
                    raise InputError(f'Escolha inválida!\n'
                                     f'Escolha um numero entre 1 e {len(cores_disponiveis)}\n')
                print("Jogador cadastrado com sucesso!\n")
                return cores_disponiveis[escolha-1], nome

            except ValueError:
                print(ALERTA_SO_NUMEROS)
                return 1, 'error'

            except InputError as ex:
                print(ex)
                return 2, 'error'

    def armazena_jogador(self, id, nome, cor_peao):
        base.jogadores_cadastrados[id] = nome, cor_peao