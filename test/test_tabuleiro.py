import unittest
from src.Tabuleiro import *

class TestTabuleiro(unittest.TestCase):

    def testeDefinirStatusCasaPassavel(self):
        print("Caso de teste 1 - casas passáveis do tabuleiro")
        retornoEsperado = defineStatusCasa(10)
        self.assertEqual(retornoEsperado, 0)

    def testeDefinirStatusCasaFinal(self):
        print("Caso de teste 2 - casa final do tabuleiro")
        retornoEsperado = defineStatusCasa(57)
        self.assertEqual(retornoEsperado, 1)

    def testeDefinirStatusCasaFora(self):
        print("Caso de teste 3 - casa fora do tabuleiro")
        retornoEsperado = defineStatusCasa(60)
        self.assertEqual(retornoEsperado, 2)
        


if __name__ == '__main__':
    unittest.main()
        
