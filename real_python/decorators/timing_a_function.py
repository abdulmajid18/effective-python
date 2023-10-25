import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6} seconds to run")
        return result

    return wrapper


@timing_decorator
def slow_function(duration):
    time.sleep(duration)
    return "Done!"


result = slow_function(2)
