"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.


Example:

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""


def sort_array(source_array):
    tmp = [x for x in source_array if x % 2]
    tmp.sort()
    for i in range(len(source_array) - 1, -1, -1):
        if source_array[i] % 2:
            source_array[i] = tmp.pop()
    return source_array


"""
BEST ANSWER:


def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]




def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
"""
