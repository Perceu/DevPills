"""
Player do jogo 
"""
import pyxel

class Player():
    x = 10
    y = 10 

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.y -= 10
        if pyxel.btnp(pyxel.KEY_S):
            self.y += 10
        if pyxel.btnp(pyxel.KEY_A):
            self.x -= 10
        if pyxel.btnp(pyxel.KEY_D):
            self.x += 10
    
    def draw(self):
        pyxel.rect(self.x, self.y, 10, 10, 7)