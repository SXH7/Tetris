import pygame

vector = pygame.Vector2

FPS = 60
BGCOLOUR = (0, 50, 50)
TILE = 35
FIELD_W = 10
FIELD_H = 20
FIELD_RES = FIELD_W * TILE, FIELD_H * TILE

OFFSET = vector(5, 1)

TIME_INTERVAL = 350

DIRECTIONS = {"left": vector(-1, 0), "right": vector(1, 0), "down": vector(0, 1)}

BLOCKS = {
    "T": [(0, 0), (-1, 0), (1, 0), (0, -1)],
    "O": [(0, 0), (0, -1), (1, 0), (1, -1)],
    "J": [(0, 0), (-1, 0), (0, -1), (0, -2)],
    "L": [(0, 0), (1, 0), (0, -1), (0, -2)],
    "I": [(0, 0), (0, 1), (0, -1), (0, -2)],
    "S": [(0, 0), (-1, 0), (0, -1), (1, -1)],
    "Z": [(0, 0), (1, 0), (0, -1), (-1, -1)],
}
