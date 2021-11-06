import json
from chat_logger import ChatLogger
from null_logger import NullLogger
from lowercase_interlocutor import LowercaseInterlocutor
from chat import Chat


with open('config.json') as fin:
    config = json.loads(fin.read())

token = config['token']
if 'logger_chat' in config:
    logger = ChatLogger.create_from_token(
        config['logger_chat']['token'],
        config['logger_chat']['chat_id']
    )
else:
    logger = NullLogger()

interlocutor = LowercaseInterlocutor()


def _on_start():
    return interlocutor.greet()


def _on_message(message):
    return interlocutor.say(message)


chat = Chat(bot_token=token,
            start_callback=_on_start,
            message_callback=_on_message,
            logger=logger)
chat.start()
