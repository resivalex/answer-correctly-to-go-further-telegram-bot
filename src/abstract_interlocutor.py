from abc import ABC, abstractmethod


class AbstractInterlocutor(ABC):

    @abstractmethod
    def greet(self, chat_id: int):
        return 'Greet message'

    @abstractmethod
    def say(self, chat_id: int, message: str):
        return f'Answer to message "{message}"'
