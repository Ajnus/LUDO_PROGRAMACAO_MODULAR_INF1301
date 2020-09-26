from db import base

class Peao:
    def __init__(self):
        pass

    def cores_disponiveis(self):
        cores = base.peoes_cores_disponiveis
        return cores

    def remove_cor(self, cor):
        cores = base.peoes_cores_disponiveis
        cores.remove(cor)
        base.peoes_cores_disponiveis = cores
