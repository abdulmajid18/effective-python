characters = b'\x63\x6c\x69\x63\x68\xc3\xa9'

print(characters)
# b'clich\xc3\xa9'


decoded_chars = characters.decode("utf-8")
print(decoded_chars)
iso_decoded = characters.decode("iso8859-5")
print(iso_decoded)



# mutable byte
ba = bytearray(b"abcdefgh")
ba[4:6] = b"\x15\xa3"
print(ba)

ba = bytearray(b"abcdefgh")
ba[3] = ord(b'g')
ba[4] = 68
print( ba)