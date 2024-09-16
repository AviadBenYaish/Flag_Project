import pygame

import consts
while True:
    screen = pygame.display.set_mode((1280, 640))

def screen_update():
    screen.fill(consts.BACKGROUND_COLOR)