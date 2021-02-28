from abc import ABC, abstractmethod

from antidote import Service

from src.shared.domain.query import Query


class CommandHandler(ABC, Service):
    @abstractmethod
    def __call__(self, query: Query):
        pass
