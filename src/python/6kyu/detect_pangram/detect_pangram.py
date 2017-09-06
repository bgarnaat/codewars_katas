"""
DESCRIPTION:


A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string


def is_pangram(s):
    extra_chars = ' ' + string.punctuation + string.digits
    return len(set(s.translate(str.maketrans('', '', extra_chars)).lower())) == 26


"""
BEST ANSWER:


import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
