from board import Board
from game import Player
from checker import Checker
from constants import *

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