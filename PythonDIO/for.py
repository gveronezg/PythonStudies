texto = input('Digite um texto para que as vogais sejam destacadas\n:')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
print()

for numero in range(0,18+1):
    print(numero, end='')
print()

for numero in list(range(18+1)):
    print(numero, end='')
print()

for numero in range(0,18+1,2):
    print(numero, end='')
print()