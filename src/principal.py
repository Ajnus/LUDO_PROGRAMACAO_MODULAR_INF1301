from src.jogador import *
from src.peao import *

def main():
    jogador = Jogador()
    peao = Peao()
    coresDisponiveis = peao.coresDisponiveis()
    numeroDeJogadores = 4
    id = 0
    while id < numeroDeJogadores:
        cor, nome = jogador.cadastraJogador(coresDisponiveis)
        if type(cor) == str:
            peao.removeCor(cor)
            jogador.armazenaJogador(id, nome, cor)
            id += 1

main()