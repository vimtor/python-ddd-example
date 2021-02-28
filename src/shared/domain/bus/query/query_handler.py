from abc import ABC, abstractmethod

from antidote import Service

from src.shared.domain.bus.query.query import Query


class QueryHandler(ABC, Service):
    @abstractmethod
    def __call__(self, query: Query):
        pass
