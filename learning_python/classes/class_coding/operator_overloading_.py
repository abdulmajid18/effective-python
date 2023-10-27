from learning_python.classes.class_coding.classes_eg import SecondClass


class ThirdClass(SecondClass):
    def __int__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):  # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):  # In-place change: named
        self.data *= other
