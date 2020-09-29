import unittest
from src.jogador import *

class TestJogador(unittest.TestCase):


    def testCadastraJogadorCorretamente(self):
        jogador = Jogador()
        resultado = jogador.cadastraJogador(['Vermelho'])
        self.assertEqual(('Vermelho', 'Luan'), resultado)


if __name__ == '__main__':
    unittest.main()