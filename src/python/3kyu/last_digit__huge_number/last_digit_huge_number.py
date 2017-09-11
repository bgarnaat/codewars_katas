"""
DESCRIPTION:


For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1
because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.
"""


def last_digit(lst):
    if not lst:
        return 1
    if len(lst) is 1:
        return lst[0] % 10
    prev = lst[-1]
    for idx, item in enumerate(lst[1:-1][::-1]):
        if not item and prev:
            prev = 0
        else:
            prev = pow(item, prev, 4) or 4
    return pow(lst[0], prev, 10)


"""
BEST SOLUTIONS:



from functools import reduce

def mod_off(number, mod):
    return min(number, (number - 2) % mod + 2)
def pow_mod(exp, base):
    return mod_off(base, 20) ** mod_off(exp, 4)
def last_digit(lst):
    return reduce(pow_mod, lst[::-1], 1) % 10

------------------------------------------------------

from functools import reduce

def _powmod(exp, base):
    return (1 if exp == 0
            else base if exp == 1 or base == 0
            else pow(base, 2 + ((exp - 2) % 20), 100) or 20)

def last_digit(arr):
    return reduce(_powmod, arr[::-1], 1) % 10

-----------------------------------------------------

def last_digit(lst):
    dig = lst[-1] if lst else 1
    b = dig != 0
    for p in lst[-2::-1]:
        dig = 1 if p == dig == 0 else pow(p, dig or 20*b, 20)
        b = (dig or 20*b) == 0 or p != 0
    return dig % 10
"""
