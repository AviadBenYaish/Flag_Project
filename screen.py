import pygame

import consts
from game_field import grass_positions

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
positions_of_grass = grass_positions()


def screen_update(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grass()
    draw_background_bombs()
    # soldier_position_x_y = get_x_y_position()
    draw_soldier(consts.PLAYER_INITIAL_POSITION_SCREEN)
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
    block_position = consts.BLOCK_SIZE[0]
    for i in range(49):
        pygame.draw.line(screen, consts.LINES_COLOR, (block_position, 0), (block_position, consts.SCREEN_HEIGHT))
        block_position += consts.BLOCK_SIZE[0]
    block_position = consts.BLOCK_SIZE[0]
    for i in range(24):
        pygame.draw.line(screen, consts.LINES_COLOR, (0, block_position), (consts.SCREEN_WIDTH, block_position))
        block_position += consts.BLOCK_SIZE[0]