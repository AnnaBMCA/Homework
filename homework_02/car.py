"""
создайте класс `Car`, наследник `Vehicle`
"""
import base
import engine as e


class Car(base.Vehicle):
    engine = None

    def set_engine(self, eng=e.Engine(5.2, 4)):
        self.engine = eng


c = Car(200, 500, 15)
c.set_engine()
print(c.engine)