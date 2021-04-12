"""
создайте класс `Plane`, наследник `Vehicle`
"""
import base
import exceptions as ex


class Plane(base.Vehicle):
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
                raise ex.CargoOverload
        except ex.CargoOverload:
            print("I can't take this cargo")
        else:
            self.cargo += w

    def remove_all_cargo(self, z):
        z = self.cargo
        self.cargo = 0
        return z


p = Plane(500, 100, 15, 50)
p.load_cargo(5)
print(p.cargo)
#print(p.remove_all_cargo(2))