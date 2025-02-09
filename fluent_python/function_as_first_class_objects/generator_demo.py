def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


# Creating a generator
gen = count_up_to(5)

# Fetching values from the generator
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Can be used in a loop
for num in gen:
    print(num)  # Output: 3, 4, 5

"""
A generator expression is like a lazy version of a list comprehension.
"""
# List comprehension (creates a full list in memory)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (creates values lazily)
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
