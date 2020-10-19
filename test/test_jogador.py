import unittest
from src.jogador import *

class TestJogador(unittest.TestCase):


    def testCadastraJogadorCorretamente(self):
        resultado = cadastraJogador(['Vermelho'])
        self.assertEqual(('Vermelho', 'Luan'), resultado)

    def testArmazenarJogador(self):
        armazenaJogador(7, 'Luan', 'Roxo')
        resultado = base.jogadoresCadastrados
        self.assertEqual(resultado[7], ('Luan', 'Roxo'))


if __name__ == '__main__':
    unittest.main()