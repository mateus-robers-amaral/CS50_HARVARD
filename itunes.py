import json
import requests
import sys

#condicao de ser um nome de uma banda
if len(sys.argv) != 2:
    sys.exit()

#variavel que busca o nome da banda na biblioteca da apple a partir do sys.argv de posicao 1
    #trocar o limit = n, define a quantidade de musicas pesquisadas da banda
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

#a variavel determina uma formatacao do dicionario puxado pela biblioteca requests
o = response.json()
#o loop define a busca de 'trackName' dentro da lista de 'results' e encerra quando bate o numero definido por limit
for result in o["results"]:
    print(result["trackName"])
