from typing import NamedTuple
import typing

Coordinate1 = typing.NamedTuple("Coordinate", [('lat', float), ('lon', float)])
print(issubclass(Coordinate1, tuple))
print(typing.get_type_hints(Coordinate1))


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'N' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}° {we}'


# print(issubclass(Coordinate, typing.NamedTuple)) # type error due to comparison
print(issubclass(Coordinate, tuple))
