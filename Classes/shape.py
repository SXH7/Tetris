from params import *
import pygame
import random


class Shape:
    def __init__(self, tetris):
        self.tetris = tetris
        self.whichshape = random.choice(list(BLOCKS.keys()))
        self.blocks = [Block(self, pos) for pos in BLOCKS[self.whichshape]]
        self.landing = False
    
    def rotate(self, angle):
        pivot = self.blocks[0].pos
        newblocks = [block.rotate(pivot) for block in self.blocks]
        
        if not self.collision(newblocks):
            for i, block in enumerate(self.blocks):
                block.pos = newblocks[i]

    def move(self, direction):
        direction = DIRECTIONS[direction]
        new_pos = [block.pos + direction for block in self.blocks]
        collision = self.collision(new_pos)
        if not collision:
            for block in self.blocks:
                block.pos += direction
        elif direction == [0, 1]:
            self.landing = True

    def collision(self, block_positions):
        return any(map(Block.collision, self.blocks, block_positions))

    
    def update(self):
        self.move(direction="down")


class Block(pygame.sprite.Sprite):
    def __init__(self, shape, pos):
        self.shape = shape
        self.pos = vector(pos) + OFFSET
        super().__init__(shape.tetris.sprite)
        self.image = pygame.Surface([TILE, TILE])
        self.image.fill("orange")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE
        self.alive = True

    def checkalive(self):
        if not self.alive:
            self.kill()

    def rotate(self, pivot):
        translate = self.pos - pivot
        rotated = translate.rotate(90)
        return rotated + pivot

    def setpos(self):
        self.rect.topleft = self.pos * TILE

    def collision(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and 0 <= y < FIELD_H and (y < 0 or not self.shape.tetris.fieldArray[y][x]):
            return False
        return True

    def update(self):
        self.checkalive()
        self.setpos()
