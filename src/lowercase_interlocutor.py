from abstract_interlocutor import AbstractInterlocutor


class LowercaseInterlocutor(AbstractInterlocutor):

    def greet(self):
        return 'Welcome!'

    def say(self, message: str):
        return message.lower()
