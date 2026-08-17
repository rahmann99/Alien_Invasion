import sys
import pygame

class AlienInavsion:
    """ to manage assets and behaviour"""

    def __init__(self):
        """ initialize and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Huahhahahahah")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """ make the most recent screen visible"""
            pygame.display.flip() 

if __name__ == '__main__':
    ai = AlienInavsion()
    ai.run_game()