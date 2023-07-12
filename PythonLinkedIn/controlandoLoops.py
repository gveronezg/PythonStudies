def loopBreak():
    for x in range(5,10):
        if x == 7:
            break
            # Interrompe a execução do loop
        print('O valor de x é:', x)

#loopBreak()

def loopContinue():
    for x in range(5,10):
        if x == 7:
            continue
            # Este comando (continue) faz com que o loop continue seu processo sem que seja pausado. Ele interrempe apenas 1 execução
        print("O valor de x é:", x)

loopContinue()