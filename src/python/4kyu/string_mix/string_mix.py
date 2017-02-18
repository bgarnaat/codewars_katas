"""
Description:

Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings will be in decreasing order of their length and when they have the same length sorted alphabetically (more precisely sorted by codepoint); the different groups will be separated by '/'.

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""


from collections import Counter


def mix(s1, s2):
    ct_1, ct_2 = Counter(s1), Counter(s2)
    output = []

    for item in (ct_1 + ct_2):
        if item[0].isalpha() and item[0].islower() and max(ct_1[item[0]], ct_2[item[0]]) > 1:
            if ct_1[item[0]] > ct_2[item[0]]:
                output.append('1:' + item[0] * ct_1[item[0]])
            elif ct_1[item[0]] < ct_2[item[0]]:
                output.append('2:' + item[0] * ct_2[item[0]])
            else:
                output.append('=:' + item[0] * ct_1[item[0]])

    output.sort()
    output.sort(key=lambda x: len(x), reverse=True)
    return '/'.join(output)


"""
BEST ANSWER:


rom collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))




from string import ascii_lowercase

def mix(s1, s2):
    c1 = [s1.count(ascii_lowercase[i]) for i in range(0, 26)]
    c2 = [s2.count(ascii_lowercase[i]) for i in range(0, 26)]

    m = [max(c1[i], c2[i]) for i in range(0,26)]
    strings = []

    for i in range(0, 26):
        if m[i] > 1:
            prefix = ["2", "1"][m[i] == c1[i]]
            prefix = [prefix, "="][c1[i] == c2[i]]
            strings.append(prefix + ":" + ascii_lowercase[i] * m[i])

    return "/".join(sorted(strings, key = lambda x : (-len(x), x)))
"""
