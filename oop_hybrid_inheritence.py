class A:
    def display(self):
        print("Display from A class")


class B(A):
    def display(self):
        print("Display from B class")


class C:
    def show(self):
        print("Hi from C class")


class D(B, C):
    def display(self):
        super().display()
        A.display(self)
        print("Display from D class")


d1 = D()
d1.display()
print(D.mro())