import pygame
from constants import *

class Checker:
    def __init__(self, row, col, color):
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
        if self.color == RED:
            self.home_base = RED_BASE
            self.target_base = BLUE_BASE

        if self.color == BLUE:
            self.home_base = BLUE_BASE
            self.target_base = RED_BASE

        if self.color == YELLOW:
            self.home_base = YELLOW_BASE
            self.target_base = GREEN_BASE

        if self.color == GREEN:
            self.home_base = GREEN_BASE
            self.target_base = YELLOW_BASE

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
        self.update_status()
        if self.selected:
            color = GREEN
        elif not self.selected:
            color = BLACK
            if self.target:
                color = L_BLUE

        pygame.draw.circle(win, color, (self.x, self.y), SQUARE_SIZE//2 - BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), SQUARE_SIZE//2 - OUTLINE - BORDER)

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
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE//2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE//2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.get_position()

    def change_selected(self, value):
        self.selected = value


