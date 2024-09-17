import consts
import random

from Screen import draw_boom

game_matrix = []
def create_game_field():
    global game_matrix
    bomb_count = 0
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


def hit_mine(soldier_position):
    leg1 = (soldier_position[0] + 3, soldier_position[1])
    leg2 = (soldier_position[0] + 3, soldier_position[1] + 1)
    if game_matrix[leg1[0]][leg1[1]] != consts.SQUARE_BOMB and game_matrix[leg2[0]][leg2[1]] != consts.SQUARE_BOMB:
        return False
    return True

