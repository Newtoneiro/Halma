from constants import *
from board import Board
import pygame
from checker import Checker
import math
from random import choice

class Game:
    def __init__(self, win, board):
        self.win = win
        self.turn = RED
        self._board = board
        self._selected_checker = 0
        self.result = None

    def update(self):
        if not self.result:
            self.board().draw(self.win)
            pygame.display.update()
            self.check_win()
        else:
            pygame.quit()

    def check_win(self):
        target_score = 19
        if self.board().player3 and self.board().player4:
            target_score = 13
        player1_score = 0
        player2_score = 0
        player3_score = 0
        player4_score = 0
        for checker in self.board().player1.checkers:
            if checker.target:
                player1_score += 1
        for checker in self.board().player2.checkers:
            if checker.target:
                player2_score += 1
        if self.board().player3 and self.board().player4:
            for checker in self.board().player3.checkers:
                if checker.target:
                    player3_score += 1
            for checker in self.board().player4.checkers:
                if checker.target:
                    player4_score += 1

        if player1_score > 0:                             # Anti-spoiling prevention (one wins simply by covering all possible enemy base spaces)
            for checker in self.board().player2.checkers:
                if checker.home:
                    player1_score += 1
        if player2_score > 0:
            for checker in self.board().player1.checkers:
                if checker.home:
                    player2_score += 1
        if self.board().player3 and self.board().player4:
            if player3_score > 0:
                for checker in self.board().player4.checkers:
                    if checker.home:
                        player3_score += 1
            if player4_score > 0 :
                for checker in self.board().player3.checkers:
                    if checker.home:
                        player4_score += 1

        if player1_score == target_score:
            self.result = self.board().player1
        if player2_score == target_score:
            self.result = self.board().player2
        if self.board().player3 and self.board().player4:
            if player3_score == target_score:
                self.result = self.board().player3
            if player4_score == target_score:
                self.result = self.board().player4
        if self.result:
            print(f'The winner is {self.result.name}')

    def selected_checker(self):
        return self._selected_checker

    def change_selected_checker(self, checker):
        self._selected_checker = checker

    def change_turn(self):
        if self.board().player3 and self.board().player4:
            if self.turn == RED:
                self.turn = YELLOW
            elif self.turn == YELLOW:
                self.turn = BLUE
            elif self.turn == BLUE:
                self.turn = GREEN
            elif self.turn == GREEN:
                self.turn = RED
        else:
            if self.turn == RED:
                self.turn = BLUE
            elif self.turn == BLUE:
                self.turn = RED

    def board(self):
        return self._board

class Player():
    def __init__(self, name, colour, checkers=None):
        if not checkers:
            checkers = []
        self.checkers = checkers
        self.name = name
        self.colour = colour

    def add_game(self, game):
        self.game = game

    def add_checker(self, checker):
        self.checkers.append(checker)

