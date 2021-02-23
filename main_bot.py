import time
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker
from game import Game, Player, Bot, EasyBot


FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Halma')


def transfer_into_rows_and_cols(x, y):
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN, GREEN, False, False, False, 4, 1, True, 60)
    game.play()
    pygame.quit()


if __name__ == '__main__':
    main()
