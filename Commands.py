import random
import subprocess
import time
import webbrowser
from datetime import datetime
from enum import Enum

import keyboard
import pyautogui
import win32con
import win32gui


class PrintsCommander:
    def __init__(self):
        super().__init__()
        self.colors = self.Colors

    class Colors(Enum):
        OKCYAN = '\033[96m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    def print_error(self, text):
        return print(f"{self.colors.FAIL.value}", datetime.now().strftime('%H:%M:%S'), text, f"{self.colors.ENDC.value}")

    def print_info(self, text):
        return print(f"{self.colors.OKCYAN.value}", datetime.now().strftime('%H:%M:%S'), text, f"{self.colors.ENDC.value}")


class ClickCommander(PrintsCommander):
    def __init__(self):
        super().__init__()

    def click_coordinates(self, coordinates: list):
        try:
            pyautogui.click(coordinates[0] + random.randint(0, 5), coordinates[1] + random.randint(0, 5))
        except Exception as e:
            self.print_error(f"Failed to left click {coordinates} due to {e}")

    def right_click_coordinates(self, coordinates: list):
        try:
            pyautogui.click(coordinates[0] + random.randint(0, 5), coordinates[1] + random.randint(0, 5))
        except Exception as e:
            self.print_error(f"Failed to right click {coordinates} due of {e}")

    @staticmethod
    def find_coordinates():
        while True:
            if keyboard.is_pressed('p'):
                print(pyautogui.position())
                time.sleep(0.1)
            elif keyboard.is_pressed('q'):
                break


class ImageDetectionManager:
    @staticmethod
    def locateImageOnScreen(self, image):
        counter = 0
        for _ in pyautogui.locateAllOnScreen(self, image(image), confidence=0.94, grayscale=True):
            counter += 1
            print(_)
        return counter


class GameRunner(PrintsCommander):
    @staticmethod
    def run_runescape():
        path = 'rs-launch://www.runescape.com/k=5/l=$(Language:0)/jav_config.ws'
        webbrowser.open(path)
        time.sleep(10)
        # self.print_info(f'Created window for {user.username}')

    def stop_runescape(self):
        subprocess.call("TASKKILL /F /IM Runescape.exe", shell=True)
        self.print_info(f"Ended all Runescape tasks")


class WindowManager(PrintsCommander):
    def __init__(self):
        super().__init__()
        self.list_of_windows = []

    def get_list_of_windows(self):
        list_of_windows = []
        try:
            def winEnumHandler(hwnd, ctx):
                if win32gui.IsWindowVisible(hwnd):
                    if win32gui.GetWindowText(hwnd) == 'RuneScape':
                        # print(hwnd, win32gui.GetWindowText(hwnd), ",")
                        list_of_windows.append(hwnd)

            win32gui.EnumWindows(winEnumHandler, None)
        except Exception as e:
            self.print_error(f"Failed to get list of windows: {e}")

        self.print_info(f"List_of_windows: {list_of_windows}")
        self.list_of_windows = list_of_windows
        return list_of_windows

    def window_set_pos(self, hwnd, resolution: list):
        try:
            rect = win32gui.GetWindowRect(hwnd)
            win32gui.MoveWindow(hwnd, resolution[0], resolution[1], resolution[2], resolution[3], True)
            print(win32gui.GetWindowText(hwnd), "hwnd", hwnd, "rect", rect)
        except Exception as e:
            rect = win32gui.GetWindowRect(hwnd)
            win32gui.MoveWindow(hwnd, resolution[0], resolution[1], resolution[2], resolution[3], True)
            print(win32gui.GetWindowText(hwnd), "hwnd", hwnd, "rect", rect)
            self.print_error(f"Failed to set position of window {hwnd} due to {e}")

    def window_bring_to_front(self, hwnd):
        try:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            win32gui.SetActiveWindow(hwnd)
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            win32gui.SetActiveWindow(hwnd)
            win32gui.SetForegroundWindow(hwnd)
            self.print_error(f"Failed to bring window {hwnd} to front due to {e}")

    def window_bring_to_back(self, hwnd):
        try:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        except Exception as e:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            self.print_error(f"Failed to minimize window {hwnd} due to {e}")


class Commands(ClickCommander, ImageDetectionManager, GameRunner, WindowManager):
    def __init__(self):
        ClickCommander.__init__(self)
        ImageDetectionManager.__init__(self)
        GameRunner.__init__(self)
        WindowManager.__init__(self)
        self.print_commands = PrintsCommander()
        self.click_commander = ClickCommander()
        self.image_detection_manager = ImageDetectionManager()
        self.game_runner = GameRunner()
        self.window_manager = WindowManager()
