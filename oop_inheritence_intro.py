class Human:
    def __init__(self, num_heart):
        self.numb_eyes = 2
        self.numb_nose = 1
        self.num_heart  = num_heart

    def eat(self):
        print('I can eat')

    def work(self):
        print('I can work')


class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name

    def flirt(self):
        print('I can flirt')

    def work(self):
        super().work()
        print('I can code')


male_1 = Male('john', 1)
# male_1.flirt()
# male_1.work()
print(male_1.numb_nose)
print(male_1.name)
print(male_1.num_heart)