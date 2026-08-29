import pygame

class Ship:
    """ A class to manage ship."""

    def __init__(self, ai_game):
        """ Initialoizeing the ship while setting a starting position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for ships exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag: the ship is not moving to start with
        self.moving_right = False
        self.moving_left = False

    def update(self):
            """ Update ship position according to movement flag """
            # Update the ships  x value, not the rect
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            elif self.moving_left and self.rect.left > 0:
                 self.x -= self.settings.ship_speed

            # Update rect object from self.x
            self.rect.x = self.x

    def blitme(self):
        """draw the ship at current location"""
        self.screen.blit(self.image, self.rect)
