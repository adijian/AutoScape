import random
import time
from enum import Enum

import keyboard
import pyautogui
import win32api
import win32con

from AbstractBot import AbstractBot


class BronzeBarBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates

    class Coordinates(Enum):
        BANK_1 = [3508, 210]
        STORE_BARS_2 = [3187, 747]

    def run(self, window, project_coordinates):
        time.sleep(2)
        self.click_coordinates(self.coordinates.BANK_1.value)
        time.sleep(2)
        self.click_coordinates(self.coordinates.STORE_BARS_2.value)
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(2)

    def reset_interface(self, window, project_coordinates):
        time.sleep(2)
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 3557, 473, 100000, 0)
        time.sleep(2)

        self.print_info(f"Reset window {window} to position")
