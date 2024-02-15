class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.pi * radius *radius

    def circumference(self):
        # return 2 * Circle.pi * self.radius
        return 2 * self.pi * self.radius


circle_1 = Circle(4)
print(circle_1.circumference())
circle_2 = Circle(14)
print(circle_2.circumference())
circle_2 = Circle(6)
print(circle_2.area)