import pytest
"""
TEST CASES:


test.describe('Basic Tests')
test.assert_equals(print_nums(), '')
test.assert_equals(print_nums(2), '2')
test.assert_equals(print_nums(1, 12, 34), '01\n12\n34')
test.assert_equals(print_nums(1009, 2), '1009\n0002')
"""

def test_print_nums_no_input():
    from format_to_the_2nd import print_nums
    assert print_nums() == ''


def test_print_nums_one_input():
    from format_to_the_2nd import print_nums
    assert print_nums(2) == '2'


def test_print_nums_two_input():
    from format_to_the_2nd import print_nums
    assert print_nums(1009, 2) == '1009\n0002'


def test_print_nums_three_input():
    from format_to_the_2nd import print_nums
    assert print_nums(1, 12, 34) =='01\n12\n34'
