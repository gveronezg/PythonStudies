frutas = ['laranja', 'manga', 'pera', 'maça'] # construindo uma lista
print(frutas)
legumes = [] # construindo uma lista vazia
print(legumes)
linguagem = list('python') # construindo uma lista com um argumento interável
print(linguagem)
numeros = list(range(50)) # criando uma lista com os numeros retornados por uma função
print(numeros)
carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True] # lista com vários tipos de elementos
print(carro)

"""
podemos acessar a lista e obter um elemento através do seu número de indice
"""
print(frutas[2])
print(frutas[0])
"""
construindo uma matriz 3x3
"""
matriz = [
    [1,"a",3,'x'],
    ["b",5,6,"z",23,44],
    [7,8,"c",9,21,"o","i"]
]
print(matriz[0])       # isto retorna o valor da LINHA 0
print(matriz[0][0])    # isto retorna um elemento especifico de uma linha e coluna
print(matriz[0][-1])   # isto retorna o ultimo elemento a direita da linha
print(matriz[-1][-1])  # isto retorna o ultimo elemento a direita da ultima linha a baixo
"""
fatiando uma palavra com python
"""
print(linguagem)
print(linguagem[2:])    # do indice 2 até o fim
print(linguagem[:2])    # do início até antes do indice 2
print(linguagem[1:3])   # do indice 1 até antes do indice 3
print(linguagem[0:3:2]) # do indice 0 até antes do indice 3 de 2 em 2
print(linguagem[::])    # do início ao fim
print(linguagem[::-1])  # do fim ao início
"""
percorrendo uma lista através do for
"""
for info in carro:
    print(info)
"""
criando uma lista a partir de outra lista
"""
pares = []
impares = []
"""
for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero) # o append adiciona o parametro dentro da lista que o chama
    else:
        impares.append(numero) # o append adiciona o parametro dentro da lista que o chama
"""
    # pode tambem ser criado desta forma abaixo
# [retorno que recebo FOR "i" IN "lista" IF (condição)]
pares = [numero for numero in numeros if numero % 2 ==0]
impares = [numero for numero in numeros if numero % 2 !=0]
print(pares)
print(impares)
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)