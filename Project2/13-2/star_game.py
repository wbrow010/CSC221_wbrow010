import pygame
import random
import sys

from star import Star


class StarGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 800))
        self.stars = pygame.sprite.Group()
        self.stars_grid()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.update_screen()
            self.clock.tick(60)


    def stars_grid(self):
        star = Star(self)
        star_width  = star.rect.width
        star_height = star.rect.height

        star_x = 2 * star_width
        
        star_y = 2 * star_height

        while star_y < (800 - 2 * star_height):

            while star_x < (800 - 2 * star_width):
                self.create_star(star_x, star_y)
                star_x += 2 * star_width

            star_x = 2 * star_width #resets the x
            star_y += 2 * star_height


    def create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.rect.x = x_position + random.randint(-50,50)
        new_star.rect.y = y_position + random.randint(-50,50)

        self.stars.add(new_star)

    def update_screen(self):
        self.screen.fill((0,0,0))
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    sg = StarGame()
    sg.run_game()