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
            User("runescapejian9@googlemail.com", "deejian8", self.type_of_bots.SMITHING, int(399)),
            # User("runescapejian003@googlemail.com", "deejian8", self.type_of_bots.FIREMAKING_INCENSE, int(2518/28)),
            # User("runescapejian004@gmail.com", "deejian8", self.type_of_bots.SMITHING, int(399)),
            # User("runescapejian004@googlemail.com", "deejian8", self.type_of_bots.SMITHING, int(399))
        ]

    def standard_start(self, user: User):
        user.start_game()
        user.login(self.coordinates.USERNAME.value, self.coordinates.PASSWORD.value, self.coordinates.LOGIN.value, self.SetUp.RESOLUTION.value)
        user.choose_world(self.coordinates.WORLD_1.value, self.coordinates.WORLD_2.value)

    def custom_start(self, product, u_list):
        self.stop_runescape()
        for q in u_list:
            self.standard_start(q)
            q.window_bring_to_back(q.window_hwnd)

        # for q1 in u_list:
        #     q1.window_bring_to_front(q1.window_hwnd)
        #     q1.type.reset_interface(q1.window_hwnd, product)
        #     q1.window_bring_to_back(q1.window_hwnd)
        #
        # repeat_counter, max_repeat = 0, 0
        # for q2 in u_list:
        #     if q2.repeat_needed > max_repeat:
        #         max_repeat = q2.repeat_needed
        #         self.print_info(f'{q2.repeat_needed} is bigger')
        # self.print_info(f'Repeat counter: {max_repeat}')
        #
        # for re in range(max_repeat):
        #     for p in u_list:
        #         if p.repeat_needed > 0 and not p.done_repeat:
        #             p.window_bring_to_front(p.window_hwnd)
        #             p.type.run(p.window_hwnd, [])
        #             p.repeat_needed -= 1
        #             p.window_bring_to_back(p.window_hwnd)
        #         elif p.repeat_needed <= 0 and not p.done_repeat:
        #             p.done_repeat = True
        #             self.print_info(f'{p.username} is done.')
        #     self.print_info(f"Rep count: {re}/{max_repeat} "
        #                     f"Percentage: {(re / max_repeat):.2f} "
        #                     f"Time left: {((47.5 * (max_repeat - re)) / 60 / 60):.2f} hours")
        #
        #     time.sleep(random.randint(45, 50))


if __name__ == "__main__":
    game_manager = GameManager()
    # game_manager.find_coordinates()
    for i in range(1):
        game_manager.custom_start([game_manager.type_of_bots.SMITHING.coordinates.RUNE_BAR_2.value,
                                   game_manager.type_of_bots.SMITHING.optional_coordinates.ARROWS.value],
                                  game_manager.list_of_user_objects_1)
    # game_manager.stop_runescape()
