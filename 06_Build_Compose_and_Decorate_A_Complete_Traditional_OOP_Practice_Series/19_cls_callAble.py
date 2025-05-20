# 19. callable() and __call__() Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method 
# that multiplies an input by the factor. Test it with callable() and by calling the object like a function.



from typing import Any


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
    
multiplier = Multiplier(3)
print(callable(multiplier))

print(multiplier(4))
res = multiplier(5)
print(res)