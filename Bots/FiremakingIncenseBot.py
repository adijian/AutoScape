import time
from enum import Enum

import keyboard
import pyautogui
import win32api
import win32con

from Bots.Abstract.AbstractBot import AbstractBot


class FiremakingIncenseBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates

    class Coordinates(Enum):
        BANK_1 = [959, 131]
        LOG_2 = [1792, 681]
        STICKS_3 = [1109, 540]

    def run(self, window, project_coordinates):
        time.sleep(2)
        self.click_coordinates(self.coordinates.BANK_1.value)
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(2)
        self.click_coordinates(self.coordinates.LOG_2.value)
        time.sleep(2)
        pyautogui.press('space')
        time.sleep(2)

    def reset_interface(self, window, project_coordinates):
        time.sleep(2)
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 998, 473, 100000, 0)
        time.sleep(2)
        self.click_coordinates(self.coordinates.BANK_1.value)
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(2)
        self.click_coordinates(self.coordinates.LOG_2.value)
        time.sleep(2)
        self.click_coordinates(self.coordinates.STICKS_3.value)
        time.sleep(2)

        self.print_info(f"Reset window {window} to position")
