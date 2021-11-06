from abstract_logger import AbstractLogger


class NullLogger(AbstractLogger):

    def log(self, message: str):
        pass
