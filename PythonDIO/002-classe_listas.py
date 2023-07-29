# função que preenche a lista
def preenchendo():
    lista = []
    lista.append(1)
    lista.append("Python")
    lista.append([40,30,20])
    return lista

lista = preenchendo()
print(lista)

# função clear limpa a lista
lista.clear()
print(lista)

lista = preenchendo()
print(lista)

# função copy copia a lista
copia_lista = lista.copy()
print(copia_lista)

# para provar se são copias porém não são uma unica lista, vamos printar seus ids
print(id(copia_lista), id(lista)) # 140404283981184 140404279281472

# adicionando elementos repitidos na lista usando a função extend
lista.extend(['vermelho', 'azul', 'verde', 'azul', 'amarelo'])

# contando cada elemento adicionado
print(lista.count('vermelho'))
print(lista.count('azul'))
print(lista.count('verde'))
print(lista)
print(copia_lista)

# printando o index de um elemento da tabela
print(lista.index("verde"))
print(lista.index(1))

# excluindo o ultimo elemento de uma lista através do pop
print(lista)
lista.pop()
print(lista)
# excluindo um elemento de uma lista através do pop usando o indice como parametro
print(lista)
lista.pop(2)
print(lista)

# excluindo um elemento de uma lista através do remove usando o próprio elemento como parâmetro
print(lista)
lista.pop()
print(lista)

# espelhando uma lista usando o método reverse 
lista.reverse()
print(lista)

lista.clear()
lista.extend(['vermelho', 'azul', 'verde', 'azul', 'amarelo', ".py", ".js", '.html', '.css', '.dart'])

# listando por ordem alfabética os elementos da lista utilizando o método sort
lista.sort()
print(lista)

# listando por ordem alfabética ao contrário os elementos da lista
lista.sort(reverse=True)
print(lista)

# ordenando a lista pelo tamanho dos elementos
lista.sort(key=lambda x:len(x))
print(lista)

# ordenando a lista pelo tamanho dos elementos de forma decrescente
lista.sort(key=lambda x:len(x), reverse=True)
print(lista)

# visualizando o tamanho da lista através da função len
print(len(lista))

# listando do maios para o menor elemento da lista usando a função sorted
sorted(lista, key=lambda x:len(x))
print(lista)
