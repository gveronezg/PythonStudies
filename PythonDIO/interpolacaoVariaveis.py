# OLD STYLE

nome = 'Gabriel'
idade = 27
profissao = 'Desenvolvedor'
linguagem = 'Python'
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

nome = 'Eliene'
idade = 29
profissao = 'Psicóloga'
abordagem = 'Psicodramática'
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e utilizo a abordagem {}.".format(nome, idade, profissao, abordagem))

nome = 'Gabriel'
idade = 27
profissao = 'Analista'
linguagem = 'Python'
print("Olá, me chamo {2}. Eu tenho {3} anos de idade, trabalho como {0} e utilizo a linguagem {1}.".format(profissao, linguagem, nome, idade))

print("Olá, me chamo {name}. Eu tenho {old} anos de idade, trabalho como {profession} e utilizo a linguagem {language}.".format(
    name=nome, old=idade, profession=profissao, language=linguagem))

#definindo um dicionário
dados = {'name': 'Gabriel', 'old': '27', 'profession': 'Analista', 'lenguage': 'Python'}

print("Olá, me chamo {name}. Eu tenho {old} anos de idade, trabalho como {profession} e utilizo a linguagem {lenguage}.".format(**dados))

# f-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e utilizo a linguagem {linguagem}.")

PI = 3.14159

# entre chaves podemos definir a quantidade de espaços e casas decimais do numero printado
# {variavel:x.yf} onde x é a quantidade de espaços e y é o numero de casas decimais
print(f'Valor de PI: {PI:.3f}') # = "Valor de PI: 3.14"
print(f'Valor de PI: {PI:10.2f}') # = "Valor de PI:      3.14"