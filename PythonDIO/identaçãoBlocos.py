def sacar(valor: float):
    saldo = 500
    if saldo >= valor:
        print('Valor sacado!')
    print('Volte sempre!')


def depositar(valor: float):
    saldo = 500
    saldo += valor

sacar(1000)

