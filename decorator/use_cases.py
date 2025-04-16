def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.role != 'admin':
            raise PermissionError("You do not have permissions.")
        return func(user, *args, **kwargs)

    return wrapper


@requires_admin
def delete_user(user, user_id):
    print(f"User {user_id} deleted.")


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper