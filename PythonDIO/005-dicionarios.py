"""
para declararmos um dicionário vamos atribuir um nome seguido de = e abrir e fechar {}
ele sempre será composto de valores pares
chave: valor
"""

dicionario = {"nome": 'Gabriel', "idade": 27}

# também podemos declarar um dicionário usando o construtor dict()
dicionario = dict(nome='Gabriel', idade=27)

# e também podemos adicionar uma nova chave num dicionário já criado desta forma
dicionario["telefone"] = '3333-1234'

# acessando e printando seus valores através da chave
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["telefone"])

# alterando os valores das chaves
dicionario["nome"] = 'Eliene'
dicionario["idade"] = 29
dicionario["telefone"] = '9988-1781'

# podemos também criar um dicionário dentro de outro dicionário tendo assim um dicionário aninhado, exemplo
contatos = {
    "guilherme@gmail.com": {"nome": 'Guilherme', "telefone": '3333-2221'},
    "geovane@gmail.com": {"nome": 'Geovane', "telefone": '3443-2121'},
    "eduardo@gmail.com": {"nome": 'Eduardo', "telefone": '3344-9871'},
    "gustavo@gmail.com": {"nome": 'Gustavo', "telefone": '3333-7766'},
}

# acessando um valor de chave especifico de uma das chaves desse dicionário
print(contatos["geovane@gmail.com"]["telefone"])

# 2 formas de percorrer um dicionário usando o for
    
    # forma não utilizada
for chave in contatos:
    print(chave, contatos[chave])

    # forma utilizada
for chave, valor in contatos.items():
    print(chave, valor)

# MÉTODOS DA CLASSE DICT

# {}.copy
copia = contatos.copy()
# esse método quando usado atribui uma cópia do dicionário á variável
copia["guilherme@gmail.com"]['nome'] = 'Gui'
print(copia)

# {}.fromkeys
copia = dict.fromkeys(["CEP","Cidade"])
# usando esse método é criado e atribuido um novo dicionário á variável, com as chaves passadas entre conchetes porém com valores "None"
print(copia)
# já dessa forma o funcionamento é o mesmo, porém ao invés de "None" as chaves receberão o valor passado no ultimo parâmetro do método
copia = dict.fromkeys(["Cidade","CEP"],"valorX")
print(copia)

# {}.get
# o método get é utilizado para retornar o valor da chave em parametro
# no entanto quando não encontrada a chave ele retornará o valor "None"
print(contatos.get("chave"))
# podendo também retornar um valor definido caso a chave não exista
print(contatos.get("chave",{'Essa chave não existe no dicionário!'}))
# caso exista a chave ele ignora o valor definido
print(contatos.get("guilherme@gmail.com",{'Essa chave não existe no dicionário!'}))

# {}.items
copia.items()
# esse método retorna uma lista de tuplas de cada chave do dicionários
print(copia.items())

# {}.keys
contatos.keys()
# esse método retorna somente as chaves do dicionário
print(contatos.keys())

# {}.pop
print(contatos.pop("guilherme@gmail.com","Chave inexistente não removida!"))
# esse método remove a chave do dicionário caso encontre
print(contatos.pop("chave","Chave inexistente não removida!"))
# caso a chave não exista no dicionário ele retorna a mensagem pré definida como parâmetro

# {}.popitem
print(contatos.popitem())
# nesse método não se irforma nada pois o único objetivo dele é eliminar o ultimo item do dicionário

# {}.setdefault
teste = dict(A=1,B=2,C=3,D=4,E=5)
print(teste.setdefault("B",'Bê'))
# esse método retorna o valor da chave quando ela é encontrada
print(teste.setdefault("F",'éfi'))
# e caso a chave não exista ele a cria e atribui o valor setado á ela

# {}.update
teste.update()
# o método update atualiza o valor da chave caso encontre
teste.update({"B":{"fonema":'bê',"ordem":'segunda_letra'}})
# caso não encontre ele atualiza o dicionário com a nova chave 
teste.update({"G":{"fonema":'gê',"ordem":'sétima_letra'}})
print(teste)

# {}.values
print(teste.values())
# este método retorna somente as valores das chave do dicionário

# {}.in
resultado = "geovane@gmail.com" in contatos
# o método in é usado para verificar se existe determinada chave no dicionário
print(resultado)
resultado = "guilherme@gmail.com" in contatos
# o método in é usado para verificar se existe determinada chave no dicionário, caso não existe é retornado FALSE
print(resultado)
resultado = "idade" in contatos["eduardo@gmail.com"]
# e com ele também é possivel fazer a mesma verificação dentro de dicionários aninhados
print(resultado)
resultado = "telefone" in contatos["eduardo@gmail.com"]
print(resultado)

# {}.del
print(teste)
del teste["B"]["ordem"]
# o método del pode ser usado para remover uma chave e seu valor, de uma chave
del teste['G']
# ou até mesmo remover a chave inteira do dicionário
print(teste)

del contatos
# para apagar o dicionário inteiro basta colocar del seguido do nome do dicionário a ser deletado