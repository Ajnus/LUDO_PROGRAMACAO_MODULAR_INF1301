from src.peao import *
import unittest


class TestePeao(unittest.TestCase):

    def testeCoresDisponiveis(self):
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Verde', 'Roxo'])

    def testeCriarPeoes(self):
        resultado = criarPeoes()
        self.assertEqual(resultado, 0)

    def testeArmazenarPeao(self):
        resultado = armazenaPeao(22, 'Azul', 3)
        self.assertEqual(resultado, 0)

    def testeRemoverCor(self):
        removeCor('Verde')
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Roxo'])
