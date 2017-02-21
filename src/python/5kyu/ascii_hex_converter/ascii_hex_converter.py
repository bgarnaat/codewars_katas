"""
Description:

Write a module Converter that can take ASCII text and convert it to hexadecimal. The class should also be able to take hexadecimal and convert it to ASCII text.

Example

Converter.to_hex("Look mom, no hands")
=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
=> "Look mom, no hands"
"""


class Converter(object):
    @staticmethod
    def to_ascii(h):
        return ''.join([chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2)])

    @staticmethod
    def to_hex(s):
        return ''.join([hex(ord(i))[2:] for i in s])


"""
BEST ANSWER:


class Converter():
    @staticmethod
    def to_ascii(h):
        return h.decode("hex")
    @staticmethod
    def to_hex(s):
        return s.encode("hex")
"""
