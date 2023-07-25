"""
    A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
"""

maior_idade = 18
idade = int(input('Entre com sua idade: '))

if idade >= maior_idade:
    def passou():
        resposta = input('Você passou em todos os testes?\nSim OU Não: ')
        if resposta.lower() == 'sim':
            return True
        elif resposta.lower() in ['não', 'nao']:
            return False
        else:
            print('Opção inválida, digite novamente por favor.')
            return passou()
    aprovado = passou()

    if aprovado == True:
        print('Você já é maior de idade e passou nos testes. Pode agendar a retirada da sua CNH.')
    elif not aprovado:
        print('Para obter sua CNH você precisa passar em todos os testes.')
else:
    print('Após completar 18 anos e passar nos testes, você poderá tirar sua CNH.')