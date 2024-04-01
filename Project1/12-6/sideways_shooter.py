import sys

import pygame

from ship import Ship
from bullet import Bullet

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1000, 800))

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def play_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship.up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.down = True
                    elif event.key == pygame.K_SPACE:
                        self.create_bullet()
                    elif event.key == pygame.K_q:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.ship.up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.down = False

            self.ship.update()

            self.update()

            self.clock.tick(60) #60fps

    def create_bullet(self):
        self.bullets.add(Bullet(self))

    def update(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

        self.screen.fill((170,170,170))

        self.ship.draw()

        for bullet in self.bullets.sprites():
            bullet.draw()

        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.play_game()