import pygame

import soldier
from soldier import *
import consts
from game_field import *
from screen import screen, screen_update

state = {
    "state": consts.RUNNING_STATE,
    "soldier_position": consts.PLAYER_INITIAL_POSITION,
    "is_window_open": True,
    "is_moving": False,
}

def main():
    pygame.init()
    while state["is_window_open"]:
        handling_user_events()
        if state["is_moving"]:
            if hit_mine(state["soldier_position"]):
                state["state"] = consts.LOSING_STATE
        screen_update(state)

def handling_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state["soldier_position"] = soldier.moving_up(state["soldier_position"])
                print(state["soldier_position"])
            if event.key == pygame.K_DOWN:
                state["soldier_position"] = soldier.moving_down(state["soldier_position"])
                print(state["soldier_position"])
            if event.key == pygame.K_RIGHT:
                state["soldier_position"] = soldier.moving_right(state["soldier_position"])
                print(state["soldier_position"])
            if event.key == pygame.K_LEFT:
                state["soldier_position"] = soldier.moving_left(state["soldier_position"])
                print(state["soldier_position"])


main()
handling_user_events()