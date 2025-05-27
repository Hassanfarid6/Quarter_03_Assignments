# 9. Abstract Classes and Methods Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

# Polymorphism is a concept where different classes can use the same method
# name but behave differently.
class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass
        
class Rectangle(Shape):
    
    def __init__(self, width, hight) -> None:
        self.width = width
        self.hight = hight

    def area(self):
        return self.width * self.hight

res = Rectangle(7, 5)

print("Area of Rectangle: ",res.area())