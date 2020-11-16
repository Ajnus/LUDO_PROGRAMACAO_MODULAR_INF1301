from src.excecoes import *
import unittest


class TesteExcecoes(unittest.TestCase):

    def testeValidaNumeroInteiroCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('3')
        self.assertEqual(0, resultado)

    def testeValidaNumeroInteiroPassandoChar(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('k')
        self.assertEqual(2, resultado)

    def testeValidaNumeroInteiroPassandoFloat(self):
        excecao = InputError()
        resultado = excecao.validaNumeroInteiro('2.3')
        self.assertEqual(2, resultado)

    def testeValidaIntervaloCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(2, 1, 4)
        self.assertEqual(0, resultado)

    def testeValidaIntervaloAcimaDoIntervalo(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(5, 1, 4)
        self.assertEqual(1, resultado)

    def testeValidaIntervaloAbaixoDoIntervalo(self):
        excecao = InputError()
        resultado = excecao.validaIntervalo(0, 1, 4)
        self.assertEqual(1, resultado)

    def testeValidaNomeCorretamente(self):
        excecao = InputError()
        resultado = excecao.validaNome('Luan')
        self.assertEqual(0, resultado)

    def testeValidaNomeMaiorQueLimiteDeCaracteres(self):
        excecao = InputError()
        resultado = excecao.validaNome('Luan Aguiar dos Santos Ferreira')
        self.assertEqual(1, resultado)

    def testeValidaNomeEmBranco(self):
        excecao = InputError()
        resultado = excecao.validaNome('')
        self.assertEqual(1, resultado)


if __name__ == '__main__':
    unittest.main()
