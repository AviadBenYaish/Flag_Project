import consts
import game_field


def moving_up(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] -= 1
    if soldier_position[0] >= 0:
        return tuple(soldier_position)
    elif soldier_position[0] < 0:
        soldier_position[0] = 0
        return tuple(soldier_position)



def moving_down(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] += 1
    if soldier_position[0] <= len(game_field.game_field())-4:
        return tuple(soldier_position)
    elif soldier_position[0] > len(game_field.game_field())-4:
        soldier_position[0] = len(game_field.game_field())-4
        return tuple(soldier_position)


def moving_left(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[1] -= 1
    if soldier_position[1] >= 0:
        return tuple(soldier_position)
    elif soldier_position[0] < 0:
        soldier_position[0] = 0
        return tuple(soldier_position)
#   fix left function

def moving_right(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[1] += 1
    if soldier_position[1] <= len(game_field.game_field()[0]) - 2:
        return tuple(soldier_position)
    elif soldier_position[1] > len(game_field.game_field()[0]) - 2:
        soldier_position[1] = len(game_field.game_field()[0]) - 2
        return tuple(soldier_position)


# print(moving_up(soldier_position))
