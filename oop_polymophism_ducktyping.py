# duck type -- is used to allow the data type to be dynamic

#  you don't need to specify the data type of the variable in dynamic typing
class Duck:
    def swim(self):
        print('I am a duck and i can swim')

    def speaks(self):
        print('Quack Quack')


class Dog:
    def swim(self):
        print('I am a dog and i can swim')

    def speaks(self):
        print('Woof Woof')


class Person:
    def speaks(self):
        print('Woof Woof')


class Demo:
    def display(self, duck):
        duck.swim()
        duck.speaks()
        print('Information displayed')


d = Duck()
dog = Dog()
person = Person()
# display(d)
demo = Demo()
demo.display(d)