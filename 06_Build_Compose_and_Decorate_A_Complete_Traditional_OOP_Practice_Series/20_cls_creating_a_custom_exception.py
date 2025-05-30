# 20. Creating a Custom Exception Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises 
# this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, age, message="Minimum age is 18."):
        self.age = age
        self.message = message
        super().__init__(f"{message} You entered: {age}")


def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"{age} Age must be 18 or older")
    else:
        print("Access granted!!")


try:
    # check_age(10)  # Minimum age is 18. You entered: 10 Age must be 18 or older
    check_age(18)  # Access granted!!
except InvalidAgeError as e:
    print(e)