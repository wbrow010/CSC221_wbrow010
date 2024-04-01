import pygame
 
class Character:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12-2/images/character.bmp')

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def character_blit(self):
        self.screen.blit(self.image, self.rect)