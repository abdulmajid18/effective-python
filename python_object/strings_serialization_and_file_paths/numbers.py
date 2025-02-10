print("123".isdigit())      # True
print("123".isdecimal())    # True
print("123".isnumeric())    # True

print("⅕".isdigit())        # False (because it's a fraction)
print("⅕".isdecimal())      # False
print("⅕".isnumeric())      # True  ✅

print("٢".isdigit())        # True (because it's an Arabic numeral)
print("٢".isdecimal())      # True
print("٢".isnumeric())      # True

print("45.2".isdigit())     # False (because of the period)
print("45.2".isdecimal())   # False
print("45.2".isnumeric())   # False

print("45".isdecimal())   # ✅ True (only digits)
print("45.2".isdecimal()) # ❌ False (period `.` is not a decimal digit)
print("-45".isdecimal())  # ❌ False (negative sign `-` is not a decimal digit)

num = "45\u06602"  # Equivalent to "45.2" using Unicode decimal character
print(num)          # Prints: 45٢ (which might look like "45.2")
print(float(num))   # Prints: 450.0 (Oops! The Unicode decimal character was treated as 0)
