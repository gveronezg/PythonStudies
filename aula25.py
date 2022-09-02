'''
operadores relacionais
'''
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

muitoJovem = 20
muitoVelho = 30

if idade >= muitoJovem and idade <= muitoVelho:
    print(f'{nome}, você pode pegar emprestimo se quiser')
else:
    print(f'{nome}, infelizmente pegar empréstimo não é uma opção')