import tkinter as tk
from PIL import Image
from db.dominioTabelas import *
from src.dado import rolarDado
root = tk.Tk()

# Permite o usuario mudar o tamanho da tela
root.resizable(width=False, height=False)
root.geometry('1000x750')  # Cria uma janela
root.configure(background='green')
root.title("Ludo - Grupo 5")  # Nome da Janela

# Usado no futuro também para rotações
centroPath = "Imagens\\centro.gif"
sLeftPath = "Imagens\\paradaverde.gif"
sTopPath = "Imagens\\paradavermelho.gif"
sRightPath = "Imagens\\paradaazul.gif"
sBotPath = "Imagens\\paradaamarelo.gif"

# Carregando as imagens na posição default do tabuleiro, amarelo joga
imgCentro = tk.PhotoImage(file=centroPath)
imgCaixaBranco = tk.PhotoImage(file="Imagens\\caixabranco.gif")
imgCaixaEstrela = tk.PhotoImage(file="Imagens\\caixaestrela.gif")

topLeft = tk.PhotoImage(file="Imagens\\baseverde.gif")
topRight = tk.PhotoImage(file="Imagens\\basevermelho.gif")
botRight = tk.PhotoImage(file="Imagens\\baseazul.gif")
botLeft = tk.PhotoImage(file="Imagens\\baseamarelo.gif")

cLeft = tk.PhotoImage(file="Imagens\\caixaverde.gif")
cTop = tk.PhotoImage(file="Imagens\\caixavermelho.gif")
cRight = tk.PhotoImage(file="Imagens\\caixaazul.gif")
cBot = tk.PhotoImage(file="Imagens\\caixaamarelo.gif")

sLeft = tk.PhotoImage(file=sLeftPath)
sTop = tk.PhotoImage(file=sTopPath)
sRight = tk.PhotoImage(file=sRightPath)
sBot = tk.PhotoImage(file=sBotPath)

#Pecas
azul = tk.PhotoImage(file="Imagens\\azul.gif")
amarelo = tk.PhotoImage(file="Imagens\\amarelo.gif")
vermelho = tk.PhotoImage(file="Imagens\\vermelho.gif")
verde = tk.PhotoImage(file="Imagens\\verde.gif")

# estado/posição inicial do tabuleiro
tabState = 0

start = 0

