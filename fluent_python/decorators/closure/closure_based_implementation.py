def make_averager():
    series = []  # Local variable, not a global or function argument

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager  # Return the inner function


avg = make_averager()  # avg is now an instance of averager
print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0


print(avg.__closure__)  # (<cell at 0x...: list object at 0x...>,)
print(avg.__closure__[0].cell_contents)  # [10, 11, 12]
