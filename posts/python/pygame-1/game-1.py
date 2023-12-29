"""
Modelo de game simples. 
Movimentação em 4 eixos.
Sem nenhuma mecanica.
"""

import pygame
from player import Player
pygame.init()

screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    keys = pygame.key.get_pressed()
    player.update(keys)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()