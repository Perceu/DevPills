'''
Esse é um exemplo de orientação a objeto 

Esse exemplo instancia as classes que estendem 
Pessoa e executam os metodos de comprimentar e escreveDocumento
'''

from fisica import Fisica
from juridica import Juridica

def main():
    p1 = Fisica("Goku", "000")
    p2 = Juridica("Gohan", "001")
    p1.comprimentar()
    p1.escreveDocumento()
    p2.comprimentar()
    p2.escreveDocumento()

if __name__=="__main__":
    main()
    print("Segue e compartilha!")