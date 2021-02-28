from abc import ABC, abstractmethod


class ValueObject(ABC):
    def __init__(self, value):
        self.validate(value)
        self.value = value

    def __repr__(self):
        return self.value

    @abstractmethod
    def validate(self, value):
        pass
