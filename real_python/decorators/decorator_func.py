# decorator function

def add_banner(func):
    def wrapper():
        print("*" * 11)
        func()
        print("*" * 11)

    return wrapper


@add_banner
def hello():
    print("Hello Abdul!")


hello()