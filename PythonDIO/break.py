# Por conta do (while) o bloco abaixo será executado infinitas vezes até que o usuário entre com a opção 0 para sair.
while True:
    numero = int(input('Entre com um número qualquer ou entre com o número 5 para encerrar: '))

    if numero == 5:
        print('Encerrando em...')
        break

    if numero == 22:
        print('Desculpe, essa opção é inelegível.')
        continue
    
    print(numero)

for numero in reversed(range(6)):
    if numero == 0:
        break
    print(numero, end=', ')
print('Encerrado!')