"""
Buscando um json e imprimindo na tela
"""
import httpx

r = httpx.get('https://raw.githubusercontent.com/Perceu/DevPills/main/statics/contatos.json')
print(r.json())