import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage firing bullets"""

    def __int__(self, ai_game):
        """ creating bullet object at ship position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and the set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop


        #Store the bullets position as a float
        self.y = float(self.rect.y)


    def update(self):
        """ Move bullets ups the screens"""