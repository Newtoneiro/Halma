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

    def draw(self, win):
        if self.selected:
            color = GREEN
        elif not self.selected:
            color = BLACK
        pygame.draw.circle(win, color, (self.x, self.y), SQUARE_SIZE//2 - BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), SQUARE_SIZE//2 - OUTLINE - BORDER)

    def get_position(self):
        self.x = self.row * SQUARE_SIZE + SQUARE_SIZE//2
        self.y = self.col * SQUARE_SIZE + SQUARE_SIZE//2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.get_position()

    def change_selected(self, value):
        self.selected = value
