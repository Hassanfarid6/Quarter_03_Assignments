# ---- Class Decorator ka Example ----
# Yeh ek decorator hai jo class ke methods ko track karta hai
def method_tracker(cls):
    # Har method ko wrap karo taake uske call hone ka pata chale
    for name, method in cls.__dict__.items():
        if callable(method):  # Agar yeh ek method hai
            def wrapped_method(*args, **kwargs):
                print(f"Method {name} call ho raha hai!")
                return method(*args, **kwargs)
            setattr(cls, name, wrapped_method)  # Original method ko replace karo
    return cls

# Is decorator ko class par lagao 
@method_tracker
class Toy:
    # Yeh ek toy class hai
    def __init__(self, name):
        self.name = name  # Toy ka naam

    def play(self):
        # Yeh method toy ke saath khelne ke liye hai
        return f"{self.name} ke saath khel raha hoon!"

# ---- Property Decorator ka Example ----
class ToyBox:
    # Yeh ek toy box class hai jismein color hota hai
    def __init__(self, color):
        self._color = color  # _color ek private variable hai

    @property
    def color(self):
        # Yeh color ko as a property return karta hai
        return f"Toy box ka color hai: {self._color}"

    @color.setter
    def color(self, new_color):
        # Yeh color ko change karne ke liye hai
        if new_color:  # Check karo ke new_color khali toh nahi
            self._color = new_color
            print(f"Color change ho gaya: {new_color}")
        else:
            print("Color khali nahi ho sakta!")

    @color.deleter
    def color(self):
        # Yeh color ko delete karne ke liye hai
        print("Color hata diya gaya!")
        self._color = None

# ---- Code Chalane ka Example ----
# Class Decorator ka test
toy = Toy("Robot")  # Ek toy banaya
print(toy.play())  # Output: Method play call ho raha hai! Robot ke saath khel raha hoon!

# Property Decorator ka test
box = ToyBox("Red")  # Ek toy box banaya jiska color Red hai
print(box.color)  # Output: Toy box ka color hai: Red
box.color = "Blue"  # Color change karo
print(box.color)  # Output: Toy box ka color hai: Blue
del box.color  # Color delete karo
print(box.color)  # Output: Toy box ka color hai: None

# ---- Decorators Ki Details ----
# Class Decorator: method_tracker har method call ko track karta hai aur uska naam print karta hai
# Property Decorator: @property se hum color ko variable ki tarah use kar sakte hain
# @setter se hum color change kar sakte hain, aur @deleter se color hata sakte hain
# Yeh sab class ke behavior ko control karne mein madad karte hain
# Jaise: Toy box ka color dekhna, change karna, ya hataana asaan ho jata hai