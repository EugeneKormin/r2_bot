from Mouse import Mouse
from Keyboard import Keyboard
from GameObject import GameObject


class FarmingBot(object):
    def __init__(self):
        self.__mouse = Mouse()
        self.__keyboard = Keyboard()
        self.__gameObject = GameObject()
        self.__execute()

    def __execute(self):
        pass
