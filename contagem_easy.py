
import requests
import json

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)

dicionario = {}

for x in lista:
    if x not in dicionario:
        dicionario[x] = 1

    else:
        dicionario[x] += 1

print(dicionario.items())

for chave, valor in dicionario.items():
    print(valor)
