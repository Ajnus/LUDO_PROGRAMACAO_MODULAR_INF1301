import unittest
from src.dado import *

class TesteDado(unittest.TestCase):

    def testeRolarDados(self):
        rolar = rolarDado()
        self.assertTrue(1 <= rolar <= 6)

if __name__ == '__main__':
    unittest.main()
