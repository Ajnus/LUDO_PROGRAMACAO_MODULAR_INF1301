from db import base
from src.peao import *
import unittest
class TestPeao(unittest.TestCase):

    def testCoresDisponiveis(self):
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Verde', 'Vermelho'])

    def testArmazenarPeao(self):
        armazenaPeao([7, 8], 'Preto')
        resultado = base.peoesCadastrados
        self.assertEqual(resultado['Preto'], [7,8])

    def testCriarPeoes(self):
        criarPeoes()
        self.assertEqual(5, len(base.peoesCadastrados))

    def testRemoverCor(self):
        removeCor('Verde')
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Vermelho'])
