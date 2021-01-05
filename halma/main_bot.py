
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker
from game import Game, Player
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


player1 = Player('Arnold')
player2 = Player('Bot')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(player1, player2)
    game = Game(WIN, board)

    while run:
        clock.tick(FPS)

        if not game.result:
            if game.turn == RED:
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

                                pygame.display.set_caption('Halma, BLUE')

                                game.change_turn()

            # if game.turn == RED:
            #     moves = []
            #     while len(moves) == 0:
            #         checker = choice(player1.checkers)
            #         moves = [move for move in game.board().valid_moves(checker) if move]
            #     moves_dict = {math.sqrt((move[0] ** 2) + (move[1] ** 2)): move for move in moves}
            #     max_len = max(moves_dict.keys())

            #     if checker.target:
            #         current_pos = math.sqrt(checker.row ** 2 + checker.col ** 2)
            #         if max_len > current_pos:
            #             move = moves_dict[max_len]
            #             game.board().move_checker(checker, move[0], move[1])
            #             game.change_turn()

            #     elif not checker.target:
            #         move = moves_dict[max_len]
            #         game.board().move_checker(checker, move[0], move[1])
            #         game.change_turn()
            #     pygame.display.set_caption('Halma, BLUE')

            if game.turn == BLUE:
                moves = []
                while len(moves) == 0:
                    checker = choice(player2.checkers)
                    moves = [move for move in game.board().valid_moves(checker) if move]

                moves_dict = {math.sqrt(move[1] ** 2 + move[0] ** 2): move for move in moves}
                min_len = min(moves_dict.keys())

                if checker.target:
                    current_pos = math.sqrt(checker.row ** 2 + checker.col ** 2)
                    if min_len < current_pos:
                        move = moves_dict[min_len]
                        game.board().move_checker(checker, move[0], move[1])
                        game.change_turn()

                elif not checker.target:
                    move = moves_dict[min_len]
                    game.board().move_checker(checker, move[0], move[1])
                    game.change_turn()
                pygame.display.set_caption('Halma, RED')

        if game.result:
            run = False

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
