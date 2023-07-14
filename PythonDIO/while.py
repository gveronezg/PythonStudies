opcao = -1

# Por conta do (if) o bloco será executado apenas 1 vez. 
if opcao != 0:
    opcao = int(input('[9] Sacar\n[8] Extrato\n[0] Sair\n:'))

    if opcao == 9:
        print('Sacando...')
    elif opcao == 8:
        print('Exibindo o extrato...')

# Por conta do (while) o bloco abaixo será executado infinitas vezes até que o usuário entre com a opção 0 para sair.
while opcao != 0:
    opcao = int(input('[1] Sacar\n[2] Extrato\n[0] Sair\n:'))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigado, volte sempre!')