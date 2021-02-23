from checker import Checker
from game import Game, Player, Bot, EasyBot
from constants import *

#Player

def test_make_player_without_checkers():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []


def test_make_player_with_checkers():
    checker1 = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    checker2 = Checker(15, 15, BLUE, BLUE_BASE, RED_BASE, 50)
    checkers = [checker1, checker2]
    player = Player('Zygfryd', GREEN, checkers)
    assert player.name == 'Zygfryd'
    assert player.colour == GREEN
    assert len(player.checkers) == 2


def test_player_add_game():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []
    game = 'game_object'
    player.add_game(game)
    assert player.game == 'game_object'


def test_player_add_Checker():
    player = Player('Zygfryd', RED)
    assert player.name == 'Zygfryd'
    assert player.colour == RED
    assert player.checkers == []
    checker1 = Checker(4, 11, BLUE, BLUE_BASE, RED_BASE, 50)
    player.add_checker(checker1)
    assert len(player.checkers) == 1


#bot


def test_make_bot():
    bot = Bot('Blue', RED)
    assert bot.name == 'Blue'
    assert bot.colour == RED
    assert bot.checkers == []


# Checking the alghoritm using these kind of tests would be ineffective and exhausting,
# so i decided to test it in practice for both easy and hard bot.


# GAME

def test_create_game_normal_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game.win == WIN
    assert game.turn == RED
    assert game.tiny_window == False
    assert game.WIDTH == 800
    assert game.HEIGHT == 800
    assert game.SQUARE_SIZE == 50
    assert game._selected_checker == 0
    assert game.result == None
    assert game.hard_difficulty == False
    assert game.mute == False
    assert game.how_many_players == 4
    assert game.mode == 0
    assert game.FPS == 60


def test_create_game_tiny_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, True, 2, 1, True, 60)
    assert game.turn == RED
    assert game.tiny_window == True
    assert game.WIDTH == 400
    assert game.HEIGHT == 400
    assert game.SQUARE_SIZE == 25
    assert game._selected_checker == 0
    assert game.result == None
    assert game.hard_difficulty == False
    assert game.mute == True
    assert game.how_many_players == 2
    assert game.mode == 1
    assert game.FPS == 60


def test_game_transwer_into_rows_and_cols(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game.transfer_into_rows_and_cols(650, 530) == (10, 13)


def test_game_transwer_into_rows_and_cols_tiny_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, False, 4, 0, True, 60)
    assert game.transfer_into_rows_and_cols(250, 130) == (5, 10)


def test_game_create_a_board(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, False, False, 4, 0, True, 60)
    assert game._board.SQUARE_SIZE == 50
    assert game._board.win == WIN
    assert type(game._board.player1) == Player
    assert type(game._board.player2) == Player
    assert type(game._board.player3) == Player
    assert type(game._board.player4) == Player


def test_game_create_a_board_tiny_window_2v2_pvai(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, True, False, False, 2, 1, True, 60)
    assert game._board.SQUARE_SIZE == 25
    assert type(game._board.player1) == Player
    assert type(game._board.player2) == EasyBot


def test_game_create_a_board_4v4_bot(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 2, True, 60)
    assert game._board.SQUARE_SIZE == 50
    assert game._board.win == WIN
    assert type(game._board.player1) == Bot
    assert type(game._board.player2) == Bot
    assert type(game._board.player3) == Bot
    assert type(game._board.player4) == Bot


def test_game_board_select_animate(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 2, True, 60)
    assert game._board.animations == True
    game.choose_animate(False)
    assert game._board.animations == False


def test_game_check_win(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.result == None
    checker1 = Checker(15, 15, RED, RED_BASE, BLUE_BASE, 50)
    checker1.update_status()
    checker2 = Checker(0, 3, BLUE, BLUE_BASE, RED_BASE, 50)
    checker2.update_status()
    game.board().player1.checkers = [checker1, checker1, checker1]
    game.board().player2.checkers = [checker2, checker2, checker2]
    game.check_win()
    assert game.result == None
    # The rest of cases were tested in live playthroughs, because it would take a lot
    # of time to create individual pieces and assign them to game.board() players
    # Nonetheless i assured this win checking function works properly


def test_game_change_selected_checker(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.selected_checker() == 0
    checker1 = Checker(15, 15, RED, RED_BASE, BLUE_BASE, 50)
    game.change_selected_checker(checker1)
    assert game.selected_checker() == checker1
    game.change_selected_checker(0)
    assert game.selected_checker() == 0


def test_game_change_turn4p(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 4, 0, True, 60)
    assert game.turn == RED
    game.change_turn()
    assert game.turn == YELLOW
    game.change_turn()
    assert game.turn == BLUE
    game.change_turn()
    assert game.turn == GREEN
    game.change_turn()
    assert game.turn == RED


def test_game_change_turn2p(monkeypatch):
    def fake_sounds(self):
        return None
    WIN = 'window'
    monkeypatch.setattr('board.Board.get_jump_sounds', fake_sounds)
    game = Game(WIN, RED, False, True, False, 2, 0, True, 60)
    assert game.turn == RED
    game.change_turn()
    assert game.turn == BLUE
    game.change_turn()
    assert game.turn == RED