
from Classes.tetris import Tetris
from params import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(FIELD_RES)
        self.clock = pygame.time.Clock()
        self.tetris = Tetris(self)
    
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)
    
    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.tetris.draw()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.events()


if __name__ == "__main__":
    game = Game()
    game.run()