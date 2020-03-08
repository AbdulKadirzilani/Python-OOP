# Base class A
# Base class B
#super class

class A:
    def Phone(self):

        print("Base class A")

class B(A):

    def Phone(self):
        super().Phone()
        print("Base class B")

x = B()


print(x.Phone())