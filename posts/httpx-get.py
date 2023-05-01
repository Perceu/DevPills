"""
Buscando um json na internet e imprimindo na tela

Dependencias:
>> pip install httpx

"""
import httpx

r = httpx.get('https://raw.githubusercontent.com/Perceu/DevPills/main/statics/contatos.json')
print(r.json())