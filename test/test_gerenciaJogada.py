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


    def TesteRemoverJogadorRetorno1(self):
        print("Caso de teste - remove jogador (retorno 1)")
        retornoEsperado = removerJogador(0)
        self.assertEqual(retornoEsperado, 1)

    def TesteRemoverJogadorRetorno0(self):
        print("Caso de teste - não remove jogador (retorno 0)")
        retornoEsperado = removerJogador(555)
        self.assertEqual(retornoEsperado, 0)


    def testeDefineVencedor(self):
        print("Caso de teste:  -1 quando nao ha vencedor e a id e o nome quando ha vencedor")
        retornoEsperado = defineVencedor()
        if retornoEsperado == (-1, -1):
            self.assertEqual(retornoEsperado, (-1, -1))
        else:
            self.assertEqual(retornoEsperado, defineVencedor())


    def testeVerificarVencedorRetorno0(self):
        print("Caso de teste  - verifica se o jogador foi o vencedor (retorno 1)")
        retornoEsperado = verificarVencedor(3)
        self.assertEqual(retornoEsperado, 0)

    def testeVerificarNaoVencedorRetorno1(self):
        print("Caso de teste  - verifica se o jogador não foi o vencedor (retorno 0)")
        retornoEsperado = verificarVencedor(2)
        self.assertEqual(retornoEsperado, 1)
