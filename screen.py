import pygame
from game_field import get_x_y_position
import consts
from game_field import grass_positions
pygame.init()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
positions_of_grass = grass_positions()

# text_font = pygame.font.SysFont('Arial', 30)
#
#
# def winning_message(text, font, text_color, x, y):
#     img = font.render(text, True, text_color)
#     screen.blit(img, (x, y))



def screen_update(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grass()
    draw_background_bombs()
    draw_soldier(state["soldier_position"])
    draw_flag()
    if state["state"] == consts.WINING_STATE:
        print()
    # winning_message('YOU WIN', text_font, (0, 0, 0), 220, 150)
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
