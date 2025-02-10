hex_res = list(map(hex, b'abc'))
print(hex_res)

bin_res = list(map(bin, b'abc'))
print(bin_res)

print(bytes([137, 80, 78, 71, 13, 10, 26, 10]))
# Output: b'\x89PNG\r\n\x1a\n'
