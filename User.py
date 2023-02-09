import time

import keyboard

from AbstractBot import AbstractBot
from Commands import Commands


class User(Commands):
    def __init__(self, username, password, bot_type: AbstractBot, repeat_needed):
        Commands.__init__(self)
        self.username = username
        self.password = password
        self.type = bot_type
        self.window_hwnd = ''
        self.repeat_needed = repeat_needed
        self.done_repeat = False

    def get_window(self):
        self.window_hwnd = self.get_list_of_windows()[0]
        self.print_info(f"The window '{self.window_hwnd}' was created for '{self.username}'")

    def start_game(self):
        self.run_runescape()
        self.get_window()
        self.window_to_back()

    def window_to_front(self):
        self.window_bring_to_front(self.window_hwnd)

    def window_to_back(self):
        self.window_bring_to_back(self.window_hwnd)

    def login(self, coordinates_username, coordinates_password, coordinates_login, resolution):
        self.window_set_pos(self.window_hwnd, resolution)
        self.window_to_front()
        time.sleep(2)
        self.click_coordinates(coordinates_username)
        keyboard.write(self.username)
        time.sleep(2)
        self.click_coordinates(coordinates_password)
        keyboard.write(self.password)
        time.sleep(2)
        self.click_coordinates(coordinates_login)
        time.sleep(4)
        self.print_info(f"The user {self.username} has logged in")

    def choose_world(self, coordinates_world1, coordinates_world2):
        self.click_coordinates(coordinates_world1)
        self.click_coordinates(coordinates_world2)
        time.sleep(2)
        self.click_coordinates(coordinates_world1)
        self.click_coordinates(coordinates_world2)
        time.sleep(4)
        self.print_info(f"The user {self.username} has chose world")
