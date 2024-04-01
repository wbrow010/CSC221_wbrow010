import sys

import pygame

class BlueSky:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600,600))

    def play_game(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.screen.fill((0,0,200))

            pygame.display.flip()

            self.clock.tick(60) #60fps


if __name__ == '__main__':
    bsg = BlueSky()
    bsg.play_game()