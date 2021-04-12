from abc import ABC
import exceptions as ex


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
                    raise ex.NotEnoughFuel
            except ex.NotEnoughFuel:
                print("Your fuel level is too low")
            else:
                self.started = True

    def move(self, distance):
        try:
            self.fuel = self.fuel - self.fuel_consumption * distance
            if self.fuel <= 0:
                raise ex.LowFuelError
        except ex.LowFuelError:
            print("Fuel amount is not enough for this distance")


v = Vehicle(500, 0, 15)
v.move(10)
v.start()
print(v.started)


