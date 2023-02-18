from Demos.security.security_enums import Enum

from Bots.FiremakingIncenseBot import FiremakingIncenseBot
from Bots.HerbloreBot import HerbloreBot
from Bots.HerbloreUnfBot import HerbloreUnfBot
from Bots.MiningIronBot import MiningIronBot
from Bots.MiningCopperBot import MiningCopperBot
from Bots.SmithingItemsBot import SmithingItemsBot
from Bots.SmithingBarsBot import SmithingBarsBot

"""
            User(username="", password="deejian8",
                 bot_type=self.type_of_bots.SMITHING, repeat_needed=int(19575), hide_window=True,
                 args=[self.type_of_bots.SMITHING.coordinates.RUNE_BAR_2.value,
                       self.type_of_bots.SMITHING.optional_coordinates.ARROWS.value],
                 world_args=[self.Coordinates.WORLD_MEMBER_1.value])
                 
             User(username="", password="deejian8",
                 bot_type=self.type_of_bots.HERBLORE_UNF_BOT, repeat_needed=int(1434 / 14), hide_window=True,
                 world_args=[self.Coordinates.WORLD_FREE_1.value])
                 
             User(username="", password="deejian8",
                 bot_type=self.type_of_bots.MINING_IRON_BOT, repeat_needed=int(1434 / 14), hide_window=True,
                 args2=[0],
                 world_args=[self.Coordinates.WORLD_FREE_1.value])

"""


class BotManager:
    def __init__(self):
        self.type_of_bots = self.TypeOfBots

    class TypeOfBots(Enum):
        FIREMAKING_INCENSE = FiremakingIncenseBot()
        HERBLORE = HerbloreBot()
        HERBLORE_UNF_BOT = HerbloreUnfBot()
        MINING_COPPER_BOT = MiningCopperBot()
        MINING_IRON_BOT = MiningIronBot()
        SMITHING_BARS = SmithingBarsBot()
        SMITHING_ITEMS = SmithingItemsBot()
