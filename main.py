
import pygame
import game_field
import consts
import soldier
from Screen import screen_update

state = {
    "state": consts.RUNNING_STATE,
    "soldier_position": consts.PLAYER_INITIAL_POSITION,
    "is_window_open": True,
    "is_moving": False,
}

def main():
    pygame.init()
    game_field.create_game_field()
    while state["is_window_open"]:
        if state["state"] == consts.BOOM_STATE:
            pygame.time.wait(1000)
            pygame.event.clear()
            state["state"] = consts.RUNNING_STATE
        handling_user_events()
        if state["is_moving"]:
            if game_field.hit_mine(state["soldier_position"]):
                state["state"] = consts.LOSING_STATE
            if is_win(state["soldier_position"]):
                state["state"] = consts.WINING_STATE
            state["is_moving"] = False
        screen_update(state)

def handling_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if state["state"] != consts.LOSING_STATE and state["state"] != consts.WINING_STATE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state["state"] = consts.BOOM_STATE
                if event.key == pygame.K_UP:
                    state["soldier_position"] = soldier.moving_up(state["soldier_position"])
                    state["is_moving"] = True
                if event.key == pygame.K_DOWN:
                    state["soldier_position"] = soldier.moving_down(state["soldier_position"])
                    state["is_moving"] = True
                if event.key == pygame.K_RIGHT:
                    state["soldier_position"] = soldier.moving_right(state["soldier_position"])
                    state["is_moving"] = True
                if event.key == pygame.K_LEFT:
                    state["soldier_position"] = soldier.moving_left(state["soldier_position"])
                    state["is_moving"] = True

def is_win(soldier_position):
    soldier_position = list(soldier_position)
    for num in range(3):
        if 21 <= (soldier_position[0] + num) and (soldier_position[0] + num <= 23) and 46 <= (
                soldier_position[1] + 1) and (soldier_position[1] + 1) <= 49:
            return True
        elif 21 <= (soldier_position[0] + 2) and (soldier_position[0] + 2 <= 23) and 46 <= (soldier_position[1]+1) and (
        soldier_position[1]+1) <= 49:
            return True
        else:
            return False

main()
handling_user_events()