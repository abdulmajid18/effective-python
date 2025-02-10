class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)


@Logger
def greet(name):
    print(f"Hello, {name}!")


greet("Rozz")
