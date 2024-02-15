# public -- anyone outside the class can use them
# private -- with a class and with in the derived class
# protected -- with in a particular class only

class Student:
    def __init__(self, name, roll_no, age):
        self.name = name  # public instance variable
        self._roll_no = roll_no  # protected instance variable
        self.__age = age  # private instance variable

    def __display(self):
        print(f'My name is {self.name} with roll number {self._roll_no} and my age is {self.__age} from student class')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 35:
            print('Age should be less than 35')
        else:
            self.__age = age

    def displayPrivateData(self):
        self.__display()


# class Branch(Student):
#     def show(self):
#         print(f'The age is {self.__age}')

# function to call


# def showData():
s1 = Student('John', 78, 22)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
# b1 = Branch('Joan', 56, 22)
# b1.show()
s1.displayPrivateData()  # used to display private data of a class

# showData()

# name mandling
# print(dir(s1))
# print(s1._Student__age)
s1._Student__display()  # using file mandling you can display the private data