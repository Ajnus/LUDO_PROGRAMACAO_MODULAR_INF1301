from db import base
from src.peao import *
import unittest


class TestePeao(unittest.TestCase):

    def testeCoresDisponiveis(self):
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Verde', 'Vermelho'])

    def testeArmazenarPeao(self):
        armazenaPeao([7, 8], 'Preto')
        resultado = base.peoesCadastrados
        self.assertEqual(resultado['Preto'], [7, 8])

    def testeCriarPeoes(self):
        criarPeoes()
        self.assertEqual(5, len(base.peoesCadastrados))

    def testeRemoverCor(self):
        removeCor('Verde')
        resultado = coresDisponiveis()
        self.assertEqual(resultado, ['Amarelo', 'Azul', 'Vermelho'])
