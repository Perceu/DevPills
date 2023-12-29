"""
Personagem do jogo que se movimenta pela tela.
"""
import pygame

class Player():
    position = pygame.Vector2(50, 50)

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.position.y -= 10
        if keys_pressed[pygame.K_s]:
            self.position.y += 10
        if keys_pressed[pygame.K_a]:
            self.position.x -= 10
        if keys_pressed[pygame.K_d]:
            self.position.x += 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 25)