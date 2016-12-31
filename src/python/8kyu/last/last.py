"""
Find the last element of a list.


Example:

last([1,2,3,4]) # => 4
last("xyz") # => z
last(1,2,3,4) # => 4


In javascript and CoffeeScript a list will be an array, a string or the list of arguments.
"""


def last(*lst):
    try:
        return lst[-1][-1]
    except TypeError:
        return lst[-1]


"""
BEST ANSWER:

def last(*args):
    try:
        return args[-1][-1]
    except:
        return args[-1]

"""
