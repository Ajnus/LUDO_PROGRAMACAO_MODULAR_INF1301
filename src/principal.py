from src.jogador import *
from src.peao import *
from src.Tabuleiro import *
import tkinter as tk


def main():
    session = Session()
    # Criando e cadastrando peoes:
    if len(session.query(Peao.codigo).all()) < 16:
        criarPeoes()

    # Criando e cadastrando jogadores
    cores = coresDisponiveis()
    numeroDeJogadores = 4
    jogadoresCadastrados = 0
    while jogadoresCadastrados < numeroDeJogadores:
        cor, nome, codigo = cadastraJogador(cores)
        if type(cor) == str:
            removeCor(cor)
            armazenaJogador(codigo, nome, cor)
            jogadoresCadastrados += 1

    # criar tabuleiro
    #criarTabuleiro()

    # mover tabuleiro
    #moverTabuleiro()
    #moverTabuleiro()

    #root.mainloop()


main()
