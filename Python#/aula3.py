# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Kaggle tem base de dados gratuitas para outros treinos

Passo a Passo
    1º Entender o desafio e a empresa
    2º Importar a base de dados
    3º Preparar a BD para a inteligência artificial
    4º Criar um modelo de IA -> Score de crédito: Ruim, Méio, Bom
    5º Escolher o melhor modelo
    6º Usar o modelo em um cenário real

    instalar 2 métodos do python
        pandas , scikit-learn
"""
import pandas as pd

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

bd = pd.read_csv("clientes.csv") # lendo a base de dados usando o panda
print(bd)
print(bd.info())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Colunas de texto
    profissao
    mix_credito
    comportamento_pagamento
"""
# Do módulo sklearn, vou importar apenas a ferramenta labelEncoder
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder() # criando o codificador
bd["profissao"] = codificador.fit_transform(bd["profissao"]) # transformando a coluna da tabela para valores codificados
bd["mix_credito"] = codificador.fit_transform(bd["mix_credito"])
bd["comportamento_pagamento"] = codificador.fit_transform(bd["comportamento_pagamento"])
print(bd.info()) # é possivel notar que o tipo destas colunas foram de object para int64

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
As colunas que eu desejo prever serão meu Y
e as colunas que eu vou usar nessa previsão serão meu X
"""
y = bd["score_credito"]
x = bd.drop(["score_credito","id_cliente"], axis=1) # usando todas as colunas relevantes para a análise

    # esta ferramente que vou importar do módulo sklearn é usada para realizar os treinos e testes com a IA
from sklearn.model_selection import train_test_split
    # esta é a forma padrão para que as partes do BD sejam seraparadas para treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3, random_state=1) # farçando o uso de 30% dos registros para testes e de forma aleatória

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
    Vamos utilizar 2 tipos de IA
        ARVORE DE DECISÃO
        KNN - NEAREST NEIGHBORS
"""

    # importando as 2 IAs
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

    # criando as 2 IAs
modelo_arvore_decisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

    # treinando os 2 modelos de IA
modelo_arvore_decisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
    Vamos comparar os resultados dos 2 modelos com o teste
    e assim concularemos a melhor acurácia
"""
    # importando a ferramente que irá calcular a pontuação de acertos das IAs
from sklearn.metrics import accuracy_score

    # aqui as IAs estão tentando prever quais seriam os resultados baseados nos dados que receberam do bd para teste
previsao_arvore_decisao = modelo_arvore_decisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy()) # o modelo KNN só consegue funcionar tranformando os dados com o NUMPY

    # agora comparando os resultados, com os dados, será printado a pontuação confome as previsões corretas
print(accuracy_score(y_teste, previsao_arvore_decisao))
print(accuracy_score(y_teste, previsao_knn))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
    Após realizar o primeiro teste de acurácia obtivemos o resultado:
    Arvore  = 0.8268 %
    KNN     = 0.7324 %
"""
novos_clientes = pd.read_csv('novos_clientes.csv') # lendo uma tabela de novos clientes
novos_clientes["profissao"] = codificador.fit_transform(novos_clientes["profissao"]) # transformando a coluna da tabela para valores codificados
novos_clientes["mix_credito"] = codificador.fit_transform(novos_clientes["mix_credito"])
novos_clientes["comportamento_pagamento"] = codificador.fit_transform(novos_clientes["comportamento_pagamento"])
print(novos_clientes)

previsao = modelo_arvore_decisao.predict(novos_clientes)
print(previsao)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------