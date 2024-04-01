import pygame
 
class Rocket: 
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12-4/images/rocket.bmp')

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.speed = 1

        self.x = self.rect.x
        self.y = self.rect.y

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def update(self):

        if self.up and self.rect.top > 0:
            self.y -= self.speed

        if self.down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.speed

        if self.right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        if self.left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)