from abstract_interlocutor import AbstractInterlocutor
from db import DB


class CouterInterlocutor(AbstractInterlocutor):

    def __init__(self):
        self.__db = DB()

    def greet(self, chat_id: int):
        self.__ensure_sql_table_presence()
        if self.__is_new_chat(chat_id):
            self.__put_initial_record(chat_id)
            return 'Welcome!'
        else:
            return 'Welcome, again!'

    def say(self, chat_id: int, message: str):
        self.__ensure_sql_table_presence()
        if self.__is_new_chat(chat_id):
            counter = 1
            self.__put_initial_record(chat_id)
            self.__update_chat_counter(chat_id, counter)
        else:
            counter = self.__get_chat_counter(chat_id)
            counter += 1
            self.__update_chat_counter(chat_id, counter)
        return f'You wrote messages {counter} times'

    def __is_new_chat(self, chat_id):
        return self.__db.fetch_all(f'''
            SELECT COUNT(*)
            FROM counts
            WHERE chat_id = {chat_id}''')[0][0] == 0

    def __ensure_sql_table_presence(self):
        self.__db.execute('''
            CREATE TABLE IF NOT EXISTS counts (
                chat_id INTEGER,
                counter INTEGER
            )
        ''')

    def __put_initial_record(self, chat_id):
        self.__db.execute(f'''
            INSERT INTO counts
            (chat_id, counter)
            VALUES
            ({chat_id}, 0)
        ''')

    def __update_chat_counter(self, chat_id, counter):
        self.__db.execute(f'''
            UPDATE counts
            SET counter = {counter}
            WHERE chat_id = {chat_id}
        ''')

    def __get_chat_counter(self, chat_id):
        return self.__db.fetch_all(f'''
            SELECT counter
            FROM counts
            WHERE chat_id = {chat_id}
        ''')[0][0]
