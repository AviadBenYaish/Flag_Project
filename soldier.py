import consts


def moving_up(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[1] -= 1
    return tuple(soldier_position)
def moving_down(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[1] += 1
    return tuple(soldier_position)
def moving_left(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] -= 1
    return tuple(soldier_position)
def moving_right(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] += 1
    return tuple(soldier_position)














# print(moving_up(soldier_position))

