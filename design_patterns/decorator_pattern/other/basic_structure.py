def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper


@decorator
def my_function():
    print("Hello, World!")


my_function()
