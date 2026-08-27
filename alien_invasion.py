import sys
import pygame

from settings import Settings
class AlienInavsion:
    """ to manage assets and behaviour"""

    def __init__(self):
        """ initialize and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_width,self.settings.screen_height)
        pygame.display.set_caption("Alien Huahhahahahah")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """ make the most recent screen visible"""
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip() 

if __name__ == '__main__':
    ai = AlienInavsion()
    ai.run_game()