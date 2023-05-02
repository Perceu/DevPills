"""
Buscando um json na internet e imprimindo na tela

Dependencias:
>> pip install httpx

"""
import httpx

url_base = 'https://raw.githubusercontent.com'
url_repo = '/Perceu/DevPills/main/statics'

r = httpx.get(f"{url_base}{url_repo}/contatos.json")

print(r.json())