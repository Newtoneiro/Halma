from checker import Checker
from game import Game, Player, EasyBot, Bot
from board import Board
from constants import *
import pygame

#checker.py

def test_create_checker_red():
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    assert checker.SQUARE_SIZE == 50
    assert checker.row == 0
    assert checker.col == 0
    assert checker.selected == False
    assert checker.target == False
    assert checker.home == True
    assert checker.useless_moves == []
    assert checker.made_moves == []
    assert checker.home_base == RED_BASE
    assert checker.target_base == BLUE_BASE
    assert checker.being_moved == False


def test_create_checker_blue():
    checker = Checker(0, 0, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.SQUARE_SIZE == 50
    assert checker.row == 0
    assert checker.col == 0
    assert checker.selected == False
    assert checker.target == False
    assert checker.home == True
    assert checker.useless_moves == []
    assert checker.made_moves == []
    assert checker.home_base == BLUE_BASE
    assert checker.target_base == RED_BASE
    assert checker.being_moved == False


def test_update_being_moved():
    checker = Checker(0, 0, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.being_moved == False
    checker.being_moved_change(True)
    assert checker.being_moved == True
    checker.being_moved_change(False)
    assert checker.being_moved == False


def test_checker_add_useless_move():
    checker = Checker(0, 0, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.useless_moves == []
    checker.add_useless_move((2, 4))
    assert checker.useless_moves == [(2, 4)]


def test_checker_add_made_move():
    checker = Checker(0, 0, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.made_moves == []
    checker.add_made_move((2, 4))
    assert checker.made_moves == [(2, 4)]


def test_checker_update_status():
    checker = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.home == True
    assert checker.target == False
    checker.move(0, 0)
    checker.update_status()
    assert checker.home == False
    assert checker.target == True


def test_checker_change_target():
    checker = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.target == False
    checker.change_target()
    assert checker.target == True
    checker.change_target()
    assert checker.target == False


def test_checker_change_home():
    checker = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.home == True
    checker.change_home()
    assert checker.home == False
    checker.change_home()
    assert checker.home == True


def test_checker_change_selected():
    checker = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.selected == False
    checker.change_selected(True)
    assert checker.selected == True
    checker.change_selected(False)
    assert checker.selected == False


def test_checker_get_possition():
    checker = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.x == 775
    assert checker.y == 775


def test_checker_get_possition_2():
    checker = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.x == 575
    assert checker.y == 225


def test_checker_move():
    checker = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    assert checker.x == 575
    assert checker.y == 225
    checker.move(5, 1)
    assert checker.x == 75
    assert checker.y == 275

#Player

def test_make_player_without_checkers():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []


def test_make_player_with_checkers():
    checker1 = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    checker2 = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    checkers = [checker1, checker2]
    player = Player('Zygfryd', GREEN, checkers)
    assert player.name == 'Zygfryd'
    assert player.colour == GREEN
    assert len(player.checkers) == 2


def test_player_add_game():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []
    game = 'game_object'
    player.add_game(game)
    assert player.game == 'game_object'


def test_player_add_Checker():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []
    checker1 = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    player.add_checker(checker1)
    assert len(player.checkers) == 1


#bot


def test_make_bot():
    bot = Bot('Blue', RED)
    assert bot.name == 'Blue'
    assert bot.colour == RED
    assert bot.checkers == []


#board.py


def test_board_create_2players(monkeypatch):
    # I dont need to check if the sounds imported correctly
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.SQUARE_SIZE == 50
    assert board.player1 == player1
    assert board.player2 == player2
    assert board.player3 == None
    assert board.player4 == None
    assert board.BLUE_BASE == BLUE_BASE_2
    assert board.RED_BASE == RED_BASE_2
    assert board.win == 'window'
    assert board.rows == ROWS
    assert board.cols == COLS
    assert board.GREEN_BASE == GREEN_BASE
    assert board.YELLOW_BASE == YELLOW_BASE


def test_board_create_4players(monkeypatch):
    # I dont need to check if the sounds imported correctly
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    player3 = Player('ZYGFRYYD2', GREEN)
    player4 = Player('Radziwił2', YELLOW)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2, player3, player4)
    assert board.SQUARE_SIZE == 50
    assert board.player1 == player1
    assert board.player2 == player2
    assert board.player3 == player3
    assert board.player4 == player4
    assert board.BLUE_BASE == BLUE_BASE
    assert board.RED_BASE == RED_BASE
    assert board.GREEN_BASE == GREEN_BASE
    assert board.YELLOW_BASE == YELLOW_BASE
    assert board.win == 'window'
    assert board.rows == ROWS
    assert board.cols == COLS


def test_board_moves_paths_clear(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.SQUARE_SIZE == 50
    assert board.player1 == player1
    assert board.player2 == player2
    board.moves_paths = {'1' : (2, 3)}
    assert len(board.moves_paths) != 0
    board.moves_paths_clear()
    assert len(board.moves_paths) == 0


def test_board_create_board_list_2p(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert len(board.board) == 16
    total_checkers = 0
    for row in board.board:
        for OBJECT in row:
            if OBJECT != 0:
                total_checkers += 1
    assert total_checkers == 38


def test_board_create_board_list_4p(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    player3 = Player('ZYGFRYYD2', GREEN)
    player4 = Player('Radziwił2', YELLOW)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2, player3, player4)
    assert len(board.board) == 16
    total_checkers = 0
    for row in board.board:
        for OBJECT in row:
            if OBJECT != 0:
                total_checkers += 1
    assert total_checkers == 52


def test_board_space_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.space_right(0, 4) == (0, 5)
    assert board.space_right(15, 15) == None

def test_board_space_left(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.space_left(0, 4) == None
    assert board.space_left(15, 11) == (15, 10)


def test_board_space_up(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.space_up(0, 4) == None
    assert board.space_up(14, 11) == (13, 11)


def test_board_space_down(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.space_down(4, 4) == (5, 4)
    assert board.space_down(15, 15) == None


def test_board_space_crosswise_up_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.crosswise_up_right(4, 4) == (3, 5)
    assert board.crosswise_up_right(15, 15) == None


def test_board_space_crosswise_up_left(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.crosswise_up_left(15, 11) == (14, 10)
    assert board.crosswise_up_left(15, 15) == None


def test_board_space_crosswise_down_left(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.crosswise_down_left(4, 1) == (5, 0)
    assert board.crosswise_down_left(15, 15) == None


def test_board_space_crosswise_down_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.crosswise_down_right(4, 1) == (5, 2)
    assert board.crosswise_down_right(13, 12) == None


def test_board_check_jump_up(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_up(15, 11) == (13, 11)
    assert board.check_jump_up(13, 12) == None


def test_board_check_jump_down(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_down(0, 4) == (2, 4)
    assert board.check_jump_down(1, 4) == None


def test_board_check_jump_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_right(0, 3) == (0, 5)
    assert board.check_jump_right(1, 4) == None


def test_board_check_jump_left(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_left(15, 12) == (15, 10)
    assert board.check_jump_left(1, 4) == None


def test_board_check_jump_up_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_up_right(2, 3) == (0, 5)
    assert board.check_jump_up_right(1, 4) == None


def test_board_check_jump_down_right(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_down_right(3, 0) == (5, 2)
    assert board.check_jump_down_right(15, 15) == None


def test_board_check_jump_down_left(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.check_jump_down_left(13, 12) == (15, 10)
    assert board.check_jump_down_left(15, 15) == None


def test_board_check_all_directions(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert board.check_all_directions(1, 1) == [(2, 1), (1, 0), (1, 2), (0, 1), (2, 0), (3, 3), (0, 0), (0, 2)]
    assert board.check_all_directions(0, 0) == [(1, 0), (0, 1)]


def test_board_check_jump_all_directions(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert board.check_jump_all_directions(1, 1) == [(3, 3), (5, 3), (3, 5), (7, 3)]


def test_board_get_all_jumps_from_square(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert board.get_all_jumps_from_square(1, 1) == [(3, 3)]
    assert board.get_all_jumps_from_square(4, 3) == [(4, 5), (2, 5)]


def test_board_get_path(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert board.get_path((1, 1), (7, 5)) == [(1, 1), (3, 3), (5, 3), (7, 3), (5, 5), (7, 5)]
    assert board.get_path((1, 1), (3, 3)) == [(1, 1), (3, 3)]


def test_board_cut_path(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, checker, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, checker, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    assert board.cut_path((1, 1), (7, 5)) == [(1, 1), (3, 3), (5, 3), (7, 3), (7, 5)]
    assert board.cut_path((1, 1), (3, 3)) == [(1, 1), (3, 3)]


def test_board_get_checker(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    assert board.get_checker(0, 0) != 0
    assert board.get_checker(8, 8) == 0


def test_board_move_checker(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.animations = False
    board.move_checker(board.get_checker(0, 0), 5, 5)
    assert board.get_checker(5, 5) != 0
    assert board.get_checker(5, 5).row == 5


def test_board_set_mute(monkeypatch):
    def fake_sounds(self):
        return None

    WIN = 'window'
    player1 = Player('ZYGFRYYD', RED)
    player2 = Player('Radziwił', BLUE)
    checker = Checker(0, 0, RED, RED_BASE, BLUE_BASE, 50)
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    board = Board(50, WIN, player1, player2)
    board.set_mute(False)
    assert board.mute == False
    board.set_mute(True)
    assert board.mute == True


# GAME

def test_create_game_normal_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game.win == WIN
    assert game.turn == RED
    assert game.tiny_window == False
    assert game.WIDTH == 800
    assert game.HEIGHT == 800
    assert game.SQUARE_SIZE == 50
    assert game._selected_checker == 0
    assert game.result == None
    assert game.hard_difficulty == False
    assert game.mute == False
    assert game.how_many_players == 4
    assert game.mode == 0
    assert game.FPS == 60


def test_create_game_tiny_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, True, 2, 1, True, 60)
    assert game.turn == RED
    assert game.tiny_window == True
    assert game.WIDTH == 400
    assert game.HEIGHT == 400
    assert game.SQUARE_SIZE == 25
    assert game._selected_checker == 0
    assert game.result == None
    assert game.hard_difficulty == False
    assert game.mute == True
    assert game.how_many_players == 2
    assert game.mode == 1
    assert game.FPS == 60


def test_game_transwer_into_rows_and_cols(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game.transfer_into_rows_and_cols(650, 530) == (10, 13)


def test_game_transwer_into_rows_and_cols_tiny_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, False, 4, 0, True, 60)
    assert game.transfer_into_rows_and_cols(250, 130) == (5, 10)


def test_game_create_a_board(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game._board.SQUARE_SIZE == 50
    assert game._board.win == WIN
    assert type(game._board.player1) == Player
    assert type(game._board.player2) == Player
    assert type(game._board.player3) == Player
    assert type(game._board.player4) == Player


def test_game_create_a_board_tiny_window_2v2_pvai(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, False, 2, 1, True, 60)
    assert game._board.SQUARE_SIZE == 25
    assert type(game._board.player1) == Player
    assert type(game._board.player2) == EasyBot


def test_game_create_a_board_4v4_bot(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 2, True, 60)
    assert game._board.SQUARE_SIZE == 50
    assert game._board.win == WIN
    assert type(game._board.player1) == Bot
    assert type(game._board.player2) == Bot
    assert type(game._board.player3) == Bot
    assert type(game._board.player4) == Bot


def test_game_board_select_animate(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 2, True, 60)
    assert game._board.animations == True
    game.choose_animate(False)
    assert game._board.animations == False


def test_game_check_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.result == None
    checker1 = Checker(15, 15, RED, RED_BASE, BLUE_BASE, 50)
    checker1.update_status()
    checker2 = Checker(0, 3, BLUE, BLUE_BASE, RED_BASE, 50)
    checker2.update_status()
    game.board().player1.checkers = [checker1, checker1, checker1]
    game.board().player2.checkers = [checker2, checker2, checker2]
    game.check_win()
    assert game.result == None
    # The rest of cases were tested in live playthroughs, because it would take a lot
    # of time to create individual pieces and assign them to game.board() players
    # Nonetheless i assured this win checking function works properly


def test_game_change_selected_checker(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.selected_checker() == 0
    checker1 = Checker(15, 15, RED, RED_BASE, BLUE_BASE, 50)
    game.change_selected_checker(checker1)
    assert game.selected_checker() == checker1
    game.change_selected_checker(0)
    assert game.selected_checker() == 0


def test_game_change_turn4p(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 0, True, 60)
    assert game.turn == RED
    game.change_turn()
    assert game.turn == YELLOW
    game.change_turn()
    assert game.turn == BLUE
    game.change_turn()
    assert game.turn == GREEN
    game.change_turn()
    assert game.turn == RED


def test_game_change_turn2p(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.turn == RED
    game.change_turn()
    assert game.turn == BLUE
    game.change_turn()
    assert game.turn == RED








