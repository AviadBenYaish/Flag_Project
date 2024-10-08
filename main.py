import time
import pygame as pg

import pygame
import game_field
import consts
import soldier
from Database import create_file, add_game_position, load_game_position
from Screen import screen_update

pg.init()
click_down, click_up = False, False

state = {
    "state": consts.RUNNING_STATE,
    "soldier_position": consts.PLAYER_INITIAL_POSITION,
    "is_window_open": True,
    "is_moving": False,
}


def main():
    pygame.init()
    create_file()
    game_field.create_game_field()
    while state["is_window_open"]:
        if state["state"] == consts.BOOM_STATE:

            add_game_position(state["soldier_position"], 4)
            load_game_position(4)
            pygame.time.wait(1000)
            pygame.event.clear()
            state["state"] = consts.RUNNING_STATE
        if state["state"] == consts.LOSING_STATE:
            pygame.time.wait(3000)
            break
        if state["state"] == consts.WINING_STATE:
            pygame.time.wait(3000)
            break
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
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                 pygame.K_8, pygame.K_9]:
                    int(pygame.key.name(event.key))
                    
                if event.key in [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6,
                                 pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]:
                    list_ = eval(pygame.key.name(event.key))
                    int(list_[0])


def is_win(soldier_position):
    soldier_position = list(soldier_position)
    for num in range(3):
        if 21 <= (soldier_position[0] + num) and (soldier_position[0] + num <= 23) and 46 <= (
                soldier_position[1] + 1) and (soldier_position[1] + 1) <= 49:
            return True
        elif 21 <= (soldier_position[0] + 2) and (soldier_position[0] + 2 <= 23) and 46 <= (
                soldier_position[1] + 1) and (
                soldier_position[1] + 1) <= 49:
            return True
        else:
            return False


main()
handling_user_events()
