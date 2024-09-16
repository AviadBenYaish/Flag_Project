import pygame
from pygame.draw import lines

import consts
from game_field import grass_positions

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
positions_of_grass = grass_positions()


def screen_update(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grass()
    draw_background_bombs()
    draw_soldier(state["soldier_position"])
    pygame.display.flip()


def draw_grass():
    for position in positions_of_grass:
        image = pygame.transform.scale(consts.GRASS_IMAGE, (50, 50))
        image_rect = image.get_rect(topleft=position)
        screen.blit(image, image_rect)
def draw_flag():
    image = pygame.transform.scale(consts.GRASS_IMAGE, (50, 50))
    image_rect = image.get_rect(topleft=position)
    screen.blit(image, image_rect)

def draw_soldier(position):
    image = pygame.transform.scale(consts.PLAYER_IMAGE, consts.PLAYER_SIZE)
    image_rect = image.get_rect(topleft=position)
    screen.blit(image, image_rect)


def draw_background_bombs():
    for i in range(consts.BLOCK_SIZE[0], consts.BLOCK_SIZE[0]*50, consts.BLOCK_SIZE[0]):
        pygame.draw.line(screen, consts.LINES_COLOR, (i, 0), (i, consts.SCREEN_HEIGHT))