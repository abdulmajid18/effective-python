import random


class BingoCage:
    def __init__(self, items):
        """Accepts any iterable and stores a shuffled list."""
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        """Pops an item from the shuffled list."""
        if not self._items:
            raise LookupError('pick from empty BingoCage')
        return self._items.pop()

    def __call__(self):
        """Allows the instance to be called as a function."""
        return self.pick()


# Usage:
bingo = BingoCage(range(3))
print(bingo.pick())  # Random item (e.g., 1)
print(bingo())  # Shortcut for pick()
print(callable(bingo))  # True (can be used like a function)


class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@Memoize
def expensive_function(x):
    print(f"Computing {x}...")
    return x * x


print(expensive_function(5))  # Computes and stores result
print(expensive_function(5))  # Returns cached result (no computation)


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def expensive_function(x):
    print(f"Computing {x}...")
    return x * x


print(expensive_function(5))  # Computes and stores
print(expensive_function(5))  # Uses cache
