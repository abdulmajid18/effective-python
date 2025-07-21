from first_class_demo import FirstClass
import first_class_demo

class SecondClass(FirstClass):
    def display(self): ...


class SecondClassTwo(first_class_demo.FirstClass):
    def display(self): ...