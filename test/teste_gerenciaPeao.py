from db import base
from src.gerenciaPeao import *
import unittest


class TestePeao(unittest.TestCase):

    def testeContarPeaoNaBase(self):
        resultado = contarPeaoNaBase(3)
        self.assertEqual(resultado, (4, [0, 1, 2, 3]))

    def testeContarPeaoNaBaseZeroPeao(self):
        resultado = contarPeaoNaBase(4)
        self.assertEqual(resultado, (0, []))

    def testeContarPeaoNaBaseCodigoNaoRegistrado(self):
        resultado = contarPeaoNaBase(23)
        self.assertEqual(resultado, 1)
