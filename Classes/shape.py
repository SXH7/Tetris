from params import *
import pygame

class Shape:

    def __init__(self, tetris):
        self.tetris = tetris
        self.whichshape = random.choice(list(BLOCKS.keys()))
        print(whichshape)
        Block(self, BLOCKS[whichshape])

    def update(self):
        pass

class Block(pygame.sprite.Sprite):
    def __init__(self, shape, pos):
        self.shape = shape
        self.pos = vector(pos)+OFFSET
        super().__init__(shape.tetris.sprite)
        self.image = pygame.Surface([TILE, TILE])
        self.image.fill('orange')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE

        
