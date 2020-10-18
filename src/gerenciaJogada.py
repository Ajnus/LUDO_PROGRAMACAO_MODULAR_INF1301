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
            empate.append(primeiroJogador)
            empate.append(jogador[id])

    if len(empate) != 0:
        return empate
    return primeiroJogador
