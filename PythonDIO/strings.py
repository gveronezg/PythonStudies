curso = 'pYtHon'

# (upper()) converte toda a string para maiusculo
print(curso.upper()) # = "PYTHON"

# (lower()) converte toda a string para minusculo
print(curso.lower()) # = "python"

# (title()) converte a primeira letra para maiusculo e as demais para minusculo
print(curso.title()) # = "Python"

curso = '   Python '

# (strip()) remove os espaços em branco da esquerda e da direita
print(curso.strip()) # = "Python"

# (lstrip()) remove os espaços em branco da esquerda apenas
print(curso.lstrip()) # = "Python "

# (rstrip()) remove os espaços em branco da direita apenas
print(curso.rstrip()) # = "   Python"

curso = 'Python'

# (center(numero, 'caracter')) centraliza a palavra entre o numero total de caracteres adicionados
# como exemplo vou centralizar a palavra entre um total de 10 caracteres completando com $
print(curso.center(10,"$")) # = "$$Python$$"
# se não adicionado o segundo parametro com o caracter, será usado o espaço em branco no preenchimento

# ('caracter'.join(variavel)) adiciona o caracter entre os caracteres da variavel string
# como exemplo vou adicionar $ entre as letras da string
print('$'.join(curso)) # = "P$y$t$h$o$n"

for letra in curso:
    print(letra, end='-')
print()