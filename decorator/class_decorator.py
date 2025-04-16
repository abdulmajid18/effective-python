class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function {self.func.__name__}")
        return self.func(*args, **kwargs)


@LogDecorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
