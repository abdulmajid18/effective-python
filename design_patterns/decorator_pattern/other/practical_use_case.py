# logging
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log
def add(a, b):
    return a + b


add(3, 5)

# timng
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "Finished"


slow_function()


def requires_auth(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied")
            return
        return func(user)

    return wrapper


@requires_auth
def secret_data(user):
    print("Access Granted: Here is the secret data")


secret_data("guest")  # Access Denied
secret_data("admin")  # Access Granted
