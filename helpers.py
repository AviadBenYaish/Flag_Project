import consts
import random


def grass_positions():
    grass_positions_list = []
    for i in range(20):
        grass_x = random.randrange(consts.SCREEN_WIDTH - 50)
        grass_y = random.randrange(consts.SCREEN_HEIGHT - 50)
        grass_positions_list.append((grass_x, grass_y))
    return grass_positions_list


def get_x_y_position(grid_position):
    row = grid_position[0]
    col = grid_position[1]
    x = col * consts.BLOCK_SIZE[0]
    y = row * consts.BLOCK_SIZE[0]
    return x, y


