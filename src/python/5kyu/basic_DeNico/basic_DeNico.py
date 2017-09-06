"""
Task

Write a function deNico/de_nico() that accepts two parameters:

key/$key - string consists of unique letters and digits
message/$message - string with encoded message
and decodes the message using the key.

First create a numeric key basing on the provided key by assigning each letter position in which it is located after setting the letters from key in an alphabetical order.

For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
Let's decode cseerntiofarmit on using our crazy key.

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n
After using the key:

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n


Notes

The message is never shorter than the key.
Don't forget to remove trailing whitespace after decoding the message
Examples

deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key"
Check the test cases for more examples.
"""


def de_nico(key, msg):
    numeric_key = [key.index(char) for char in sorted(key)]
    key_index = [numeric_key.index(i) for i in range(len(key))]
    split_msg = [msg[i:i + len(key)] for i in range(0, len(msg), len(key))]

    output_msg = ''

    for part in split_msg:
        for idx in key_index:
            try:
                output_msg += part[idx]
            except IndexError:
                pass
    return output_msg.strip(' ')


"""
BEST SOLUTION:


def de_nico(key, msg):
    ll, order, s = len(key), [sorted(key).index(c) for c in key], ''
    while msg:
        s, msg = s + ''.join(msg[i] for i in order if i < len(msg)), msg[ll:]
    return s.strip()
"""
