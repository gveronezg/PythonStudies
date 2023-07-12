print("Hello World")

f = 0
print(f)

f = 'abc'
print(f)

print('string'+str(123))

def AlgumaFuncao():
    'declarando a variável (f) como (global) seu valor se estende até mesmo para fora da função'
    global f
    f = "def"
    print(f)
AlgumaFuncao()

print(f)