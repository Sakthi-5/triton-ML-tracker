from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass