import unittest
from src.jogador import *
from db.dominioTabelas import Session
from src.excecoes import InputError


class TesteJogador(unittest.TestCase):
    session = Session()
    excecao = InputError()

    def testeCadastraJogadorCorretamente(self):
        codigo = self.excecao.gerarCodigoJogador()
        resultado = cadastraJogador(['Vermelho'])
        self.assertEqual(('Vermelho', 'Luan', codigo), resultado)

    def testeArmazenarJogador(self):
        codigo = self.excecao.gerarCodigoJogador()
        print(codigo)
        resultado = armazenaJogador(codigo, 'Luan', 'Amarelo', 0)
        self.assertEqual(resultado, 0)

    def testeArmazenarJogadorComCodigoExistente(self):
        codigo = self.excecao.gerarCodigoJogador() - 1
        resultado = armazenaJogador(codigo, 'Luan', 'Amarelo', 0)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    unittest.main()
