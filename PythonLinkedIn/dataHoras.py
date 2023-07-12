from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def manipulaDataHora():
    hoje = date.today()
    print('Hoje é:', hoje)
    print('Partes da data:', hoje.day, hoje.month, hoje.year)
    print('Numero do dia da semana:', hoje.weekday())
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    print('Nome do dia da semana:', dias[hoje.weekday()])
    data = datetime.now()
    print('Data e hora:', data)
    tempo = datetime.time(data)
    print('Hora atual:', tempo)
#manipulaDataHora()

def formataDataHora():
    hoje = datetime.now()
    print(hoje.strftime('O ano é: %y'))
    print(hoje.strftime('Data e hoje local: %c'))
    print(hoje.strftime('A hora atual é: %I:%M:%S %p'))
formataDataHora()

def deltaTempo():
    delta = timedelta(days = 86, hours = 8532, minutes = 7645)
    print(delta)
    hoje = datetime.now()
    print('Data no futuro:', hoje+delta)
    print('Data no passado:', hoje-delta)
deltaTempo()