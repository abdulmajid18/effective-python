def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        #count += 1  # ❌ UnboundLocalError
       # total += new_value  # ❌ UnboundLocalError
        return total / count

    return averager


# UnboundLocalError: local variable 'count' referenced before assignment


def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total  # ✅ Declaring count and total as nonlocal
        count += 1
        total += new_value
        return total / count
    return averager
