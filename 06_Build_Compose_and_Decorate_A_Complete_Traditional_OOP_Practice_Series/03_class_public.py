# 3. Public Variables and Methods Assignment:
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand     # Public Variable

    def start(self):            # Public Method
        print(f"start {self.brand}")

# Instance of the Car class
res = Car("Mira")

# Public Variable
print(res.brand) 

# public Method
res.start()