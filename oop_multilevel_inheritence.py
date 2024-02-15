class Human:  # the object class
    can_breath = True
    def __init__(self, num_heart):
        print("Init Human class")
        self.num_eyes = 2
        self.heart = num_heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")


class Male(Human):
    def __init__(self, name):
        print("Init Male class")
        self.name = name

    def sleep(self):
        print("I can sleep whole day")


class Boy(Male):
    def __init__(self, name, heart, dance):
        self.dance = dance
        Human.__init__(self, heart)
        Male.__init__(self, name)

    def work(self):
        # Human.work(self)
        super().work()
        print("I can code")


# class Programmer(Boy):
#     def work(self):
#         print("I can write programmes")


boy_1 = Boy('John', 1, True)
# boy_1.eat()
# boy_1.sleep()
# boy_1.work()
# prog_1 = Programmer()
# prog_1.work()
print(boy_1.name)
print(boy_1.heart)
print(boy_1.dance)
print(boy_1.can_breath)
# print(Boy.mro())