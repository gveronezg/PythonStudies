import textwrap

def menu():
    menu = """
    Bem Vindo ao PyBank
    Entre com a letra da opção desejada
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tListar Contas
    [u]\tNovo Usuário
    [f]\tFechar

    """
    return input(textwrap.dedent(menu))

def depositando(saldo, valor, extrato, /): # A /(barra) no final, significa que tudo deve ser recebido de forma posicional. OU SEJA. Passando apenas a variável
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R$ {valor:.2f}\n'
        print(f'\nValor de R$ {valor:.2f} depositado com sucesso, obrigado pela confiança.')
    else:
        print('\nNão é possivel depositar valores negativos.')
    return saldo, extrato

def sacando(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # O *(asterisco) no início, significa que tudo deve ser recebido de forma nomeada. OU SEJA. Passando apenas a variável
    saldo_insuficiente = valor > saldo
    limite_estourado = valor > limite
    quarto_saque = numero_saques > limite_saques
    if saldo_insuficiente:
        print(f'Infelizmente seu saldo atual é de apenas R$ {saldo:.2f} Solicite um valor igual ou menor que este.')
    elif quarto_saque:
        print('O límite diário de 3 saques por dia já foi atingido, fique avontade para sacar mais amanhã.')
    elif limite_estourado:
        print('Solicite um valor igual ou menor que 500 reais pois este é o limite por saque.')
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        print(f'Valor de R$ {valor:.2f} sacado com sucesso, retire as cédulas abaixo.')
        extrato += f'Saque de R$ {valor:.2f}\n'
    else:
        print('Impossível sacar um valor negativo.')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): # Por conta da / e do *. o saldo será recebido de forma posicional e o extrato de forma nomeada
    print('Confira abaixo seu extrato:')
    print('---------------------------------------')
    print()
    print('Não foram realizadas movimentações.'if not extrato else extrato)
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print('---------------------------------------')

def nova_conta(usuarios):
    cpf = input("Entre somente com os números do seu CPF: ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com este CPF!")
        return
    nome = input("Entre com seu nome completo: ")
    data_nascimento = input("Entre com sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Entre com o endereço (logradouro; nro; bairro; cidade; estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def verifica_usuario(cpf, usuarios):
    usuarios_verificados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_verificados[0] if usuarios_verificados else None

def criar_conta(agencia, nro_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = verifica_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": nro_conta, "usuario": usuario}
    print("Usuário não encontrado, nova conta não criada!") 


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))
            
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao.lower() == 'd':
            valor = float(input('Entre com o valor a ser depositado:\n'))
            saldo, extrato = depositando(saldo,valor,extrato)

        elif opcao.lower() == 's':
            valor = float(input('Entre com o valor a ser sacado:\n'))
            saldo, extrato = sacando(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )
        
        elif opcao.lower() == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.lower() == 'n':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao.lower() == 'l':
            listar_contas(contas)

        elif opcao.lower() == 'u':
            nova_conta(usuarios)

        elif opcao.lower() == 'f':
            print()
            print('Fechando o sistema!')
            break

        else:
            print()
            print('Opção inválida, por favor selecione a letra da opção desejada.')
    
main()