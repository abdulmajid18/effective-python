"""This implementation works, but whenever you call this function
you’ll also need to create a list of arguments to pass to it.
This can be inconvenient, especially if you don’t know up front
all the values that should go into the list"""


def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
