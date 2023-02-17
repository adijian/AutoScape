import random
import time
from enum import Enum

import keyboard
import pyautogui
import win32api
import win32con

from AbstractBot import AbstractBot


class MiningBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates

    class Coordinates(Enum):
        RESET_INTERFACE = [1735, 80]
        ROCK_1 = [913, 532]
        ROCK_2 = [980, 458]
        CAVE = [ 1358, 527]
        FURNACE = [636, 909]
        EMPTY = [622, 745]
        CAVE_OUTSIDE = [1341, 218]
        ROCK = [665, 784]

    def run(self, window, project_coordinates):
        if project_coordinates[0] != 0: self.reset_interface(window, project_coordinates)
        print(self.locateImageOnScreen(r'Images\Copper_Ore.png'))
        if self.locateImageOnScreen(r'Images\Copper_Ore.png') > 25:
            time.sleep(2)
            self.click_coordinates(self.coordinates.CAVE.value)
            time.sleep(5)
            self.click_coordinates(self.coordinates.FURNACE.value)
            time.sleep(8)
            self.click_coordinates(self.coordinates.EMPTY.value)
            time.sleep(5)
            self.click_coordinates(self.coordinates.CAVE_OUTSIDE.value)
            time.sleep(8)
            self.click_coordinates(self.coordinates.ROCK.value)
            time.sleep(5)
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
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 998, 473, -100000, 0)
        time.sleep(2)

        self.print_info(f"Reset window {window} to position")
