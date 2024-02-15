# Abstraction, you don't see how the programs works but only see the results, it also works in design level
from oop_abstract_class import Vehicle


class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print('Start with kick')


class Scoot(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print('self start')

    def display(self):
        print(f'The chosen color is {self.color}')

class Car(Vehicle):
    def __init__(self, n, x):
        self.no_tyre = n
        self.no_of_gears = 6

    def start(self):
        print('Start with key')