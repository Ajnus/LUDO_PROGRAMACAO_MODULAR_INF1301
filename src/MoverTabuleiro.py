import tkinter as tk
from PIL import Image
#import Tabuleiro
from Tabuleiro import tabState
from Tabuleiro import Tabuleiro
from Tabuleiro import centroPath

def moverTabuleiro():
    global tabState
    global topLeft
    global topRight
    global botRight
    global botLeft

    global cLeft
    global cTop
    global cRight
    global cBot

    global sLeft
    global sTop
    global sRight
    global sBot

    global ImgCentro

    global sLeftPath
    global sTopPath
    global sRightPath
    global sBotPath

    # altera estado do tabuleiro
    tabState += 1
    if (tabState > 3):
        tabState = 0

    # rotaciona imagem centro (cria nova imagem rotacionada a partir da original, mantendo o uso da tkInter)
    ImgCentroR = Image.open(centroPath)
    ImgCentroR = ImgCentroR.rotate(-90*tabState)
    ImgCentroR.save("Imagens\\centroR.gif")
    ImgCentro = tk.PhotoImage(file="Imagens\\centroR.gif")

    # SUBSTITUI posição das bases e casas coloridas
    if tabState == 0:   # amarelo joga
        topLeft = tk.PhotoImage(file="Imagens\\baseverde.gif")
        topRight = tk.PhotoImage(file="Imagens\\basevermelho.gif")
        botRight = tk.PhotoImage(file="Imagens\\baseazul.gif")
        botLeft = tk.PhotoImage(file="Imagens\\baseamarelo.gif")

        cLeft = tk.PhotoImage(file="Imagens\\caixaverde.gif")
        cTop = tk.PhotoImage(file="Imagens\\caixavermelho.gif")
        cRight = tk.PhotoImage(file="Imagens\\caixaazul.gif")
        cBot = tk.PhotoImage(file="Imagens\\caixaamarelo.gif")

        sLeftPath = "Imagens\\paradaverde.gif"
        sTopPath  = "Imagens\\paradavermelho.gif"
        sRightPath = "Imagens\\paradaazul.gif"
        sBotPath = "Imagens\\paradaamarelo.gif"

    if tabState == 1:   # azul joga
        topLeft = tk.PhotoImage(file="Imagens\\baseamarelo.gif")
        topRight = tk.PhotoImage(file="Imagens\\baseverde.gif")
        botRight = tk.PhotoImage(file="Imagens\\basevermelho.gif")
        botLeft = tk.PhotoImage(file="Imagens\\baseazul.gif")

        cLeft = tk.PhotoImage(file="Imagens\\caixaamarelo.gif")
        cTop = tk.PhotoImage(file="Imagens\\caixaverde.gif")
        cRight = tk.PhotoImage(file="Imagens\\caixavermelho.gif")
        cBot = tk.PhotoImage(file="Imagens\\caixaazul.gif")

        sLeftPath = "Imagens\\paradaamarelo.gif"
        sTopPath  = "Imagens\\paradaverde.gif"
        sRightPath = "Imagens\\paradavermelho.gif"
        sBotPath = "Imagens\\paradaazul.gif"

    elif tabState == 2:   # vermelho joga
        topLeft = tk.PhotoImage(file="Imagens\\baseazul.gif")
        topRight = tk.PhotoImage(file="Imagens\\baseamarelo.gif")
        botRight = tk.PhotoImage(file="Imagens\\baseverde.gif")
        botLeft = tk.PhotoImage(file="Imagens\\basevermelho.gif")

        cLeft = tk.PhotoImage(file="Imagens\\caixaazul.gif")
        cTop = tk.PhotoImage(file="Imagens\\caixaamarelo.gif")
        cRight = tk.PhotoImage(file="Imagens\\caixaverde.gif")
        cBot = tk.PhotoImage(file="Imagens\\caixavermelho.gif")

        sLeftPath = "Imagens\\paradaazul.gif"
        sTopPath  = "Imagens\\paradaamarelo.gif"
        sRightPath = "Imagens\\paradaverde.gif"
        sBotPath = "Imagens\\paradavermelho.gif"
    elif tabState == 3:   # verde joga
        topLeft = tk.PhotoImage(file="Imagens\\basevermelho.gif")
        topRight = tk.PhotoImage(file="Imagens\\baseazul.gif")
        botRight = tk.PhotoImage(file="Imagens\\baseamarelo.gif")
        botLeft = tk.PhotoImage(file="Imagens\\baseverde.gif")

        cLeft = tk.PhotoImage(file="Imagens\\caixavermelho.gif")
        cTop = tk.PhotoImage(file="Imagens\\caixaazul.gif")
        cRight = tk.PhotoImage(file="Imagens\\caixaamarelo.gif")
        cBot = tk.PhotoImage(file="Imagens\\caixaverde.gif")

        sLeftPath = "Imagens\\paradavermelho.gif"
        sTopPath  = "Imagens\\paradaazul.gif"
        sRightPath = "Imagens\\paradaamarelo.gif"
        sBotPath = "Imagens\\paradaverde.gif"

    rotacionaCasaSaida()
    Tabuleiro()         # renderiza com as mudanças
    return

def rotacionaCasaSaida():
    global sLeft
    global sTop
    global sRight
    global sBot

    global sLeftPath
    global sTopPath
    global sRightPath
    global sBotPath

    # mesmo algoritmo da rotação da imagem do centro, possivelmente podem ser condensados num só
    sLeftR = Image.open(sLeftPath)
    sLeftR = sLeftR.rotate(-90*tabState)
    sLeftR.save(sLeftPath[:-4] + 'R' + ".gif")
    sLeft = tk.PhotoImage(file=sLeftPath[:-4] + 'R' + ".gif")

    sTopR = Image.open(sTopPath)
    sTopR = sTopR.rotate(-90*tabState)
    sTopR.save(sTopPath[:-4] + 'R' + ".gif")
    sTop = tk.PhotoImage(file=sTopPath[:-4] + 'R' + ".gif")

    sRightR = Image.open(sRightPath)
    sRightR = sRightR.rotate(-90*tabState)
    sRightR.save(sRightPath[:-4] + 'R' + ".gif")
    sRight = tk.PhotoImage(file=sRightPath[:-4] + 'R' + ".gif")

    sBotR = Image.open(sBotPath)
    sBotR = sBotR.rotate(-90*tabState)
    sBotR.save(sBotPath[:-4] + 'R' + ".gif")
    sBot = tk.PhotoImage(file=sBotPath[:-4] + 'R' + ".gif")
    return