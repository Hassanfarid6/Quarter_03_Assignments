# 1. Using self Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these
# values via a constructor. Add a method display() that prints student details.

class Using_Self:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My name is: {self.name}")
        print(f"My marks is: {self.marks}")

res = Using_Self("hassan", 85)
res.display()

res = Using_Self("Ali", 98)
res.display()
