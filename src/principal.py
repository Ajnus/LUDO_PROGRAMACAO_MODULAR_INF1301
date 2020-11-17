from src.jogador import *
from src.peao import *
from src.tabuleiro import *
import tkinter as tk


def main():

    session = Session()

    #Criando tabuleiro
    if len(session.query(Tabuleiro.casa).all()) < 76:
        criarCasasTabuleiro()

    #Criando e cadastrando peoes:
    if len(session.query(Peao.codigo).all()) < 16:
        criarPeoes()

    #Criando e cadastrando jogadores
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
