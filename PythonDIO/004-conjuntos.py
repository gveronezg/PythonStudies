"""
Um conjunto é uma coleção de objetos com elementos únicos, ou seja, que não se repetem.
"""
# CRIANDO SETS

# para eliminar elementos duplicados de uma lista, basta apenas passar o construitor set que ele fará da lista um conjunto
set([1,2,3,1,3,4])

set("abacaxi")

set(("palio", "gol", "celta", "palio"))

# criando um conjunto utilizando chaves
linguagens = {"python", "java", "python", "css", "html"}
print(linguagens)

# Conjuntos não possuem indice, para acessar um determinado elemento pelo indice, é nessário converte-lo em uma lista
numeros = {1,2,3,2,1}
numeros = list(numeros)
print(numeros[0])
# Uma outra forma é printar os elementos um a um através do conjunto
numeros = {1,2,3,2,1}
for numero in numeros:
    print(numero)
# É possivel contar com a função enumerate para isso
carros = {'gol', 'celta', 'palio'}
for indice, carro in enumerate(carros):
    print(f'Indice {indice} = Carro: {carro}')

# COMPARAÇÕES DE CONJUNTOS

# {}.union
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.union(conjunto_b))

# {}.intersection
print(conjunto_a.intersection(conjunto_b))

# {}.difference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# {}.symmetric_difference
print(conjunto_a.symmetric_difference(conjunto_b))

# {}.issubset = um conjunto contem o outro?
conjunto_b = {4,1,2,5,6,3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# {}.isdisjoint = um conjunto não toca no outro?
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# {}.add
sorteio = {1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

# {}.copy
sorteio.copy()
print(sorteio)

# {}.clear
sorteio.clear()
print(sorteio)

# {}.discard
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
numeros.discard(1)
numeros.discard(41)
print(numeros)

# {}.pop = sempre tirar o valor da esquerda pra direita
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros)

# {}.remove = igual ao .discard, porém se o elemento não existir ele apresentará um erro
numeros.remove(7)
print(numeros)

# {}len
print(len(numeros))

# {}in = serve para verificar se um elemento está no conjunto
print(1 in numeros)
print(9 in numeros)
print(3 in numeros)
print(5 in numeros)