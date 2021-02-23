import os
import sys
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker
from game import Game, Player

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Halma, RED')

def main():
    run = True
    game = Game(WIN, YELLOW, False, False, True, 4, 0, True, FPS)
    game.playpvp()
    pygame.quit()


if __name__ == '__main__':
    main()
