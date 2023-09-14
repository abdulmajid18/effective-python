from typing import NoReturn


def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


if __name__ == '__main__':
    a = never_returns()
    print(a)
