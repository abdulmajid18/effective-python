from typing import NamedTuple


class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float


s2 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s2)


class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2


s3 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s3.middle)
