import cv2

from Screen import Screen


class GameObject(object):
    def __init__(self):
        self.__screen = Screen(WINDOW_NAME="R2")

    def get_objects(self, OBJECT_NAME):
        cv2.imshow("r2", self.__screen.updated_img)
        cv2.waitKey(1)
