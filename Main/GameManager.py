import random
import time
from enum import Enum

from Bots.Abstract.BotManager import BotManager
from Commands import Commands
from User import User


class GameManager(BotManager, Commands):
    class SetUp(Enum):
        RESOLUTION_1 = [-8, -8, 1920, 1080]
        RESOLUTION_2 = [2552, -8, 1920, 1080]

    class Coordinates(Enum):
        USERNAME = [1090, 414]
        PASSWORD = [1091, 506]
        LOGIN = [958, 553]
        WORLD_FREE_1 = 'Free'
        WORLD_MEMBER_1 = 'Member'

    def __init__(self):
        BotManager.__init__(self)
        Commands.__init__(self)
        self._resolution = self.SetUp.RESOLUTION_1
        self.coordinates = self.Coordinates
        self.list_of_user_objects_1 = [
            User(username="adijrunescape@gmail.com", password="deejian8",
                 bot_type=self.type_of_bots.SMITHING_ITEMS, repeat_needed=int(19575), hide_window=True,
                 set_up_args=[self.type_of_bots.SMITHING_ITEMS.coordinates.RUNE_BAR_2.value,
                              self.type_of_bots.SMITHING_ITEMS.optional_coordinates.ARROWS.value],
                 world_args=[self.Coordinates.WORLD_MEMBER_1.value])
            ,
            # copper
            User(username="runescapejian005@gmail.com", password="deejian8",
                 bot_type=self.type_of_bots.HERBLORE_UNF_BOT, repeat_needed=int(1434 / 14), hide_window=True,
                 world_args=[self.Coordinates.WORLD_FREE_1.value])
            ,
            # incense
            User(username="runescapejian005@googlemail.com", password="deejian8",
                 bot_type=self.type_of_bots.HERBLORE_UNF_BOT, repeat_needed=int(436 / 14), hide_window=True,
                 world_args=[self.Coordinates.WORLD_FREE_1.value])

            # ,
            # User(username="runescapejian003@googlemail.com", password="deejian8",
            #      bot_type=self.type_of_bots.HERBLORE_UNF_BOT, repeat_needed=int(1000 / 14), hide_window=True,
            #      world_args=[self.Coordinates.WORLD_FREE_1.value])
            # ,
            # User(username="runescapejian006@gmail.com", password="deejian8",
            #      bot_type=self.type_of_bots.HERBLORE_UNF_BOT, repeat_needed=int(1000 / 14), hide_window=True,
            #      world_args=[self.Coordinates.WORLD_FREE_1.value])
        ]

    def standard_start(self, u_list):
        self.stop_runescape()
        for q in u_list:
            q.start_game()
            q.login(self.coordinates.USERNAME.value, self.coordinates.PASSWORD.value, self.coordinates.LOGIN.value, self.SetUp.RESOLUTION_1.value)
            q.choose_world(q.world_args[0])
            q.window_bring_to_back(q.window_hwnd)
            self.print_info(q.repeat_needed)

    def custom_start(self, u_list):
        self.standard_start(u_list)
        for q1 in u_list:
            q1.window_bring_to_front(q1.window_hwnd)
            q1.type.reset_interface(q1.window_hwnd, q1.set_up_args)
            q1.window_bring_to_back(q1.window_hwnd)

        max_repeat = -1
        max_repeat = 1000
        for q2 in u_list:
            # if q2.repeat_needed > max_repeat:
            if q2.repeat_needed < max_repeat:
                max_repeat = q2.repeat_needed
                self.print_info(f'{q2.repeat_needed} is bigger')
        self.print_info(f'Repeat counter: {max_repeat}')

        min_rep, max_rep = 60, 80
        average_rep = ((min_rep + max_rep) / 2) / 60
        max_hour = 6 * 60
        if max_repeat > max_hour / average_rep: max_repeat = int(max_hour / average_rep)

        for re in range(max_repeat):
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

    # game_manager.standard_start(game_manager.list_of_user_objects_1)
    game_manager.custom_start(game_manager.list_of_user_objects_1)

    # game_manager.stop_runescape()
