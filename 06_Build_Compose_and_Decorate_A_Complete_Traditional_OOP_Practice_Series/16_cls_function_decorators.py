# 16. Function Decorators Assignment:
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().


def log_function_call(func):

    def wrap():
        print("Function is being called")
        func()

    return wrap


# A decorator is like a wrapper that adds extra behavior 
# to a function without changing its code.
@log_function_call
def say_hello():

    print("Hello!!")
    
say_hello()

