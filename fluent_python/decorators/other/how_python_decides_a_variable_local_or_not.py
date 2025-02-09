x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"  # This is a local variable

    inner()
    print(x)  # Still "enclosing" because `inner()` does not change it


outer()
print(x)  # Still "global"
