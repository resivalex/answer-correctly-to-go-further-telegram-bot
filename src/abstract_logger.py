from abc import ABC, abstractmethod


class AbstractLogger(ABC):

    @abstractmethod
    def log(self, message: str):
        pass
