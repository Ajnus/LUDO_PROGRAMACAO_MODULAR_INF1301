from src.Tabuleiro import *
import unittest

class TestTabuleiro(unittest.TestCase):

    def testeCriarTabuleiro(self):
        resultado = criarTabuleiro()
        self.assertEqual(1, resultado)

    def testeMoverTabuleiro(self): # teste a função na n+1-ésima posição
        resultado = moverTabuleiro()
        self.assertEqual(1, resultado)

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
        
    def TesteRemoverPeaoRetorno1(self):
        print("Caso de teste - remove peao (retorno 1)")
        retornoEsperado = removerPeaoDoJogador(2)
        self.assertEqual(retornoEsperado, 1)

    def TesteRemoverPeaoRetorno0(self):
        print("Caso de teste - não remove peao (retorno 0)")
        retornoEsperado = removerPeaoDoJogador(555)
        self.assertEqual(retornoEsperado, 0)
