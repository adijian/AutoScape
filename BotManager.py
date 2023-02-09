from Demos.security.security_enums import Enum

from FiremakingIncenseBot import FiremakingIncenseBot
from HerbloreBot import HerbloreBot
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
