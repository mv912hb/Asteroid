class Torpedo:

    def __init__(self, coor_x, coor_y, speed_x, speed_y, heading):
        """
        Initialize new torpedo in game
        :param coor_x: X coordinate
        :param coor_y: Y coordinate
        :param speed_x: Speed by X
        :param speed_y: speed by Y
        :param heading: heading angle
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__heading = heading
        self.__radius = 4
        self.__energy = 200

    def cycle(self):
        """

        :return: reduces the energy of torpedo by 1 for every cycle
        """
        self.__energy = self.__energy - 1

    def get_energy(self):
        """

        :return: current energy level of torpedo
        """
        return self.__energy

    def get_radius(self):
        """

        :return: raduis of torpedo
        """
        return self.__radius

    def get_heading(self):
        """

        :return: current heading of torpedo
        """
        return self.__heading

    def get_coor(self):
        """

        :return: coordinates of torpedo by both axes
        """
        return self.__coor_x, self.__coor_y

    def get_speed(self):
        """

        :return: speed of torpedo by both axes
        """
        return self.__speed_x, self.__speed_y

    def set_coor(self, coor_x, coor_y):
        """
        changes coordinates of torpedo by both axes
        :param coor_x: new coordinate by axis X
        :param coor_y: new coordinate by axis Y
        """
        self.__coor_x = coor_x
        self.__coor_y = coor_y

    def set_speed(self, speed_x, speed_y):
        """
        changes current speed of torpedo by both axes
        :param speed_x: new speed by axis X
        :param speed_y: new speed by axis Y
        """
        self.__speed_x = speed_x
        self.__speed_y = speed_y
