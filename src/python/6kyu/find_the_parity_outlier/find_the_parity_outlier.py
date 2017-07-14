"""
Description:

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""


def find_outlier(integers):
    even = [x for x in integers[:3] if not x % 2]

    if len(even) > 1:
        return [x for x in integers if x % 2][0]
    return [x for x in integers if not x % 2][0]
