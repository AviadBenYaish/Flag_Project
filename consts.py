import pygame
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
BLOCK_SIZE = (SCREEN_WIDTH / 50, SCREEN_HEIGHT / 25)
BACKGROUND_COLOR = (76, 153, 0)
SQUARE_EMPTY = 'EMPTY'
SQUARE_FLAG = 'FLAG'
SQUARE_BOMB = 'BOMB'
SQUARE_BODY = 'BODY'
SQUARE_LEGS = 'LEGS'
GRASS_IMAGE = pygame.image.load("./images/grass.png")
FLAG_IMAGE = pygame.image.load("./images/flag.png")
LINES_COLOR = (0, 102, 0)
PLAYER_IMAGE = pygame.image.load("./images/soldier.png")
PLAYER_INITIAL_POSITION = (0, 0)
PLAYER_SIZE = (410 / 5, 512 / 5)
EMPTY_SQUARE = 'EMPTY'