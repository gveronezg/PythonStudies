#    *VERIFICANDO O TAMANHO DA STR COM A FUNÇÃO LEN*
usuario = input('Digite seu usuário: ')
qtdCaracteres = len(usuario)
print(usuario,qtdCaracteres,type(qtdCaracteres))
if qtdCaracteres < 7:
    print('Você precisa digitar pelo menos 7 letras.')
else:
    print('Você foi cadastrado no sistema.')

#    *SOMANDO AS QUANTIDADES RETORNADAS POR LEN DE DUAS STR*
string1=input('Digite alguma coisa: ')
string2=input('Digite outra coisa: ')
print(f'A quantidade total de caracteres digitados foi: {len(string1)+len(string2)}')

#    *MOSTRANDO O QUE A FUNÇÃO LEN FAZ "POR BAIXO DOS PANOS"
string2 = 'teyba'
print(len(string2))
print(string2.__len__())