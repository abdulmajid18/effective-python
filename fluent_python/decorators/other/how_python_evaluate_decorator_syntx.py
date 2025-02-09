def decorator(a):
    print("decorator  ", a)


@decorator
def some_function():
    pass


# equivalent to
def some_function():
    pass


some_function = decorator(some_function)  # The function is wrapped by the decorator
