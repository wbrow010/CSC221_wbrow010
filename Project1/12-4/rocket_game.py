import sys

import pygame

from rocket import Rocket

class RocketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((600,600))

        self.rocket = Rocket(self)

    def play_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.rocket.right = True
                        
                    elif event.key == pygame.K_LEFT:
                        self.rocket.left = True

                    elif event.key == pygame.K_UP:
                        self.rocket.up = True

                    elif event.key == pygame.K_DOWN:
                        self.rocket.down = True

                    elif event.key == pygame.K_q:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.rocket.right = False

                    elif event.key == pygame.K_LEFT:
                        self.rocket.left = False

                    elif event.key == pygame.K_UP:
                        self.rocket.up = False

                    elif event.key == pygame.K_DOWN:
                        self.rocket.down = False

            self.rocket.update()
            self.update()

            self.clock.tick(60) #60fps

    def update(self):
        self.screen.fill((0,0,200))
        self.rocket.draw()

        pygame.display.flip()


if __name__ == '__main__':
    rg = RocketGame()
    rg.play_game()