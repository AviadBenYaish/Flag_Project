from time import sleep
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
        draw_soldier(state["soldier_position"], state["state"])
        draw_flag()
    if state["state"] == consts.BOOM_STATE:
        screen.fill(consts.BACKGROUND_COLOR_BOOMS)
        draw_background_bombs()
        draw_booms()
        draw_soldier(state["soldier_position"], state["state"])
    if state["state"] == consts.LOSING_STATE:
        losing_message()
    if state["state"] == consts.WINING_STATE:
        winning_message()
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


def draw_soldier(position, soldier_state):
    if soldier_state == consts.BOOM_STATE:
        image = pygame.transform.scale(consts.PLAYER_IMAGE_NIGHT, consts.PLAYER_SIZE)
    else:
        image = pygame.transform.scale(consts.PLAYER_IMAGE, consts.PLAYER_SIZE)
    soldier_position_x_y = get_x_y_position(position)
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


def draw_massage(massage, font_size, text_color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size, bold=True)
    text_img = font.render(massage, True, text_color)
    text_width = text_img.get_width()
    text_height = text_img.get_height()
    location_x = location[0] - text_width / 2
    location_y = location[1] - text_height / 2
    screen.blit(text_img, (location_x, location_y))

def losing_message():
    draw_massage(consts.LOSING_MASSAGE, consts.LOSE_FONT_SIZE, "black", consts.LOSE_FONT_LOCATION)

def winning_message():
    draw_massage(consts.WINNING_MASSAGE, consts.WINING_FONT_SIZE, (0, 0, 0), consts.WINING_FONT_LOCATION)

