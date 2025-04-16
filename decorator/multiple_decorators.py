def decorator_1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        result = func(*args, **kwargs)
        print("Decorator 1 after")
        return result

    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        result = func(*args, **kwargs)
        print("Decorator 2 after")
        return result

    return wrapper


@decorator_1
@decorator_2
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
