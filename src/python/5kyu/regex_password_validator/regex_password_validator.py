"""
Description:


You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
"""


from re import search


def re_search(s):
    regex = "(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*\d+)(?=^[\w]{6,}$)(?=[^_]+$)"
    return bool(search(regex, s))
