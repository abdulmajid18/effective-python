class Gizmo:
    def __init__(self):  # Fix the method name
        print(f"Gizmo id: {id(self)}")


x = Gizmo()
print(x)
# Uncommenting the following line will still cause a TypeError:
# y = Gizmo() * 10
"""
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
"""

print(dir())

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles

print(lewis is charles)
print(lewis == charles)

print(f" Charles id {id(charles)} Lewis id {id(lewis)}")
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance':950}
print(alex == charles)
print(alex is not charles)