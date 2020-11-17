import random


def criarDado():
    return tuple(range(1, 7))


def rolarDado(dado):
    return random.choice(dado)
