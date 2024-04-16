import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):

    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.image = pygame.image.load('13-4/images/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = self.rect.y

    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        self.y += 5
        self.rect.y = self.y