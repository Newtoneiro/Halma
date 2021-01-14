from checkers import Field, CoordinatesError, Checker, CheckerError, OccupationError
import pytest


def test_field_create():
    A1 = Field([1, 1], False)
    assert A1.row() == 1
    assert A1.column() == 1

def test_field_create_invalid():
    with pytest.raises(CoordinatesError):
        A1 = Field([], False)

def test_checker_create_empty_field():
    A1 = Field([1, 1], False)
    assert A1.occupied() is False
    checker1 = Checker('BLACK', A1)
    assert checker1.colour() == 'BLACK'
    assert checker1.occupied_field() == A1
    assert A1.occupied() is True

def test_checker_create_invalid_colour():
    A1 = Field([1, 1], False)
    assert A1.occupied() is False
    with pytest.raises(CheckerError):
        checker1 = Checker('fsafsa', A1)

def test_checker_create_no_colour():
    A1 = Field([1, 1], False)
    assert A1.occupied() is False
    with pytest.raises(CheckerError):
        checker1 = Checker('', A1)

def test_checker_create_no_field():
    A1 = Field([1, 1], False)
    assert A1.occupied() is False
    with pytest.raises(CoordinatesError):
        checker1 = Checker('RED')


def test_checker_create_occupied_field():
    A1 = Field([1, 1], True)
    assert A1.occupied() is True
    with pytest.raises(OccupationError):
        checker1 = Checker('BLACK', A1)

def test_move_checker():
    A1 = Field([1, 1], False)
    A2 = Field([1, 2], False)
    assert A1.occupied() is False
    assert A1.occupied() is False
    checker1 = Checker('BLACK', A1)
    assert checker1.colour() == 'BLACK'
    assert checker1.occupied_field() == A1
    assert A1.occupied() is True
    checker1.move(A2)
    assert A1.occupied() is False
    assert A2.occupied() is True
    assert checker1._occupied_field == A2

def test_move_right():
    checker1 = Checker('BLACK', D4)
    checker1.move_right()
    assert D4.occupied() is False
    assert checker1.occupied_field().column() == 5
    assert checker1.occupied_field().row() == 5
    assert D5.occupied() is True

A1 = Field([8, 1], False)
A2 = Field([8, 2], False)
A3 = Field([8, 3], False)
A4 = Field([8, 4], False)
A5 = Field([8, 5], False)
A6 = Field([8, 6], False)
A7 = Field([8, 7], False)
A8 = Field([8, 8], False)
B1 = Field([7, 1], False)
B2 = Field([7, 2], False)
B3 = Field([7, 3], False)
B4 = Field([7, 4], False)
B5 = Field([7, 5], False)
B6 = Field([7, 6], False)
B7 = Field([7, 7], False)
B8 = Field([7, 8], False)
C1 = Field([6, 1], False)
C2 = Field([6, 2], False)
C3 = Field([6, 3], False)
C4 = Field([6, 4], False)
C5 = Field([6, 5], False)
C6 = Field([6, 6], False)
C7 = Field([6, 7], False)
C8 = Field([6, 8], False)
D1 = Field([5, 1], False)
D2 = Field([5, 2], False)
D3 = Field([5, 3], False)
D4 = Field([5, 4], False)
D5 = Field([5, 5], False)
D6 = Field([5, 6], False)
D7 = Field([5, 7], False)
D8 = Field([5, 8], False)
E1 = Field([4, 1], False)
E2 = Field([4, 2], False)
E3 = Field([4, 3], False)
E4 = Field([4, 4], False)
E5 = Field([4, 5], False)
E6 = Field([4, 6], False)
E7 = Field([4, 7], False)
E8 = Field([4, 8], False)
F1 = Field([3, 1], False)
F2 = Field([3, 2], False)
F3 = Field([3, 3], False)
F4 = Field([3, 4], False)
F5 = Field([3, 5], False)
F6 = Field([3, 6], False)
F7 = Field([3, 7], False)
F8 = Field([3, 8], False)
G1 = Field([2, 1], False)
G2 = Field([2, 2], False)
G3 = Field([2, 3], False)
G4 = Field([2, 4], False)
G5 = Field([2, 5], False)
G6 = Field([2, 6], False)
G7 = Field([2, 7], False)
G8 = Field([2, 8], False)
H1 = Field([1, 1], False)
H2 = Field([1, 2], False)
H3 = Field([1, 3], False)
H4 = Field([1, 4], False)
H5 = Field([1, 5], False)
H6 = Field([1, 6], False)
H7 = Field([1, 7], False)
H8 = Field([1, 8], False)

my_map = [ 
    [H1, H2, H3, H4, H5, H6, H7, H8],
    [G1, G2, G3, G4, G5, G6, G7, G8],
    [F1, F2, F3, F4, F5, F6, F7, F8],
    [E1, E2, E3, E4, E5, E6, E7, E8],
    [D1, D2, D3, D4, D5, D6, D7, D8],
    [C1, C2, C3, C4, C5, C6, C7, C8],
    [B1, B2, B3, B4, B5, B6, B7, B8],
    [A1, A2, A3, A4, A5, A6, A7, A8]
]
