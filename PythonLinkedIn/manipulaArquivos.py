import os
from os import path
import shutil
from shutil import make_archive
import zipfile

def copiaArquivo():
    arq = "NovoArquivo.txt"
    if path.exists(arq):
        pathAtual = path.realpath(arq)
        novoPath = pathAtual + '.bkp'
        shutil.copy(pathAtual, novoPath)
        shutil.copystat(pathAtual, novoPath)
#copiaArquivo()

def renomearArquivo():
    arq = "NovoArquivo.txt.bkp"
    if path.exists(arq):
        os.rename(arq, 'ArquivoAlterado.txt')
#renomearArquivo()

def criaZipModo1():
    arq = "arquivoCompactado.txt"
    shutil.make_archive(arq, 'zip', '/media/champslinux/HD/Python/PythonStudies/PythonLinkedIn')
#criaZipModo1()

def criaZipModo2():
    with zipfile.ZipFile("arquivoZipModo2.zip", 'w') as novoZip:
        novoZip.write('ArquivoAlterado.txt')
        novoZip.write('NovoArquivo.txt')
        novoZip.write('arquivoCompactado.txt.zip')
#criaZipModo2()

def deletaArquivo():
    os.remove('arquivoZipModo2.zip')
#deletaArquivo()