class Bot(Player):
    def __init__(self, name, colour, checkers=None):
        super().__init__(name, colour, checkers)

    def make_moves_dict(self):
        moves_dict = {}
        for checker in self.checkers:
            if self.colour == BLUE:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (checker.col + 1) ** 2)
            if self.colour == RED:
                current_pos = math.sqrt((16 - checker.row) ** 2 + (16 - checker.col) ** 2)
            if self.colour == YELLOW:
                current_pos = math.sqrt((16 - checker.row) ** 2 + (checker.col + 1) ** 2)
            if self.colour == GREEN:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (16 - checker.col) ** 2)
            moves = [move for move in self.game.board().valid_moves(checker) if move and move not in checker.useless_moves]
            for move in moves:
                if self.colour == BLUE:
                    moves_dict[current_pos - math.sqrt((move[0] + 1) ** 2 + (move[1] + 1) ** 2)] = (checker, move)
                elif self.colour == RED:
                    moves_dict[current_pos - math.sqrt((16 - move[0]) ** 2 + (16 - move[1]) ** 2)] = (checker, move)
                elif self.colour == YELLOW:
                    moves_dict[current_pos - math.sqrt((16 - move[0]) ** 2 + (move[1] + 1) ** 2)] = (checker, move)
                elif self.colour == GREEN:
                    moves_dict[current_pos - math.sqrt((move[0] + 1) ** 2 + (16 - move[1]) ** 2)] = (checker, move)
        self.moves_dict = moves_dict

    def best_checker_with_move_len(self):
        best_len = max(self.moves_dict.keys())
        checker = self.moves_dict[best_len][0]

        return checker, best_len

    def best_move(self, checker, best_len):
        if checker.target:
            if self.colour == BLUE:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (checker.col + 1) ** 2)
            if self.colour == RED:
                current_pos = math.sqrt((16 - checker.row) ** 2 + (16 - checker.col) ** 2)
            if self.colour == YELLOW:
                current_pos = math.sqrt((16 - checker.row) ** 2 + (checker.col + 1) ** 2)
            if self.colour == GREEN:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (16 - checker.col) ** 2)

            if best_len < current_pos:
                move = self.moves_dict[best_len][1]
            else:
                self.moves_dict.pop(best_len)
                checker, best_len = self.best_checker_with_move_len()
                move = self.best_move(checker, best_len)

        elif not checker.target:
            move = self.moves_dict[best_len][1]

        if move in checker.made_moves:
            if checker.color == RED or checker.color == BLUE:
                move = (move[1], move[0])
            else:
                move = move
        checker.add_made_move(move)

        return move

class EasyBot(Player):
    def __init__(self, name, colour, checkers=None):
        super().__init__(name, colour, checkers)

    def make_moves_dict(self):
        moves_dict = {}
        moves = []
        while len(moves) == 0:
            checker = choice(self.checkers)
            moves = [move for move in self.game.board().valid_moves(checker) if move]

        if self.colour == BLUE:
            current_pos = math.sqrt((checker.row + 1) ** 2 + (checker.col + 1) ** 2)
        if self.colour == RED:
            current_pos = math.sqrt((16 - checker.row) ** 2 + (16 - checker.col) ** 2)
        if self.colour == YELLOW:
            current_pos = math.sqrt((16 - checker.row) ** 2 + (checker.col + 1) ** 2)
        if self.colour == GREEN:
            current_pos = math.sqrt((checker.row + 1) ** 2 + (16 - checker.col) ** 2)

        for move in moves:
            if self.colour == BLUE:
                moves_dict[current_pos - math.sqrt((move[0] + 1) ** 2 + (move[1] + 1) ** 2)] = (checker, move)
            elif self.colour == RED:
                moves_dict[current_pos - math.sqrt((16 - move[0]) ** 2 + (16 - move[1]) ** 2)] = (checker, move)
            elif self.colour == YELLOW:
                moves_dict[current_pos - math.sqrt((16 - move[0]) ** 2 + (move[1] + 1) ** 2)] = (checker, move)
            elif self.colour == GREEN:
                moves_dict[current_pos - math.sqrt((move[0] + 1) ** 2 + (16 - move[1]) ** 2)] = (checker, move)
        self.moves_dict = moves_dict

    def best_checker_with_move_len(self):
        best_len = max(self.moves_dict.keys())
        checker = self.moves_dict[best_len][0]

        return checker, best_len

    def best_move(self, checker, best_len):
        if checker.target:
            if self.colour == BLUE:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (checker.col + 1) ** 2)
            if self.colour == RED:
                current_pos = math.sqrt((16-checker.row) ** 2 + (16 - checker.col) ** 2)
            if self.colour == YELLOW:
                current_pos = math.sqrt((16 - checker.row) ** 2 + (checker.col + 1) ** 2)
            if self.colour == GREEN:
                current_pos = math.sqrt((checker.row + 1) ** 2 + (16 - checker.col) ** 2)

            if best_len < current_pos:
                move = self.moves_dict[best_len][1]
            if best_len < 0:
                checker, best_len = self.best_checker_with_move_len()
                move = self.best_move(checker, best_len)

        elif not checker.target:
            move = self.moves_dict[best_len][1]

        return move

