"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, w):
        try:
            if (self.cargo+w) >= self.max_cargo:
                raise CargoOverload
        except CargoOverload:
            print("I can't take this cargo")
        else:
            self.cargo += w

    def remove_all_cargo(self):
        z = self.cargo
        self.cargo = 0
        return z


# p = Plane(500, 100, 15, 5)
# p.load_cargo(50)
# print(p.cargo)
# print(p.remove_all_cargo())

