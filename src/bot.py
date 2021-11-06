import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chat_logger import ChatLogger
from null_logger import NullLogger


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

logger.log('Bot started')

updater = Updater(token=config['token'], use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    logger.log(f'/start was triggered\n{str(update.effective_chat)}')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome!")


def upper_and_lower_case(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text

    response = f'{message.upper()}\n{message.lower()}'
    logger.log(f'Chat {chat_id}:\n{message}\nBot:\n{response}')
    context.bot.send_message(chat_id=chat_id, text=response)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, upper_and_lower_case)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
updater.start_polling()
