from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Chat:

    def __init__(self, bot_token, start_callback, message_callback, logger):
        self.__bot_token = bot_token
        self.__start_callback = start_callback
        self.__message_callback = message_callback
        self.__logger = logger

    def start(self):
        updater = Updater(token=self.__bot_token, use_context=True)
        dispatcher = updater.dispatcher

        start_handler = CommandHandler('start', self.__get_tg_start_callback())
        message_handler = MessageHandler(Filters.text, self.__get_tg_message_callback())
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(message_handler)

        self.__logger.log('Bot started')

        updater.start_polling()

    def __get_tg_start_callback(self):
        def callback(update, context):
            chat_id = update.effective_chat.id
            self.__logger.log(f'/start was triggered\n{str(update.effective_chat)}')
            context.bot.send_message(chat_id=chat_id, text=self.__start_callback())

        return callback

    def __get_tg_message_callback(self):
        def callback(update, context):
            chat_id = update.effective_chat.id
            message = update.message.text

            response = self.__message_callback(message)
            self.__logger.log(f'Chat {chat_id}:\n{message}\n\nBot:\n{response}')
            context.bot.send_message(chat_id=chat_id, text=response)

        return callback
