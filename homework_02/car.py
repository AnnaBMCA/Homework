"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = None


    def set_engine(self, eng=Engine(5.2, 4)):
        self.engine = eng



# c = Car(200, 500, 15)
# c.set_engine()
#print(c.engine)

