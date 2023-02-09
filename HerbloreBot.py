import random
import time

import keyboard
import pyautogui

from AbstractBot import AbstractBot


class HerbloreBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates

    class Coordinates:
        BANK_1 = [3539, 795]
        WELL_2 = [3499, 482]

    def run(self, window, args):
        self.window_bring_to_front(window)
        time.sleep(random.randint(1, 2))
        self.click_coordinates([self.coordinates.BANK_1[0] + random.randint(0, 10), self.coordinates.BANK_1[1] + random.randint(0, 10)])
        time.sleep(random.randint(1, 2))
        pyautogui.press("1")
        time.sleep(random.randint(1, 2))
        self.click_coordinates([self.coordinates.WELL_2[0] + random.randint(0, 10), self.coordinates.WELL_2[1] + random.randint(0, 10)])
        time.sleep(random.randint(1, 2))
        pyautogui.press("space")
        time.sleep(random.randint(16, 18))

    def reset_interface(self, window, args):
        self.window_bring_to_front(window)
        keyboard.press('up')
        time.sleep(random.randint(2, 3))
        keyboard.release('up')
        time.sleep(random.randint(1, 2))
        self.print_info(f"Reset window {window} to position")


