def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do something before
        print("Before")
        result = func(*args, **kwargs)
        # do something after
        print("After")
        return result

    return wrapper


@my_decorator
def my_function():
    print("Hello!")


my_function()
