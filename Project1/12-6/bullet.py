import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (0,0,0)
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.midright = game.ship.rect.midright
        self.speed = 15
        self.x = self.rect.x

    def update(self):
        self.x += self.speed

        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)