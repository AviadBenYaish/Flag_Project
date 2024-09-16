import pygame
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


main()
handling_user_events()