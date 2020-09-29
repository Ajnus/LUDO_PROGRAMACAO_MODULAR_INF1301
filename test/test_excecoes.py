from src.excecoes import *
import unittest

class TestExcecoes(unittest.TestCase):

    def testValidaNumeroInteiroCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('3')
        self.assertEqual(0, resultado)

    def testValidaNumeroInteiroPassandoChar(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('k')
        self.assertEqual(2, resultado)

    def testValidaNumeroInteiroPassandoFloat(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('2.3')
        self.assertEqual(2, resultado)


    def testValidaIntervaloCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(2, 1, 4)
        self.assertEqual(0, resultado)

    def testValidaIntervaloAcimaDoIntervalo(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(5, 1, 4)
        self.assertEqual(1, resultado)

    def testValidaIntervaloAbaixoDoIntervalo(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(0, 1, 4)
        self.assertEqual(1, resultado)


    def testValidaNomeCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaNome('Luan')
        self.assertEqual(0, resultado)

    def testValidaNomeMaiorQueLimiteDeCaracteres(self):
        excecao = InputError()
        resultado = excecao.validaNome('Luan Aguiar dos Santos Ferreira')
        self.assertEqual(1, resultado)

    def testValidaNomeEmBranco(self):
        excecao = InputError()
        resultado = excecao.validaNome('')
        self.assertEqual(1, resultado)

if __name__ == '__main__':
    unittest.main()
