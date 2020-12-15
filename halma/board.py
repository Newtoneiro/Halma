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
        board = []
        for row in range(0, self.rows):
            n_row = []
            for col in range(0, self.cols):
                if row in {0, 1} and col in {0, 1, 2, 3}:
                    n_row.append(Checker(row, col, RED))
                elif row == 2 and col in {0, 1, 2}:
                    n_row.append(Checker(row, col, RED))
                elif row == 3 and col in {0, 1}:
                    n_row.append(Checker(row, col, RED))
                elif row == 12 and col in {14, 15}:
                    n_row.append(Checker(row, col, BLUE))
                elif row == 13 and col in {13, 14, 15}:
                    n_row.append(Checker(row, col, BLUE))
                elif row in {14, 15} and col in {12, 13, 14, 15}:
                    n_row.append(Checker(row, col, BLUE))
                else:
                    n_row.append(0)
            board.append(n_row)
        self.board = board
    
    def space_right(self, row, col):
        if col == COLS - 1:
            return None
        if self.get_checker(row, col+1) == 0:
            return (row, col+1)
        return None
    
    def space_left(self, row, col):
        if col == 0:
            return None
        if self.get_checker(row, col-1) == 0:
            return (row, col-1)
        return None
    
    def space_down(self, row, col):
        if row == COLS - 1:
            return None
        if self.get_checker(row+1, col) == 0:
            return (row+1, col)
        return None
    
    def space_up(self, row, col):
        if row == 0:
            return None
        if self.get_checker(row-1, col) == 0:
            return (row-1, col)
        return None
    
    def crosswise_up_right(self, row, col):
        if row == 0 or col == COLS:
            return None
        if self.get_checker(row-1, col+1) == 0:
            return (row-1, col+1)
        return None

    
    def crosswise_up_left(self, row, col):
        if row == 0 or col == 0:
            return None
        if self.get_checker(row-1, col-1) == 0:
            return (row-1, col-1)
        return None

    
    def crosswise_down_right(self, row, col):
        if row == ROWS or col == COLS:
            return None
        if self.get_checker(row+1, col+1) == 0:
            return (row+1, col+1)
        return None

    
    def crosswise_down_left(self, row, col):
        if row == ROWS or col == 0:
            return None
        if self.get_checker(row+1, col-1) == 0:
            return (row+1, col-1)
        return None

    def valid_moves(self, checker):
        row = checker.row
        col = checker.col
        valid_moves = [
            self.space_down(row, col),
            self.space_left(row, col),
            self.space_right(row, col),
            self.space_up(row, col),
            self.crosswise_down_left(row, col),
            self.crosswise_down_right(row, col),
            self.crosswise_up_left(row, col),
            self.crosswise_up_right(row, col)
        ]
        
        return valid_moves
    
    def draw_valid_moves_indicators(self, checker, win):
        valid_moves = self.valid_moves(checker)
        for element in valid_moves:
            if element:
                row, col = element[0], element[1]
                pygame.draw.circle(win, GREEN, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 5)

 
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
                    if checker.selected:
                        self.draw_valid_moves_indicators(checker, win)





