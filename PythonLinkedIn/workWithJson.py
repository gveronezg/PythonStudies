import urllib.request
import json

def manipulaJSON():
    endereco = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webURL = urllib.request.urlopen(endereco)
    if (webURL.getcode() == 200):
        dados = webURL.read()
        oJSON = json.loads(dados)

        contagem = oJSON["metadata"]['count']
        print('Contagem:' + str(contagem))

        for local in oJSON['features']:
            if local['properties']['place'] == '10 km S of Wilson, Oklahoma':
                print('Encontrado registro especifico!')
            else:
                print(local['properties']['place'])
manipulaJSON()