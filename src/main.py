import json
from chat_logger import ChatLogger
from null_logger import NullLogger
from quiz_interlocutor import QuizInterlocutor
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

interlocutor = QuizInterlocutor(config['quiz'])


def _on_start(chat_id: int):
    return interlocutor.greet(chat_id)


def _on_message(chat_id: int, message: str):
    return interlocutor.say(chat_id, message)


chat = Chat(bot_token=token,
            start_callback=_on_start,
            message_callback=_on_message,
            logger=logger)
chat.start()
