import random
from dakar import Dakar


class Car(Dakar):

    speed_limit = 130

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed
        self.distance = 0
        self.penalty = 0


    @classmethod
    def set_speed_limit(cls, new_speed_limit):
        cls.speed_limit = new_speed_limit

    def set_speed(self, new_speed):
        self.speed = new_speed



    def double_or_half_speed(self):
        surprise = random.randint(1, 2)
        if surprise == 1:
            self.speed = self.speed * 2
            if self.__class__.speed_limit < self.speed:
                self.speed = self.__class__.speed_limit
                self.penalty += 1
        else:
            self.speed = self.speed / 2

    def points(self):
        return self.distance*3-self.penalty*25

    def status(self):
        print("speed:", self.speed, "distance:", self.distance, "speed limit:", self.speed_limit, "points:", self.points)



    @staticmethod
    def convert_spped_to_mps(speed_in_kmh):
        return speed_in_kmh / 3.6


def main():
    number_of_cars = 6
    number_of_laps = 2
    min_initial_speed = 50
    max_initial_speed = 80

    Car.set_speed_limit(120)
    #Car.set_speed_limit(130)

    cars = []
    for i in range(number_of_cars):
        initial_speed = random.randint(min_initial_speed, max_initial_speed)
        car = Car(initial_speed)
        cars.append(car)

    for lap in range(number_of_laps):
        for i in range(number_of_cars):
            car = cars[i]
            car.passed_one_circle()
            car.double_or_half_speed()
            car.points()
            car.status()
