from abstract_interlocutor import AbstractInterlocutor


class LowercaseInterlocutor(AbstractInterlocutor):

    def greet(self, chat_id: int):
        return 'Welcome!'

    def say(self, chat_id: int, message: str):
        return message.lower()
