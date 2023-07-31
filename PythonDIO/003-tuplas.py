"""
TUPLAS são estruturas IMUTÁVEIS
enquanto as listas são mutáveis
"""

letras = tuple("python")

numeros = tuple([1,2,3,4,5])

# sempre deixar uma ultima virgura dentro dos parênteses
pais = ("Brasil",)

frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[0])
print(frutas[2])

# declarando uma tupla que é composta de outras 3 tuplas

matriz = (
    (1,"a",2),
    ("b",3,4),
    (6,5,"c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

tupla = ('p', 'y', 't', 'h', 'o', 'n',)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# MÉTODOS

# ().count
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# ().index

print(tupla.index("t"))
print(tupla.index("o"))
print(tupla.index("p"))

# len()
print(len(tupla))