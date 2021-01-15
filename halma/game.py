from constants import *
from board import Board
import pygame
from checker import Checker
import math
from random import choice

class Game:
    def __init__(self, win, starting_player, tiny_window, hard, mute, how_many_players, mode, animations, FPS):
        self.tiny_window = tiny_window
        if self.tiny_window:
            self.win = pygame.display.set_mode((400, 400))
            self.HEIGHT = 400
            self.WIDTH = 400
        else:
            self.win = win
            self.HEIGHT = 800
            self.WIDTH = 800
        self.SQUARE_SIZE = self.WIDTH//ROWS
        self.turn = starting_player
        self._selected_checker = 0
        self.result = None
        self.hard_difficulty = hard
        self.mute = mute
        self.how_many_players = how_many_players
        self.mode = mode
        self.create_board()
        self.board().set_mute(self.mute)
        self.choose_animate(animations)
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def transfer_into_rows_and_cols(self, x, y):
        row = y//self.SQUARE_SIZE
        col = x//self.SQUARE_SIZE
        return row, col

    def play(self):
        if self.mode == 0:
            self.playpvp()
        elif self.mode == 1:
            self.playpvai()
        elif self.mode ==2:
            self.playaivai()

    def playpvp(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            if not self.result:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.player_make_a_move()
            if self.result:
                run = False
            self.update()

    def playpvai(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            if not self.result:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.turn == RED:
                            self.player_make_a_move()
                    if self.turn != RED:
                        self.bot_make_a_move()
            if self.result:
                run = False
            self.update()

    def playaivai(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.clock.tick(self.FPS)
            if not self.result:
                self.bot_make_a_move()
            if self.result:
                run = False
            self.update()

    def player_make_a_move(self):
        if self.selected_checker() == 0:
            x, y = pygame.mouse.get_pos()
            row, col = self.transfer_into_rows_and_cols(x, y)
            if self.board().get_checker(row, col) != 0:
                if self.board().get_checker(row, col).color == self.turn:
                    self.change_selected_checker(self.board().get_checker(row, col))
                    if self.selected_checker() != 0:
                        self.selected_checker().change_selected(True)

        elif self.selected_checker() != 0:
            x, y = pygame.mouse.get_pos()
            row, col = self.transfer_into_rows_and_cols(x, y)
            all_possible_moves = self.board().valid_moves(self.selected_checker())
            if self.board().get_checker(row, col) != 0 or (row, col) not in all_possible_moves:
                self.selected_checker().change_selected(False)
                self.change_selected_checker(0)
            else:
                self.board().move_checker(self.selected_checker(), row, col)
                self.selected_checker().change_selected(False)
                self.change_selected_checker(0)
                self.change_turn()

    def bot_make_a_move(self):
        if self.turn == RED:
            self.board().player1.make_moves_dict()
            checker, leng = self.board().player1.best_checker_with_move_len()
            move = self.board().player1.best_move(checker, leng)
            self.board().move_checker(checker, move[0], move[1])
            self.change_turn()

        elif self.turn == BLUE:
            self.board().player2.make_moves_dict()
            checker, leng = self.board().player2.best_checker_with_move_len()
            move = self.board().player2.best_move(checker, leng)
            self.board().move_checker(checker, move[0], move[1])
            self.change_turn()

        elif self.turn == GREEN:
            self.board().player3.make_moves_dict()
            checker, leng = self.board().player3.best_checker_with_move_len()
            move = self.board().player3.best_move(checker, leng)
            self.board().move_checker(checker, move[0], move[1])
            self.change_turn()

        elif self.turn == YELLOW:
            self.board().player4.make_moves_dict()
            checker, leng = self.board().player4.best_checker_with_move_len()
            move = self.board().player4.best_move(checker, leng)
            self.board().move_checker(checker, move[0], move[1])
            self.change_turn()

    def create_board(self):
        if self.mode == 0:
            player1 = Player('RED', RED)
            player2 = Player('BLUE', BLUE)
            player3 = Player('GREEN', GREEN)
            player4 = Player('YELLOW', YELLOW)
            if self.how_many_players == 4:
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2, player3, player4)
            elif self.how_many_players == 2:
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2)
        elif self.mode == 1:
            if self.how_many_players == 2:
                player1 = Player('RED', RED)
                if self.hard_difficulty:
                    player2 = Bot('BOT', BLUE)
                elif not self.hard_difficulty:
                    player2 = EasyBot('BOT', BLUE)
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2)
            elif self.how_many_players == 4:
                player1 = Player('RED', RED)
                if self.hard_difficulty:
                    player2 = Bot('BOT BLUE', BLUE)
                    player3 = Bot('BOT GREEN', GREEN)
                    player4 = Bot('BOT YELLOw', YELLOW)
                elif not self.hard_difficulty:
                    player2 = EasyBot('BOT BLUE', BLUE)
                    player3 = EasyBot('BOT GREEN', GREEN)
                    player4 = EasyBot('BOT YELLOw', YELLOW)
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2, player3, player4)
        elif self.mode == 2:
            if self.how_many_players == 2:
                if self.hard_difficulty:
                    player1 = Bot('BOT RED', RED)
                    player2 = Bot('BOT BLUE', BLUE)
                elif not self.hard_difficulty:
                    player1 = EasyBot('BOT RED', RED)
                    player2 = EasyBot('BOT BLUE', BLUE)
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2)
            elif self.how_many_players == 4:
                if self.hard_difficulty:
                    player1 = Bot('BOT RED', RED)
                    player2 = Bot('BOT BLUE', BLUE)
                    player3 = Bot('BOT GREEN', GREEN)
                    player4 = Bot('BOT YELLOW', YELLOW)
                elif not self.hard_difficulty:
                    player1 = EasyBot('BOT RED', RED)
                    player2 = EasyBot('BOT BLUE', BLUE)
                    player3 = EasyBot('BOT GREEN', GREEN)
                    player4 = EasyBot('BOT YELLOW', YELLOW)
                self._board = Board(self.SQUARE_SIZE, self.win, player1, player2, player3, player4)
        if self.how_many_players == 2:
            self._board.player1.add_game(self)
            self._board.player2.add_game(self)
        elif self.how_many_players == 4:
            self._board.player1.add_game(self)
            self._board.player2.add_game(self)
            self._board.player3.add_game(self)
            self._board.player4.add_game(self)

    def update(self):
        if not self.result:
            self.board().draw(self.win)
            pygame.display.update()
            self.check_win()

    def choose_animate(self, value):
        self.board().animations = value

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
        return self.moves_dict[best_len][1]
