"""
O (is) é uma expressão de identidade pois ele retorna True quando os 2 objetos/variaveis comparados ocupam exatamente o mesmo espaço de memória de processamento
"""

saldo, limite = 200, 200

print(saldo is limite)
print(saldo is not limite)

limite = 100

print(saldo is limite)
print(saldo is not limite)