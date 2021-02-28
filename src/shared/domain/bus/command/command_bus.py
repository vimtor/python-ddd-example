from abc import ABC, abstractmethod


class CommandBus(ABC):
    @abstractmethod
    def register(self, command, handler):
        pass

    @abstractmethod
    def dispatch(self, command):
        pass
