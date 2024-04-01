import sys

import pygame

class KeyGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((600,600))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_q:
                        sys.exit()

            self.update()

            self.clock.tick(60) #60fps

    def update(self):
        self.screen.fill((200,200,200))
        pygame.display.flip()


if __name__ == '__main__':
    kg = KeyGame()
    kg.run_game()