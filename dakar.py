from random import *

class Dakar:


    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
        self.penalty = 0

    #abstract points metodus

    def status(self):
        print("speed:", self.speed, "distance:", self.distance, "speed limit:", self.speed_limit, "penalty:", self.points)

    def passed_one_circle(self):
        self.distance += self.speed


def main():
    number_of_cars = 6
    number_of_laps = 2
    min_initial_speed = 50
    max_initial_speed = 80

    #Car.set_speed_limit(120)
    #Car.set_speed_limit(130)

    cars = []
    for i in range(number_of_cars):
        initial_speed = randint(min_initial_speed, max_initial_speed)
        car = Dakar(initial_speed)
        cars.append(car)

    for lap in range(number_of_laps):
        for i in range(number_of_cars):
            car = cars[i]
            car.passed_one_circle()
            car.double_or_half_speed()
            car.points()
            car.status()

main()
