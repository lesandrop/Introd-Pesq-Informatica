import requests
import json

usuario = "" #Precisa ser configurado
token="" #Precisa ser configurado

commits_url = f'https://api.github.com/repos/facebook/react/commits?per_page=100&page=1'
api = requests.get(commits_url, auth=(usuario, token))

dados_api = api.json()

while 'next' in api.links.keys():
	api = requests.get(api.links['next']['url'], auth=(usuario, token))
	dados_api.extend(api.json())

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dados_api, f, ensure_ascii=False, indent=4)