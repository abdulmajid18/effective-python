from coordinates import Coordinate

accra = Coordinate(55.76, 37.58)
print(accra)

location = Coordinate(55.76, 37.58)
print(location == accra)

print((location.lat, location.lon) == (accra.lat, accra.lon))