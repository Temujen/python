import random


class Car:
    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f"{self.name} start drive")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self):
        direction = ["left", "right", "around"]
        print(f"{self.name} turned {random.choice(direction)}")

    def show_speed(self):
        print(f"{self.name} - Current speed {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} - Speed limit (60km/h) exceeded")
        else:
            print(f"{self.name} - Current speed {self.speed} km/h")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} - speed limit (40km/h) exceeded")
        else:
            print(f"{self.name} - current speed {self.speed} km/h")


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'white', 'Ford')
town_car.go()
print(f"{town_car.name} is {town_car.color} color")
town_car.turn()
town_car.show_speed()
town_car.stop()
print(town_car.is_polise)

sport_car = SportCar(150, 'Red', 'Ferrari')
sport_car.go()
sport_car.turn()
sport_car.show_speed()
sport_car.stop()
print(sport_car.is_polise)

work_car = WorkCar(40, "Gray", "Gazel")
work_car.go()
work_car.turn()
work_car.show_speed()
work_car.stop()
print(work_car.is_polise)

police_car = PoliceCar(80, "white", "Lada vesta", True)
police_car.go()
police_car.turn()
police_car.show_speed()
police_car.stop()
print(police_car.is_polise)
