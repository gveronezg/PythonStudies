def loopWhile():
    x = 0
    while(x<5):
        print(x)
        x=x+1

loopWhile()

def loopFor():
    for x in range(5,10):
        print(x)

loopFor()

def loopArray():
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    for d in dias:
        print(d, end="-feira\n")

loopArray()

def loopEnum():
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    for i, d in enumerate(dias):
        print(i, d, end="-feira\n")

loopEnum()