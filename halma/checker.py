import pygame
from constants import OUTLINE, BORDER
from constants import BLACK, L_BLUE, L_GREEN, D_BLUE
from constants import D_GREEN


class Checker:
    """
    The piece's class, it's responsible for thing strictly related to
    the piece, like displaying it, containing basic info about itself
    aswell ass the state it's in (whether its being selecter or moved)
    """
    def __init__(self, row, col, color, home_base, target_base, SQUARE_SIZE):
        self.SQUARE_SIZE = SQUARE_SIZE # Quick disclaimer why every checker has its own squaresize:
        self.row = row                 # When i decided to add tinywindow mode, it was the first solution
        self.col = col                 # that came to my mind, to fix the square size not scaling correctly
        self.x = 0
        self.y = 0
        self.get_position()
        self.color = color
        self.selected = False
        self.target = False
        self.home = True
        self.useless_moves = []
        self.made_moves = []
        self.home_base = home_base
        self.target_base = target_base
        self.being_moved = False

    def being_moved_change(self, smthg):
        """
        smthg stands for bool, this function is usef by board class,
        so it's safe to assume that smthg will never be anything else
        than bool
        """
        self.being_moved = smthg

    def add_useless_move(self, move):
        """
        It's used by bots to prevent a checker getting stuck in endgame
        phase
        """
        self.useless_moves.append(move)

    def add_made_move(self, move):
        """
        This function is also made to prevent a checker from being stuck
        """
        self.made_moves.append(move)

    def update_status(self):
        """
        Every time a round ends, the position of checker is being checker,
        and coresponding actions are taken
        """
        if (self.row, self.col) in self.target_base:
            self.target = True
        else:
            self.target = False

        if (self.row, self.col) in self.home_base:
            self.home = True
        else:
            self.home = False

    def draw(self, win):
        """
        Draws a checker on window, considering whether it's in homebase,
        targetbase or selected. I've decided to test that one visually
        """
        if not self.being_moved:
            self.update_status()
            if self.selected:
                color = L_GREEN
                pygame.draw.circle(win, D_GREEN, (self.x, self.y), self.SQUARE_SIZE//2 - 4)
            elif not self.selected:
                color = BLACK
                if self.target:
                    pygame.draw.circle(win, D_BLUE, (self.x, self.y), self.SQUARE_SIZE//2 - 4)
                    color = L_BLUE

            pygame.draw.circle(win, color, (self.x, self.y), self.SQUARE_SIZE//2 - BORDER)
            pygame.draw.circle(win, self.color, (self.x, self.y), self.SQUARE_SIZE//2 - OUTLINE - BORDER)

    def change_target(self):
        """
        Switches self.target value
        """
        if self.target:
            self.target = False
        elif not self.target:
            self.target = True

    def change_selected(self, value):
        """
        Switches self.selected value
        """
        self.selected = value

    def change_home(self):
        """
        Switches self.home value
        """
        if self.home:
            self.home = False
        elif not self.home:
            self.home = True

    def get_position(self):
        """
        It calculates self's center coordinates for draw function
        """
        self.x = self.col * self.SQUARE_SIZE + self.SQUARE_SIZE//2
        self.y = self.row * self.SQUARE_SIZE + self.SQUARE_SIZE//2

    def move(self, row, col):
        """
        Changes the row, col and coordinates of the checker
        """
        self.row = row
        self.col = col
        self.get_position()

