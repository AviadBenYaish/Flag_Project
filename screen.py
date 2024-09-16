import pygame

import consts
screen = pygame.display.set_mode((1280, 640))

def screen_update():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()