"""This is where *args can be really useful, because it allows
you to pass a varying number of positional arguments. Take the
following example:"""


# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))


# sum_integers_args_2.py
def my_sum_2(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum2(1, 2, 3))
