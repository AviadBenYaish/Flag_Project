import pygame
from soldier import *
import consts
from game_field import grass_positions
from screen import screen, screen_update

state = {
    "soldier_position": consts.PLAYER_INITIAL_POSITION
}

def main():
    pygame.init()
    while True:
        screen_update(state)

def handling_user_events():
    moving_up(state["soldier_position"])
    print(moving_up(state["soldier_position"]))
handling_user_events()
main()
handling_user_events()