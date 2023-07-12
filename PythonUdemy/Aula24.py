'''
Condições IF, ELIF e ELSE - Aula 4
'''
if False:
    print("Verdadeiro.")
    num1=2
    num2=4
    print(num1+num2)
elif True:
    print("Agora é verdadeiro.")
    print(22+22)
elif False:
    print('Mais uma verdadeira.')
    nome=input("Qual o seu nome? ")
    print(f'Seu nome é {nome}.')
else:
    print('Não é verdadeira.')
    print('A minha expressão não é verdadeira.')