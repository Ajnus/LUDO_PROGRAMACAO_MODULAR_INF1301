import unittest
from src.jogador import *

class Test_Jogador(unittest.TestCase):


    def test_cadastra_jogador_corretamente(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual(('Vermelho', 'Luan'), resultado)

    def test_cadastra_jogador_insere_letra_inves_numero(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual((2,'error'), resultado)

    def test_cadastra_jogador_insere_valor_maior_que_limite(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual((3,'error'), resultado)

    def test_cadastra_jogador_insere_valor_menor_que_limite(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual((3,'error'), resultado)

    def test_cadastra_jogador_nome_vazio(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual((1,'error'), resultado)

    def test_cadastra_jogador_nome_maior_que_20_caracteres(self):
        jogador = Jogador()
        resultado = jogador.cadastra_jogador(['Vermelho'])
        self.assertEqual((1,'error'), resultado)


if __name__ == '__main__':
    unittest.main()