class Averager:
    def __init__(self):
        self.series = []  # Store all values

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
