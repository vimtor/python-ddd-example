from abc import ABC

from antidote import inject

from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.query.query_bus import QueryBus


class ApiController(ABC):
    @inject
    def __init__(self, query_bus: QueryBus, command_bus: CommandBus):
        self.query_bus = query_bus
        self.command_bus = command_bus
