def counter():
    count = 0  # Enclosing variable

    def increment():
        # count += 1  # ❌ ERROR: Python assumes `count` is local (LEGB rule)
        return count

    return increment


count_up = counter()
# count_up()  # UnboundLocalError: local variable 'count' referenced before assignment


def counter():
    count = 0

    def increment():
        nonlocal count  # Tell Python to modify the enclosing 'count'
        count += 1
        return count

    return increment


count_non_local = counter()
print(count_up())  # 1
print(count_up())  # 2
print(count_up())  # 3
