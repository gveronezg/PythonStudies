"""
Por onde começar?
    Escreva o Passo a Passo do seu projeto!
        1º Importar a base de dados.
        2º Visualizar a base de dados.
        3º Tratamento de erros (resolver os erros da base de dados).
        4º Análise inicial dos dados (entender como estão os cancelamentos).
        5º Análise profunda da base de dados (encontrando a causa dos cancelamentos).

        Instalando os pacotes no ubuntu através do terminal:
            sudo apt install python3-pandas python3-numpy python3-openpyxl python3-plotly
        Instalando o Jupter:
            Nas extensões do VSCode instale e habilite o jupter
            E instale o kernel Jupyter também.
"""

    #   1º Importar a base de dados.

# panda é uma biblioteca utilizada para trabalhar com BDs
import pandas
# lendo o arquivo csv através do comando panda
tabela = pandas.read_csv("cancelamentos.csv")

    #   2º Visualizar a base de dados.
    
# printando o BD
print(tabela)

    #   3º Tratamento de erros (resolver os erros da base de dados).

# mostra as informações da BD
print(tabela.info())
# dropa as linhas que contem valores vazios
tabela = tabela.dropna()
# printa a tabela com informações
print(tabela.info())

# a coluna com os numeros de Customer ID são inúteis para a nossa análise, então vamos exclui-la.
# segundo parâmetro para definir o eixo (axis) a ser exluido (linha -> 0 ; coluna -> 1)
tabela = tabela.drop("CustomerID",axis=1)
# mostrando a nova tabela
print(tabela)

    #    4º Análise inicial dos dados (entender como estão os cancelamentos).

# mostrando apenas a coluna "cancelou" da tabela e contando os seus valores
print(tabela["cancelou"].value_counts())

# usando o normalize, mostraremos o resultado em percentual
print(tabela["cancelou"].value_counts(normalize=True))

# mostrando apenas a coluna "cancelou" da tabela e contando os seus valores
print(tabela["duracao_contrato"].value_counts())

# usando o normalize, mostraremos o resultado em percentual formatando unsando o método .map e .format (.map("{:.1%}".format))
print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format))

# usando o (groupby) conseguimos agrupar os valores que temos na coluna e através do (.count) conseguimos contar os valores das outras
print(tabela.groupby('duracao_contrato').count())
"""
    Não consegui descobrir por que esta parte do código está fazendo com que a execução do código fique estagnada... :'(
        
# usando o (groupby) conseguimos agrupar os valores que temos na coluna e através do (.sum) conseguimos somar os valores das outras
print(tabela.groupby("duracao_contrato").sum())
# usando o (groupby) conseguimos agrupar os valores que temos na coluna e através do (.mean) conseguimos fazer a média dos valores das outras
print(tabela.groupby('duracao_contrato').mean())
# observação
print('Através dessa análise, percebemos que a média de cancelamentos dos clientes que tem contrato mensal é de praticamente 100%')
"""
# vamos desconsiderar os clientes com contrato mensal para analisarmos qual seria a nova porcentagem de cancelamento sem eles
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]

# mostrando apenas a coluna "cancelou" da tabela e contando os seus valores
print(tabela["cancelou"].value_counts())

# usando o normalize, mostraremos o resultado em percentual formatando unsando o método .map e .format (.map("{:.1%}".format))
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

    #   5º Análise profunda da base de dados (encontrando a causa dos cancelamentos).

# importando o plotly previamente instalado, para usar como ferramenta de gráficos interativos no python. Atribuindo o "apelido = px" através do as.
import plotly.express as px

for coluna in tabela.columns:
        # criando uma gráfico de histograma passando os 3 parametros básicos para cria-lo (tabela,eixoX,eixoY)
        grafico = px.histogram(tabela,x=coluna,color="cancelou")
        # assim mostraremos o gráfico onde mostra:
        # as colunas dos tipos de assinaturas cadastradas (Standard,Basic,Premium)
        # as cores dos tipos de resposta para cancelamento (1,0)
        grafico.show()

insight = """
Insights tirados das análises dos gráficos:
    COLUNA              |   OBSERVAÇÃO
    ------------------------------------------------------------------------------
    idade               |   Todos os clientes acima de 50 anos cancelaram!
    ligacoes_callcenter |   Todos os clientes que ligam 5 vezes ou mais cancelaram!
    dias_atraso         |   Todos os clientes com mais de 20 dias de atraso cancelaram!
    total_gasto         |   Todos os clientes que tem um total de gastos menores que 500 cancelaram
"""
print(insight)