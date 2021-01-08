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

def transfer_into_rows_and_cols(x, y):
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    player1 = Player('Arnold', RED)
    player2 = Player('Boczek', BLUE)
    player3 = Player('Boczek', GREEN)
    player4 = Player('Boczek', YELLOW)
    board = Board(player1, player2, player3, player4)
    game = Game(WIN, board)
    game.board().player1.add_game(game)
    game.board().player2.add_game(game)
    game.board().player3.add_game(game)
    game.board().player4.add_game(game)

    while run:
        clock.tick(FPS)

        if not game.result:
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
                            if game.turn == RED:
                                pygame.display.set_caption('Halma, BLUE')
                            elif game.turn == BLUE:
                                pygame.display.set_caption('Halma, RED')
                            game.change_turn()
        if game.result:
            run = False

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
