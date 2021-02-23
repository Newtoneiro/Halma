import pygame
from constants import ROWS, COLS, OUTLINE, BORDER, GREEN, YELLOW, BLUE, RED
from constants import BLACK, HEIGHT, WIDTH, GREY, WHITE, L_BLUE, L_GREEN
from constants import RED_BASE, BLUE_BASE, YELLOW_BASE, GREEN_BASE
from constants import RED_BASE_2, BLUE_BASE_2, D_GREEN
from checker import Checker

class Board:
    """
    Second most important class, it's responsible for placing checkers on the board,
    and contains information about their placements. It also calculates valid moves for
    a player, draws and animates the board and pieces.
    """
    def __init__(self, SQUARE_SIZE, win, player1, player2, player3=None, player4=None):
        """
        Initiates the board instance considering the number of players given as
        the arguments.
        """
        self.SQUARE_SIZE = SQUARE_SIZE
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
        self.win = win
        self.moves_paths = {}
        self.animations = True
        self.animation_speed = (HEIGHT * 50)//800
        self.get_jump_sounds()

    def moves_paths_clear(self):
        """
        Resets self.moves_paths, which is used buy animation function
        """
        self.moves_paths = {}

    def draw_squares(self, win):
        """
        Draws the board and 'these funy lines' being the blue and red lines
        you can see on the board, indicating the bases. This function,
        aswell as the other drawing functions were each tested visually
        """
        win.fill(BLACK)
        pygame.draw.rect(win, GREY, (OUTLINE, OUTLINE, (WIDTH - OUTLINE), (HEIGHT - OUTLINE)))
        for row in range(0, ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BLACK, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE + OUTLINE, self.SQUARE_SIZE + OUTLINE))
                pygame.draw.rect(win, WHITE, (col * self.SQUARE_SIZE + OUTLINE, row * self.SQUARE_SIZE + OUTLINE, (self.SQUARE_SIZE - OUTLINE), (self.SQUARE_SIZE - OUTLINE)))

        # These funny lines
        for row in {4, 12}:
            for col in {0, 14}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {0, 14}:
            for col in {4, 12}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (2 * self.SQUARE_SIZE)))

        for row in {2, 14}:
            for col in {3, 12}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 13}:
            for col in {2, 13}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 12}:
            for col in {2, 14}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (self.SQUARE_SIZE)))

        for row in {2, 13}:
            for col in {3, 13}:
                pygame.draw.rect(win, RED, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (self.SQUARE_SIZE)))

        for row in {5, 11}:
            for col in {0, 14}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {4, 11}:
            for col in {2, 14}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (self.SQUARE_SIZE)))

        for row in {4, 12}:
            for col in {2, 13}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {3, 12}:
            for col in {3, 13}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (self.SQUARE_SIZE)))

        for row in {3, 13}:
            for col in {3, 12}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {2, 13}:
            for col in {4, 12}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (self.SQUARE_SIZE)))

        for row in {2, 14}:
            for col in {4, 11}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (self.SQUARE_SIZE), (2 * OUTLINE)))

        for row in {0, 14}:
            for col in {5, 11}:
                pygame.draw.rect(win, L_BLUE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, (2 * OUTLINE), (2 * self.SQUARE_SIZE)))

    def create_board(self):
        """
        Creates a list of rows containing lists of objects in columns of these rows.
        """
        board = []
        for row in range(0, self.rows):
            n_row = []
            for col in range(0, self.cols):
                if (row, col) in self.RED_BASE:
                    checker = Checker(row, col, RED, self.RED_BASE.copy(), self.BLUE_BASE.copy(), self.SQUARE_SIZE)
                    self.player1.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.BLUE_BASE:
                    checker = Checker(row, col, BLUE, self.BLUE_BASE.copy(), self.RED_BASE.copy(), self.SQUARE_SIZE)
                    self.player2.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.GREEN_BASE and self.player3:
                    checker = Checker(row, col, GREEN, self.GREEN_BASE.copy(), self.YELLOW_BASE.copy(), self.SQUARE_SIZE)
                    self.player3.add_checker(checker)
                    n_row.append(checker)
                elif (row, col) in self.YELLOW_BASE and self.player4:
                    checker = Checker(row, col, YELLOW, self.YELLOW_BASE.copy(), self.GREEN_BASE.copy(), self.SQUARE_SIZE)
                    self.player4.add_checker(checker)
                    n_row.append(checker)
                else:
                    n_row.append(0)
            board.append(n_row)
        self.board = board

    # All of the following methods are used in valid moves related functions,
    # Each one of them is responsible for checking a single direction on the board
    # and returning information about the move (is it valid, is there another checker on the way etc.)

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

    def check_all_directions(self, row, col):
        """
        Returns list of moves that are max. 1 square away from
        starting position
        """
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
        possible_moves_cut = [move for move in possible_moves if move]
        return possible_moves_cut

    def check_jump_all_directions(self, row, col, already_jumped=None):
        """
        Recursively checks possible "jumped moves" meaning only the jumps
        that are achieved by concussive jumping over pieces
        """
        if not already_jumped:
            already_jumped = []
        jumped_moves = self.get_all_jumps_from_square(row, col)
        jumped_moves += already_jumped

        for move in jumped_moves:
            if move not in already_jumped:
                new_moves = self.check_jump_all_directions(move[0], move[1], jumped_moves)
                for move in new_moves:
                    if move not in jumped_moves:
                        jumped_moves.append(move)
        return jumped_moves

    def get_all_jumps_from_square(self, row, col):
        """
        Checks possible jumps that are max. 2 squares away from the
        current position
        """
        jumped_moves = []
        if self.check_jump_up(row, col):
            jumped_moves.append(self.check_jump_up(row, col))
        if self.check_jump_up_left(row, col):
            jumped_moves.append(self.check_jump_up_left(row, col))
        if self.check_jump_left(row, col):
            jumped_moves.append(self.check_jump_left(row, col))
        if self.check_jump_down_left(row, col):
            jumped_moves.append(self.check_jump_down_left(row, col))
        if self.check_jump_down(row, col):
            jumped_moves.append(self.check_jump_down(row, col))
        if self.check_jump_down_right(row, col):
            jumped_moves.append(self.check_jump_down_right(row, col))
        if self.check_jump_right(row, col):
            jumped_moves.append(self.check_jump_right(row, col))
        if self.check_jump_up_right(row, col):
            jumped_moves.append(self.check_jump_up_right(row, col))
        for jump in jumped_moves:
            if not jump:
                jumped_moves.remove(jump)
        return jumped_moves

    def get_path(self, start, finish):
        """
        Function used to animate checkers' movements.
        It's supposed to return a list of moves that further can be
        made into an actual path
        """
        moves_close_start = self.check_all_directions(start[0], start[1])
        jumped_moves_start = self.check_jump_all_directions(start[0], start[1])
        jumped_moves_finish = self.check_jump_all_directions(finish[0], finish[1])
        if finish in moves_close_start:
            return [start, finish]
        jumps_made = [start]
        for jump in jumped_moves_start:
            if jump in jumped_moves_finish:
                jumps_made.append(jump)
                if finish in jumps_made:
                    return jumps_made

    def cut_path(self, start, finish):
        """
        Remakes the get_path returned list so that there is only one path
        left leading from start to finish
        """
        jumps_made = self.get_path(start, finish)
        if finish in self.check_all_directions(start[0], start[1]):
            return [start, finish]
        path = []
        moves_dict = {}
        for move in jumps_made:
            if move != finish:
                path.append(move)
                possible_jumps = self.get_all_jumps_from_square(move[0], move[1])
                for move in path:
                    if move in possible_jumps:
                        possible_jumps.remove(move)
                moves_to_remove = []
                for valueable_move in possible_jumps:
                    if valueable_move not in jumps_made:
                        moves_to_remove.append(valueable_move)
                for move_to_remove in moves_to_remove:
                    possible_jumps.remove(move_to_remove)
                moves_dict[move] = possible_jumps
        run = True
        while run:
            keys_to_remove = []
            for start_square in moves_dict.keys():
                if len(moves_dict[start_square]) == 0:
                    keys_to_remove.append(start_square)
            for places_to_go in moves_dict.values():
                for key in keys_to_remove:
                    if key in places_to_go:
                        places_to_go.remove(key)
            for key in keys_to_remove:
                moves_dict.pop(key)
            if len(keys_to_remove) == 0:
                run = False
        for move_list in moves_dict.values():
            for element in move_list:
                if element != finish:
                    if element not in moves_dict.keys():
                        move_list.remove(element)
        path = [start]
        while finish not in path:
            key = path[-1]
            path.append(moves_dict[key][0])
        return path

    def valid_moves(self, checker):
        """
        Returns final list of valid_moves for a checker.
        """
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
            forbidden_moves = self.GREEN_BASE + self.YELLOW_BASE
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

    def draw_valid_moves_indicators(self, checker, win):
        """
        Function drawing valid moves indicators on the board.
        This one was tested visually.
        """
        valid_moves = self.valid_moves(checker)
        for element in valid_moves:
            if element:
                row, col = element[0], element[1]
                pygame.draw.circle(win, D_GREEN, (col*self.SQUARE_SIZE + self.SQUARE_SIZE//2, row*self.SQUARE_SIZE + self.SQUARE_SIZE//2), 7)
                pygame.draw.circle(win, L_GREEN, (col*self.SQUARE_SIZE + self.SQUARE_SIZE//2, row*self.SQUARE_SIZE + self.SQUARE_SIZE//2), 5)

    def get_checker(self, row, col):
        """
        Returns a coresponding object from self.board
        """
        return self.board[row][col]

    def move_checker(self, checker, row, col):
        """
        Moves checker to the designated space
        """
        if self.animations:
            self.move_checker_animate(checker, row, col)
        self.board[checker.row][checker.col], self.board[row][col] = self.board[row][col], self.board[checker.row][checker.col]
        checker.move(row, col)

    def get_jump_sounds(self):
        """
        Loads in the sounds played when a checker jumps
        """
        jumpsound0 = pygame.mixer.Sound('./jumpsounds/jump0.wav')
        jumpsound1 = pygame.mixer.Sound('./jumpsounds/jump1.wav')
        jumpsound2 = pygame.mixer.Sound('./jumpsounds/jump2.wav')
        jumpsound3 = pygame.mixer.Sound('./jumpsounds/jump3.wav')
        jumpsound4 = pygame.mixer.Sound('./jumpsounds/jump4.wav')
        jumpsound5 = pygame.mixer.Sound('./jumpsounds/jump5.wav')
        jumpsound6 = pygame.mixer.Sound('./jumpsounds/jump6.wav')
        jumpsound7 = pygame.mixer.Sound('./jumpsounds/jump7.wav')
        jumpsound8 = pygame.mixer.Sound('./jumpsounds/jump8.wav')
        self.jumpsounds = [
            jumpsound0,
            jumpsound1,
            jumpsound2,
            jumpsound3,
            jumpsound4,
            jumpsound5,
            jumpsound6,
            jumpsound7,
            jumpsound8
        ]

    def set_mute(self, mute):
        """
        Sets the value of self.mute
        """
        self.mute = mute

    def move_checker_animate(self, checker, row, col):
        """
        Function that brings life into this borring game, makes the
        checkers move arround in somewhat coordinated way.
        Tested visually. A lot.
        """
        FPS = 85
        clock = pygame.time.Clock()
        moves_list = self.cut_path((checker.row, checker.col), (row, col))
        x0 = checker.x
        y0 = checker.y
        sound_count = -1
        for move in moves_list:
            if sound_count != 8:
                sound_count += 1
            if move == (checker.row, checker.col):
                pass
            else:
                y1 = move[0]*self.SQUARE_SIZE + self.SQUARE_SIZE//2
                x1 = move[1]*self.SQUARE_SIZE + self.SQUARE_SIZE//2
                if x1 > x0:
                    delta_x = abs(x1-x0)
                else:
                    delta_x = -abs(x1-x0)
                if y1 > y0:
                    delta_y = abs(y1-y0)
                else:
                    delta_y = -abs(y1-y0)

                checker.being_moved_change(True)
                while (x0, y0) != (x1, y1):
                    self.draw(self.win)
                    x0 += delta_x//self.animation_speed
                    y0 += delta_y//self.animation_speed
                    pygame.draw.circle(self.win, BLACK, (x0, y0), self.SQUARE_SIZE//2 - BORDER)
                    pygame.draw.circle(self.win, checker.color, (x0, y0), self.SQUARE_SIZE//2 - OUTLINE - BORDER)
                    pygame.display.update()
                    clock.tick(FPS)
                checker.being_moved_change(False)
                y0 = move[0]*self.SQUARE_SIZE + self.SQUARE_SIZE//2
                x0 = move[1]*self.SQUARE_SIZE + self.SQUARE_SIZE//2
                if not self.mute:
                    self.jumpsounds[sound_count].play()

    def draw(self, win):
        """
        Draws the board with all the prompts like valid moves indicators
        and checkers themself.
        Tested visually.
        """
        self.draw_squares(win)
        for row in range(0, ROWS):
            for col in range(0, COLS):
                checker = self.get_checker(row, col)
                if checker != 0:
                    checker.draw(win)
                    if checker.selected:
                        self.draw_valid_moves_indicators(checker, win)

