from db import base

def criarPeoes():
    cores = base.peoesCoresDisponiveis
    id = 0
    posicao = 0
    for cor in cores:
        listaIds = []
        for i in range(4):
            listaIds.append([id, posicao])
            id += 1
        armazenaPeao(listaIds, cor)

def armazenaPeao(listaId, corPeao):
    base.peoesCadastrados[corPeao] = listaId

def coresDisponiveis():
    cores = base.peoesCoresDisponiveis
    return cores

def removeCor(cor):
    cores = base.peoesCoresDisponiveis
    cores.remove(cor)
    base.peoesCoresDisponiveis = cores

if __name__ == '__main__':
    criarPeoes()
    print(base.peoesCadastrados)