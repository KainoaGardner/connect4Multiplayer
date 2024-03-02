import pygame


pygame.init()

TILESIZE = 100
WIDTH = TILESIZE * 7
HEIGHT = TILESIZE * 6 + TILESIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

