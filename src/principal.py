from src.jogador import *
from src.peao import *
from src.partida import *
from src.tabuleiro import *
import tkinter as tk
from db.dominioTabelas import Session
from db.dominioTabelas import Partida


def main():

    session = Session()

    # Criando a partida
    numPartida = criaPartida()



    #Criando e cadastrando peoes:
    if len(session.query(Peao.codigo).all()) < 16:
        print(criarPeoes())

    #Criando e cadastrando jogadores
    cores = coresDisponiveis()
    numeroDeJogadores = 4
    jogadoresCadastrados = 0
    while jogadoresCadastrados < numeroDeJogadores:
        cor, nome, codigo = cadastraJogador(cores)
        if type(cor) == str:
            removeCor(cor)
            armazenaJogador(codigo=codigo, nome=nome, corPeao=cor, numpartida=numPartida)
            jogadoresCadastrados += 1

    armazenaPartida(numPartida)


    #Criando tabuleiro
    if len(session.query(Tabuleiro.casa).all()) < 76:
        criarCasasTabuleiro()

    # criar tabuleiro
    #criarTabuleiro()

    # mover tabuleiro
    #moverTabuleiro()
    #moverTabuleiro()

    #root.mainloop()



main()
