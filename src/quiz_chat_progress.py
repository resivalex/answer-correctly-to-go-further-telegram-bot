class QuizChatProgress:

    def __init__(self, chat_id, db):
        self.__chat_id = chat_id
        self.__db = db

    def exists(self):
        return int(self.__db.fetch_all(f'''
            SELECT COUNT(*)
            FROM quiz_progresses
            WHERE chat_id = {self.__chat_id}''')[0][0]) != 0

    def persist(self):
        self.__db.execute(f'''
            INSERT INTO quiz_progresses
            (chat_id, completed_steps)
            VALUES
            ({self.__chat_id}, 0)
        ''')

    def completed_steps(self):
        if not self.exists():
            return 0

        return int(self.__db.fetch_all(f'''
            SELECT completed_steps
            FROM quiz_progresses
            WHERE chat_id = {self.__chat_id}
        ''')[0][0])

    def go_to_next_step(self):
        steps = self.completed_steps() + 1
        if self.exists():
            self.__db.execute(f'''
                UPDATE quiz_progresses
                SET completed_steps = {steps}
                WHERE chat_id = {self.__chat_id}
            ''')
        else:
            self.persist()
