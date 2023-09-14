from typing import List


class EvenOnly(List[int]):
    def append(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)


if __name__ == '__main__':
    e = EvenOnly()
    # e.append("a string") # raise a type error
    # e.append(3) # raise a value error
    e.append(4)

