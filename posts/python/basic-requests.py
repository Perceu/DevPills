# Biblioteca para fazer requisições para sites, muito usada 
# para raspagem de dados e consumo de apis
# aqui buscamos todos os projetos da 
# fundação apache em um formato json

import requests
import pprint

response = requests.get(
    'https://projects.apache.org/json/foundation/projects.json'
)

pprint.pprint(
    response.json(),
    indent=4
)