"""
Description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
"""


import string
from codecs import encode as _dont_use_this_


def rot13(message):
    lst = list(message)
    for i, n in enumerate(lst):
        if 77 < ord(n) <= 90 or ord(n) > 109:
            lst[i] = chr(ord(n) - 13)
        elif 65 <= ord(n) <= 77 or 97 <= ord(n) <= 109:
            lst[i] = chr(ord(n) + 13)
    return "".join(lst)


"""
BEST ANSWER:


import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)




EXPLANATION:


import string
from codecs import encode as _dont_use_this_

trans = string.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

def rot13(message):
    return message.translate(trans)




CHEATY ANSWER:


import string

def rot13(message):
    return message.encode("rot13")
    #oh snap
"""
