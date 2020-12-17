import tkinter as tk
from PIL import Image
from db.dominioTabelas import *
from src.dado import rolarDado
from db.dominioTabelas import Session,Peao
import src.principal

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

CasasB = {1: ('22', '374'), 2: ('23', '323'), 3: ('73', '323'), 4: ('121', '323'), 5: ('174', '323'), 6: ('223', '322'), 7: ('272', '321'), 8: ('322', '274'), 9: ('323', '222'), 10: ('323', '170'), 11: ('325', '125'), 12: ('323', '74'), 13: ('322', '21'), 14: ('373', '20'), 15: ('423', '23'), 16: ('424', '74'), 17: ('422', '123'), 18: ('423', '172'), 19: ('423', '223'), 20: ('423', '273'), 21: ('474', '321'), 22: ('523', '322'), 23: ('571', '323'), 24: ('625', '324'), 25: ('674', '323'), 26: ('722', '321'), 27: ('724', '373'), 28: ('723', '421'), 29: ('665', '415'), 30: ('624', '421'), 31: ('574', '422'), 32: ('524', '425'), 33: ('473', '424'), 34: ('423', '472'), 35: ('424', '522'), 36: ('422', '573'), 37: ('425', '624'), 38: ('422', '673'), 39: ('424', '721'), 40: ('375', '723'), 41: ('323', '722'), 42: ('315', '665'), 43: ('323', '623'), 44: ('322', '572'), 45: ('323', '522'), 46: ('323', '472'), 47: ('275', '423'), 48: ('222', '423'), 49: ('174', '425'), 50: ('125', '425'), 51: ('76', '424'), 52: ('22', '424'),53: ('373', '675'), 54: ('374', '624'), 55: ('373', '575'), 56: ('375', '524'), 57: ('374', '475'), 58: ('377', '421'),59: ('674', '375'), 60: ('624', '375'), 61: ('574', '376'), 62: ('528', '373'), 63: ('470', '371'), 64: ('421', '373'),65: ('73', '373'), 66: ('125', '375'), 67: ('176', '376'), 68: ('224', '375'), 69: ('273', '375'), 70: ('324', '374'),71: ('373', '75'), 72: ('373', '127'), 73: ('373', '174'), 74: ('376', '227'), 75: ('375', '276'), 76: ('377', '322'),77: ('50', '670'), 78: ('210', '670'), 79: ('50', '530'), 80: ('210', '530'),81: ('650', '670'), 82: ('530', '670'), 83: ('650', '530'), 84: ('530', '530'),85: ('50', '50'), 86: ('50', '210'), 87: ('210', '50'), 88: ('210', '210'),89: ('650', '50'), 90: ('530', '50'), 91: ('650', '210'), 92: ('530', '210')}
#Casa 3 - Saida Verde
#Casa 16 - Saida Vermelho
#Casa 29 - Saida Azul
#Casa 42 - Saida Amarelo
#Casa 11,24,37,50 - Estrela

#CasasVerdes = {65: ('73', '373'), 66: ('125', '375'), 67: ('176', '376'), 68: ('224', '375'), 69: ('273', '375'), 70: ('324', '374')}
#CasasVermelhas = {71: ('373', '75'), 72: ('373', '127'), 73: ('373', '174'), 74: ('376', '227'), 75: ('375', '276'), 76: ('377', '322')}
#CasasAzul = {59: ('674', '375'), 60: ('624', '375'), 61: ('574', '376'), 62: ('528', '373'), 63: ('470', '371'), 64: ('421', '373')}
#CasasAmarelo = {53: ('373', '675'), 54: ('374', '624'), 55: ('373', '575'), 56: ('375', '524'), 57: ('374', '475'), 58: ('377', '421')}

#BaseAzul = {81: ('650', '670'), 82: ('530', '670'), 83: ('650', '530'), 84: ('530', '530')}
#BaseAmarelo = {77: ('50', '670'), 78: ('210', '670'), 79: ('50', '530'), 80: ('210', '530')}
#BaseVermelo = {89: ('650', '50'), 90: ('530', '50'), 91: ('650', '210'), 92: ('530', '210')}
#BaseVerde = {85: ('50', '50'), 86: ('50', '210'), 87: ('210', '50'), 88: ('210', '210')}

