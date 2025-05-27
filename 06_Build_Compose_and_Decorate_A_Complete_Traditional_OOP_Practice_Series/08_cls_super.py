# 8. The super() Function Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher
#  from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

    # Method to display person's details
    def display(self):
        print(f"Name: {self.name}")

# This is the Teacher class that inherits from Person
class Teacher(Person):
    # Constructor to initialize name (from Person) and subject
    def __init__(self, name, subject):
        # Use super() to call the Person class's __init__ method
        super().__init__(name)  # Pass name to Person's constructor
        self.subject = subject  # Store the subject as an instance variable
    
    # Method to display teacher's details, including name and subject
    def display(self):
        # Call the Person class's display method using super()
        super().display()  # Prints the name from Person class
        print(f"Subject: {self.subject}")  # Print the teacher's subject

res = Teacher("Ali", "Math")
res.display()

