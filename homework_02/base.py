from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            try:
                if self.fuel <= 0:
                    raise NotEnoughFuel
            except NotEnoughFuel:
                print("Your fuel level is too low")
            else:
                self.started = True

    def move(self, distance):
        try:
            self.fuel = self.fuel - self.fuel_consumption * distance
            if self.fuel <= 0:
                raise LowFuelError
        except LowFuelError:
            print("Fuel amount is not enough for this distance")


#v = Vehicle(500, 0, 15)
#v.move(1)
#v.start()
#print(v.started)


