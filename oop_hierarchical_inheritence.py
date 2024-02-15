class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showDetail(self):
        print(f"My name is {self.name} and i'm {self.age} years old")
    def eat(self):
        print("I can eat")


class Male(Human):
    def __init__(self,name, age, location):
        Human.__init__(self, name, age)
        self.location = location
    def sleep(self):
        print("I can sleep")


class Female(Human):
    def __init__(self, name, age, dance):
        self.dance = dance
        Human.__init__(self, name, age)

    def showDetail(self):
        # Human.showDetail(self)
        print(f"Know dancing {self.dance}")

    def work(self):
        print("I can write code")


female = Female('Joan', 22, True)
female.eat()
female.showDetail()
male = Male('John', 21, 'Dodoma')
male.sleep()
print(male.location)
male.showDetail()