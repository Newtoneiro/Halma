from checker import Checker
from game import Game, Player
from constants import *

def test_create_checker():
    checker = Checker(1, 2, RED)
    assert checker.row == 1
    assert checker.col == 2
    assert checker.color == RED
    assert checker.x == 125
    assert checker.y == 75
    assert checker.target_base == BLUE_BASE
    assert checker.home_base == RED_BASE

def test_create_checker_blue():
    checker = Checker(1, 2, BLUE)
    assert checker.row == 1
    assert checker.col == 2
    assert checker.color == BLUE
    assert checker.x == 125
    assert checker.y == 75
    assert checker.target_base == RED_BASE
    assert checker.home_base == BLUE_BASE

def test_change_home():
    checker = Checker(1, 2, RED)
    assert checker.home == True
    checker.change_home()
    assert checker.home == False

def test_change_home_reversed():
    checker = Checker(1, 2, RED)
    checker.change_home()
    assert checker.home == False
    checker.change_home()
    assert checker.home == True

def test_change_target():
    checker = Checker(1, 2, RED)
    assert checker.target == False
    checker.change_target()
    assert checker.target == True

def test_change_target_reversed():
    checker = Checker(1, 2, RED)
    checker.change_target()
    assert checker.target == True
    checker.change_target()
    assert checker.target == False

def test_checker_move():
    checker = Checker(1, 2, RED)
    assert checker.row == 1
    assert checker.col == 2
    assert checker.color == RED
    assert checker.x == 125
    assert checker.y == 75
    checker.move(7, 8)
    assert checker.row == 7
    assert checker.col == 8
    assert checker.x == 425
    assert checker.y == 375

def test_create_player():
    player1 = Player('Maciek')
    assert player1.name == 'Maciek'
    assert player1.checkers == []

def test_player_add_checkers():
    player1 = Player('Maciek')
    assert player1.name == 'Maciek'
    assert player1.checkers == []
    checkers = [Checker(0, 0, RED), Checker(0, 1, RED)]
    for checker in checkers:
        player1.add_checker(checker)
    assert len(player1.checkers) == 2



