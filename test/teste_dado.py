import unittest
from src.dado import *


class TesteDado(unittest.TestCase):
    dado = criarDado()

    def testeCriarDado1(self):
        print("Teste Dado 1")
        self.assertEqual(self.dado[0], 1)

    def testeCriarDado2(self):
        print("Teste Dado 2")
        self.assertEqual(self.dado[1], 2)

    def testeCriarDado3(self):
        print("Teste Dado 3")
        self.assertEqual(self.dado[2], 3)
    
    def testeCriarDado4(self):
        print("Teste Dado 4")
        self.assertEqual(self.dado[3], 4)

    def testeCriarDado5(self):
        print("Teste Dado 5")
        self.assertEqual(self.dado[4], 5)

    def testeCriarDado6(self):
        print("Teste Dado 6")
        self.assertEqual(self.dado[5], 6)
        
    def testeRolarDados(self):
        dado = criarDado()
        rolar = rolarDado(dado)
        self.assertTrue(1 <= rolar <= 6)


if __name__ == '__main__':
    unittest.main()
