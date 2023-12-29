"""
pyxel e um framework de desenvolvimento 
de jogos em 8 bits.

Muito simples mas otimo para testar ideias

"""
import pyxel
from player import Player

pyxel.init(200, 200)

player = Player()

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    player.update()

def draw():
    pyxel.cls(0)
    player.draw()

pyxel.run(update, draw)