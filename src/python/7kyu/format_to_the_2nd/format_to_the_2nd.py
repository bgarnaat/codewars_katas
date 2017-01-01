"""
Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.

For example, given 1, 23, 2, 17, 102, the following string should be printed out:

001
023
002
017
102

Write a function print_nums(n1, n2, n3, ...) that takes a variable number of arguments and returns the string to be printed out.
"""


def print_nums(*args):
    return '\n'.join(['0' * (len(str(max(args))) - len(str(x))) + str(x) for x in args])


"""
BEST ANSWER:


def print_nums(*arr):
    if not arr: return ''
    ln = len(str(max(arr)))
    return '\n'.join(str(c).zfill(ln) for c in arr)



def print_nums(*args):
    try:
        fmt = '{{:0>{}}}'.format(len(str(max(args)))).format
    except ValueError:
        return ''
    return '\n'.join(fmt(a) for a in args)



def print_nums(*args):
  width = max((len(str(num)) for num in args), default=0)
  return '\n'.join('{:0{}d}'.format(num, width) for num in args)
"""
