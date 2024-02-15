class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
        print('From human class')

    def eat(self):
        print('I can eat')

    def work(self):
        print('I can work')


class Male:
    def __init__(self, name):
        self.name = name
        print('From male class')

    def flirt(self):
        print('I can flirt')

    def work(self):
        print('I can code')


class Boy(Human, Male):
    def __init__(self, name, language, num_heart):
        Human.__init__(self, num_heart)
        Male.__init__(self, name)
        self.language = language

    def sleep(self):
        print('I can sleep')

    def work(self):
        print('I can test')

    def display(self):
        print(f"Hi, i am {self.name}, i work on {self.language} and i have {self.num_heart} heart")


boy_1 = Boy('John', 'C++', 1)
# boy_1.flirt()
# boy_1.work()
# Male.work(boy_1)
# method resolution order
# print(Boy.mro())
# print(boy_1.name)
# print(boy_1.num_heart)
# print(boy_1.language)
# print(boy_1.num_nose)
boy_1.display()