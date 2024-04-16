import sys

import pygame

from raindrop import Raindrop

class RaindropsGame:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 800))

        self.raindrops = pygame.sprite.Group()
        self.create_drops()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.update_raindrops()
            self.update_screen()
            self.clock.tick(60)

    def create_drop(self, x_position, y_position):
        new_drop = Raindrop(self)
        new_drop.y = y_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.raindrops.add(new_drop)

    def create_drops(self):
        drop = Raindrop(self)
        drop_width  = drop.rect.width
        drop_height = drop.rect.height

        drop_x = drop_width
        drop_y = drop_height

        while drop_y < (800 - (2 * drop_height)):
            while drop_x < (800 - (2 * drop_width)):
                self.create_drop(drop_x, drop_y)
                drop_x += 2 * drop_width

            # Finished a row; reset x value, and increment y value.
            drop_x = drop_width
            drop_y += 2 * drop_height

    def create_drops_row(self):
        drop = Raindrop(self)
        drop_width  = drop.rect.width
        drop_height = drop.rect.height

        drop_x = drop_width
        drop_y = -1 * drop_height

        while drop_x < (800 - (2 * drop_width)):
            self.create_drop(drop_x, drop_y)
            drop_x += 2 * drop_width

    def update_raindrops(self):
        self.raindrops.update()

        new_row_needed = False

        for drop in self.raindrops.copy():

            if drop.check_disappeared():
                self.raindrops.remove(drop)
                new_row_needed = True

        if new_row_needed:
            self.create_drops_row()

    def update_screen(self):
        self.screen.fill((100,255,100))

        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    rd_game = RaindropsGame()
    rd_game.run_game()