def criarTabuleiro():

    # Imagem Central
    tk.Label(image=imgCentro, width=150, height=150).place(x=298, y=298)

    # Construindo o lado Topo Esquerdo.

    horizontal = 0  # quantidade de pixels para pular
    consertaCaixa = 1  # Variavel de ajuda para implementar os quadrados coloridos

    tk.Label(image=topLeft, width=295, height=300).place(
        x=-1, y=-1)  # Topo Esquerdo
    while(horizontal != 300):
        vertical = 0
        while (vertical != 150):
            if horizontal == 50 and vertical == 0:
                tk.Label(image=sLeft, width=46, height=46).place(
                    x=(0 + horizontal), y=(300 + vertical))  # Inserindo a casa de saída do topo esquerdo
            elif horizontal == 100 and vertical == 100:
                tk.Label(image=imgCaixaEstrela, width=46, height=46).place(
                    x=(0 + horizontal), y=(300 + vertical))
            # Verifica se é a caixa do meio e verifica se ja passou a primeira casa do meio.
            elif consertaCaixa == 2 and horizontal > 0:
                tk.Label(image=cLeft, width=46, height=46).place(
                    x=(0 + horizontal), y=(300 + vertical))  # Inserindo as caixas ligadas ao topo esquerdo
            else:
                # Inserindo as caixas brancas.
                tk.Label(image=imgCaixaBranco, width=46, height=46).place(
                    x=(0 + horizontal), y=(300 + vertical))
            vertical += 50
            consertaCaixa += 1
        consertaCaixa = 1
        horizontal += 50

    # Construindo o lado Topo Direito
    horizontal = 0
    consertaCaixa = 1

    tk.Label(image=topRight, width=295, height=295).place(x=450, y=0)

    while(horizontal != 300):
        vertical = 0
        while (vertical != 150):
            if horizontal == 50 and vertical == 100:
                tk.Label(image=sTop, width=46, height=46).place(
                    x=(300 + vertical), y=(0 + horizontal))
            elif horizontal == 100 and vertical == 0:
                tk.Label(image=imgCaixaEstrela, width=46, height=46).place(
                    x=(300 + vertical), y=(0 + horizontal))
            elif consertaCaixa == 2 and horizontal > 0:
                tk.Label(image=cTop, width=46, height=46).place(
                    x=(300 + vertical), y=(0 + horizontal))
            else:
                tk.Label(image=imgCaixaBranco, width=46, height=46).place(
                    x=(300 + vertical), y=(0 + horizontal))
            vertical += 50
            consertaCaixa += 1
        consertaCaixa = 1
        horizontal += 50

    # Construindo a lado Base Direita
    horizontal = 0
    consertaCaixa = 1

    tk.Label(image=botRight, width=295, height=295).place(x=450, y=450)
    while(horizontal != 300):
        vertical = 0
        while (vertical != 150):
            if horizontal == 200 and vertical == 100:
                tk.Label(image=sRight, width=46, height=46).place(
                    x=(450 + horizontal), y=(300 + vertical))
            elif horizontal == 150 and vertical == 0:
                tk.Label(image=imgCaixaEstrela, width=46, height=46).place(
                    x=(450 + horizontal), y=(300 + vertical))
            elif consertaCaixa == 2 and horizontal < 250:
                tk.Label(image=cRight, width=46, height=46).place(
                    x=(450 + horizontal), y=(300 + vertical))
            else:
                tk.Label(image=imgCaixaBranco, width=46, height=46).place(
                    x=(450 + horizontal), y=(300 + vertical))
            vertical += 50
            consertaCaixa += 1
        consertaCaixa = 1
        horizontal += 50

    # Construindo a lado Base Esquerda
    horizontal = 0
    consertaCaixa = 1

    tk.Label(image=botLeft, width=295, height=295).place(x=0, y=450)
    while(horizontal != 300):
        vertical = 0
        while (vertical != 150):
            if horizontal == 200 and vertical == 0:
                tk.Label(image=sBot, width=46, height=46).place(
                    x=(300 + vertical), y=(450 + horizontal))
            elif horizontal == 150 and vertical == 100:
                tk.Label(image=imgCaixaEstrela, width=46, height=46).place(
                    x=(300 + vertical), y=(450 + horizontal))
            elif consertaCaixa == 2 and horizontal < 250:
                tk.Label(image=cBot, width=46, height=46).place(
                    x=(300 + vertical), y=(450 + horizontal))
            else:
                tk.Label(image=imgCaixaBranco, width=46, height=46).place(
                    x=(300 + vertical), y=(450 + horizontal))
            vertical += 50
            consertaCaixa += 1
        consertaCaixa = 1
        horizontal += 50

        #Peos
        #Azul
        tk.Label(image=azul, width=20, height=20).place(x=650, y=670)
        tk.Label(image=azul, width=20, height=20).place(x=530, y=670)
        tk.Label(image=azul, width=20, height=20).place(x=650, y=530)
        tk.Label(image=azul, width=20, height=20).place(x=530, y=530)

        #Amarelo
        tk.Label(image=amarelo, width=20, height=20).place(x=50, y=670)
        tk.Label(image=amarelo, width=20, height=20).place(x=210, y=670)
        tk.Label(image=amarelo, width=20, height=20).place(x=50, y=530)
        tk.Label(image=amarelo, width=20, height=20).place(x=210, y=530)

        #Vermelho
        tk.Label(image=vermelho, width=20, height=20).place(x=650, y=50)
        tk.Label(image=vermelho, width=20, height=20).place(x=530, y=50)
        tk.Label(image=vermelho, width=20, height=20).place(x=650, y=210)
        tk.Label(image=vermelho, width=20, height=20, ).place(x=530, y=210)

        #Verde
        tk.Label(image=verde, width=20, height=20).place(x=50, y=50)
        tk.Label(image=verde, width=20, height=20).place(x=50, y=210)
        tk.Label(image=verde, width=20, height=20).place(x=210, y=50)
        tk.Label(image=verde, width=20, height=20).place(x=210, y=210)

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

    global imgCentro

    global sLeftPath
    global sTopPath
    global sRightPath
    global sBotPath

    # altera estado do tabuleiro
    tabState += 1
    if (tabState > 3):
        tabState = 0

    # rotaciona imagem centro (cria nova imagem rotacionada a partir da original, mantendo o uso da tkInter)
    imgCentroR = Image.open(centroPath)
    imgCentroR = imgCentroR.rotate(-90*tabState)
    imgCentroR.save("Imagens\\centroR.gif")
    imgCentro = tk.PhotoImage(file="Imagens\\centroR.gif")

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

