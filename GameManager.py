import random
import time
from enum import Enum

from BotManager import BotManager
from Commands import Commands
from User import User


class GameManager(BotManager, Commands):
    class SetUp(Enum):
        RESOLUTION = [2552, -8, 1920, 1080]

    class Coordinates(Enum):
        USERNAME = [3395, 413]
        PASSWORD = [3387, 507]
        LOGIN = [3509, 554]
        WORLD_1 = [3729, 529]
        WORLD_2 = [3727, 577]

    def __init__(self):
        BotManager.__init__(self)
        Commands.__init__(self)
        self.coordinates = self.Coordinates
        self.list_of_user_objects_1 = [
            User("adijrunescape@gmail.com", "deejian8", self.type_of_bots.SMITHING, int(418), [self.type_of_bots.SMITHING.coordinates.RUNE_BAR_2.value,
                                                                                               self.type_of_bots.SMITHING.optional_coordinates.ARROWS.value])
            # ,
            # User("runescapejian003@googlemail.com", "deejian8", self.type_of_bots.FIREMAKING_INCENSE, int(30344 / 28))
        ]

    def standard_start(self, u_list):
        self.stop_runescape()
        for q in u_list:
            q.start_game()
            q.login(self.coordinates.USERNAME.value, self.coordinates.PASSWORD.value, self.coordinates.LOGIN.value, self.SetUp.RESOLUTION.value)
            q.choose_world(self.coordinates.WORLD_1.value, self.coordinates.WORLD_2.value)
            q.window_bring_to_back(q.window_hwnd)
            self.print_info(q.repeat_needed)

    def custom_start(self, u_list):
        self.standard_start(u_list)
        for q1 in u_list:
            q1.window_bring_to_front(q1.window_hwnd)
            q1.type.reset_interface(q1.window_hwnd, q1.args)
            q1.window_bring_to_back(q1.window_hwnd)

        max_repeat = -1
        for q2 in u_list:
            if q2.repeat_needed > max_repeat:
                max_repeat = q2.repeat_needed
                self.print_info(f'{q2.repeat_needed} is bigger')
        self.print_info(f'Repeat counter: {max_repeat}')

        min_rep, max_rep = 50, 70
        average_rep = (min_rep + max_rep) / 2
        if max_repeat > (average_rep * 6):
            max_repeat = average_rep * 6

        for re in range(int(max_repeat)):
            for p in u_list:
                if p.repeat_needed > 0 and not p.done_repeat:
                    p.window_bring_to_front(p.window_hwnd)
                    p.type.run(p.window_hwnd, p.args2)
                    p.repeat_needed -= 1
                    p.window_bring_to_back(p.window_hwnd)
                elif p.repeat_needed <= 0 and not p.done_repeat:
                    p.done_repeat = True
                    self.print_info(f'{p.username} is done.')
            random_rep = random.randint(min_rep, max_rep)
            self.print_info(f"Rep count: {re}/{max_repeat} "
                            f"Random: {random_rep} "
                            f"Percentage: {(re / max_repeat):.2f} "
                            f"Time left: {(average_rep * (max_repeat - re)) / 60 / 60:.2f} hours")

            time.sleep(random_rep)


if __name__ == "__main__":
    game_manager = GameManager()
    # game_manager.find_coordinates()

    game_manager.standard_start(game_manager.list_of_user_objects_1)
    # game_manager.custom_start(game_manager.list_of_user_objects_1)

    # game_manager.stop_runescape()
