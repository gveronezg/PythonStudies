import sqlite3

def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def selecionaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha)

def manipulacaoDados():
    comandoINSERT = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste1', 'XX1', 'Teste Inclusão1')"
    pathBD = '/media/champslinux/HD/Python/PythonStudies/PythonLinkedIn/mydatabase.db'
    comandoSELECT = 'SELECT nome_estado, sigla_estado, nome_capital FROM estados'
    manipulaDados(pathBD, comandoINSERT)
    selecionaDados(pathBD, comandoSELECT)

manipulacaoDados()