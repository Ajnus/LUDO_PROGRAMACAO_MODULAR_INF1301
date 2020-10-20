import unittest
from src.Tabuleiro import *

class TestTabuleiro(unittest.TestCase):

    def testeCriarTabuleiro(self):
        if (criarTabuleiro() == 1):
            print("Tabuleiro criado com sucesso!\n")
        
    def testeMoverTabuleiro(self, n): # teste a função na n+1-ésima posição
        i = 0
        while (i < n):
            if (moverTabuleiro() == 1): # no futuro 'n' pode ser útil para determinar número de rodadas/turnos da partida
                    print("Tabuleiro girado com sucesso!\n")
            i+=1

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
        
