import sys

import pygame
import random
from alien import Alien

from ship import Ship
from bullet import Bullet

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1000, 800))

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

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
            self.update()
            self.update_screen()

            self.clock.tick(60) #60fps

    def create_bullet(self):
        self.bullets.add(Bullet(self))

    def update(self):

        if random.random() < 0.02:
            self.spawn_alien()

        self.ship.update()
        self.bullets.update()
        self.aliens.update()

        for bullet in self.bullets.copy ():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

        self.alien_bullet_collision()


    def update_screen(self):
        self.screen.fill((170,170,170))
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def spawn_alien(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def alien_bullet_collision(self):
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)


if __name__ == '__main__':
    game = SidewaysShooter()
    game.play_game()