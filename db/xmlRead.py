import xml.etree.ElementTree as ET
import requests

from src.jogador import armazenaJogador
from src.peao import armazenaPeao
from src.tabuleiro import armazenaStatusCasaTabState
from src.gerenciaJogada import armezenaOrdem

def xmlRead(xmlDoc):
    tree =  ET.parse(xmlDoc)

    root=tree.getroot()

    filtro="*"
    for child in root.iter(filtro):
            if ("Peão" in child.tag):
                armazenaPeao(child.get('id'), child.get('cor'), child.get('pos'))

            if ("Casa_" in child.tag):
                armazenaStatusCasaTabState(child.tag[-2:], child.get('statusCasa'), child.get('tabState'))

            elif ("Jogador_" in child.tag):
                armazenaJogador(child.get('id'), child.get('nome'), child.get('cor'))

            elif ("Ordem" in child.tag and "Jog" not in child.tag):
                armezenaOrdem(child.get('ordemJogadores'))

xmlRead("statusPartida.xml")