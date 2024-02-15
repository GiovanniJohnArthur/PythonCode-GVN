class A:
    def display(self):
        print("Display from A class")


class B(A):
    pass
    # def display(self):
    #     print("Display from B class")


class C(A):
    def show(self):
        print("Hi from C class")

    # def display(self):
    #     print("Display from C class")


class D(B, C):
    pass
    # def display(self):
        # super().display()
        # A.display(self)
        # print("Display from D class")


d1 = D()
d1.display()
print(D.mro())