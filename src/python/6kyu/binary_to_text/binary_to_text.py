"""
Description:

Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
"""


def binary_to_string(binary):
    # chop = [binary[x*8:(x+1)*8][::-1] for x in range(len(binary) // 8)]
    # return ''.join([chr(sum([int(z) * 2 ** idx for idx, z in enumerate(y)])) for y in chop])

    return ''.join([chr(sum([int(z) * 2 ** idx for idx, z in enumerate(binary[x * 8:(x + 1) * 8][::-1])])) for x in range(len(binary) // 8)])


"""
BEST ANSWER:


def binary_to_string(binary):
    return "".join( [ chr( int(binary[i: i+8], 2) ) for i in range(0, len(binary), 8) ] )
"""
