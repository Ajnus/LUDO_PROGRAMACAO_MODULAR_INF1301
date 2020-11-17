import xml.etree.ElementTree as ET
from db.dominioTabelas import Session,Peao,Jogador,Tabuleiro

session = Session()

xmlDoc = ET.Element('StatusPartida')
posPeos = ET.SubElement(xmlDoc,'PosPeos')
statusCasa = ET.SubElement(xmlDoc,'StatusCasa')
infoJogador = ET.SubElement(xmlDoc,'InfoJogador')
ordemJogadores = ET.SubElement(xmlDoc,'OrdemJogadores')
l =[]

for i in range(16):  #Ajustar para a quantidade exata de peos no jogo
    posiPeao = session.query(Peao.posicao).filter_by(codigo = i).one()[0]
    if   (0 <= i <= 3):
        cor = 'Amarelo'
    elif (4 <= i <= 7):
        cor='Azul'
    elif (8 <= i <= 11):
        cor = 'Verde'
    else:
        cor = 'Vermelho'
    ET.SubElement(posPeos,'Peão_{}'.format(i), pos = str(posiPeao), id = str(i), cor = cor)

for i in range(1,77):
    statusC = session.query(Tabuleiro.statusCasa).filter_by(casa = i).one()[0]
    ET.SubElement(statusCasa,'Casa_{}'.format(i), status = str(statusC))

for i in range(4):
    codJ = session.query(Jogador.codigo).all()[-1-i][0]
    nomeJ = session.query(Jogador.nome).filter_by(codigo = codJ).one()[0]
    corJ = session.query(Jogador.corpeao).filter_by(codigo = codJ).one()[0]
    ET.SubElement(infoJogador,'Jogador_{}'.format(i), nome=nomeJ, id= str(codJ), cor=corJ)
    l.append(codJ)

ET.SubElement(ordemJogadores,'Ordem', ordemJogadores = str(l))


def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings

prettify(xmlDoc)

tree = ET.ElementTree(xmlDoc)
tree.write('statusPartida.xml',encoding='UTF-8',xml_declaration=True)