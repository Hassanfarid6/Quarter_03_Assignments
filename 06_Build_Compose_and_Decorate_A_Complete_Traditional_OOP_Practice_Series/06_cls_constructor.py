# 6. Constructors and Destructors Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message
# when it is destroyed (destructor).

class Logger: 
    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' ban gaya hai!")
        
    def __del__(self):
        print(f"Logger object '{self.name}' destroy ho gaya hai!")

logger1 = Logger("FirstLogger")
logger2 = Logger("SecondLogger")
print("Objects banaye ja chuke hain, ab program khatam hoga.")