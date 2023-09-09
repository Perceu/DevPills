'''
Classe de pessoa fisica que estende pessoa 
e adiciona propriedades e metodos 
'''
from pessoa import Pessoa

class Fisica(Pessoa):
    '''
    Pessoa Fisica
    '''
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome)
        self.cpf = cpf

    def escreveDocumento(self):
        '''Docstring'''
        print (f"documento da pessoa {self.cpf}")