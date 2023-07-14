print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 500
saque = 200
limite = 150
conta_especial = True

'Usando o (and) todas as expressão precisam ser True para que seja retornado True'
print(saldo >= saque and saque <= limite)

'Usando o (or) todas as expressão precisam ser False para que seja retornado False'
print(saldo >= saque or saque <= limite)

'Aqui foi criado uma lista vazia que em python é considerada com valor False'
contatos_emergencia = []

'2000 é maior que 1500, por isso o valor dessa expressão é True. Porém quando usado o not, o valor da expressão é invertido, neste caso com o not ele retornará False'
print(not 2000 > 1500)

'Aqui temos o comando not transformando essa lista vazia com valor False para True'
print(not contatos_emergencia)

'Essa string é True por conter dados e não ser uma string vazia, porém com o not ela passa a retornar False'
print(not "saque 1500;")

'Essa string é falsa por se tratar de uma string vazia, então quando aplicado o not ela se torna True'
print(not "")

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp1)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)