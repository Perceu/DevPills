'''
Classe base

Para gerar o UML do projeto use o pylint

# Para gerar o UML desse projeto
# pip install pylint
# pyreverse -o png posts/python/orientacao-objeto

'''

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def comprimentar(self):
        print(f"Oi me chamo {self.nome}!")
