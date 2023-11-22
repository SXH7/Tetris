from params import *
from Classes.shape import Shape
import pygame
import math


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite = pygame.sprite.Group()
        self.fieldArray = self.fieldArray()
        self.shape = Shape(self)

    def checklines(self):
        row = FIELD_H -1
        for y in range(FIELD_H -1, -1, -1):
            for x in range(FIELD_W):
                self.fieldArray[row][x] = self.fieldArray[y][x]
                if(self.fieldArray[y][x]):
                    self.fieldArray[row][x].pos = vector(x, y)

            if sum(map(bool, self.fieldArray[y]))<FIELD_W:
                row-=1
            else:
                for x in range(FIELD_W):
                    self.fieldArray[row][x].alive = False
                    self.fieldArray[row][x] = 0

    def markBlocksInArray(self):
        for block in self.shape.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.fieldArray[y][x] = block   

    def fieldArray(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def update(self):
        
        if self.app.trigger:
            self.checklines()
            self.shape.update()
            self.checklanding()
        self.sprite.update()

    def checklanding(self):
        if self.shape.landing:
            self.markBlocksInArray()
            self.shape = Shape(self)

    def draw(self):
        self.drawgrid()
        self.sprite.draw(self.app.screen)

    def drawgrid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pygame.draw.rect(
                    self.app.screen, "black", (x * TILE, y * TILE, TILE, TILE), 1
                )

    def control(self, pressedkey):
        if pressedkey == pygame.K_LEFT or pressedkey == pygame.K_a:
            self.shape.move("left")
        elif pressedkey == pygame.K_RIGHT or pressedkey == pygame.K_d:
            self.shape.move("right")
        elif pressedkey == pygame.K_DOWN or pressedkey == pygame.K_s:
            self.shape.move("down")
        elif pressedkey == pygame.K_e:
            self.shape.rotate(90)
        elif pressedkey == pygame.K_q:
            self.shape.rotate(-90)
