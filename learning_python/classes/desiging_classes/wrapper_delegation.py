class RealObject:
    def perform_operation(self):
        print("RealObject is performing the operation")


class Wrapper:
    def __init__(self, real_object):
        self._real_object = real_object

    def perform_operation(self):
        print("Wrapper is delegating the operation to RealObject")
        self._real_object.perform_operation()


if __name__ == "__main__":
    # Create an instance of the RealObject
    real_object = RealObject()

    # Create a Wrapper around the RealObject
    wrapper = Wrapper(real_object)

    # Demonstrate delegation
    wrapper.perform_operation()
