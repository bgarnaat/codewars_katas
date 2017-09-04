"""
DESCRIPTION:


Given an array with 3 subarrays, which each contain a number of hexadecimal color codes loosely defining red, green and blue colors based on their predominant byte value, return a string description of which of the three colors each array contains.

Input is an array that holds 3 arrays each of length between 3 and 10. Each array holds a number of color codes with either red, green or blue byte predominant and thus being defined as red, green or blue. Based on this definition each array contains color codes in exactly two colors- a majority color, which is all color codes apart from one and a minority color- the remaining one. Majority color and minority color of an array will never be the same, but different combinations are possible across the arrays (i.e Red+Blue,Red+Blue,Red+Blue is a valid combination).There will be no invalid inputs.

Color codes will be given as strings of hexadecimal values in form RRGGBB. Out of the three components, one(L) is in range 01-FF and the other two in range from 00-(L-1). So one value is always bigger than either of the other two, and thus the whole color is defined as red, green or blue.(This allows for colors such as 010000 and FFFEFE both be defined as red, which is unrealistic in terms of human vision, but I have left it so as the purpose of the task is more to describe colors by looking at differences between numerical values of bytes and for a restricted range of input than by what they would actually look like.) All alphabetic chars in input are in uppercase.

Your task is to determine the majority color and the minority color for each array. Return a string in formmajCol+minCol,majCol+minCol,majCol+minCol where the three comma separated pairs refer to each array sequentially and majCol and minCol are color names (red, green, blue) capitalized. The string shouldn't contain any spaces.

All ranges in the above text are inclusive.

Example:

Input:

colArr=[ [ "FFA07A","FA8072","8DC4DE" ], ["7FFF00","ADFF2F", "FF0000","00FF7F","00FF7F"], ["ADD8E6","6B8E23","9ACD32","32CD32","00FF00"]]

Output:

Red+Blue,Green+Red,Green+Blue
"""
from collections import Counter


def get_colors(col_arr):
    output_list = []

    for sub_arr in col_arr:
        max_counter = Counter([_colorizer(arr) for arr in sub_arr])
        max_color = max_counter.most_common(1)[0][0]
        min_color = max_counter.most_common()[-1][0]
        output_list.append(max_color + '+' + min_color)
    return ','.join(output_list)


def _colorizer(color):
    color_list = [(int(color[0:2], 16), 'Red'), (int(color[2:4], 16), 'Green'), (int(color[4:6], 16), 'Blue')]
    return max(color_list)[1]


"""
BEST SOLUTION:


from collections import Counter

COLORS = ['Red','Green','Blue']

def getColor(col):
    lst = [int(col[2*i:2*(i+1)], 16) for i in range(3)]
    return COLORS[lst.index(max(lst))]

def get_colors(col_arr):
    lst = []
    for arr in col_arr:
        config = {v:k for k,v in Counter(getColor(col) for col in arr).items()}
        lst.append("{}+{}".format(config[max(config)], config[min(config)]))
    return ','.join(lst)
"""
