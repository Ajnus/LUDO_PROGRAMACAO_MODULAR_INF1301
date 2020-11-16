from src.peao import *
import unittest
class TestPeao(unittest.TestCase):

    def testCoresDisponiveis(self):
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Verde', 'Vermelho'])

    def testCriarPeoes(self):
        resultado = criarPeoes()
        self.assertEqual(resultado, 0)

    def testArmazenarPeao(self):
        resultado = armazenaPeao(22, 'Azul', 3)
        self.assertEqual(resultado, 0)

    def testRemoverCor(self):
        removeCor('Verde')
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Vermelho'])
