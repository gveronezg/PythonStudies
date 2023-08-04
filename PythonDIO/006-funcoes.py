    # ESTUDO APROFUNDADO SOBRE FUNÇÕES
# a função é um bloco de código onde seu nome é seu identificador
# podemos chamar os parâmetros da função de entrada
# já aquilo que ela retorna é a sua saida

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem2(nome):
    print(f'Seja bem vindo(a) {nome}!')

def exibir_mensagem3(nome="Anônimo"):
    print(f'Seja bem vindo(a) {nome}!')

exibir_mensagem()
exibir_mensagem2('Gabriel')
exibir_mensagem3()

# utilizando o return em funções

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(13))

# ARGUMENTOS NOMEADOS

def salvar_carro(marca,modelo,ano,placa):
    print(f'Carro inserido com sucesso! {marca};{modelo};{ano};{placa}')

salvar_carro('Fiat','Palio',1999,'ABC1234') # é obrigatório passar na ordem correta para manter os valores corretos
salvar_carro(marca='Fiat',modelo='Palio',ano=1999,placa='ABC1234') # os argumentos precisam ser exatamentos os mesmos dos parâmetros da função
salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':1999,'placa':'ABC1234'}) # passando um dicionário como argumento para a função

# ARGS E KWARGS

def exibir_poema(data_extenso,*args,**kwargs):
    texto = "\n".join(args) # concatenando todas as strings args com \n deixando cada uma em uma linha
    meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)
# função(data_por_extenso, titulo e frases como argumentos, ator e ano como chaves de argumentos)
exibir_poema("Sexta-Feira, 4 de Agosto de 2023", "Zen of Python", "Beautiful is better than ugly...", actor="Tim Peters", ano=1999)

# PARÂMETROS ESPECIAIS

# função f(somente, por, posição, /, somente, por, chave)
def criar_carro(modelo, ano, placa, /, marca, motor, flex):
    print(modelo, ano, placa, marca, motor, flex)
criar_carro("gol", 2000, "GVG-1996", flex=False, marca="VW", motor=1.0)

# função f(*, somente, por, chaves)
def carros(*, modelo, ano, placa, marca, motor, flex):
    print(modelo, ano, placa, marca, motor, flex)
carros(flex=False, modelo="uno", ano=1996, placa="TOP-4321", marca="Fiat", motor=1.0)

# função hibrida...
def cars(modelo, ano, placa, /, *, marca, motor, flex):
    print(modelo, ano, placa, marca, motor, flex)
cars("chevete", 1989, "JRJ-1996", flex=False, marca="chevrolet", motor=1.6)

# OBJETOS DE PRIMEIRA CLASSE

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação é: {resultado}')

exibir_resultado(7,5,somar)
exibir_resultado(7,5,subtrair)

sub = subtrair

print(sub(10,5))

# ESCOPO LOCAL E ESCOPO GLOBAL

salario = 2000

def salario_bonus(bonus, lista):
    copia_lista = lista.copy()
    copia_lista.append(2)
    print(f'Copia da lista: {copia_lista}')

    global salario # essa linha é indispensável para trazer a variável de escopo blocal para o escopo local da função
    salario += bonus
    return salario

lista = [1]
print(salario_bonus(500, lista))
print(lista)