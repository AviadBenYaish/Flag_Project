import pygame
from soldier import *
import consts
from game_field import *
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
    game_field_ = game_field()
    game_field_ = move_right_matrix(game_field_)

    for i in game_field_:
        print(i)

handling_user_events()
main()