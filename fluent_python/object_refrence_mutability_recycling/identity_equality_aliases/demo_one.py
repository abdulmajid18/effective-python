a = [1,2,3]

b = a

print(f" B is A {b is a}")
print(f" B == A {b == a}")

a.append(4)
print("A is now ", a)
print(f" B is A {b is a}")
print(f" B == A {b == a}")
print("B is ", b)
