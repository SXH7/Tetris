from params import *
from Classes.shape import Shape
import pygame
import math


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite = pygame.sprite.Group()
        self.shape = Shape(self)

    def update(self):
        self.shape.update()
        self.sprite.update()

    def draw(self):
        self.drawgrid()
        self.sprite.draw(self.app.screen)
        

    def drawgrid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(self.app.screen, "black", (x*TILE, y*TILE, TILE, TILE), 1)

