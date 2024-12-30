from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = "WGS84"


print(Coordinate.__annotations__)


class CoordinateTrash(NamedTuple):
    lat: float
    lon: float


trash = CoordinateTrash('Ni!', None)
print(trash)
