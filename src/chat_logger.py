from abstract_logger import AbstractLogger
from telegram import Bot


class ChatLogger(AbstractLogger):

    @staticmethod
    def create_from_token(token: str, chat_id: int, prefix=''):
        bot = Bot(token=token)
        return ChatLogger(bot, chat_id, prefix=prefix)

    def __init__(self, bot: Bot, chat_id: int, prefix=''):
        self.__bot = bot
        self.__chat_id = chat_id
        self.__prefix = prefix

    def log(self, message: str):
        self.__bot.sendMessage(chat_id=self.__chat_id, text=f'{self.__prefix}{message}')
