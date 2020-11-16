from src.mensagem import *
from db.dominioTabelas import Session, Jogador, Peao

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message=''):
        self.message = message

    def validaIntervalo(self, numero, minimo, maximo):
        try:
            if  numero < minimo or numero > maximo:
                raise InputError(f'Escolha inválida!\n'
                                 f'Escolha um numero entre {minimo} e {maximo}\n')
            status = 0

        except InputError as ex:
            print(ex)
            status = 1

        return status

    def validaNome(self, nome):
        try:
            if len(nome) > 20:
                raise InputError(f'Escolha inválida!\n'
                                 'O nome pode ter no máximo 20 caracteres\n')
            elif len(nome) == 0:
                raise InputError(f'Escolha inválida!\n'
                                 'O nome tem que ter no mínimo 1 caracter diferente de espaço em branco.\n')
            status = 0

        except InputError as ex:
            print(ex)
            status = 1

        return status

    def validaNumeroInteiro(self, numeroString):
        try:
            int(numeroString)
            status = 0

        except ValueError:
            print(ALERTA_SO_NUMEROS_INTEIROS)
            status = 2

        return status

    def gerarCodigoJogador(self):
        session = Session()
        try:
            codigo = session.query(Jogador.codigo).all()[-1][0] + 1  # pega o ultimo codigo de jogador cadastrado no BD e soma 1
        except:
            codigo = 0

        return codigo

    def gerarCodigoPeao(self):
        session = Session()
        try:
            codigo = session.query(Peao.codigo).all()[-1][0] + 1  # pega o ultimo codigo de jogador cadastrado no BD e soma 1
        except:
            codigo = 0

        return codigo