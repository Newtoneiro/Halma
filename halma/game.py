from constants import *
from board import Board
import pygame
from checker import Checker

class Game:
    def __init__(self, win, board):
        self.win = win
        self.turn = RED
        self._board = board
        self._selected_checker = 0
        self.result = None

    def update(self):
        self.board().draw(self.win)
        pygame.display.update()
        self.check_win()


    def check_win(self):
        player1_score = 0
        player2_score = 0
        for checker in self.board().player1.checkers:
            if checker.target:
                player1_score += 1
        for checker in self.board().player2.checkers:
            if checker.target:
                player2_score += 1
        if player1_score == 19:
            self.result = self.board().player1
        if player2_score == 19:
            self.result = self.board().player2
        if self.result:
            print(f'The winner is {self.result.name}')
            pygame.quit()


    def selected_checker(self):
        return self._selected_checker

    def change_selected_checker(self, checker):
        self._selected_checker = checker

    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        elif self.turn == BLUE:
            self.turn = RED

    def board(self):
        return self._board

class Player():
    def __init__(self, name, checkers=None):
        if not checkers:
            checkers = []
        self.checkers = checkers
        self.name = name

    def add_checker(self, checker):
        self.checkers.append(checker)