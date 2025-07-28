
# ---- Example 1: Normal Function ----
# Yeh ek normal function hai jo callable hai
def say_hello(name):
    # Yeh function naam lekar hello kehta hai
    return f"Hello, {name}!"

# ---- Example 2: Lambda Function ----
# Lambda function ek chhota, naam ke baghair ka function hai
add_numbers = lambda x, y: x + y

# ---- Example 3: Class ----
# Class bhi callable hoti hai, kyunki isse call karne se naya object banta hai
class Toy:
    def __init__(self, name):
        # Yeh toy ka naam set karta hai
        self.name = name

    def play(self):
        # Yeh method toy ke saath khelne ke liye hai
        return f"{self.name} ke saath khel raha hoon!"

# ---- Example 4: Method ----
# Class ke andar ka method bhi callable hota hai
# (play method upar Toy class mein hai)

# ---- Example 5: __call__ Method ----
# Agar kisi class mein __call__ method ho, toh uska object callable ban jata hai
class CallableToy:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        # Yeh special method object ko function ki tarah chala deta hai
        return f"{self.name} ko function ki tarah call kiya gaya!"

# ---- Code Chalane ka Example ----
# Example 1: Normal Function call
print(say_hello("Ali"))  # Output: Hello, Ali!

# Example 2: Lambda Function call
print(add_numbers(5, 3))  # Output: 8

# Example 3: Class call (naya object banega)
toy = Toy("Robot")  # Class ko call kiya, naya object bana
print(toy.play())   # Output: Robot ke saath khel raha hoon!

# Example 4: Method call
# play method ko object ke sath call karte hain
print(toy.play())   # Output: Robot ke saath khel raha hoon!

# Example 5: __call__ Method
callable_toy = CallableToy("Magic Box")  # Object banaya
print(callable_toy())  # Object ko function ki tarah call kiya
# Output: Magic Box ko function ki tarah call kiya gaya!

# ---- Callable Ki Details ----
# Callable woh cheez hai jise tum () laga kar chala sakte ho
# Examples: Functions (say_hello), Lambda functions (add_numbers), Classes (Toy),
# Methods (play), aur objects jo __call__ rakhte hain (CallableToy)
# Agar kisi cheez mein __call__ method ho, woh callable hoti hai
# Jaise: Ek toy jo button dabane se khud start ho jaye