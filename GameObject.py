from Screen import Screen


class GameObject(object):
    def __init__(self):
        self.__screen = Screen(WINDOW_NAME="")

    def get_objects(self, OBJECT_NAME, screen):
        screen = self.__screen.update_img()

