def my_decorator(func):
    print("Decorating function!")  # This runs when the module is loaded
    return func  # Returns the original function unchanged


@my_decorator
def say_hello():
    print("Hello!")



print("Module loaded!")