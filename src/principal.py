from src.jogador import *
from src.peao import *
from src.Tabuleiro import *
import tkinter as tk


def main():
    #Criando e cadastrando peoes:
    criarPeoes()

    #Criando e cadastrando jogadores
    cores = coresDisponiveis()
    numeroDeJogadores = 4
    id = 0
    while id < numeroDeJogadores:
        cor, nome = cadastraJogador(cores)
        if type(cor) == str:
            removeCor(cor)
            armazenaJogador(id, nome, cor)
            id += 1

    # criar tabuleiro
    criarTabuleiro()

    # mover tabuleiro
    #moverTabuleiro()
    #moverTabuleiro()

    root.mainloop()

main()
