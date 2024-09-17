import consts
import random

game_matrix = []


def game_field():
    global game_matrix
    bomb_count = 0
    game_matrix = []
    for i in range(consts.GAME_MATRIX_ROWS):
        game_row = []
        for j in range(consts.GAME_MATRIX_COLOUMNS):
            if 21 <= i and i <= 23 and 46 <= j and j <= 49:
                game_row.append(consts.SQUARE_FLAG)

            else:
                game_row.append(consts.SQUARE_EMPTY)

        game_matrix.append(game_row)
    while bomb_count < consts.BOMBS_AMOUNT:
        random_row = random.randint(0, consts.GAME_MATRIX_ROWS - 1)
        random_coll = random.randint(0, consts.GAME_MATRIX_COLOUMNS - 3 )
        if game_matrix[random_row][random_coll] != consts.SQUARE_BOMB and game_matrix[random_row][
            random_coll] != consts.SQUARE_FLAG:
            if random_row != 3 or random_coll not in [0, 1]:

                if random_row > 2 and random_coll < 48:


                    if game_matrix[random_row][random_coll + 2] != consts.SQUARE_BOMB and game_matrix[random_row][
                        random_coll + 2] != consts.SQUARE_FLAG:
                        bomb_count += 1
                        game_matrix[random_row][random_coll] = consts.SQUARE_BOMB
                        game_matrix[random_row][random_coll + 1] = consts.SQUARE_BOMB
                        game_matrix[random_row][random_coll + 2] = consts.SQUARE_BOMB

    return game_matrix


for i in game_field():
    print(i)



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


def hit_mine(soldier_position, game_matrix_):
    print(game_matrix_)
    leg1 = (soldier_position[0] + 3, soldier_position[1])
    leg2 = (soldier_position[0] + 3, soldier_position[1] + 1)
    if game_matrix[leg1[0]][leg1[1]] != consts.SQUARE_BOMB and game_matrix[leg2[0]][leg2[1]] != consts.SQUARE_BOMB:
        return False
    return True
