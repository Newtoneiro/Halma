import pygame
from constants import *

class Checker:
    def __init__(self, row, col, color, home_base, target_base, SQUARE_SIZE):
        self.SQUARE_SIZE = SQUARE_SIZE
        self.row = row
        self.col = col
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

    def being_moved_change(self, smtgh):
        self.being_moved = smtgh

    def add_useless_move(self, move):
        self.useless_moves.append(move)

    def add_made_move(self, move):
        self.made_moves.append(move)

    def update_status(self):
        if (self.row, self.col) in self.target_base:
            self.target = True
        else:
            self.target = False

        if (self.row, self.col) in self.home_base:
            self.home = True
        else:
            self.home = False

    def draw(self, win):
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
        if self.target:
            self.target = False
        elif not self.target:
            self.target = True

    def change_home(self):
        if self.home:
            self.home = False
        elif not self.home:
            self.home = True

    def get_position(self):
        self.x = self.col * self.SQUARE_SIZE + self.SQUARE_SIZE//2
        self.y = self.row * self.SQUARE_SIZE + self.SQUARE_SIZE//2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.get_position()

    def change_selected(self, value):
        self.selected = value


