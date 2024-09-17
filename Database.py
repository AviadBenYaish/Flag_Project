import os.path
from logging import fatal
from operator import index
from pprint import PrettyPrinter

import pandas as pd
import csv

from Screen import positions_of_grass, draw_flag
from game_field import booms_position
from helpers import grass_positions


def create_file():
    path = "./database.csv"
    if not os.path.isfile(path):
        with open(path, mode='w', newline='') as file:
            csv.writer(file)
            headers = {"key":[], "grass_position": [], "soldier_position": [], "booms_position": []}
            df_headers = pd.DataFrame(headers)
            df_headers.to_csv("database.csv", mode='w', header=True)


def add_game_position(soldier_position, key):
    df_game_csv = pd.read_csv("database.csv")
    booms_positions = booms_position()
    print(df_game_csv["key"].values)
    if key in df_game_csv["key"].values:
        row_index = df_game_csv.loc[df_game_csv['key'] == key].index[0]
        print(row_index)
        df_game_csv = df_game_csv.drop(row_index)
        df_game_csv.to_csv("database.csv", mode='w', header=True, index=False)
    game_info = {"key":[key], "grass_position": [positions_of_grass], "soldier_position": [soldier_position], "booms_position": [booms_positions]}
    game_info_pd = pd.DataFrame(game_info)
    df_game_csv = df_game_csv._append(game_info_pd, ignore_index=True)
    df_game_csv.to_csv("database.csv", mode='w', header=True, index=False)


def load_game_position(key):
    df_game_position = pd.read_csv("database.csv")
    df_game_position = df_game_position.loc[df_game_position["key"] == key]
    print(df_game_position)
