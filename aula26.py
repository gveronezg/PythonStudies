"""
operadores lógicos
and, or, not
in e not in

# Verdadeiro e  Falso       = Verdadeiro
#comparacao1 and comparacao2

# Verdadeiro ou Falso       = Verdadeiro
#comparacao1 and comparacao2

#
a=2
b=3

if b > a:
    print('B é maior que A.')
else:
    print('A é maior que B.')

# PODEMOS USAR O not PARA VERIFICAR SE UMA VARIÁVEL ESTA VAZIA, POR EXEMPLO:
c = ''
d = 0

if not (c and d):
    print('Por favor não deixe de preencher c e/ou d.')

teyba = "Xuleiba"

if 'i' in teyba:
    print(f'Existe a letra i na {teyba}')
else:
    print('Não existe.')
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuarioBd = 'Gabriel'
senhaBd = '123456'

if usuario == usuarioBd and senha == senhaBd:
    print('Você esta logado no sistema.')
else:
    print('Usuário ou senha inválidos.')