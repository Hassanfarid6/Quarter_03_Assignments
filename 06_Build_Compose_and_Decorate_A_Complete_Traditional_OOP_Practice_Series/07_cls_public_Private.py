# 7. Access Modifiers: Public, Private, and Protected Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee: 
    def __init__(self, name, salary, ssn):
        self.name = name          # public Variable
        self._salary = salary     # protected variable
        self.__ssn = ssn          # private variable

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")      

res = Employee("ali", 900000, "hasan")

print(res.name)  # Access public variable
print(res._salary)  # Access protected variable
# This will fail because __ssn is private
print(res.__ssn)    # can not Access dirtectly
# Trying to access the private variable directly will cause an AttributeError
# To access private variable, use name mangling: res._Employee__ssn (not recommended)
# Example: print(res._Employee__ssn)  # Output: hasan


res.display()