from abc import ABC, abstractmethod


class AbstractInterlocutor(ABC):

    @abstractmethod
    def greet(self):
        return 'Greet message'

    @abstractmethod
    def say(self, message: str):
        return f'Answer to message "{message}"'
