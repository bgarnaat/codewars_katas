"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.


Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


import operator


def longest_consec1(strarr, k):
    """
    Method #1:  Max of list using len(x) as max key

    str_lst = [''.join(strarr[i:i+k]) for i in range(len(strarr) - (k-1))]
    return max(str_lst, key=lambda x: len(x))
    """
    if 0 < k <= len(strarr):
        return max([''.join(strarr[i:i+k]) for i in range(len(strarr) - (k-1))], key=lambda x: len(x))
    return ''


def longest_consec2(strarr, k):
    """
    Method #2:  Sorted list then return item at idx 0

    str_lst = [(len(''.join(strarr[i:i+k])), ''.join(strarr[i:i+k])) for i in range(len(strarr) - (k-1))]
    return sorted(str_lst, reverse=True, key=operator.itemgetter(0))[0][1]
    """
    if 0 < k <= len(strarr):
        return sorted([(len(''.join(strarr[i:i+k])), ''.join(strarr[i:i+k])) for i in range(len(strarr) - (k-1))], reverse=True, key=operator.itemgetter(0))[0][1]
    return ''


def longest_consec3(strarr, k):
    """
    Method #3:

    iterate through list comparing each index to current longest string
    reassign longest string as necessary
    """
    if 0 < k <= len(strarr):
        str_lst = [''.join(strarr[i:i+k]) for i in range(len(strarr) - (k-1))]
        longest_out = ''
        for item in str_lst:
            if len(item) > len(longest_out):
                longest_out = item
        return longest_out
    return ''
