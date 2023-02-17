import time

import keyboard
import pyautogui

from AbstractBot import AbstractBot
from Commands import Commands


class User(Commands):
    def __init__(self, username, password, bot_type: AbstractBot, repeat_needed, hide_window=True, args=None, args2=None, world_args=None):
        Commands.__init__(self)
        self.username = username
        self.password = password
        self.type = bot_type
        self.window_hwnd = ''
        self.repeat_needed = repeat_needed
        self.done_repeat = False
        if args is None: self.args = []
        self.args = args
        if args2 is None: self.args2 = []
        self.args2 = args2
        if world_args is None: self.world_args = []
        self.world_args = world_args
        self.hide_window = hide_window

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
        time.sleep(10)
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

    def choose_world(self, free_or_member):
        time.sleep(10)
        pyautogui.press('2') if free_or_member == 'Member' else pyautogui.press('1')
        time.sleep(3)
        self.print_info(f"The user {self.username} has chose world")

    def window_bring_to_back(self, hwnd):
        if self.hide_window:
            super().window_bring_to_back(self.window_hwnd)
