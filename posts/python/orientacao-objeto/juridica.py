'''
Classe de pessoa juridica que estende pessoa 
e adiciona propriedades e metodos 
'''
from pessoa import Pessoa

class Juridica(Pessoa):
    '''
    Pessoa juridica
    '''

    def __init__(self, nome: str, cnpj: str):
        super().__init__(nome)
        self.cnpj = cnpj

    def escreveDocumento(self):
        print (f"documento da pessoa {self.cnpj}")