def traduz(CasaB):
    global cx,cy
    for i in CasaB.items():
        if cx-20<=int(i[1][0])<=cx+20 and cy-20<=int(i[1][1])<=cy+20:
            return i[0]


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

def posPeao():
    global AM0,AM1,AM2,AM3,AZ4,AZ5,AZ6,AZ7,VD8,VD9,VD10,VD11,VM12,VM13,VM14,VM15
    # Azul
    AZ4 = tk.Label(image=azul, width=20, height=20)
    AZ4.place(x=650, y=670)
    AZ5 = tk.Label(image=azul, width=20, height=20)
    AZ5.place(x=530, y=670)
    AZ6 = tk.Label(image=azul, width=20, height=20)
    AZ6.place(x=650, y=530)
    AZ7 = tk.Label(image=azul, width=20, height=20)
    AZ7.place(x=530, y=530)

    # Amarelo
    AM0 = tk.Label(image=amarelo, width=20, height=20)
    AM0.place(x=50, y=670)
    AM1 = tk.Label(image=amarelo, width=20, height=20)
    AM1.place(x=210, y=670)
    AM2 = tk.Label(image=amarelo, width=20, height=20)
    AM2.place(x=50, y=530)
    AM3 = tk.Label(image=amarelo, width=20, height=20)
    AM3.place(x=210, y=530)

    # Vermelho
    VM12 = tk.Label(image=vermelho, width=20, height=20)
    VM12.place(x=650, y=50)
    VM13 = tk.Label(image=vermelho, width=20, height=20)
    VM13.place(x=530, y=50)
    VM14 = tk.Label(image=vermelho, width=20, height=20)
    VM14.place(x=650, y=210)
    VM15 = tk.Label(image=vermelho, width=20, height=20)
    VM15.place(x=530, y=210)

    # Verde
    VD8 = tk.Label(image=verde, width=20, height=20)
    VD8.place(x=50, y=50)
    VD9 = tk.Label(image=verde, width=20, height=20)
    VD9.place(x=50, y=210)
    VD10 = tk.Label(image=verde, width=20, height=20)
    VD10.place(x=210, y=50)
    VD11 = tk.Label(image=verde, width=20, height=20)
    VD11.place(x=210, y=210)

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

    rotacionaCasaSaida()
    criarTabuleiro()

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



