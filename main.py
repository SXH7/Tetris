from Classes.tetris import Tetris
from params import *
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(FIELD_RES)
        self.clock = pygame.time.Clock()
        self.tetris = Tetris(self)
        self.timer()

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.trigger = False
        pygame.time.set_timer(self.user_event, TIME_INTERVAL)

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.tetris.draw()
        pygame.display.flip()

    def events(self):
        self.trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.tetris.control(event.key)
            elif event.type == self.user_event:
                self.trigger = True

    def run(self):
        while True:
            self.update()
            self.draw()
            self.events()


if __name__ == "__main__":
    game = Game()
    game.run()
