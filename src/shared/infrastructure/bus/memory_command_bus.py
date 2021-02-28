from src.shared.domain.bus.command.command_bus import CommandBus


class MemoryCommandBus(CommandBus):
    def __init__(self):
        self.handlers = {}

    def register(self, command, handler):
        self.handlers[command.name()] = handler

    def dispatch(self, command):
        self.handlers[command.name()](command)
