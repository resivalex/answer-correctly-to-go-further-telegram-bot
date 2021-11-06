from abstract_interlocutor import AbstractInterlocutor
from db import DB
from quiz_chat_progress import QuizChatProgress


class QuizInterlocutor(AbstractInterlocutor):

    def __init__(self, scenario):
        self.__db = DB()
        self.__scenario = scenario

    def greet(self, chat_id: int):
        self.__ensure_sql_table_presence()
        progress = self.__get_progress(chat_id)
        current_state_message = self.__current_state_message(progress)
        if progress.exists():
            return self.__scenario['welcome_again_message'] + '\n\n' + current_state_message
        progress.persist()

        return self.__scenario['welcome_message'] + '\n\n' + current_state_message

    def say(self, chat_id: int, message: str):
        self.__ensure_sql_table_presence()
        progress = self.__get_progress(chat_id)

        if not progress.exists():
            return self.greet(chat_id)

        if self.__is_completed(progress):
            return self.__current_state_message(progress)

        current_step = self.__steps()[progress.completed_steps()]
        expected_answer = current_step['correct_answer']
        if message.lower().strip() == expected_answer.lower().strip():
            progress.go_to_next_step()
            return current_step['correct_answer_message'] + '\n\n' + self.__current_state_message(progress)
        else:
            return current_step['wrong_answer_message']

    def __get_progress(self, chat_id):
        return QuizChatProgress(chat_id=chat_id, db=self.__db)

    def __current_state_message(self, progress: QuizChatProgress):
        steps = self.__steps()
        if self.__is_completed(progress):
            return self.__scenario['complete_message']

        return steps[progress.completed_steps()]['question']

    def __is_completed(self, progress: QuizChatProgress):
        return progress.completed_steps() >= len(self.__steps())

    def __steps(self):
        return self.__scenario['steps']

    def __ensure_sql_table_presence(self):
        self.__db.execute('''
            CREATE TABLE IF NOT EXISTS quiz_progresses (
                chat_id INTEGER,
                completed_steps INTEGER
            )
        ''')
