from src.gerenciaJogada import *
import unittest

class TestDado(unittest.TestCase):

    def testPrimeiroJogadorId2(self):
        resultado = definirPrimeiroJogador([(0, 2), (1, 2), (2, 4), (3, 2)])
        self.assertEqual(2, resultado)


    def testPrimeiroJogadorEmpate(self):
        resultado = definirPrimeiroJogador([(0, 2), (1, 4), (2, 4), (3, 2)])
        self.assertEqual([1, 2], resultado)


    def testPrimeiroJogadorListaVazia(self):
        resultado = definirPrimeiroJogador([])
        self.assertEqual(-1, resultado)