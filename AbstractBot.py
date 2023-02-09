from abc import abstractmethod

from Commands import Commands


class AbstractBot(Commands):
    @abstractmethod
    def run(self, window, args):
        pass

    @abstractmethod
    def reset_interface(self, window, args):
        pass
