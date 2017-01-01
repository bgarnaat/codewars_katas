"""
Description:

In this kata you have to implement a base converter, which converts between arbitrary bases / alphabets. Here are some pre-defined alphabets:

bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
The function convert() should take an input (string), the source alphabet (string) and the target alphabet (string). You can assume that the input value always consists of characters from the source alphabet. You don't need to validate it.


Examples:

convert("15", dec, bin) #should return "1111"
convert("15", dec, oct) #should return "17"
convert("1010", bin, dec) #should return "10"
convert("1010", bin, hex) #should return "a"

convert("0", dec, alpha) #should return "a"
convert("27", dec, allow) #should return "bb"
convert("hello", allow, hex) #should return "320048"


Additional Notes:

The maximum input value can always be encoded in a number without loss of precision in JavaScript. In Haskell, intermediate results will probably be to large for Int.
The function must work for any arbitrary alphabets, not only the pre-defined ones
You don't have to consider negative numbers
"""


def convert(data, source, target):
    """BEGIN (or end)"""
    data = data[::-1]
    len_in = len(source)
    len_tar = len(target)

    # convert from base <source> to base 10 (used as a common base for translation)
    base = sum([source.index(val) * len_in ** idx for idx, val in enumerate(data)])

    output = []
    if base == 0:
        output.append(target[0])
    else:
        while base:
            output.append(target[base % len_tar])
            base = base // len_tar

    return ''.join(output[::-1])


"""
BEST ANSWER:




def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0]




from math import log

def convert(value, source, target):
    value = sum(source.find(c) * (len(source) ** i) for i, c in enumerate(reversed(value)))
    return ''.join(target[(value / (len(target) ** i)) % len(target)] for i in xrange(0 if not value else int(log(value, len(target))),-1,-1))
"""
