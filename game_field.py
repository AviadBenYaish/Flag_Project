import consts
import random


def game_field():
    bomb_count = 0
    game_matrix = []
    for i in range(25):
        game_row = []
        for j in range(50):
            if 21 <= i and i <= 23 and 46 <= j and j <= 49:
                game_row.append(consts.SQUARE_FLAG)
            elif i <= 2 and j <= 1:
                game_row.append(consts.SQUARE_BODY)
            elif i == 3 and j <= 1:
                game_row.append(consts.SQUARE_LEGS)

            else:
                game_row.append(consts.SQUARE_EMPTY)

        game_matrix.append(game_row)
    while bomb_count < 20:
        random_row = random.randint(0, 24)
        random_coll = random.randint(0, 47)
        if game_matrix[random_row][random_coll] != consts.SQUARE_BOMB and game_matrix[random_row][
            random_coll] != consts.SQUARE_FLAG:
            if game_matrix[random_row][random_coll] != consts.SQUARE_BODY  and game_matrix[random_row][random_coll] != consts.SQUARE_LEGS:

                if game_matrix[random_row][random_coll + 2] != consts.SQUARE_BOMB and game_matrix[random_row][
                    random_coll + 2] != consts.SQUARE_FLAG:
                    bomb_count += 1
                    game_matrix[random_row][random_coll] = consts.SQUARE_BOMB
                    game_matrix[random_row][random_coll + 1] = consts.SQUARE_BOMB
                    game_matrix[random_row][random_coll + 2] = consts.SQUARE_BOMB

    return game_matrix




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
    return (x, y)