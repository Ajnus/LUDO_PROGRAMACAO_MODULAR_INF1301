import tkinter as tk
from PIL import Image
from db.dominioTabelas import *
from src.tabuleiro import *
import unittest

class TesteTabuleiro(unittest.TestCase):

    #Deixar comentado até resolver a parte grafica.
    '''
    def testeCriarTabuleiro(self):
        resultado = criarTabuleiro()
        self.assertEqual(1, resultado)

    def testeMoverTabuleiro(self):  # teste a função na n+1-ésima posição
        resultado = moverTabuleiro()
        self.assertEqual(1, resultado)
    '''
    def testeDefinirStatusCasaPassavel(self):
        print("Caso de teste 1 - casas passáveis do tabuleiro")
        retornoEsperado = definirStatusCasa(10)
        self.assertEqual(retornoEsperado, 0)

    def testeDefinirStatusCasaFinal(self):
        print("Caso de teste 2 - casa final do tabuleiro")
        retornoEsperado = definirStatusCasa(57)
        self.assertEqual(retornoEsperado, 1)

    def testeDefinirStatusCasaFora(self):
        print("Caso de teste 3 - casa fora do tabuleiro")
        retornoEsperado = definirStatusCasa(60)
        self.assertEqual(retornoEsperado, 2)

    def testeAlterarStatusCasa(self):
        resultado = alteraStatusCasa(60)
        self.assertEqual(resultado, 0)

    def testeAlterarStatusCasaIdInexistente(self):
        resultado = alteraStatusCasa(222)
        self.assertEqual(resultado, 1)

    def testeVerificarStatusCasa(self):
        resultado = verificarStatusCasa(76)
        self.assertEqual(resultado, False)

    def testeVerificarStatusCasaIdInexistente(self):
        resultado = verificarStatusCasa(222)
        self.assertEqual(resultado, 1)
        
    def testeRemoverPeaoRetorno0(self):
        print("Caso de teste - remove peao (retorno 0)")
        retornoEsperado = removerPeaoDoJogador(2)
        self.assertEqual(retornoEsperado, 0)

    def testeRemoverPeaoRetorno1(self):
        print("Caso de teste - não remove peao (retorno 0)")
        retornoEsperado = removerPeaoDoJogador(555)
        self.assertEqual(retornoEsperado, 1)

    def testeMoverPeaoRetorno0(self):
        print("Caso de teste - move peao (retorno 0)")
        retornoEsperado = moverPeao(1, 5)
        self.assertEqual(retornoEsperado, 0)

    def testeMoverPeaoRetorno1(self):
        print("Caso de teste - não move peao (retorno 1)")
        retornoEsperado = moverPeao(559, 1)
        self.assertEqual(retornoEsperado, 1)

    def testeSairBaseRetorno0(self):
        print("Caso de teste - sai da base (retorno 0)")
        retornoEsperado = sairBase(4)
        self.assertEqual(retornoEsperado, 0)

    def testeSairBaseRetorno1(self):
        print("Caso de teste - não sai da base (retorno 1)")
        retornoEsperado = sairBase(600)
        self.assertEqual(retornoEsperado, 1)

    def testeMoverParaBaseRetorno0(self):
        print("Caso de teste - move para a base (retorno 0)")
        retornoEsperado = moverParaBase(12)
        self.assertEqual(retornoEsperado, 0)

    def testeMoverParaBaseRetorno1(self):
        print("Caso de teste - não move para base (retorno 1)")
        retornoEsperado = moverParaBase(900)
        self.assertEqual(retornoEsperado, 1)
