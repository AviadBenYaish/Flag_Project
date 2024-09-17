from itertools import count

import pygame
import consts
import game_field
from helpers import grass_positions, get_x_y_position

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
positions_of_grass = grass_positions()


def screen_update(state):
    if state["state"] == consts.RUNNING_STATE:
        screen.fill(consts.BACKGROUND_COLOR)
        draw_grass()
        draw_background_bombs()
        draw_soldier(state["soldier_position"])
        draw_flag()
    elif state["state"] == consts.BOOM_STATE:
        screen.fill(consts.BACKGROUND_COLOR_BOOMS)
        draw_background_bombs()
        draw_booms()
        draw_soldier(state["soldier_position"])
    pygame.display.flip()

def draw_grass():
    for position in positions_of_grass:
        image = pygame.transform.scale(consts.GRASS_IMAGE, (50, 50))
        image_rect = image.get_rect(topleft=position)
        screen.blit(image, image_rect)
def draw_flag():
    flag_position = get_x_y_position(consts.FLAG_POSITION)
    image = pygame.transform.scale(consts.FLAG_IMAGE, (100, 100))
    image_rect = image.get_rect(topleft=flag_position)
    screen.blit(image, image_rect)


def draw_soldier(position):
    soldier_position_x_y = get_x_y_position(position)
    image = pygame.transform.scale(consts.PLAYER_IMAGE, consts.PLAYER_SIZE)
    image_rect = image.get_rect(topleft=(soldier_position_x_y[0], soldier_position_x_y[1] + consts.BLOCK_SIZE[0] / 3))
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


def draw_booms():
    counter = 1
    count_ = 0
    for i_row in range(len(game_field.game_matrix)):
        for i_col in range(len(game_field.game_matrix[i_row])):
            if game_field.game_matrix[i_row][i_col] == consts.SQUARE_BOMB and counter == 1:
                draw_boom((i_row, i_col))
                count_ += 1
                counter += 1
            elif counter == 3:
                counter = 0
            elif game_field.game_matrix[i_row][i_col] == consts.SQUARE_BOMB:
                counter += 1


def draw_boom(position):
    boom_position = get_x_y_position(position)
    image = pygame.transform.scale(consts.BOMB_IMAGE, (consts.BLOCK_SIZE[0] * 3, consts.BLOCK_SIZE[0]))
    image_rect = image.get_rect(topleft=boom_position)
    screen.blit(image, image_rect)
