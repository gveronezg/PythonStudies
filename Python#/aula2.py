"""
Notas:
    Aula de automação com python
    pyautogui é um módelo de automação do python para que o proprio código execute comandos dentro da interface

Passo a Passo do projeto
    1º Entrar no sistema
        Abrir o navegador
        Acessar o link
            https://dlp.hashtagtreinamentos.com/python/intensivao/login
        Fazer login
    2º Importar a base de dados de produtos para cadastrar
    3º Cadastrar o produto
    4º Repetir o processo de cadastro com todos os produtos
"""
import pandas as pd
import time # módulo de espera independente. Exemplo: Chamado na linha 36 solicitando espera de 3 segundos.

import pyautogui
DIGITA = (pyautogui.write) # -> escreve um texto
APERTA = (pyautogui.press) # -> aperta 1 tecla
CLICA = (pyautogui.click) # -> clica com o botão esquerdo do mouse

# regra de espera para que o código execute com um "delay"
pyautogui.PAUSE = 0.3

    # 1º Entrando no sistema

    # Abrindo o navegador
pyautogui.press("win") # aperta a tecla do windows
pyautogui.write('chrome') # escreve chrome
pyautogui.press('enter') # aperta a tecla enter

    # Abrindo uma aba anônima usando comando "hotkey" combinado de 3 teclas
# pyautogui.hotkey("ctrl", "shift", 'n')

    # Acessando o link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1.2)
pyautogui.hotkey('win', 'up')

    # Pegando a posição de onde eu deixar o ponteiro do mouse após 3 segundos de clicar na tecla enter
# print(pyautogui.position())

    # Fazendo login
pyautogui.click(x=833, y=-671)
pyautogui.write("champs")

" A partir de agora vou usar as variáveis de atalho que criei no inicio do código... "

APERTA('tab')
DIGITA('senha')
APERTA('tab')
APERTA('enter')
time.sleep(1)

    # 2º Importando a base de dados de produtos para cadastrar
    
bd = pd.read_csv("produtos.csv")
print(bd)
    
    # 3º Cadastrando o 1º produto

# linha = 0 # iniciando na primeira linha do BD

for linha in bd.index:
    pyautogui.click(x=861, y=-801) # clicando no campo de código do sistema

        # pegando no BD o valor do campo que vamos preencher
    codigo = bd.loc[linha, "codigo"] # usamos a função "loc" passando 2 parametros, o numero da linha e o nome da coluna.
    pyautogui.write(str(codigo)) # escrevendo no campo o valor que pegamos no BD sempre em tipo string 
    APERTA('tab') # passando para o próximo campo
    pyautogui.write(str(bd.loc[linha, "marca"])) # escrevendo no campo o valor que pegamos no BD diretamente usando o (loc) 
    APERTA('tab')
    pyautogui.write(str(bd.loc[linha, "tipo"]))
    APERTA('tab')
    pyautogui.write(str(bd.loc[linha, "categoria"]))
    APERTA('tab')
    pyautogui.write(str(bd.loc[linha, "preco_unitario"]))
    APERTA('tab')
    pyautogui.write(str(bd.loc[linha, "custo"]))
    APERTA('tab')
    obs = bd.loc[linha, "obs"]
    if not pd.isna(obs): # verificando através do panda se a célula é vazia
        pyautogui.write(str(obs))
    else:
        pyautogui.write("")
    APERTA('tab')
    APERTA('enter')

    # 4º Repetir o processo de cadastro com todos os produtos
    
    # dando scroll de tudo para cima
# pyautogui.scroll(5000)
APERTA('pgup')