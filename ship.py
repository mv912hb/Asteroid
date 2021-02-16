class Ship:

    def __init__(self, coor_x, coor_y, heading):
        """
        Initialize ship in game
        :param coor_x: X coordinate
        :param coor_y: Y coordinate
        :param speed_x: Speed by X
        :param speed_y: speed by Y
        :param heading: heading angle
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y
        self.__heading = heading
        self.__speed_x = 0
        self.__speed_y = 0
        self.__radius = 1

    def get_radius(self):
        """

        :return: radius of a ship
        """
        return self.__radius

    def get_heading(self):
        """

        :return: ship nose heading
        """
        return self.__heading

    def get_speed(self):
        """

        :return: current speed of ship by both axes
        """
        return self.__speed_x, self.__speed_y

    def get_coor(self):
        """

        :return: coordinates of ship by both axes
        """
        return self.__coor_x, self.__coor_y

    def set_heading(self, heading):
        """
        changes current heading of ship
        :param heading: new heading of ship
        """
        self.__heading = heading

    def set_speed(self, speed_x, speed_y):
        """
        changes current speed of ship by both axes
        :param speed_x: new speed by axis X
        :param speed_y: new speed by axis Y
        """
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def set_coor(self, coor_x, coor_y):
        """
        changes coordinates of ship by both axes
        :param coor_x: new coordinate by axis X
        :param coor_y: new coordinate by axis Y
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y

