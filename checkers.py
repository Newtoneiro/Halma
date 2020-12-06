class CoordinatesError(Exception):
    pass

class CheckerError(Exception):
    pass

class OccupationError(Exception):
    pass

def letters_into_numbers(letter):
    letters_into_numbers = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8
    }
    return letters_into_numbers[letter]


class Checker():
    def __init__(self, colour=None, occupied_field=None):
        if not occupied_field:
            raise CoordinatesError('Checker needs an occupied field')
        if occupied_field.occupied() is True:
            raise OccupationError('This field is already occupied')
        if not colour or colour != 'RED' and colour != 'BLACK':
            raise CheckerError('Checker colour invalid')
        occupied_field.change_occupation(True)
        self._occupied_field = occupied_field
        self._colour = colour

    def colour(self):
        return self._colour

    def occupied_field(self):
        return self._occupied_field


class Field():
    def __init__(self, coordinates=None, occupied=False):
        if not coordinates:
            raise CoordinatesError('Invalid coordinates argument')
        self._width = letters_into_numbers(coordinates[0])
        self._length = coordinates[1]
        self._occupied = occupied

    def width(self):
        return self._width

    def length(self):
        return self._length

    def occupied(self):
        return self._occupied

    def change_occupation(self, occupation=None):
        if not occupation:
            return
        self._occupied = occupation


A1 = Field(['A', 1], False)
Checker
