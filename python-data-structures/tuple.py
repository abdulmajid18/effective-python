import datetime


def middle(stock, date):
    symbol, current, high, low = stock
    return ((high + low) / 2), date


result = middle(("AAPL", 123.52, 53.15, 137.98), datetime.date(2020, 12, 4))
print(result)
