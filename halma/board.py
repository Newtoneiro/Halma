import pygame
from constants import *
from checker import Checker

class Board:
    def __init__(self, player1, player2, player3=None, player4=None):
        self.rows = ROWS
        self.cols = COLS
        self.RED_BASE = RED_BASE
        self.BLUE_BASE = BLUE_BASE
        self.GREEN_BASE = GREEN_BASE
        self.YELLOW_BASE = YELLOW_BASE
        if player3 and player4:
            self.player3 = player3
            self.player4 = player4
        else:
            self.player3 = None
            self.player4 = None
            self.RED_BASE = RED_BASE_2
            self.BLUE_BASE = BLUE_BASE_2
        self.player1 = player1
        self.player2 = player2
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        pygame.draw.rect(win, GREY, (OUTLINE, OUTLINE,(WIDTH - OUTLINE), (HEIGHT - OUTLINE)) )
        for row in range(0, ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE + OUTLINE, SQUARE_SIZE + OUTLINE))
                pygame.draw.rect(win, WHITE, (col * SQUARE_SIZE + OUTLINE, row * SQUARE_SIZE + OUTLINE, (SQUARE_SIZE - OUTLINE), (SQUARE_SIZE - OUTLINE)))

        # These funny lines
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

        for row in {5, 11}:
            for col in {0, 14}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * SQUARE_SIZE), (2 * OUTLINE)))

        for row in {4, 11}:
            for col in {2, 14}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (SQUARE_SIZE)))

        for row in {4, 12}:
            for col in {2, 13}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 12}:
            for col in {3, 13}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (SQUARE_SIZE)))

        for row in {3, 13}:
            for col in {3, 12}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (SQUARE_SIZE), (2 * OUTLINE)))

        for row in {2, 13}:
            for col in {4, 12}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (SQUARE_SIZE)))

        for row in {2, 14}:
            for col in {4, 11}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (SQUARE_SIZE), (2 * OUTLINE)))

        for row in {0, 14}:
            for col in {5, 11}:
                pygame.draw.rect(win, L_BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, (2 * OUTLINE), (2 * SQUARE_SIZE)))

    def create_board(self):
        board = []
        for row in range(0, self.rows):
            n_row = []
            for col in range(0, self.cols):
                if (row, col) in self.RED_BASE:
                    checker = Checker(row, col, RED, self.RED_BASE.copy(), self.BLUE_BASE.copy())
                    self.player1.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.BLUE_BASE:
                    checker = Checker(row, col, BLUE, self.BLUE_BASE.copy(), self.RED_BASE.copy())
                    self.player2.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.GREEN_BASE and self.player3:
                    checker = Checker(row, col, GREEN, self.GREEN_BASE.copy(), self.YELLOW_BASE.copy())
                    self.player3.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.YELLOW_BASE and self.player4:
                    checker = Checker(row, col, YELLOW, self.YELLOW_BASE.copy(), self.GREEN_BASE.copy())
                    self.player4.add_checker(checker)
                    n_row.append(checker)
                else:
                    n_row.append(0)
            board.append(n_row)
        self.board = board

    def space_right(self, row, col):
        if col >= COLS - 1:
            return None
        if self.get_checker(row, col+1) == 0:
            return (row, col+1)
        return self.check_jump_right(row, col)

    def space_left(self, row, col):
        if col <= 0:
            return None
        if self.get_checker(row, col-1) == 0:
            return (row, col-1)
        return self.check_jump_left(row, col)

    def space_down(self, row, col):
        if row >= ROWS - 1:
            return None
        if self.get_checker(row+1, col) == 0:
            return (row+1, col)
        return self.check_jump_down(row, col)

    def space_up(self, row, col):
        if row <= 0:
            return None
        if self.get_checker(row-1, col) == 0:
            return (row-1, col)
        return self.check_jump_up(row, col)

    def crosswise_up_right(self, row, col):
        if row <= 0 or col >= COLS-1:
            return None
        if self.get_checker(row-1, col+1) == 0:
            return (row-1, col+1)
        return self.check_jump_up_right(row, col)

    def crosswise_up_left(self, row, col):
        if row <= 0 or col <= 0:
            return None
        if self.get_checker(row-1, col-1) == 0:
            return (row-1, col-1)
        return self.check_jump_up_left(row, col)

    def crosswise_down_right(self, row, col):
        if row >= ROWS-1 or col >= COLS-1:
            return None
        if self.get_checker(row+1, col+1) == 0:
            return (row+1, col+1)
        return self.check_jump_down_right(row, col)

    def crosswise_down_left(self, row, col):
        if row >= ROWS-1 or col <= 0:
            return None
        if self.get_checker(row+1, col-1) == 0:
            return (row+1, col-1)
        return self.check_jump_down_left(row, col)

    def check_jump_up(self, row, col):
        if row <=1:
            return None
        if self.get_checker(row-1, col) != 0 and self.get_checker(row-2, col) == 0:
            return row-2, col
        return None

    def check_jump_down(self, row, col):
        if row >= ROWS - 2:
            return None
        if self.get_checker(row+1, col) != 0 and self.get_checker(row+2, col) == 0:
            return row+2, col
        return None

    def check_jump_left(self, row, col):
        if col <= 1:
            return None
        if self.get_checker(row, col-1) != 0 and self.get_checker(row, col-2) == 0:
            return row, col-2
        return None

    def check_jump_right(self, row, col):
        if col >= COLS - 2:
            return None
        if self.get_checker(row, col+1) != 0 and self.get_checker(row, col+2) == 0:
            return row, col+2
        return None

    def check_jump_up_right(self, row, col):
        if col >= COLS - 2 or row <= 1:
            return None
        if self.get_checker(row-1, col+1) != 0 and self.get_checker(row-2, col+2) == 0:
            return row-2, col+2
        return None

    def check_jump_up_left(self, row, col):
        if col <= 1 or row <= 1:
            return None
        if self.get_checker(row-1, col-1) != 0 and self.get_checker(row-2, col-2) == 0:
            return row-2, col-2
        return None

    def check_jump_down_left(self, row, col):
        if col <= 1 or row >= ROWS-2:
            return None
        if self.get_checker(row+1, col-1) != 0 and self.get_checker(row+2, col-2) == 0:
            return row+2, col-2
        return None

    def check_jump_down_right(self, row, col):
        if col >= COLS-2 or row >= ROWS-2:
            return None
        if self.get_checker(row+1, col+1) != 0 and self.get_checker(row+2, col+2) == 0:
            return row+2, col+2
        return None

    def check_jump_all_directions(self, row, col, already_jumped=None):
        if not already_jumped:
            already_jumped = []
        jumped_moves = []
        jumped_moves += already_jumped
        if self.check_jump_up(row, col):
            jumped_moves.append(self.check_jump_up(row, col))
        if self.check_jump_down(row, col):
            jumped_moves.append(self.check_jump_down(row, col))
        if self.check_jump_left(row, col):
            jumped_moves.append(self.check_jump_left(row, col))
        if self.check_jump_right(row, col):
            jumped_moves.append(self.check_jump_right(row, col))
        if self.check_jump_up_left(row, col):
            jumped_moves.append(self.check_jump_up_left(row, col))
        if self.check_jump_up_right(row, col):
            jumped_moves.append(self.check_jump_up_right(row, col))
        if self.check_jump_down_left(row, col):
            jumped_moves.append(self.check_jump_down_left(row, col))
        if self.check_jump_down_right(row, col):
            jumped_moves.append(self.check_jump_down_right(row, col))

        for move in jumped_moves:
            if move not in already_jumped:
                new_moves = self.check_jump_all_directions(move[0], move[1], jumped_moves)
                for move in new_moves:
                    if move not in jumped_moves:
                        jumped_moves.append(move)
        return jumped_moves

    def get_possible_swaps(self, checker):
        possible_swaps = []
        if col >= COLS - 1:
            if self.get_checker(row, col+1):
                possible_swaps.append(row, col+1)

        if col <= 0:
            if self.get_checker(row, col-1):
                possible_swaps.append(row, col-1)

        if row >= ROWS - 1:
            if self.get_checker(row+1, col):
                possible_swaps.append(row+1, col)

        if row <= 0:
            if self.get_checker(row-1, col):
                possible_swaps.append(row-1, col)

        if row <= 0 or col >= COLS-1:
            if self.get_checker(row-1, col+1):
                possible_swaps.append(row-1, col+1)

        if row <= 0 or col <= 0:
            if self.get_checker(row-1, col-1):
                possible_swaps.append(row-1, col-1)

        if row >= ROWS-1 or col >= COLS-1:
            if self.get_checker(row+1, col+1):
                possible_swaps.append(row+1, col+1)

        if row >= ROWS-1 or col <= 0:
            if self.get_checker(row+1, col-1):
                possible_swaps.append(row+1, col-1)

        return possible_swaps


    def valid_moves(self, checker):
        possible_moves = self.check_all_directions(checker.row, checker.col)
        jumped_moves = self.check_jump_all_directions(checker.row, checker.col)
        if checker.target:
            if checker.color == BLUE:        # once target enters enemy base, it cannot leave it
                base = self.RED_BASE
            if checker.color == RED:
                base = self.BLUE_BASE
            if checker.color == GREEN:
                base = self.YELLOW_BASE
            if checker.color == YELLOW:
                base = self.GREEN_BASE
            possible_moves_in_base = []
            jumped_moves_in_base = []
            for move in possible_moves:
                if move in base:
                    possible_moves_in_base.append(move)
            for jump in jumped_moves:
                if jump in base:
                    jumped_moves_in_base.append(jump)
            possible_moves = possible_moves_in_base
            jumped_moves = jumped_moves_in_base

        if checker.color == RED or checker.color == BLUE:
            forbidden_moves =  self.GREEN_BASE + self.YELLOW_BASE
        if checker.color == GREEN or checker.color == YELLOW:     # Player can only enter enemy base if he leaves it in the same turn
            forbidden_moves = self.RED_BASE + self.BLUE_BASE

        bad_moves = []
        for move in possible_moves:
            if move in forbidden_moves:
               bad_moves.append(move)
        if bad_moves:
            for move in bad_moves:
                possible_moves.remove(move)

        bad_jumps = []
        for jump in jumped_moves:
            if jump in forbidden_moves:
                bad_jumps.append(jump)
        if bad_jumps:
            for jump in bad_jumps:
                jumped_moves.remove(jump)

        return possible_moves + jumped_moves


    def check_all_directions(self, row, col):
        possible_moves = [
            self.space_down(row, col),
            self.space_left(row, col),
            self.space_right(row, col),
            self.space_up(row, col),
            self.crosswise_down_left(row, col),
            self.crosswise_down_right(row, col),
            self.crosswise_up_left(row, col),
            self.crosswise_up_right(row, col),
        ]
        return possible_moves

    def draw_valid_moves_indicators(self, checker, win):
        valid_moves = self.valid_moves(checker)
        for element in valid_moves:
            if element:
                row, col = element[0], element[1]
                pygame.draw.circle(win, D_GREEN, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 7)
                pygame.draw.circle(win, L_GREEN, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 5)

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