c=10
def main():
    global start,c

    if start == 0:
        criarTabuleiro()
        start = 1
    else:
        print("a")

main()

# Define todas as casas passáveis
def definirStatusCasa(posicao):
    if posicao < 57: #casas passáveis
        return 0
    if posicao == 57: # casa final
        return 1
    else:
        return 2

# Remove o peão do jogador
def removerPeaoDoJogador(idPeao):
    session = Session()
    try:
        peaoCodigo = session.query(Peao).filter_by(codigo = idPeao).one()
        session.delete(peaoCodigo)
        atualizarBD()
        return 1
    except:
        peaoCodigo = 0
        return 0

# Move o peão para base
def moverParaBase(idPeao):
    session = Session()
    try:
       posPeao = session.query(Peao).update(codigo = idPeao, posicao = 0 )
       atualizarBD()
       return 0
    except:
        return 1


def criarCasasTabuleiro():
    session = Session()
    for casa in range(1, 77):
        tabuleiro = Tabuleiro(casa=casa)
        session.add(tabuleiro)
        atualizarBD()


def armazenaStatusCasaTabState(casa, statusCasa, tabState):
    try:
        session = Session()
        statusState = Tabuleiro(casa=casa, statusCasa=statusCasa, tabState=tabState)
        session.add(statusState)
        atualizarBD()
        return 0
    except:
        return 1


def alteraStatusCasa(idCasa):
    try:
        session = Session()
        statusCasaAtual = session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).one()
        if statusCasaAtual.statusCasa == False:
            session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).update({'statusCasa': True})
        else:
            session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).update({'statusCasa': False})
        atualizarBD()
        return 0
    except:
        return 1


def verificarStatusCasa(idCasa):
    try:
        session = Session()
        casa = session.query(Tabuleiro).filter(Tabuleiro.casa == idCasa).one()
        return casa.statusCasa
    except:
        return 1


# Mover Peão
def moverPeao(idPeao, valorDado):
    session = Session()
    try:
        posPeao = session.query(Peao).filter_by(codigo=idPeao).one()
        posPeao.posicao += valorDado
        atualizarBD()
        return 0
    except:
        posPeao = -1
        return 1


# Sair da Base
def sairBase(idPeao):
    session = Session()
    try:
        posPeao = session.query(Peao).filter_by(codigo=idPeao).one()
        posPeao.posicao = 1
        atualizarBD()
        return 0
    except:
        posPeao = -1
        return 1

def clique(evento):
    main()

root.bind("<Button-1>", clique)

def valorDado():
    dado = rolarDado()
    L1 = tk.Label(root, text=dado, fg='Black', background='green', font=("Arial", 24, "bold"))
    L1.place(x=800, y=200)

#Butao
butao = tk.Button(root, text="   ROLAR   ", relief="raised", font=("Arial", 20),command = valorDado)
butao.place(x=790, y=50)

root.mainloop()