import unittest
from src.jogador import *
from db.dominioTabelas import Session
from src.excecoes import InputError

class TestJogador(unittest.TestCase):
    session = Session()
    excecao = InputError()

    def testCadastraJogadorCorretamente(self):
        codigo = self.excecao.gerarCodigoJogador()
        resultado = cadastraJogador(['Vermelho'])
        self.assertEqual(('Vermelho', 'Luan', codigo), resultado)

    def testArmazenarJogador(self):
        codigo = self.excecao.gerarCodigoJogador()
        print(codigo)
        resultado = armazenaJogador(codigo, 'Luan', 'Amarelo')
        self.assertEqual(resultado, 0)

    def testArmazenarJogadorComCodigoExistente(self):
        codigo = self.excecao.gerarCodigoJogador() - 1
        resultado = armazenaJogador(codigo, 'Luan', 'Amarelo')
        self.assertEqual(resultado, 1)


if __name__ == '__main__':
    unittest.main()