from src.jogador import *
from src.peao import *

def main():
    jogador = Jogador()
    peao = Peao()
    cores_disponiveis = peao.cores_disponiveis()
    numero_de_jogadores = 4
    id = 0
    while id < numero_de_jogadores:
        cor, nome = jogador.cadastra_jogador(cores_disponiveis)
        if type(cor) == str:
            peao.remove_cor(cor)
            jogador.armazena_jogador(id, nome, cor)
            id += 1

main()