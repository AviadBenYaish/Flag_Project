import pygame
from soldier import *
from game_field import get_x_y_position, game_field
import consts
from game_field import grass_positions
from screen import screen, screen_update

state = {
    "soldier_position": consts.PLAYER_INITIAL_POSITION,
    "is_window_open": True
}

def main():
    pygame.init()
    while state["is_window_open"]:
        handling_user_events()
        screen_update(state)

def handling_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
    print()
main()
handling_user_events()