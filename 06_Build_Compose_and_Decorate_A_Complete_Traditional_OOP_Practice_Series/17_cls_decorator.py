# 17. Class Decorators Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.


# This is a decorator that adds a greet method to a class
def add_greeting(cls):
        
    def greet(self):
        return "Hello from Decorator!"
    
    # This adds the greet method to the class
    cls.greet = greet
    
    # This returns the modified class
    return cls   


# class Greeting:
    
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


res = Person(" ")

print(res.greet())

        




