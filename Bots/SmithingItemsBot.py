import time
from enum import Enum

import keyboard
import win32api
import win32con

from Bots.Abstract.AbstractBot import AbstractBot


class SmithingItemsBot(AbstractBot):
    def __init__(self):
        super().__init__()
        self.coordinates = self.Coordinates
        self.optional_coordinates = self.OptionalCoordinates

    class Coordinates(Enum):
        ANVIL_1 = [1089, 740]
        RUNE_BAR_2 = [652, 423]
        BRONZE_BAR_2 = [601, 372]
        MITHRIL_BAR_2 = [754, 375]
        ADAMANT_BAR_2 = [598, 429]
        IRON_BAR_2 = [651, 373]
        BLANK_SPOT_INTERFACE_3 = [998, 473]

    class OptionalCoordinates(Enum):
        ARROWS = [845, 606]
        BOLTS = [903, 602]
        START_PROJECT = [1099, 745]

    def get_coordinates(self):
        return self.coordinates

    def get_optional_coordinates(self):
        return self.optional_coordinates

    def run(self, window, project_coordinates):
        for i in range(2):
            time.sleep(2)
            self.click_coordinates(self.optional_coordinates.START_PROJECT.value)
            time.sleep(2)

    def reset_interface(self, window, project_coordinates):
        time.sleep(2)
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        for i in range(10):
            keyboard.press_and_release('right')
            time.sleep(0.2)
        time.sleep(5)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 998, 473, 100000, 0)
        time.sleep(2)
        self.click_coordinates(self.optional_coordinates.START_PROJECT.value)
        time.sleep(2)
        self.click_coordinates(self.coordinates.RUNE_BAR_2.value)
        time.sleep(2)
        self.click_coordinates(self.coordinates.BLANK_SPOT_INTERFACE_3.value)
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 998, 473, -100000, 0)
        time.sleep(2)
        self.click_coordinates(project_coordinates[1])
        time.sleep(2)
        self.click_coordinates(project_coordinates[0])
        time.sleep(2)

        self.print_info(f"Reset window {window} to position")
