from functools import reduce
from operator import add

# Using reduce
result_reduce = reduce(add, range(100))
print(result_reduce)  # Output: 4950

# Using sum (more readable and efficient)
result_sum = sum(range(100))
print(result_sum)  # Output: 4950
