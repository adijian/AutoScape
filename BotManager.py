from Demos.security.security_enums import Enum

from FiremakingIncenseBot import FiremakingIncenseBot
from HerbloreBot import HerbloreBot
from HerbloreUnfBot import HerbloreUnfBot
from MiningIronBot import MiningIronBot
from MiningCopperBot import MiningCopperBot
from SmithingBot import SmithingBot
from BronzeBarBot import BronzeBarBot


class BotManager:
    def __init__(self):
        self.type_of_bots = self.TypeOfBots

    class TypeOfBots(Enum):
        SMITHING = SmithingBot()
        HERBLORE = HerbloreBot()
        FIREMAKING_INCENSE = FiremakingIncenseBot()
        BRONZE_BAR_BOT = BronzeBarBot()
        HERBLORE_UNF_BOT = HerbloreUnfBot()
        MINING_COPPER_BOT = MiningCopperBot()
        MINING_IRON_BOT = MiningIronBot()
