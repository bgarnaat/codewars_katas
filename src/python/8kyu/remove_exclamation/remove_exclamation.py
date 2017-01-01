"""
Description:

Remove a exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi!!"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
"""


def remove(s):
    # return s[:-1] if s and s[-1] == "!" else s

    # try:
    #     return s[:-1] if s[-1] == "!" else s
    # except IndexError:
    #     return s

    if s and s[-1] == '!':
        return s[:-1]
    return s


"""
BEST ANSWER:

def remove(s):
    return s[:-1] if s.endswith('!') else s
"""
