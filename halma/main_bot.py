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
    player1 = Bot('Arnold', RED)
    player2 = Bot('Bot', BLUE)
    player3 = Bot('Bot3', GREEN)
    player4 = Bot('Bot4', YELLOW)
    board = Board(WIN, player1, player2, player3, player4)
    game = Game(WIN, board)
    game.board().player1.add_game(game)
    game.board().player2.add_game(game)
    game.board().player3.add_game(game)
    game.board().player4.add_game(game)
    game.choose_animate(True)

    while run:
        clock.tick(FPS)

        if not game.result:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # if game.turn == RED:
                #     if event.type == pygame.MOUSEBUTTONDOWN:
                #         if game.selected_checker() == 0:
                #             x, y = pygame.mouse.get_pos()
                #             row, col = transfer_into_rows_and_cols(x, y)
                #             if game.board().get_checker(row, col) != 0:
                #                 if game.board().get_checker(row, col).color == game.turn:
                #                     game.change_selected_checker(game.board().get_checker(row, col))
                #                     if game.selected_checker() != 0:
                #                         game.selected_checker().change_selected(True)

                #         elif game.selected_checker() != 0:
                #             x, y = pygame.mouse.get_pos()
                #             row, col = transfer_into_rows_and_cols(x, y)
                #             all_possible_moves = game.board().valid_moves(game.selected_checker())
                #             if game.board().get_checker(row, col) != 0 or (row, col) not in all_possible_moves:
                #                 game.selected_checker().change_selected(False)
                #                 game.change_selected_checker(0)
                #             else:
                #                 game.board().move_checker(game.selected_checker(), row, col)
                #                 game.selected_checker().change_selected(False)
                #                 game.change_selected_checker(0)

                #                 pygame.display.set_caption('Halma, BLUE')

                #                 game.change_turn()


            if game.turn == RED:
                player1.make_moves_dict()
                checker, leng = player1.best_checker_with_move_len()
                move = player1.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()

            if game.turn == BLUE:
                player2.make_moves_dict()
                checker, leng = player2.best_checker_with_move_len()
                move = player2.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()

            elif game.turn == GREEN:
                player3.make_moves_dict()
                checker, leng = player3.best_checker_with_move_len()
                move = player3.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()

            elif game.turn == YELLOW:
                player4.make_moves_dict()
                checker, leng = player4.best_checker_with_move_len()
                move = player4.best_move(checker, leng)
                game.board().move_checker(checker, move[0], move[1])
                game.change_turn()

        if game.result:
            run = False

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
