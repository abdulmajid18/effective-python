l1 = [3, [55, 44], (7, 8, 9)]

l2 = list(l1)

print(l2)
print(l1 == l2)
print(l2 is l1)

# shallow copy
"""
However, using the constructor or [:] produces a shallow copy (i.e., the
outermost container is duplicated, but the copy is filled with references to
the same items held by the original container). This saves memory and
causes no problems if all the items are immutable. But if there are mutable
items, this may lead to unpleasant surprises.
"""
l3 = l1[:]
print(l1 is l3)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
print("This is initial l1", l1)
l1[1].remove(55)
print("Removed 55 from index 1", l1)
print("L2 after l1 removal", l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print("New l1", l1)
print("New l2", l2)

"""
Working with shallow copies is not always a problem, but sometimes you
need to make deep copies (i.e., duplicates that do not share references of
embedded objects). The copy module provides the deepcopy and copy
functions that return deep and shallow copies of arbitrary objects
"""


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print("Bus2 passengers after dropping Bill from bus1", bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)


"""
Note that making deep copies is not a simple matter in the general case.
Objects may have cyclic references that would cause a naïve algorithm to
enter an infinite loop. The deepcopy function remembers the objects
already copied to handle cyclic references gracefully
"""
a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
from copy import deepcopy
c = deepcopy(a)
print(c)