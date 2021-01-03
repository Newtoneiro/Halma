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

pygame.display.set_caption('Halma')

def transfer_into_rows_and_cols(x, y):
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col

player1 = Player('Arnold')
player2 = Player('Boczek')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(player1, player2)
    game = Game(WIN, board)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.selected_checker() == 0:
                    x, y = pygame.mouse.get_pos()
                    row, col = transfer_into_rows_and_cols(x, y)
                    if game.board().get_checker(row, col) != 0:
                        if game.board().get_checker(row, col).color == game.turn:
                            game.change_selected_checker(game.board().get_checker(row, col))
                            if game.selected_checker() != 0:
                                game.selected_checker().change_selected(True)

                elif game.selected_checker() != 0:
                    x, y = pygame.mouse.get_pos()
                    row, col = transfer_into_rows_and_cols(x, y)
                    all_possible_moves = game.board().valid_moves(game.selected_checker())
                    if game.board().get_checker(row, col) != 0 or (row, col) not in all_possible_moves:
                        game.selected_checker().change_selected(False)
                        game.change_selected_checker(0)
                    else:
                        game.board().move_checker(game.selected_checker(), row, col)
                        game.selected_checker().change_selected(False)
                        game.change_selected_checker(0)
                        game.change_turn()

        game.update()
    pygame.quit()


main()