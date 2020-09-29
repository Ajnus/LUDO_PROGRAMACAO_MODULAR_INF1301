from db import base

class Peao:
    def __init__(self):
        pass

    def coresDisponiveis(self):
        cores = base.peoesCoresDisponiveis
        return cores

    def removeCor(self, cor):
        cores = base.peoesCoresDisponiveis
        cores.remove(cor)
        base.peoesCoresDisponiveis = cores
