"""
Description:

The word i18n is a common abbreviation of internationalization the developer community use instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation following the same rules.

Notes:

A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
Example:

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
"""

def abbreviate(s):
    s_out = word = ''
    word_len = 0
    for l in s:
        if l.isalpha():
            word_len += 1
            word += l
        else:
            # if word_len >= 4:
            if len(word) >= 4:
                # s_out += word[0] + str(word_len - 2) + word[-1]
                s_out += word[0] + str(len(word) - 2) + word[-1]
            else:
                s_out += word
            s_out += l
            word, word_len = '', 0
            # word = ''
    if word_len >= 4:
        # s_out += word[0] + str(word_len - 2) + word[-1]
        s_out += word[0] + str(len(word) - 2) + word[-1]
    else:
        s_out += word
    return s_out


"""
Alternate:
"""


def abbreviate2(s):
    word = s_out = ''
    for l in s:
        if l.isalpha():
            word += l
        else:
            if len(word) >= 4:
                s_out += word[0] + str(len(word) - 2) + word[-1]
            else:
                s_out += word
            s_out += l
            word = ''
    if len(word) >= 4:
        s_out += word[0] + str(len(word) - 2) + word[-1]
    else:
        s_out += word
    return s_out


"""
BEST ANSWER:

import re
def abbreviate(s):
    ab = lambda w: w[:1] + str(len(w) - 2) + w[-1:]
    return re.sub(r'\w{4,}', lambda m: ab(m.group(0)), s)
"""
