from os import path
import time

def dadosArquivo():
    arquivoExiste = path.exists('NovoArquivo.txt')
    éDiretório = path.isdir('NovoArquivo.txt')
    pathArquivo = path.realpath('NovoArquivo.txt')
    pathRelativo = path.relpath('NovoArquivo.txt')
    dataCriacao = time.ctime(path.getctime('NovoArquivo.txt'))
    dataModificacao = time.ctime(path.getmtime('NovoArquivo.txt'))
    print(arquivoExiste)
    print(éDiretório)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)
dadosArquivo()
