def escreveArquivo():
    arquivo = open('NovoArquivo.txt', 'w+')
    arquivo.write('Linha gerada com a função "EscreveAquivo" \r\n')
    arquivo.close()
#escreveArquivo()

def alteraArquivo():
    arquivo = open('NovoArquivo.txt', 'a+')
    arquivo.write('Linha gerada com a função "AlteraArquivo" \r\n')
    arquivo.close()
#alteraArquivo()

def leituraArquivo():
    arquivo = open('NovoArquivo.txt', 'r')
    if (arquivo.mode == 'r'):
        conteudo = arquivo.read()
        print (conteudo)
    arquivo.close
#leituraArquivo()

def leituraArquivoGrande():
    arquivo = open('NovoArquivo.txt', 'r')
    if (arquivo.mode == 'r'):
        conteudoTotal = arquivo.readlines()
        for conteudo in conteudoTotal:
            print(conteudo)
    arquivo.close
leituraArquivoGrande()