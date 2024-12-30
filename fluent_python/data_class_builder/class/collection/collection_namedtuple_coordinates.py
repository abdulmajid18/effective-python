from collections import namedtuple

Coordinate = namedtuple("Coordinate", "lat lon")
print(issubclass(Coordinate, tuple))

accra = Coordinate(55.76, 37.58)
print(accra)

print(accra == Coordinate(55.76, 37.58))
