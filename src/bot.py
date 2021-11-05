import json
from telegram.ext import Updater
from telegram.ext import CommandHandler


with open('config.json') as fin:
    config = json.loads(fin.read())

updater = Updater(token=config['token'], use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
