# 1
# #  Overloading--same name with many methods.....compile time polymorphism
# class Demo:
#     def add(self, *args):
#         total = 0
#         for i in args:
#             total = total + i
#         return total
#     # def add(self, a, b, c = 0):
#     #     return a + b + c
#
#
# d = Demo()
# print(d.add(1, 2,))
# print(d.add(1, 2, 3))
# print(d.add(1, 2, 3, 4, 5, 6, 7))

# 2 Overriding -- occurs on inheritance.....run time polymorphism
class Father:
    def sleep(self):
        print('Sleeps from 10:00 Pm to 05:00 Am')

    def eat(self):
        print('Eating')


class Son(Father):
    def sleep(self):
        print('Sleeps from 02:00 Am to 10:00 Am')
        super().sleep()

    def eat(self):
        print('Eating')


s = Son()
s.eat()
s.sleep()