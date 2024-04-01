import pygame
 
class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12-6/images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = self.rect.y
        self.speed = 10
        self.up = False
        self.down = False

    def update(self):
        if self.up and self.rect.top > 0:
            self.y -= self.speed

        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)