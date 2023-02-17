import random
import time
from enum import Enum

import keyboard
import pyautogui
import win32api
import win32con

from AbstractBot import AbstractBot


class MiningIronBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates
        # Start at the iron ore in burthrope mine 3rd from interance

    class Coordinates(Enum):
        RESET_INTERFACE = [1735, 80]
        ROCK_1 = [1008, 535]
        ROCK_2 = [926, 603]

        CLICK_1 = [1286, 46]
        CAVE_2 = [1223, 338]
        FURNACE = [636, 909]
        EMPTY = [622, 745]
        CAVE_OUTSIDE = [1341, 218]
        CLICK_2 = [923, 1016]
        CLICK_3 = [856, 855]
        ROCK_4 = [1403, 919]

    def run(self, window, project_coordinates):
        time.sleep(2)
        if project_coordinates[0] != 0: self.reset_interface(window, project_coordinates)
        iron = self.locateImageOnScreen(r'Images\Iron_Ore.png')
        self.print_info(f'Found iron: {iron}')
        if iron > 17:
            time.sleep(2)
            self.click_coordinates(self.coordinates.CLICK_1.value)
            time.sleep(10)
            self.click_coordinates(self.coordinates.CAVE_2.value)
            time.sleep(10)
            self.click_coordinates(self.coordinates.FURNACE.value)
            time.sleep(5)
            self.click_coordinates(self.coordinates.EMPTY.value)
            time.sleep(5)
            self.click_coordinates(self.coordinates.CAVE_OUTSIDE.value)
            time.sleep(10)
            self.click_coordinates(self.coordinates.CLICK_2.value)
            time.sleep(10)
            self.click_coordinates(self.coordinates.CLICK_3.value)
            time.sleep(10)
            self.click_coordinates(self.coordinates.ROCK_4.value)
            time.sleep(10)
            self.reset_interface(window, project_coordinates)

        if project_coordinates[0] % 2 == 0:
            time.sleep(2)
            self.click_coordinates(self.coordinates.ROCK_1.value)
            time.sleep(2)
        if project_coordinates[0] % 2 == 1:
            time.sleep(2)
            self.click_coordinates(self.coordinates.ROCK_2.value)
            time.sleep(2)
        project_coordinates[0] += 1

    def reset_interface(self, window, project_coordinates):
        time.sleep(2)
        self.click_coordinates(self.coordinates.RESET_INTERFACE.value)
        time.sleep(2)
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        time.sleep(2)
        self.click_coordinates(self.coordinates.ROCK_1.value)
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, self.coordinates.ROCK_1.value[0], self.coordinates.ROCK_1.value[1], -100000, 0)
        time.sleep(2)

        self.print_info(f"Reset window {window} to position")
