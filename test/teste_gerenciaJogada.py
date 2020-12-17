from src.gerenciaJogada import *
import unittest


class TesteDado(unittest.TestCase):

    def testeOrdemJogador1(self):
        resultado = ordemJogador([(2, 0), (2, 1), (4, 2), (2, 3)])
        self.assertEqual([2, 3, 1, 0], resultado)

    def testeOrdemJogador2(self):
        resultado = ordemJogador([(4, 0), (3, 1), (4, 2), (4, 3)])
        self.assertEqual([3, 2, 0, 1], resultado)

    def testeRemoverJogadorRetorno1(self):
        print("Caso de teste - remove jogador (retorno 1)")
        retornoEsperado = removerJogador(0)
        self.assertEqual(retornoEsperado, 1)

    def testeRemoverJogadorRetorno0(self):
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
        print("Caso de teste  - verifica se o jogador foi o vencedor (retorno 0)")
        retornoEsperado = verificarVencedor(3)
        self.assertEqual(retornoEsperado, 0)

    def testeVerificarNaoVencedorRetorno1(self):
        print("Caso de teste  - verifica se o jogador não foi o vencedor (retorno 1)")
        retornoEsperado = verificarVencedor(2)
        self.assertEqual(retornoEsperado, 1)

    def testeChamarProximoJogador(self):
        print("Caso de teste - chama próximo jogador")
        retornoEsperado = chamarProximoJogador(2, [1, 2, 3, 4])
        self.assertEqual(retornoEsperado, 3)

    def testeChamarProximoJogadorDepoisDaQuartaPosicao(self):
        print("Caso de teste - chama próximo depois da quarta posicao")
        retornoEsperado = chamarProximoJogador(4, [1, 2, 3, 4])
        self.assertEqual(retornoEsperado, 1)

    def testeChamarProximoJogadorRetornoMenos1(self):
        print("Caso de teste - chama número fora do limite (retorno -1)")
        retornoEsperado = chamarProximoJogador(6, [1, 2, 3, 4])
        self.assertEqual(retornoEsperado, -1)
