fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]

print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]


fruits = ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
print(sorted(fruits, key=reverse))


from math import factorial

# Using map
print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])  # Equivalent list comprehension


"""
Functional languages commonly offer the map, filter, and reduce
higher-order functions (sometimes with different names). The map and
filter functions are still built-ins in Python 3, but since the introduction
of list comprehensions and generator expressions, they are not as important.
A listcomp or a genexp does the job of map and filter combined, but is
more readable
"""
# Using map + filter
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])  # Equivalent list comprehension
