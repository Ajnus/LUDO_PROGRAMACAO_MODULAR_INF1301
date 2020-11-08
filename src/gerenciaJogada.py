from db import base

def definirPrimeiroJogador(resultadoRolagemDado):
    id = maior = 0
    numeroSorteado = 1
    primeiroJogador = -1
    empate = []

    for jogador in resultadoRolagemDado:
        if jogador[numeroSorteado] > maior:
            maior = jogador[numeroSorteado]
            primeiroJogador = jogador[id]
            empate = []

        elif jogador[numeroSorteado] == maior:
            maior = jogador[numeroSorteado]
            if primeiroJogador not in empate:
                empate.append(primeiroJogador)
            empate.append(jogador[id])

    if len(empate) != 0:
        return empate
    return primeiroJogador

def defineVencedor(idJogador):
    jogador = base.jogadoresCadastrados[idJogador]
    peaoJogador = base.peoesCadastrados[jogador[1]]
    if (len(peaoJogador) == 0)
        print(idJogador, "é o vencedor!") #usei o print por enquanto para testar a funcao, futuramente exibir na tela do jogo
        return idJogador
    return -1
