import math
import random
import sys

from asteroid import Asteroid
from screen import Screen
from ship import *
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
LEFT = 7
RIGHT = -7


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__asteroids_amount = asteroids_amount
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = self.create_ship()
        self.__asteroids = []
        self.__torpedos = []
        self.__score = 0
        self.create_asteroids()
        self.register_asteroids()
        self.__lifes = 3

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def create_torpedo(self):
        """
        creates new torpedo in game according to conditions
        """
        if self.__screen.is_space_pressed():
            if len(self.__torpedos) < 10:
                speed_x = self.__ship.get_speed()[0] + 2 * math.cos(math.radians(self.__ship.get_heading()))
                speed_y = self.__ship.get_speed()[1] + 2 * math.sin(math.radians(self.__ship.get_heading()))
                torpedo = Torpedo(self.__ship.get_coor()[0], self.__ship.get_coor()[1], speed_x, speed_y,
                                  self.__ship.get_heading())
                self.__screen.register_torpedo(torpedo)
                self.__torpedos.append(torpedo)

    def create_asteroids(self):
        """
        creates asteroids in game
        """
        i = 0
        while i < self.__asteroids_amount:
            x = random.randint(self.__screen_min_x, self.__screen_max_x)
            y = random.randint(self.__screen_min_y, self.__screen_max_y)
            speed_x = random.randint(1, 4)
            speed_y = random.randint(1, 4)
            size = 3
            if x != self.__ship.get_coor()[0] and y != self.__ship.get_coor()[1]:
                asteroid = Asteroid(x, y, speed_x, speed_y, size)
                self.__asteroids.append(asteroid)
            else:
                continue
            i += 1

    def register_asteroids(self):
        """
        registers new asteroid in game
        """
        for asteroid in self.__asteroids:
            self.__screen.register_asteroid(asteroid, asteroid.get_size())

    def _game_loop(self):
        """
        the main function which contains data about game running process
        """
        if self.exit_condition():
            sys.exit()
        self.__screen.draw_ship(self.__ship.get_coor()[0], self.__ship.get_coor()[1],
                                self.__ship.get_heading())

        self.ship_acceleration()
        self.rotate_ship()
        self.move_ship()
        self.move_asteroid()
        self.draw_asteroids()
        self.create_torpedo()
        self.move_torpedos()
        self.draw_torpedos()

    def exit_condition(self):
        """
        checks the player in-game status and finishes the game according to lose/win conditions
        :return: True if game over or user decided to exit, False if game continues
        """
        if len(self.__asteroids) == 0:
            self.__screen.show_message("WIN", "YOU WON!")
            return True
        elif self.__lifes == 0:
            self.__screen.show_message("LOSE", "YOU ARE OUT OF LIFE! YOU LOST!")
            return True
        elif self.__screen.should_end():
            self.__screen.show_message("Exit", "You choosed to exit the game! Bye!")
            return True
        return False



    def create_ship(self):
        """
        creates ship
        :return: created ship
        """
        x = random.randint(self.__screen_min_x, self.__screen_max_x)
        y = random.randint(self.__screen_min_y, self.__screen_max_y)
        ship = Ship(x, y, 0)
        self.__screen.draw_ship(ship.get_coor()[0], ship.get_coor()[1], ship.get_heading())
        return ship

    def split_asteroid(self, asteroid, torpedo):
        """
        function splits asteroid after collision with a torpedo according to game rules
        :param asteroid: object which have to be splited
        :param torpedo: object which had an intersection with asteroid
        :return:
        """
        if asteroid.get_size() == 3:
            self.__screen.unregister_asteroid(asteroid)
            self.__asteroids.remove(asteroid)
            new_asteroid_1_speed_x = torpedo.get_speed()[0] + asteroid.get_speed()[0] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_1_speed_y = torpedo.get_speed()[1] + asteroid.get_speed()[1] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_2_speed_x = -torpedo.get_speed()[0] + asteroid.get_speed()[0] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_2_speed_y = -torpedo.get_speed()[1] + asteroid.get_speed()[1] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_1 = Asteroid(asteroid.get_coor()[0], asteroid.get_coor()[1], new_asteroid_1_speed_x,new_asteroid_1_speed_y, 2)
            new_asteroid_2 = Asteroid(asteroid.get_coor()[0], asteroid.get_coor()[1], new_asteroid_2_speed_x,new_asteroid_2_speed_y, 2)
            self.__screen.register_asteroid(new_asteroid_1, new_asteroid_1.get_size())
            self.__screen.register_asteroid(new_asteroid_2, new_asteroid_2.get_size())
            self.__asteroids.append(new_asteroid_1)
            self.__asteroids.append(new_asteroid_2)
        elif asteroid.get_size() == 2:
            self.__screen.unregister_asteroid(asteroid)
            self.__asteroids.remove(asteroid)
            new_asteroid_1_speed_x = torpedo.get_speed()[0] + asteroid.get_speed()[0] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_1_speed_y = torpedo.get_speed()[1] + asteroid.get_speed()[1] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_2_speed_x = -torpedo.get_speed()[0] + asteroid.get_speed()[0] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_2_speed_y = -torpedo.get_speed()[1] + asteroid.get_speed()[1] / math.sqrt(math.pow(asteroid.get_speed()[0], 2) + math.pow(asteroid.get_speed()[1], 2))
            new_asteroid_1 = Asteroid(asteroid.get_coor()[0], asteroid.get_coor()[1], new_asteroid_1_speed_x,new_asteroid_1_speed_y, 1)
            new_asteroid_2 = Asteroid(asteroid.get_coor()[0], asteroid.get_coor()[1], new_asteroid_2_speed_x,new_asteroid_2_speed_y, 1)
            self.__screen.register_asteroid(new_asteroid_1, new_asteroid_1.get_size())
            self.__screen.register_asteroid(new_asteroid_2, new_asteroid_2.get_size())
            self.__asteroids.append(new_asteroid_1)
            self.__asteroids.append(new_asteroid_2)
        elif asteroid.get_size() == 1:
            self.__screen.unregister_asteroid(asteroid)
            self.__asteroids.remove(asteroid)

    def move_asteroid(self):
        """
        function moves asteroid in the game board
        """
        for asteroid in self.__asteroids:
            speed_x, speed_y = asteroid.get_speed()
            old_spot_x, old_spot_y = asteroid.get_coor()
            new_spot_x = self.__screen_min_x + ((old_spot_x + speed_x - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x))
            new_spot_y = self.__screen_min_y + ((old_spot_y + speed_y - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y))
            asteroid.set_coor(new_spot_x, new_spot_y)

    def draw_asteroids(self):
        """
        function draws registered asteroids using class Screen
        :return:
        """
        for asteroid in self.__asteroids:
            self.__screen.draw_asteroid(asteroid, asteroid.get_coor()[0], asteroid.get_coor()[1])

    def draw_torpedos(self):
        """
        function draws torpedos
        """
        for torpedo in self.__torpedos:
            self.__screen.draw_torpedo(torpedo, torpedo.get_coor()[0], torpedo.get_coor()[1], torpedo.get_heading())

    def move_ship(self):
        """
        function moves out ship on the board using and changing all his attributes
        """
        speed_x, speed_y = self.__ship.get_speed()
        old_spot_x, old_spot_y = self.__ship.get_coor()
        new_spot_x = self.__screen_min_x + ((old_spot_x + speed_x - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x))
        new_spot_y = self.__screen_min_y + ((old_spot_y + speed_y - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y))
        self.__ship.set_coor(new_spot_x, new_spot_y)
        for asteroid in self.__asteroids:
            if asteroid.has_intersection(self.__ship):
                self.__screen.remove_life()
                self.__lifes -= 1
                self.__screen.show_message("ХУЙ", "ХУЙ")
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)

    def rotate_ship(self):
        """
        changes ship direction of moving by changing attribute heading
        :return:
        """
        if self.__screen.is_left_pressed():
            self.__ship.set_heading(self.__ship.get_heading() + LEFT)
        elif self.__screen.is_right_pressed():
            self.__ship.set_heading(self.__ship.get_heading() + RIGHT)

    def move_torpedos(self):
        """
        moving torpedos on board
        """
        for torpedo in self.__torpedos:
            torpedo.cycle()
            if torpedo.get_energy() <= 0:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedos.remove(torpedo)
                break
            speed_x, speed_y = torpedo.get_speed()
            old_spot_x, old_spot_y = torpedo.get_coor()
            new_spot_x = self.__screen_min_x + ((old_spot_x + speed_x - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x))
            new_spot_y = self.__screen_min_y + ((old_spot_y + speed_y - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y))
            torpedo.set_coor(new_spot_x, new_spot_y)

            for asteroid in self.__asteroids:
                if asteroid.has_intersection(torpedo):
                    if asteroid.get_size() == 3:
                        self.__score += 20
                    elif asteroid.get_size() == 2:
                        self.__score += 50
                    elif asteroid.get_size() == 1:
                        self.__score += 100
                    self.__screen.set_score(self.__score)
                    self.__screen.unregister_torpedo(torpedo)
                    self.__torpedos.remove(torpedo)
                    self.split_asteroid(asteroid, torpedo)

    def ship_acceleration(self):
        """
        changes speed of our ship(accelerates him)
        """
        if self.__screen.is_up_pressed():
            old_speed_x, old_speed_y = self.__ship.get_speed()
            new_speed_x = old_speed_x + math.cos(math.radians(self.__ship.get_heading()))
            new_speed_y = old_speed_y + math.sin(math.radians(self.__ship.get_heading()))
            self.__ship.set_speed(new_speed_x, new_speed_y)


def main(asteroids_amount):
    runner = GameRunner(asteroids_amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
