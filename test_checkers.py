from checkers import Field, CoordinatesError, Checker, CheckerError, OccupationError
import pytest

def test_field_create():
    A1 = Field(['A', 1], False)
    assert A1.length() == 1
    assert A1.width() == 1

def test_field_create_invalid():
    with pytest.raises(CoordinatesError):
        A1 = Field([], False)

def test_checker_create_empty_field():
    A1 = Field(['A', 1], False)
    assert A1.occupied() is False
    checker1 = Checker('BLACK', A1)
    assert checker1.colour() == 'BLACK'
    assert checker1.occupied_field() == A1
    assert A1.occupied() is True

def test_checker_create_invalid_colour():
    A1 = Field(['A', 1], False)
    assert A1.occupied() is False
    with pytest.raises(CheckerError):
        checker1 = Checker('fsafsa', A1)

def test_checker_create_no_colour():
    A1 = Field(['A', 1], False)
    assert A1.occupied() is False
    with pytest.raises(CheckerError):
        checker1 = Checker('', A1)

def test_checker_create_no_field():
    A1 = Field(['A', 1], False)
    assert A1.occupied() is False
    with pytest.raises(CoordinatesError):
        checker1 = Checker('RED')


def test_checker_create_occupied_field():
    A1 = Field(['A', 1], True)
    assert A1.occupied() is True
    with pytest.raises(OccupationError):
        checker1 = Checker('BLACK', A1)
