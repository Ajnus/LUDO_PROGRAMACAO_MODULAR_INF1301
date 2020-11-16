from db.dominioTabelas import Session as session, Peao, Jogador, atualizarBD


# Busca na BD os peões e seus respectivos codigos, que estão na base
def contarPeaoNaBase(codigoJogador):
    codigos = []
    try:
        corPeao = session.query(Jogador.corpeao).filter_by(codigo=codigoJogador).one()
        peoesNaBase = session.query(Peao.codigo).filter_by(cor=corPeao, posicao=0).all()

        for codigo in range(len(peoesNaBase)):
            codigos.append(peoesNaBase[codigo][0])

        qtdPeoesNaBase = len(codigos)
        return qtdPeoesNaBase, codigos

    except:
        return 1