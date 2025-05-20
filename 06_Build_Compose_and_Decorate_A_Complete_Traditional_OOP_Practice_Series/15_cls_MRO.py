# 15. Method Resolution Order (MRO) and Diamond Inheritance Assignment:
# Create four classes:

# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.


class A:

    def show()-> None:
        pass

class B(A):

    def show(self):
        print("This is B Show()")


class C(A):

    def show(self):
        print("This is C Show()")

class D(B, C):
        pass
    


res = D()
res.show()

print("MRO", D.__mro__)
