import pygame
from constants import *
from checker import Checker

class Board:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        pygame.draw.rect(win, GREY, (OUTLINE, OUTLINE,(WIDTH - OUTLINE), (HEIGHT - OUTLINE)) )
        for row in range(0, ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE + OUTLINE, SQUARE_SIZE + OUTLINE))
                pygame.draw.rect(win, YELLOW, (col * SQUARE_SIZE + OUTLINE, row * SQUARE_SIZE + OUTLINE, (SQUARE_SIZE - OUTLINE), (SQUARE_SIZE - OUTLINE)))

        for row in {4, 12}:
            for col in {0, 14}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * SQUARE_SIZE), (2* OUTLINE)))

        for row in {0, 14}:
            for col in {4, 12}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (2 * SQUARE_SIZE)))

        for row in {2, 14}:
            for col in {3, 12}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 13}:
            for col in {2, 13}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 12}:
            for col in {2, 14}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (SQUARE_SIZE)))

        for row in {2, 13}:
            for col in {3, 13}:
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (SQUARE_SIZE)))   

    def create_board(self):
        board = [[Checker(0, 0, RED), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for row in range(1, ROWS):
            n_row = []
            for col in range(0, COLS):
                n_row.append(0)
            board.append(n_row)
        self.board = board

    def get_checker(self, row, col):
        return self.board[row][col]

    def move_checker(self, checker, row, col):
        self.board[checker.row][checker.col], self.board[row][col] = self.board[row][col], self.board[checker.row][checker.col]
        checker.move(row, col)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(0, ROWS):
            for col in range(0, COLS):
                checker = self.get_checker(row, col)
                if checker != 0:
                    checker.draw(win)





