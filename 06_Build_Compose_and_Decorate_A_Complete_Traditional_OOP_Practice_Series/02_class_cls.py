# 2. Using cls Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class 
# variable and a class method with cls to manage and display the count.


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

     # cls class ko refer karta hai, jaise self instance ko refer karta hai.
     # Isse aap class ke attributes ya doosre methods ko access kar sakte ho.
    @classmethod  # used with very method cls
    def display(cls):
        print(f"Numbers of Object created: {cls.count}")
        

counter1 = Counter() 
counter2 = Counter() 
counter3 = Counter()

Counter.display()