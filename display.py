from settings import *
from game import game

def display():
    screen.fill("#b2bec3")
    game.update()
    pygame.display.update()
    clock.tick(FPS)