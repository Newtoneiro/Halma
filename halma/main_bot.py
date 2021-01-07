import time
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker
from game import Game, Player, Bot, EasyBot
from random import choice
import math

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Halma, RED')


def transfer_into_rows_and_cols(x, y):
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    player1 = EasyBot('Arnold', RED)
    player2 = EasyBot('Bot', BLUE)
    board = Board(player1, player2)
    game = Game(WIN, board)
    player1.add_game(game)
    player2.add_game(game)


    while run:
        clock.tick(FPS)

        if not game.result:
            # if game.turn == RED:
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             run = False
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             if game.selected_checker() == 0:
            #                 x, y = pygame.mouse.get_pos()
            #                 row, col = transfer_into_rows_and_cols(x, y)
            #                 if game.board().get_checker(row, col) != 0:
            #                     if game.board().get_checker(row, col).color == game.turn:
            #                         game.change_selected_checker(game.board().get_checker(row, col))
            #                         if game.selected_checker() != 0:
            #                             game.selected_checker().change_selected(True)

            #             elif game.selected_checker() != 0:
            #                 x, y = pygame.mouse.get_pos()
            #                 row, col = transfer_into_rows_and_cols(x, y)
            #                 all_possible_moves = game.board().valid_moves(game.selected_checker())
            #                 if game.board().get_checker(row, col) != 0 or (row, col) not in all_possible_moves:
            #                     game.selected_checker().change_selected(False)
            #                     game.change_selected_checker(0)
            #                 else:
            #                     game.board().move_checker(game.selected_checker(), row, col)
            #                     game.selected_checker().change_selected(False)
            #                     game.change_selected_checker(0)

            #                     pygame.display.set_caption('Halma, BLUE')

            #                     game.change_turn()

            if game.turn == RED:
                player1.make_moves_dict()
                checker, leng = player1.best_checker_with_move_len()
                move = player1.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()
                time.sleep(0.1)

            elif game.turn == BLUE:
                player2.make_moves_dict()
                checker, leng = player2.best_checker_with_move_len()
                move = player2.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()


        if game.result:
            run = False

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
