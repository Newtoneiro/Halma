import os
import sys
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker


FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Halma')

def transfer_into_rows_and_cols(x, y):
    row = x//SQUARE_SIZE
    col = y//SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    selected_checker = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_checker == 0:
                    x, y = pygame.mouse.get_pos()
                    row, col = transfer_into_rows_and_cols(x, y)
                    selected_checker = board.get_checker(row, col)
                    if selected_checker != 0:
                        selected_checker.change_selected(True)

                elif selected_checker != 0:
                    selected_checker.change_selected(False)
                    x, y = pygame.mouse.get_pos()
                    row, col = transfer_into_rows_and_cols(x, y)
                    board.move_checker(selected_checker, row, col)
                    selected_checker = 0
                
                else:
                    pass


        board.draw_squares(WIN)
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()