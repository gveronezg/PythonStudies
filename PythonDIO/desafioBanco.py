menu = """
    Bem Vindo ao PyBank
    Entre com a letra da opção desejada

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [f] Fechar

"""
saldo = 0
saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao.lower() == 'd':
        print()
        depositando = float(input('Entre com o valor a ser depositado:\n'))
        if depositando > 0:
            saldo += depositando
            extrato += f'Deposito de R$ {depositando:.2f}\n'
            print(f'Valor de R$ {depositando:.2f} depositado com sucesso, obrigado pela confiança.')
        else:
            print('Não é possivel depositar valores negativos.')

    elif opcao.lower() == 's':
        print()
        sacando = float(input('Entre com o valor a ser sacado:\n'))
        if sacando < 0:
            print('Impossível sacar um valor negativo.')
        elif sacando > saldo:
            print(f'Infelizmente seu saldo atual é de apenas R$ {saldo:.2f} Solicite um valor igual ou menor que este.')
        elif numero_saques == LIMITE_SAQUES:
            print('O límite diário de 3 saques por dia já foi atingido, fique avonte para sacar mais amanhã.')
        else:
            if sacando > saque:
                print('Solicite um valor igual ou menor a 500 reais pois este é o limite por saque.')
            else:
                numero_saques += 1
                saldo -= sacando
                print(f'Valor de R$ {sacando:.2f} sacado com sucesso, retire as cédulas abaixo.')
                extrato += f'Saque de R$ {sacando:.2f}\n'

    elif opcao.lower() == 'e':
        print()
        print('Confira abaixo seu extrato:')
        print('---------------------------------------')
        print()
        print(extrato)
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
        print('---------------------------------------')

    elif opcao.lower() == 'f':
        print()
        print('Fechando o sistema!')
        break

    else:
        print()
        print('Opção inválida, por favor selecione a letra da opção desejada.')
    