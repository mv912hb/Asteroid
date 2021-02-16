import math


class Asteroid:

    def __init__(self, coor_x, coor_y, speed_coor_x, speed_coor_y, size):
        """
        Initialize new asteroid in game
        :param coor_x: X coordinate
        :param coor_y: Y coordinate
        :param speed_coor_x: Speed by X
        :param speed_coor_y: speed by Y
        :param size: size of asteroid
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y
        self.__speed_x = speed_coor_x
        self.__speed_y = speed_coor_y
        self.__size = size

    def get_radius(self):
        """

        :return: radius of asteroid
        """
        return self.__size * 10 - 5

    def has_intersection(self, obj):
        """
        functions checks if there is an intersection between objects
        :return: True if objects collided or False if not
        """
        distance = math.sqrt(
            math.pow(obj.get_coor()[0] - self.__coor_x, 2) + math.pow(obj.get_coor()[1] - self.__coor_y, 2))
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_size(self):
        """

        :return: size of asteroid
        """
        return self.__size

    def get_coor(self):
        """

        :return: current coordinates of asteroid by both axes
        """
        return self.__coor_x, self.__coor_y

    def get_speed(self):
        """

        :return: current speed of asteroid by both axes
        """
        return self.__speed_x, self.__speed_y

    def set_speed(self, speed_x, speed_y):
        """

        :param speed_x: new speed by axis X
        :param speed_y: new speed by axis Y
        """
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def set_coor(self, coor_x, coor_y):
        """

        :param coor_x: new coordinate by axis X
        :param coor_y: new coordinate by axis Y
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y
