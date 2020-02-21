"""
Timer Singleton to keep time in seconds used by client
"""


class Timer:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Timer.__instance is None:
            Timer()
        return Timer.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Timer.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # default value
            self.seconds = 1
            Timer.__instance = self

    @staticmethod
    def get_seconds() -> int:
        return Timer.get_instance().seconds

    @staticmethod
    def set_seconds(i_seconds) -> int:
        Timer.get_instance().seconds = i_seconds
        return Timer.get_instance().seconds
