import os
import sys
import pygame
import pygame.mixer
from pygame.locals import *
from constants import *
from board import Board
from checker import Checker
from game import Game, Player
from random import randint

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Halma')


class PromptChecker:
    def __init__(self, x, y, colour, win):
        self.x = x
        self.y = y
        self.colour = colour
        self.win = win
        vx, vy = self.get_random_velocities()
        self.vx = vx
        self.vy = vy
        if self.colour == RED:
            self.delta_x = self.vx
            self.delta_y = self.vy
        if self.colour == BLUE:
            self.delta_x = -self.vx
            self.delta_y = -self.vy
        if self.colour == YELLOW:
            self.delta_x = -self.vx
            self.delta_y = self.vy
        if self.colour == GREEN:
            self.delta_x = self.vx
            self.delta_y = -self.vy

    def get_random_velocities(self):
        return (randint(1, 9), randint(1, 9))


    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        if self.x > WIDTH  or self.x < 0:
            self.delta_x = -self.delta_x
        if self.y > HEIGHT or self.y < 0:
            self.delta_y = -self.delta_y
        pygame.draw.circle(self.win, BLACK, (self.x, self.y), SQUARE_SIZE//2 - BORDER)
        pygame.draw.circle(self.win, self.colour, (self.x, self.y), SQUARE_SIZE//2 - OUTLINE - BORDER)

class MenuAnimations():
    def __init__(self, win):
        self.win = win
        self.create_checkers()
        self.main_sprite0 = pygame.image.load('./menus/menu0.png')
        self.main_sprite1 = pygame.image.load('./menus/menu1.png')
        self.main_sprite2 = pygame.image.load('./menus/menu2.png')
        self.main_sprite3 = pygame.image.load('./menus/menu3.png')
        self.main_sprite4 = pygame.image.load('./menus/menu4.png')
        self.main_sprite5 = pygame.image.load('./menus/menu5.png')
        self.button_sprite0 = pygame.image.load('./buttons/button0.png')
        self.button_sprite1 = pygame.image.load('./buttons/button1.png')
        self.button_sprite2 = pygame.image.load('./buttons/button2.png')
        self.button_sprite3 = pygame.image.load('./buttons/button3.png')
        self.button_sprite4 = pygame.image.load('./buttons/button4.png')
        self.button_sprite5 = pygame.image.load('./buttons/button5.png')
        self.button_pressed = pygame.image.load('./buttons/buttonpressed.png')
        self.gear0 = pygame.image.load('./gear/gear0.png')
        self.gear1 = pygame.image.load('./gear/gear1.png')
        self.gear2 = pygame.image.load('./gear/gear2.png')
        self.gear3 = pygame.image.load('./gear/gear3.png')
        self.gear4 = pygame.image.load('./gear/gear4.png')
        self.gear5 = pygame.image.load('./gear/gear5.png')
        self.gear_pressed = pygame.image.load('./gear/gear_pressed.png')
        self.options = pygame.image.load('./options/options.png')
        self.starting_player_marker = pygame.image.load('./options/player_choose.png')
        self.current_gear = self.gear0
        self.current_button = self.button_sprite0
        self.current_image = self.main_sprite0
        self.mute_image = pygame.image.load('./options/mute.png')
        self.unmute_image = pygame.image.load('./options/unmute.png')
        self.easy = pygame.image.load('./options/easy.png')
        self.hard = pygame.image.load('./options/hard.png')
        self.off = pygame.image.load('./options/off.png')
        self.on = pygame.image.load('./options/on.png')
        self.tiny_window = False
        self.hard_difficulty = False
        self.mute = False
        self.state = 0
        self.theme_music()
        self.in_options = False
        self.starting_player = RED

    def theme_music(self):
        pygame.mixer.music.load('./mainmenu/maintheme.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.75)

    def create_checkers(self):
        MIDDLE = (ROWS//2 * SQUARE_SIZE, COLS//2 * SQUARE_SIZE)
        redchecker = PromptChecker(MIDDLE[0], MIDDLE[1], RED, WIN)
        bluechecker = PromptChecker(MIDDLE[0], MIDDLE[1], BLUE, WIN)
        yellowchecker = PromptChecker(MIDDLE[0], MIDDLE[1], YELLOW, WIN)
        greenchecker = PromptChecker(MIDDLE[0], MIDDLE[1], GREEN, WIN)
        redchecker1 = PromptChecker(MIDDLE[0], MIDDLE[1], RED, WIN)
        bluechecker1 = PromptChecker(MIDDLE[0], MIDDLE[1], BLUE, WIN)
        yellowchecker1 = PromptChecker(MIDDLE[0], MIDDLE[1], YELLOW, WIN)
        greenchecker1 = PromptChecker(MIDDLE[0], MIDDLE[1], GREEN, WIN)
        redchecker2 = PromptChecker(MIDDLE[0], MIDDLE[1], RED, WIN)
        bluechecker2 = PromptChecker(MIDDLE[0], MIDDLE[1], BLUE, WIN)
        yellowchecker2 = PromptChecker(MIDDLE[0], MIDDLE[1], YELLOW, WIN)
        greenchecker2 = PromptChecker(MIDDLE[0], MIDDLE[1], GREEN, WIN)

        self.prompt_checkers = [
                redchecker,
                bluechecker,
                yellowchecker,
                greenchecker,
                redchecker1,
                bluechecker1,
                yellowchecker1,
                greenchecker1,
                redchecker2,
                bluechecker2,
                yellowchecker2,
                greenchecker2
            ]

    def move_checkers(self):
        for checker in self.prompt_checkers:
            checker.move()

    def update(self):
        self.make_canvas()
        self.move_checkers()
        self.update_menu_gif()

    def make_canvas(self):
        self.win.fill(BLACK)
        pygame.draw.rect(self.win, GREY, (OUTLINE, OUTLINE,(WIDTH - OUTLINE), (HEIGHT - OUTLINE)))
        for row in range(0, ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(self.win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE + OUTLINE, SQUARE_SIZE + OUTLINE))
                pygame.draw.rect(self.win, WHITE, (col * SQUARE_SIZE + OUTLINE, row * SQUARE_SIZE + OUTLINE, (SQUARE_SIZE - OUTLINE), (SQUARE_SIZE - OUTLINE)))

    def update_menu_gif(self):
        self.win.blit(self.current_image, (75, -50))
        if self.current_gear == self.gear_pressed:
            self.win.blit(self.current_gear, (48, 13))
        else:
            self.win.blit(self.current_gear, (50, 10))
        if not self.in_options:
            self.win.blit(self.current_button, (0, -25))
            self.state += 0.2
            if int(self.state) == 1:
                self.current_image = self.main_sprite1
                self.current_button = self.button_sprite1
                self.current_gear = self.gear1
            elif int(self.state) == 2:
                self.current_image = self.main_sprite2
                self.current_button = self.button_sprite2
                self.current_gear = self.gear2
            elif int(self.state) == 3:
                self.current_image = self.main_sprite3
                self.current_button = self.button_sprite3
                self.current_gear = self.gear3
            elif int(self.state) == 4:
                self.current_image = self.main_sprite4
                self.current_button = self.button_sprite4
                self.current_gear = self.gear4
            elif int(self.state) == 5:
                self.current_image = self.main_sprite5
                self.current_button = self.button_sprite5
                self.current_gear = self.gear5
            elif int(self.state) == 6:
                self.current_button = self.button_sprite0
                self.current_image = self.main_sprite0
                self.current_gear = self.gear0
            elif int(self.state) == 15:
                self.state = 0
        elif self.in_options:
            if self.starting_player == RED:
                self.win.blit(self.starting_player_marker, (75, -50))
            if self.starting_player == YELLOW:
                self.win.blit(self.starting_player_marker, (103, -50))
            if self.starting_player == BLUE:
                self.win.blit(self.starting_player_marker, (131, -50))
            if self.starting_player == GREEN:
                self.win.blit(self.starting_player_marker, (159, -50))
            if not self.mute:
                self.win.blit(self.unmute_image, (130, -100))
            elif self.mute:
                self.win.blit(self.mute_image, (130, -100))
            if not self.hard_difficulty:
                self.win.blit(self.easy, (75, -50))
            elif self.hard_difficulty:
                self.win.blit(self.hard, (75, -50))
            if not self.tiny_window:
                self.win.blit(self.off, (75, -50))
            elif self.tiny_window:
                self.win.blit(self.on, (75, -50))

    def press_button(self):
        self.current_button = self.button_pressed
        self.current_image = self.main_sprite0
        self.current_gear = self.gear0
        self.state = 12

    def press_gear(self):
        if not self.in_options:
            self.current_button = self.button_sprite0
            self.current_image = self.options
            self.current_gear = self.gear_pressed
            self.in_options = True
            self.state = 12
        elif self.in_options:
            self.in_options = False
            self.current_gear = self.gear0
            self.current_image = self.main_sprite0
            self.state = 0

    def change_starting_person(self, x):
        if x < 498:
            self.starting_player = RED
        elif x >= 498 and x < 524:
            self.starting_player = YELLOW
        elif x >= 524 and x < 550:
            self.starting_player = BLUE
        elif x >= 550:
            self.starting_player = GREEN

    def change_mute(self):
        if self.mute:
            self.mute = False
        elif not self.mute:
            self.mute = True

    def change_difficulty(self):
        if self.hard_difficulty:
            self.hard_difficulty = False
        elif not self.hard_difficulty:
            self.hard_difficulty = True

    def change_tiny_window_mode(self):
        if self.tiny_window:
            self.tiny_window = False
        elif not self.tiny_window:
            self.tiny_window = True

def main():
    run = True
    clock = pygame.time.Clock()
    menu = MenuAnimations(WIN)
    while run:
        clock.tick(FPS)
        menu.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 250 and x < 550 and y > 350 and y < 450 and not menu.in_options:
                    menu.press_button()
                    break
                elif x > 500 and x < 600 and y > 480 and y < 560:
                    menu.press_gear()
                    break
                if menu.in_options:
                    if x > 471 and x < 581 and y > 202 and y < 227:
                        menu.change_starting_person(x)
                    if x > 500 and x < 560 and y > 230 and y < 274:
                        menu.change_mute()
                    if x > 471 and x < 580 and y > 280 and y < 310:
                        menu.change_difficulty()
                    if x > 500 and x < 550 and y > 320 and y < 355:
                        menu.change_tiny_window_mode()


        pygame.display.update()


if __name__ == "__main__":
    main()