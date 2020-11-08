from src.gerenciaJogada import *
import unittest

class TestDado(unittest.TestCase):

    def testPrimeiroJogadorId2(self):
        resultado = definirPrimeiroJogador([(0, 2), (1, 2), (2, 4), (3, 2)])
        self.assertEqual(2, resultado)


    def testPrimeiroJogadorEmpate(self):
        resultado = definirPrimeiroJogador([(0, 4), (1, 3), (2, 4), (3, 4)])
        self.assertEqual([0, 2, 3], resultado)


    def testPrimeiroJogadorListaVazia(self):
        resultado = definirPrimeiroJogador([])
        self.assertEqual(-1, resultado)
        

class TestDefineVencedor(unittest.TestCase):

    def testeDefineVencedor(self):
        print("Caso de teste 1 - -1 quando nao ha vencedor e a id quando ha vencedor")
        retornoEsperado = defineVencedor(0)
        if (retornoEsperado == -1)
            self.assertEqual(retornoEsperado, -1)
        else
            self.assertEqual(retornoEsperado, 0)
)