def main2():
    session = Session()
    global start,cx,cy,AM0,AM1,AM2,AM3,AZ4,AZ5,AZ6,AZ7,VD8,VD9,VD10,VD11,VM12,VM13,VM14,VM15

    if start == 0:
        criarTabuleiro()
        posPeao()

    else:

        print(principal.ordem)

        try:
            casa = traduz(CasasB)
            peaopos = session.query(Peao).filter(Peao.posicao == casa).all()
            #print(casa)
            #for i in range(len(peaopos)):
             #   print(peaopos[i].posicao)
        except:
            pass

        if int(CasasB[81][0])-20<=cx<=int(CasasB[81][0])+20 and int(CasasB[81][1])-20<=cy<=int(CasasB[81][1])+20:
            AZ4.place(x=int(CasasB[29][0]),y=int(CasasB[29][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao":29})
        elif int(CasasB[82][0])-20<=cx<=int(CasasB[82][0])+20 and int(CasasB[82][1])-20<=cy<=int(CasasB[82][1])+20:
            AZ5.place(x=int(CasasB[29][0]),y=int(CasasB[29][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 29})
        elif int(CasasB[83][0])-20<=cx<=int(CasasB[83][0])+20 and int(CasasB[83][1])-20<=cy<=int(CasasB[83][1])+20:
            AZ6.place(x=int(CasasB[29][0]),y=int(CasasB[29][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 29})
        elif int(CasasB[84][0])-20<=cx<=int(CasasB[84][0])+20 and int(CasasB[84][1])-20<=cy<=int(CasasB[84][1])+20:
            AZ7.place(x=int(CasasB[29][0]),y=int(CasasB[29][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 29})

        if int(CasasB[77][0])-20<=cx<=int(CasasB[77][0])+20 and int(CasasB[77][1])-20<=cy<=int(CasasB[77][1])+20:
            AM0.place(x=int(CasasB[42][0]),y=int(CasasB[42][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 42})
        elif int(CasasB[78][0])-20<=cx<=int(CasasB[78][0])+20 and int(CasasB[78][1])-20<=cy<=int(CasasB[78][1])+20:
            AM1.place(x=int(CasasB[42][0]), y=int(CasasB[42][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 42})
        elif int(CasasB[79][0])-20<=cx<=int(CasasB[79][0])+20 and int(CasasB[79][1])-20<=cy<=int(CasasB[79][1])+20:
            AM2.place(x=int(CasasB[42][0]), y=int(CasasB[42][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 42})
        elif int(CasasB[80][0])-20<=cx<=int(CasasB[80][0])+20 and int(CasasB[80][1])-20<=cy<=int(CasasB[80][1])+20:
            AM3.place(x=int(CasasB[42][0]), y=int(CasasB[42][1]))
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 42})

        if int(CasasB[85][0])-20<=cx<=int(CasasB[85][0])+20 and int(CasasB[85][1])-20<=cy<=int(CasasB[85][1])+20:
            VD8.place(x=int(CasasB[3][0])-10,y=int(CasasB[3][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 3})
        elif int(CasasB[86][0])-20<=cx<=int(CasasB[86][0])+20 and int(CasasB[86][1])-20<=cy<=int(CasasB[86][1])+20:
            VD9.place(x=int(CasasB[3][0])-10,y=int(CasasB[3][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 3})
        elif int(CasasB[87][0])-20<=cx<=int(CasasB[87][0])+20 and int(CasasB[87][1])-20<=cy<=int(CasasB[87][1])+20:
            VD10.place(x=int(CasasB[3][0])-10,y=int(CasasB[3][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 3})
        elif int(CasasB[88][0])-20<=cx<=int(CasasB[88][0])+20 and int(CasasB[88][1])-20<=cy<=int(CasasB[88][1])+20:
            VD11.place(x=int(CasasB[3][0])-10,y=int(CasasB[3][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 3})

        if int(CasasB[89][0])-20<=cx<=int(CasasB[89][0])+20 and int(CasasB[89][1])-20<=cy<=int(CasasB[89][1])+20:
            VM12.place(x=int(CasasB[16][0])-10,y=int(CasasB[16][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 16})
        elif int(CasasB[90][0])-20<=cx<=int(CasasB[90][0])+20 and int(CasasB[90][1])-20<=cy<=int(CasasB[90][1])+20:
            VM13.place(x=int(CasasB[16][0])-10,y=int(CasasB[16][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 16})
        elif int(CasasB[91][0])-20<=cx<=int(CasasB[91][0])+20 and int(CasasB[91][1])-20<=cy<=int(CasasB[91][1])+20:
            VM14.place(x=int(CasasB[16][0])-10,y=int(CasasB[16][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 16})
        elif int(CasasB[92][0])-20<=cx<=int(CasasB[92][0])+20 and int(CasasB[92][1])-20<=cy<=int(CasasB[92][1])+20:
            VM15.place(x=int(CasasB[16][0])-10,y=int(CasasB[16][1])-10)
            session.query(Peao).filter(Peao.posicao == casa).update({"posicao": 16})


    root.mainloop()



def clique(evento):
    global cx,cy,start
    start = 1
    cx = root.winfo_pointerx() - root.winfo_rootx()
    cy = root.winfo_pointery() - root.winfo_rooty()
    main2()

root.bind("<Button-1>", clique)

def valorDado():
    dado = rolarDado()
    L1 = tk.Label(root, text=dado, fg='Black', background='green', font=("Arial", 24, "bold"))
    L1.place(x=800, y=200)

    return dado

#Butao
butao = tk.Button(root, text="   ROLAR   ", relief="raised", font=("Arial", 20),command = valorDado)
butao.place(x=790, y=50)


