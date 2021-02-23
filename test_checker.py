from checker import Checker
from constants import *


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
