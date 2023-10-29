"""
Criando um grafico simples para mostrar como usar 
a biblioteca matplotlib
"""
import matplotlib.pyplot as plt
meses = [
    'Janeiro', 'Fevereiro', 
    'Março', 'Abril', 
    'Maio', 'Junho', 
    'Julho', 'Agosto',
    'Setembro', 'Outubro',
    'Novembro', 'Dezembro'
]

valores = [
    50, 150,
    250, 300,
    380, 500,
    450, 300,
    450, 800,
    900, 1000,
]

plt.plot(meses, valores)
plt.show()